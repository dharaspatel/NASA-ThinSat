/*  ________________________________________________
    Description: main file that controls electronics on Burt
    Author: Dhara Patel
    ________________________________________________*/

#include <DS3231.h>
#include <Wire.h>

DS3231 Clock;
int l = 0; //the number of times launch has been called
int p = 0; //the number of times pyrolysis has been called
float pos; //pos of
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
        orient();
      }
      launch();

    case PYROLYSIS:
      pyrolysis();
  }
}

//begins I2C interface and RTC clock
void begin(){
  Wire.begin();
  Clock.setClockMode(false);
}

//syncs time to altitude estimate based on sunrise/set data to get location and alt
float sync(){
//returns accurate position
}

//orient burt properly
void orient(){

}

//calculates the state of the sat based on the position
int calc_state(){

}
