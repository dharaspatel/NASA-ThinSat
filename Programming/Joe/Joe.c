/*  ________________________________________________
    Description:  file that controls all electronics on joe
    Author: Dhara Patel

    Table of functions:
      calibrateTime()                              []
      readPhotocells()                             [x]
      getPosition()                                []
      calc_state()                                 []
      getRadarRange()                              []
      sendData()                                   [x]
      readSD()                                     []
      writeEEPROM()                                []
      readEEPROM()                                 []
      readMag()                                    [x]
      launch()                                     [x]
      pyrolysis()                                  [x]
      melt()                                       [x]
      readImg()                                    []
      readTemp()                                   []
    ________________________________________________*/


/*___INCLUDES___*/
#include "DS3231.h" //Clock
#include "Wire.h" //i2c
#include "REGS.h" //Registers
#include "SD.h" //SD Card
#include "TSLPB.h" //NSL BUS
#include "myDataPacketStructure.h" //datapacket stuff
#include "Arduino.h" //Arduino library
#include "Joe.h"

#include "ReadPhotocells.c" //reading photocells
#include "ImgProcessing.c"
#include "findlatlongalt.py"

DS3231 Clock;
EEPROM eeprom;
DateTime rtcTime; //the current time output by the rtc of the type DateTime
TSLPB tslpb; //bus
UserDataStruct_t missionData; //packet of mission data
float secLaunch; //seconds since launch
struct pho_data{ //sunset sunrise data
  long sunrises[];
  long sunsets[];
};
bool isfirstRun = true; //first photocell run
int launchCount = 0; //the number of launchers launched
int wireCount = [[3, 4], [5, 6], [7, 8], [9, 10]]; //used to melt the correct wires for the associated target launch
int state_of_burt; //nothing = 0, launch = 1, 2, 3, 4, pyrolysis = 5
float threshold[]; //the threshold for the sunset/sunrise calculations
size_t mag_data[]; //an array of x, y, z magnetometer data
struct position{
  float seconds;
  float latitude;
  float longitude;
  float altitude;
  bool moonless;
  float  inHalfOrbit[3]; //lat, long, alt of the satellite in half orbit
}; //sec, lat, long, alt
struct py_data{
  int temperature;
  int histogram[10];
} //sensor data from pyrolysis experiment

void setup(){
  tslpb.begin();
  Wire.begin();
  pinMode(ClockPowerPin, OUTPUT);
  digitalWrite(ClockPowerPin, HIGH);
  tslpb.InitTSLDigitalSensors();
  rtcTime = Clock.now();
}

void loop(){
  rtcTime = Clock.now();
  calibrateTime(rtcTime);
  readPhotocells(isfirstRun);
  position = getPosition(rtcTime, pho_data);
  state_of_burt = calc_state(position);

  switch (state_of_burt) {
    case 0:
      //j.chillin'
      delay(1);
      break;
    case 1:
      //begin launch process
      launch(launchCount);
    case 2:
      //begin pyrolysis process
      pyrolysis();
  }
}



/*___FUNCTIONS___*/

float calibrateTime(DateTime rtcTime){
  /*
    FUNCTION: Uses forcast.csv to calculate seconds from launch and sync a more accurate DateTime
    PARAMETERS: None
    RETURN: Seconds since launch
  */

  Clock.setSecond(sec_calc);
  Clock.setMinute(min_calc);
  Clock.setHour(hour_calc);
  Clock.setDate(date_calc);
  Clock.setMonth(mon_calc);
  Clock.setYear(yr_calc);

}

struct readPhotocells(bool isfirstRun){
  /*
    FUNCTION: read from all 4 photocells aka the voltage
    PARAMETERS: None
    RETURN: a struct with sunset/sunrise data
  */
  firstRun = false;
  return ReadPhotocells.main(firstRun)

}


float getPosition(DateTime rtcTime, pho_data data){
  /*
    FUNCTION: Uses forcast.csv to
    PARAMETERS: None
    RETURN: list of time, lat, long, alt, moonless
  */

}

