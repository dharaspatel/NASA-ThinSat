
// Overall Comments 
// Make a CMakeLists.txt file and use cmake, or make a makefile (no extension, just create a new file called makefile or Makefile) in order to compile your code. The makefile describes how your files are related to eachother
//    https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html#creating
// All of your .c files should have a .h file → For example, Joe.c should have a Joe.h file. These header files should contain prototypes for all of the functions/classes in the .c file. 
//    https://www.tutorialspoint.com/cprogramming/c_header_files
// Your code for different satellites should probably be in different folders each with their own makefile so it’s easy to load onto their respective boards. 
// Don’t ever include .c files → They should each have a .h file that you include
//    See lines "#include "ReadPhotocells.c""
// You need to be very careful about blocking operations. You have a lot of them in this file. The main loop needs to run reliably and not be blocked for long.



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
#include "ReadPhotocells.c" //reading photocells                              // Only include .h files, not .c
#include "ImgProcessing.c"                                                    // Same here

DS3231 Clock;
EEPROM eeprom;                                                                // Not sure where the eeprom type comes from
DateTime rtcTime; //the current time output by the rtc                        // I think this comes from RTClib, which isn't included
TSLPB tslpb; //bus
UserDataStruct_t missionData; //packet of mission data
float secLaunch; //seconds since launch
struct pho_data{
  long sunrises[];
  long sunsets[];
}; //sunset sunrise data
bool firstRun = true; //first photocell run                                   // Consider renaming to isFirstRun or something that indicates it's a state
int state; //nothing = 0, launch = 1, pyrolysis = 2                           // state is a very generic name, make it more specific. Long variable names aren't bad if it's more clear
float threshold[]; //the threshold for the sunset/sunrise calculations
int launchCount = 0; //the number of launchers released                       // All launchers are released at once, so this doesn't do what it's supposed to
bool motor = true; //using motor design?                                      // Again, not clear that this is a state. You should do a #define MOTOR, and then use ifdef statements to see if that's the current implementation
size_t mag_data[]; //an array of x, y, z magnetometer data
struct position{
  float seconds;
  float latitude;
  float longitude;
  float altitude;
  bool moonless;                                                              // <---  Why is this part of the postion struct? It seems to be derived...
  float  inHalfOrbit[3]; //lat, long, alt in half orbit                       // <-╵
}; //sec, lat, long, alt
struct py_data{
  size_t temperature;                                                          // Why is a size_t used here instead of a float or int? It makes the code less clear
  int histogram[10];
} //sensor data from pyrolysis experiment

void setup(){                                                                  // Begin shouldn't exist. Just put everything in begin in setup. 
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
      //j.chillin'
      delay(1);
      break;
    case 1:                                                                     // They should all have break statements after stuff is done
      //begin launch process
      launch(motor);                                                            // Also here the motor should be an ifdef rather than a parameter
                                                                                // You launch all of the targets at once. We need an additional sub state
                                                                                // to specify which one to launch. We're launching in 4 consecutive orbits 
                                                                                // and need launch to be a non-blocking operation so that postiiton can update. 
    case 2:
      //begin pyrolysis process
      pyrolysis();
  }
}




/*___FUNCTIONS___*/

void begin(){                                                                   // The clock needs to have it's true time set at some point with a separate script, which never happens. 
                                                                                // Every other operation (when the satellite is actually running) should just read the clock
  /*
    FUNCTION: Begins communication with I2C interface, starts the DS3231 Clock, writes table to SD
    PARAMETERS: None
    RETURN: None
  */
  tslpb.begin();
  Wire.begin();
  pinMode(ClockPowerPin, OUTPUT);                                               // ClockPowerPin doesn't exist... and even if it did you should never need to power the
                                                                                // clock on. It should always be on...
  digitalWrite(ClockPowerPin, HIGH);
  tslpb.InitTSLDigitalSensors();
  rtcTime = Clock.now();
}

float calibrateTime(DateTime rtcTime){                                          // You don't return anything in this function, so it should be void
  /*
    FUNCTION: Uses forcast.csv to calculate seconds from launch and sync a more accurate DateTime
    PARAMETERS: None                                                           // This isn't true. Your doc strings are all out of date it seems
    RETURN: Seconds since launch
  */

  Clock.setSecond(sec_calc);                                                   // I don't know what these are. sec_calc etc. don't seem to exist
  Clock.setMinute(min_calc);                                                   // The functions setSecond, setMinute etc. also don't seem to exist (from 
  Clock.setHour(hour_calc);                                                    // what I've seen of the DS3231 library, although I could be missing something)
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
  firstRun = false;                                                            // This will never get called since it's after the return statement.
}


float getPosition(DateTime rtcTime, struct pho_data){                          // Again, see below ↴
  /*
    FUNCTION: Uses forcast.csv to
    PARAMETERS: None
    RETURN: list of time, lat, long, alt, moonless
  */
}

