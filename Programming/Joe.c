/*  ________________________________________________
    Description:  file that controls all electronics on joe
    Author: Dhara Patel

    Table of functions:
      beginJoe()                                   [x]
      getTime()                                    [x]
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
#include "ReadPhotocells.c" //reading photocells
#include "ImgProcessing.c"

DS3231 Clock;
EEPROM eeprom;
DateTime rtcTime; //the current time output by the rtc
TSLPB tslpb; //bus
UserDataStruct_t missionData; //packet of mission data
float secLaunch; //seconds since launch
struct pho_data{
  long sunrises[];
  long sunsets[];
}; //sunset sunrise data
bool firstRun = true; //first photocell run
int state; //nothing = 0, launch = 1, pyrolysis = 2
float threshold[]; //the threshold for the sunset/sunrise calculations
int launchCount = 0; //the number of launchers released
bool motor = true; //using motor design?
size_t mag_data[]; //an array of x, y, z magnetometer data
struct position{
  float seconds;
  float latitude;
  float longitude;
  float altitude;
  bool moonless;
  float  inHalfOrbit[3]; //lat, long, alt in half orbit
}; //sec, lat, long, alt
struct py_data{
  size_t temperature;
  int histogram[10];
} //sensor data from pyrolysis experiment

void setup(){
  begin();
}

void loop(){
  rtcTime = Clock.now();
  calibrateTime(rtcTime);
  readPhotocells(firstRun);
  position = getPosition(rtcTime, pho_data);
  state = calc_state(position);

  switch (state) {
    case 0:
      //j.chilling
      delay(1);
      break;
    case 1:
      //begin launch process
      launch(motor);
    case 2:
      //begin pyrolysis process
      pyrolysis();
  }
}




/*___FUNCTIONS___*/

void begin(){
  /*
    FUNCTION: Begins communication with I2C interface, starts the DS3231 Clock, writes table to SD
    PARAMETERS: None
    RETURN: None
  */
  tslpb.begin();
  Wire.begin();
  pinMode(ClockPowerPin, OUTPUT);
  digitalWrite(ClockPowerPin, HIGH);
  tslpb.InitTSLDigitalSensors();
  rtcTime = Clock.now();
}

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

struct readPhotocells(bool firstRun){
  /*
    FUNCTION: read from all 4 photocells
    PARAMETERS: None
    RETURN: a struct with sunset/sunrise data
  */
  return ReadPhotocells.main(firstRun)
  firstRun = false;
}


float getPosition(DateTime rtcTime, struct pho_data){
  /*
    FUNCTION: Uses forcast.csv to
    PARAMETERS: None
    RETURN: list of time, lat, long, alt, moonless
  */
}

int calc_state(struct position){
  /*
    FUNCTION: Calculates the state of the satellite depending on the position
    PARAMETERS: the pos
    RETURN: 0 if not ready and 1 if ready
  */
  float sightAngle = 3;
  float satAngle = getTheta();
  if(satAngle <= sightAngle){
      return 1;
      launchCount ++;
  }else if(launchCount == 4 && position.moonless){
    //insert pyrolysis code
  }else{
    return 0;
  }

}

void sendData(){
  /*
    FUNCTION: sends data to the bus
    PARAMETERS: the number corresponding to the struct variable you are sending
    RETURN: None
  */
  while (!tslpb.isClearToSend()){
    delay(20);
  }
  tslpb.pushDataToNSL(missionData);
}

void readSD(char file_name[]){
  /*
    FUNCTION: Returns all of the contents of a file
    PARAMETERS: the file name of the SD card you want to read
    RETURN: None
  */
  File data_file = SD.open(file_name);
  while(data_file.avaliable()){
    return data_file.read();
  }
  data_file.close();
}

void writeEEPROM(size_t data, int address){
  /*
    FUNCTION: writes to an address on the eeprom
    PARAMETERS: the data you want to write and the address that you want to write to
    RETURN: None
  */
}

size_t readEEPROM(int address){
  /*
    FUNCTION: read an address on the eeprom
    PARAMETERS: the address you want to read from
    RETURN: the bytes of info on that address
  */
  return EEPROM.read(address);
}

size_t readMag(){
  /*
    FUNCTION: read the magnetometer on the bus side
    PARAMETERS: None
    RETURN: data one after the other
  */
  magx = tslpb.readTSLDigitalSensorRaw(Magnetometer_x);
  magy = tslpb.readTSLDigitalSensorRaw(Magnetometer_y);
  magz = tslpb.readTSLDigitalSensorRaw(Magnetometer_z);

  return magx, magy, magz;
}

void launch(bool motor){
  /*
    FUNCTION: execute all launch protocall
    PARAMETERS: boolean for which launcher design is being used (motor or rifled design)
    RETURN: None
  */
  if(motor){
    digitalWrite(IN1_ADDR, HIGH); //motor driver is going forward
    digitalWrite(IN2_ADDR, LOW);
  }

  melt([HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, LOW, LOW, LOW, LOW]);
}

void pyrolysis(){
  /*
    FUNCTION: execute all pyrolysis protocall
    PARAMETERS: None
    RETURN: None
  */

  melt([LOW, LOW, LOW, LOW, LOW, LOW, HIGH, HIGH, HIGH, HIGH]);
  readTemp();
  ImgProcessing.main(readImg());
}

void melt(int wires[]){
  /*
    FUNCTION: helper func that melts a number of burn wires
    PARAMETERS: which burn wires to melt.... ex. [HIGH, LOW, LOW, etc.] would burn only first one
    RETURN: None
  */

  for(int i = 0, i < 10, i++){
    digitalWrite(SER_ADDR, wires[i])
    digitalWrite(SRCLK_ADDR, HIGH);
    digitalWrite(SRCLK_ADDR, LOW);
  }
  digitalWrite(RCLK_ADDR, HIGH);
  digitalWrite(RCLK_ADDR, LOW);

  delay(10000);
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