int calc_state(position pos){
  /*
    FUNCTION: Calculates the state of the satellite depending on the position
    PARAMETERS: the pos
    RETURN: 0 if not ready and 1 if ready
  */
  float sightAngle = 3;
  float satAngle = getTheta();
  if(satAngle <= sightAngle){
      launchCount ++;
      return 1;
  }else if(launchCount == 4 && position.moonless){
    //insert pyrolysis code
  }else{
    return 0;
  }

}

bool sendData(UserDataStruct_t missionData, size_t data_struct){
  /*
    FUNCTION: sends data to the bus
    PARAMETERS: the data struct within missionData and missionData itself
    RETURN: boolean for success of data sent to ground
  */
  while (!tslpb.isClearToSend()){
    delay(20);
  }
  tslpb.pushDataToNSL(missionData);
  return successToNSL; //true if successfully sent to ground
}

void readSD(char file_name[], char variable_name[]){
  /*
    FUNCTION: Returns current position struct
    PARAMETERS: the file name of the SD card you want to read
    RETURN: None
  */
  File f = SD.open(file_name);
  variable =  f.read(variable);
  SD.close();
  return variable;

}

int16_t readMag(){
  /*
    FUNCTION: read the magnetometer on the bus side
    PARAMETERS: None
    RETURN: data one after the other
  */
  magx = tslpb.readTSLDigitalSensorRaw(missionData.magnetometer_x);
  magy = tslpb.readTSLDigitalSensorRaw(missionData.magnetometer_y);
  magz = tslpb.readTSLDigitalSensorRaw(missionData.magnetometer_z);

  return [magx, magy, magz];
}

bool launch(int wireCount){
  /*
    FUNCTION: execute all launch protocall for notor design (to use rifled design remove lines with "MD" notation at the end)
    PARAMETERS: boolean for which launcher design is being used (motor or rifled design)
    RETURN: success bool
  */
  if(launchCount == 0){
      melt(1); //will melt the first tilt set of wires
      melt(2);
      ifdef(motor){
        digitalWrite(IN1_ADDR, HIGH); //motor driver is going forward
        digitalWrite(IN2_ADDR, LOW);
        delay(1000); //delay to let the motor spin
        digitalWrite(IN1_ADDR, LOW); //turn motor off
      }
  }
  melt(meltWires[launchCount][0]);
  melt(meltWires[launchCount][1]);
}

void pyrolysis(){
  /*
    FUNCTION: execute all pyrolysis protocall
    PARAMETERS: None
    RETURN: None
  */

  melt(11);
  melt(12);
  readTemp();
  readImg();
}

void melt(int wire){
  /*
    FUNCTION: helper func that melts a number of burn wires
    PARAMETERS: which burn wires to melt.... ex. [HIGH, LOW, LOW, etc.] would burn only first one
    RETURN: None
  */

  for(int i = 0, i < 10, i++){
    if(i==wire){
      digitalWrite(SER_ADDR, HIGH)
    }else{
      digitalWrite(SER_ADDR, LOW)
    }
      digitalWrite(SRCLK_ADDR, HIGH);
      digitalWrite(SRCLK_ADDR, LOW);
  }
  digitalWrite(RCLK_ADDR, HIGH);
  digitalWrite(RCLK_ADDR, LOW);

  delay(7000); //melt for 7 seconds

  for(int i = 0, i < 10, i++){
    digitalWrite(SER_ADDR, LOW);
    digitalWrite(SRCLK_ADDR, HIGH);
    digitalWrite(SRCLK_ADDR, LOW);
  }
  digitalWrite(RCLK_ADDR, HIGH);
  digitalWrite(RCLK_ADDR, LOW);

}

size_t readImg(){
  /*
    FUNCTION: helper func for reading CMOS image sensor for pyrolysis experiment
    PARAMETERS: None
    RETURN: data (not processed)
  */
}

size_t readTemp(){
  /*
    FUNCTION: helper func for reading temp sensor for pyrolysis experiment
    PARAMETERS: None
    RETURN: data (not processed)
  */
  size_t v_out;

  Wire.requestFrom(TEMP_ADDR,1); //is 1 the correct number of bits?
  while(Wire.avaliable()){
    v_out = Wire.read();
  }

  return (v_out - 400)/19.5; //see pg. 2 of datasheet --> http://ww1.microchip.com/downloads/en/DeviceDoc/20001942G.pdf
}
