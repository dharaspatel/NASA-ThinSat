/*  ________________________________________________
    Description: main file that defines all functions called in both burt and bill
    Author: Dhara Patel
    ________________________________________________*/


/*___INCLUDES___*/
#include <DS3231.h>
#include <Wire.h>

/*___DEFINES___*/
#define PHO1_ADDR PINB5 //input from photodiode 1
#define PHO2_ADDR PINB4 //input from photodiode 2
#define PHO3_ADDR PIND7 //input from photodiode 3
#define PHO4_ADDR PIND6 //input from photodiode 4

#define TEMP_ADDR PINB6 //input from temp sensor

#define SPEC_ADDR PIN?

/*_________FUNCTIONS USED IN BOTH BILL AND BURT__________*/

void begin(){
  /*
    FUNCTION: Begins communication with I2C interface and starts the DS3231 Clock
    PARAMETERS: None
    RETURN: None
  */
  Wire.begin();
  Clock.setClockMode(false);
}

float sync(DateTime rtc){
  /*
    FUNCTION: Allows the rtc to be corrected using sunset/sunrise data taken from photodiodes and onboard data
    PARAMETERS: rtc time given be crystal oscillator DS3231, which is not exactly accurate
    RETURN: exact position vector (latitude, longitude) defined by the exact time calculated
  */
}

void orient(float rotation[]){
  /*
    FUNCTION: Uses the thrusters and gyroscope located on Joe to orient the satellites in a particular direction
    PARAMETERS: A rotation matrix for the desired orientation
    RETURN: None
  */
}

/*_________FUNCTIONS USED IN BURT__________*/
int calc_state(float pos){
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

void launch(){
  /*
    FUNCTION: Triggers burn wire to launch one radar target at a time
    PARAMETERS: None
    RETURN: None
  */
}

void pyrolysis(){
  /*
    FUNCTION: Triggers pyrolysis to execute gas release once
    PARAMETERS: None
    RETURN: None
  */
}

/*_________FUNCTIONS USED IN BILL__________*/
void deorbit(){
  /*
    FUNCTION: Triggers thrusters for deorbit
    PARAMETERS: None
    RETURN: None
  */
}
