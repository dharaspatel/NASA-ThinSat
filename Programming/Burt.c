/*  ________________________________________________
    Description: file that controls electronics on Burt
    Author: Dhara Patel

    Table of Functions:
      getState()
      launchMotors()
      launchBurn()
      gasRelease()
      getTemp()
      getProcessedImg()
    ________________________________________________*/

#include <DS3231.h>
#include <Wire.h>
#include <Main.h>
#include <Arduino.h>



void setup(){
}

void loop(){
}

/*___FUNCTIONS___*/

int getState(float pos){
  /*
    FUNCTION: Calculates the state of the satellite (launch, pyrolysis) by sorting into small ranges of positions
    PARAMETERS: Current position
    RETURN: An integer that represents the state (launch = 1 and pyrolysis = 2)
  */
  switch (pos) {
    case launchMIN ... launchMAX:
      return 1;
    case pyMIN ... pyMAX:
      return 2;
  }
}

void launchMotors(){
  digitalWrite(IN1_ADDR,HIGH);
  digitalWrite(IN2_ADDR,HIGH);

}

void launchBurn(){

}

void gasRelease(){

}

size_t getTemp(){
  /*
    FUNCTION: gets data from the temp sensor located on burt after gas is released
    PARAMETERS: None
    RETURN: temp sensor data
  */
  Wire.requestFrom(TEMP_ADDR,1); //is 1 the correct number of bits?
  while(Wire.avaliable()){
    return Wire.read();
  }
}

size_t getProcessedImg(){

}
