/*  ________________________________________________
    Description: file that controls electronics for Bill
    Author: Dhara Patel
    ________________________________________________*/

#include <DS3231.h>
#include <Wire.h>
#include <Main.h>

DS3231 Clock;

void setup(){
  begin();
}

void loop(){
  pos = sync();
  state = calc_state();

  if (state == deorbit){
    deorbit();
  }
}

/*_________FUNCTIONS USED IN BOTH BILL AND BURT__________*/

void orient(float rotation[]){
  /*
    FUNCTION: Uses the thrusters and gyroscope located on Joe to orient the satellites in a particular direction
    PARAMETERS: A rotation matrix for the desired orientation
    RETURN: None
  */
}

void set_pin_mode(){
  /*
    FUNCTION: Sets the mode of every pin
    PARAMETERS:
    RETURN: None
  */
  pinMode();
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
  digitalWrite(13, HIGH); //voltage to 3.7V
  delay(10000);
  digitalWrite(13, LOW);
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
