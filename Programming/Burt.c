/*  ________________________________________________
    Description: file that controls electronics on Burt
    Author: Dhara Patel
    ________________________________________________*/

#include <DS3231.h>
#include <Wire.h>
#include <Main.h>
#include "arduino.h"

DS3231 Clock;
int l = 0; //the number of times launch has been called
int p = 0; //the number of times pyrolysis has been called
float pos; //pos of satellite
bool oriented = false;

#define LAUNCH 1;
#define PYROLYSIS 2;

void setup(){
  begin();
}

void loop(){
  rtc = Clock.getTime();
  pos = sync(rtc);
  state = calc_state(pos);
  switch (state) {
    case LAUNCH:
      if (!oriented){
        orient(angle);
      }
      launch();

    case PYROLYSIS:
      pyrolysis();
  }
}