int calc_state(struct position){                                               // You can't not have no argument name. "postition" is the type, not the name of the argument.
                                                                               // Try something like "struct position pos" where pos is the argument name
  /*
    FUNCTION: Calculates the state of the satellite depending on the position
    PARAMETERS: the pos
    RETURN: 0 if not ready and 1 if ready
  */
  float sightAngle = 3;
  float satAngle = getTheta();
  if(satAngle <= sightAngle){
      return 1;
      launchCount ++;                                                           // Again, this never gets incremented.
  }else if(launchCount == 4 && position.moonless){
    //insert pyrolysis code
  }else{
    return 0;
  }

}

void sendData(){                                                                // This should maybe return a success/failure status, and have a timeout default argument
  /*
    FUNCTION: sends data to the bus
    PARAMETERS: the number corresponding to the struct variable you are sending // This parameter doesn't exist. 
                                                                                // There should also be a parameter for the data. Pulling "missionData" from globals is
                                                                                // bad practice
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
  File data_file = SD.open(file_name);                                         // You need to do SD.begin(CS_PIN_NUM) before reading the SD card
  while(data_file.avaliable()){                                                // This loop runs once
    return data_file.read();                                                   // This will return one line. Also, returning an entire file
                                                                               // is not possible with the amount of ram we have. You should have a way to look
                                                                               // up a specific time/pose in a file to see it's value
  }
  data_file.close();                                                           // This never gets called
}

void writeEEPROM(size_t data, int address){
  /*
    FUNCTION: writes to an address on the eeprom
    PARAMETERS: the data you want to write and the address that you want to write to
    RETURN: None
  */
}

size_t readEEPROM(int address){                                                 // This function doesn't seem to work. First, why a size_t? Second the amount of bytes to 
                                                                                // read isn't specified (unless you just want to read one byte. Third, a EEPROM.read seems like
                                                                                // the exact same function, so why not just use that? 
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
  magx = tslpb.readTSLDigitalSensorRaw(Magnetometer_x);                         // magx was never declared/has no type. Also, why does this function return a size_t and not an array?
  magy = tslpb.readTSLDigitalSensorRaw(Magnetometer_y);
  magz = tslpb.readTSLDigitalSensorRaw(Magnetometer_z);

  return magx, magy, magz;                                                      // A function can only return one value, so this won't work.
}

void launch(bool motor){
  /*
    FUNCTION: execute all launch protocall
    PARAMETERS: boolean for which launcher design is being used (motor or rifled design)
    RETURN: None
  */
  if(motor){                                                                     // Replace with ifdef here
    digitalWrite(IN1_ADDR, HIGH); //motor driver is going forward
    digitalWrite(IN2_ADDR, LOW);
  }                    
                                                                                 // There needs to be a delay to wait for the motor to spin up
  melt([HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, LOW, LOW, LOW, LOW]);                // We're not  going melt more than one wire at a time
}

void pyrolysis(){
  /*
    FUNCTION: execute all pyrolysis protocall
    PARAMETERS: None
    RETURN: None
  */
                                                                                 // Again, one melt at a time, and in consecutive orbits.
  melt([LOW, LOW, LOW, LOW, LOW, LOW, HIGH, HIGH, HIGH, HIGH]);
  readTemp();                                                                    // This doesn't do anything (the temperature returned isn't used)
  ImgProcessing.main(readImg());                                                 // This also doens't do anything... the information needs to be sent
                                                                                 // somewhere. 
}

void melt(int wires[]){
  /*
    FUNCTION: helper func that melts a number of burn wires
    PARAMETERS: which burn wires to melt.... ex. [HIGH, LOW, LOW, etc.] would burn only first one
    RETURN: None
  */

  for(int i = 0, i < 10, i++){                                                    // The magic number 10 should be passed into the function (we're not going to
                                                                                  // be melting more than one wire at a time anyways)
                                                                                  // In all events, you should probably use this library or something like it
                                                                                  // anyways
                                                                                  // https://github.com/Simsso/ShiftRegister74HC595
    digitalWrite(SER_ADDR, wires[i])
    digitalWrite(SRCLK_ADDR, HIGH);
    digitalWrite(SRCLK_ADDR, LOW);
  }
  digitalWrite(RCLK_ADDR, HIGH);
  digitalWrite(RCLK_ADDR, LOW);

  delay(10000);                                                                    // What does this do? You should clarify that this is the melt time and make it an 
                                                                                   // argument for the function
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
  size_t v_out;                                                                 // This shouldn't be a size_t, but a uint or an int 
                                                                                // (since it's read from the Analog to Digital Converter which is 10 bit)
                                                                                // https://www.tutorialspoint.com/cprogramming/c_data_types

  Wire.requestFrom(TEMP_ADDR,1); //is 1 the correct number of bits?             // Why are you using wire? It's not an I2C device... just read the voltage
  while(Wire.avaliable()){
    v_out = Wire.read();
  }

  return (v_out - 400)/19.5; //see pg. 2 of datasheet --> http://www.microchip.com/downloads/en/DeviceDoc/20001942G.pdf
}
