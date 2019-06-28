/*  ________________________________________________
    Description: main fill that controls electronics for Bill
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
