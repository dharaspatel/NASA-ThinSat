/*  ________________________________________________
    Description:  file that controls all electronics on joe
    Author: Dhara Patel

    Table of functions:
      beginJoe()                                   [x]
      getTime()                                    [x]
      syncTime()                                   []
      readPhotocells()                             []
      getPosition()                                []
      calc_state()                                 []
      getRadarRange()                              []
      sendToBUS()                                  [x]
      readSD()                                     []
      writeEEPROM()                                []
      readEEPROM()                                 []

    ________________________________________________*/


/*___INCLUDES___*/
#include <DS3231.h> //Clock
#include <Wire.h> //i2c
#include <Main.h> //Registers
#include <SD.h>
#include "TSLPB.h"
#include "myDataPacketStructure.h"
#include <Arduino.h>

DateTime rtcTime; //the current time output by the rtc
float secLaunch; //seconds since launch
size_t pho_data[]; //an array of the 4 photocell data
int pho_addresses = [PHO1_ADDR, PHO2_ADDR, PHO3_ADDR, PHO4_ADDR]; //array of addresses
int state; //nothing = 0, launch = 1, pyrolysis = 2
float threshold[]; //the threshold for the sunset/sunrise calculations
int launchCount = 0;

struct position{
  float seconds;
  float latitude;
  float longitude;
  float altitude;
  bool moonless;
  float  inHalfOrbit[3]; //lat, long, alt in half orbit

}

void setup(){
  beginJoe();
}/* value */

void loop(){
  rtcTime = getTime();
  secLaunch = syncTime();
  readPhotocells(pho_data, threshold);
  position = getPosition(secLaunch, pho_data);
  state = calc_state(position);

  switch (state) {
    case 0:
      //do noting; wait
      break;
    case 1:
      //begin launch process
      launch();
    case 2:
      //begin pyrolysis process
      pyrolysis();
  }
  }
}




/*___FUNCTIONS___*/

void beginJoe(){
  /*
    FUNCTION: Begins communication with I2C interface, starts the DS3231 Clock, writes table to SD
    PARAMETERS: None
    RETURN: None
  */
  Wire.begin();
  pinMode(ClockPowerPin, OUTPUT);
  digitalWrite(ClockPowerPin, HIGH);
}

DateTime getTime()
  /*
    FUNCTION: Begins communication with I2C interface, starts the DS3231 Clock, writes table to SD
    PARAMETERS: None
    RETURN: None
  */
  DatTime(clock.getYear(), clock.getYear(), clock.getDay(), clock.getHour(), clock.getMinute(), clock.getSecond());
}


float syncTime(){
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

int isLaunch(struct position){
  /*
    FUNCTION: Calculates the state of the satellite depending on the position
    PARAMETERS: the pos
    RETURN: 0 if not ready and 1 if ready
  */
  radar = [42.62328, 288.511846, 115.69]; //lat and long of radar
  radarMin[], radarMax[] = getRadarRange(position.altitude);//some equation based on the altitude of the satellite can calculate the range of the radar

  if(position.latitude > radarMin.latitude && position.latitude < radarMax.latitude){
    if(position.longitude > radarMin.longitude && position.longitude < position.longitude){
      return 1;
      launchCount ++;
    }
  }else if(launchCount == 4 && position.moonless){
    //insert pyrolysis code
  }else{
    return 0;
  }

}

float getRadarRange(float altitude){
  /*
    FUNCTION: Helper func that takes in the altitude to approximate the coordinating range of latitudes and longitudes
    PARAMETERS: the altitude
    RETURN: two arrays comtaining minimumn and maximum latitude and longitude values
  */
}

void sendToBUS(size_t data){
  /*
    FUNCTION: sends data to the bus
    PARAMETERS: an object a size of any number of bytes
    RETURN: None
  */
  Wire.beginTransmission(TX_ADDR);
  Wire.write(data);
  Wire.endTransmission();
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
