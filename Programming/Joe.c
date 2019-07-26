/*  ________________________________________________
    Description:  file that controls all electronics on joe
    Author: Dhara Patel

    Table of functions:
      beginJoe()                                   [x]
      getTime()                                    [x]
      calibrateTime()                              []
      readPhotocells()                             []
      getPosition()                                []
      calc_state()                                 []
      getRadarRange()                              []
      sendData()                                   [x]
      readSD()                                     []
      writeEEPROM()                                []
      readEEPROM()                                 []
      readMag()                                    [x]
    ________________________________________________*/


/*___INCLUDES___*/
#include <DS3231.h> //Clock
#include <Wire.h> //i2c
#include <Main.h> //Registers
#include <SD.h> //SD Card
#include "TSLPB.h" //NSL BUS
#include "myDataPacketStructure.h" //datapacket stuff
#include <Arduino.h> //Arduino library

DateTime rtcTime; //the current time output by the rtc
TSLPB tslpb; //bus
UserDataStruct_t missionData; //packet of mission data
float secLaunch; //seconds since launch
size_t pho_data[]; //an array of the 4 photocell data
int pho_addresses = [PHO1_ADDR, PHO2_ADDR, PHO3_ADDR, PHO4_ADDR]; //array of addresses
int state; //nothing = 0, launch = 1, pyrolysis = 2
float threshold[]; //the threshold for the sunset/sunrise calculations
int launchCount = 0;
size_t mag_data[]; //an array of x, y, z magnetometer data
struct position{
  float seconds;
  float latitude;
  float longitude;
  float altitude;
  bool moonless;
  float  inHalfOrbit[3]; //lat, long, alt in half orbit
}

struct sensors{
  size_t temperature;
  int histogram[10];
}

void setup(){
  begin();
}

void loop(){
  rtcTime = getTime();
  secLaunch = syncTime();
  readPhotocells(pho_data, threshold);
  position = getPosition(secLaunch, pho_data);
  state = calc_state(position);

  switch (state) {
    case 0:
      delay(1);
      break;
    case 1:
      //begin launch process
      launch();
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
}

DateTime getTime()
  /*
    FUNCTION: Begins communication with I2C interface, starts the DS3231 Clock, writes table to SD
    PARAMETERS: None
    RETURN: None
  */
  DatTime(clock.getYear(), clock.getYear(), clock.getDay(), clock.getHour(), clock.getMinute(), clock.getSecond());
}


float calibrateTime(){
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

size_t readPhotocells(){
  /*
    FUNCTION: read from all 4 photocells
    PARAMETERS: None
    RETURN: an array of data for each cell
  */
  for(i = 0; i<4; i++){
    Wire.requestFrom(pho_addresses[i],1);
    while (Wire.avaliable()){
      pho_data[i] = Wire.read();
    }
  }
  return pho_data;
}


float getPosition(float secLaunch, size_t pho_data){
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

void launch(){
  /*
    FUNCTION: execute all launch protocall
    PARAMETERS: None
    RETURN: None
  */

  digitalWrite(IN1_ADDR, HIGH); //motor driver is going forward 
  digitalWrite(IN2_ADDR, LOW);


}

void pyrolysis(){
  /*
    FUNCTION: execute all pyrolysis protocall
    PARAMETERS: None
    RETURN: None
  */


}

void melt(int wires[]){
  /*
    FUNCTION: melt a number of burn wires
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

}
