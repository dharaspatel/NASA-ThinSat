/*  ________________________________________________
    Description: reads the photocells and interprets their data; returns a struct with sunrise and sunset data
    Author: Justin Kunimune

    Table of Functions:
      setup()
      checkForSunwend()
    ________________________________________________*/

#include "REGS.h" //registers

const int PHOTODIODES[] = {PHO1_ADDR, PHO2_ADDR, PHO3_ADDR, PHO4_ADDR};
const int NUM_PHOTODIODES = 4;
const int SUN_THRESHOLD = 100;
const int SUN_MEMORY_SIZE = 6;
const long MIN_NIGHT_LENGTH = 10000; // minimum number of milliseconds in

long sunrises[SUN_MEMORY_SIZE]; // the last few sunrises
long sunsets[SUN_MEMORY_SIZE]; // the last few sunsets
long sunsetCandidate; // the last thing that might have been a sunset (we're not sure yet), or -1 if we're not considering right now
bool isBright; // is the sun visible right now?
bool isDay; // is it daytime right now?

//only run the first time
void set_up() {
  for (int i = 0; i < NUM_PHOTODIODES; i ++)
    pinMode(PHOTODIODES[i], INPUT);

  for (int i = 0; i < SUN_MEMORY_SIZE; i ++) {
    sunrises[i] = -1;
    sunsets[i] = -1;
  }
}

void checkForSunwend() {
  isBright = false;
  for (int i = 0; i < NUM_PHOTODIODES; i ++)
    if (analogRead(PHOTODIODES[i]) > SUN_THRESHOLD)
      isBright = true; // are any of the photocells receiving?

  if (isBright && !isDay) { // if you see light when you had previously thought it to be night
    for (int i = 0; i < SUN_MEMORY_SIZE-1; i ++)
      sunrises[i] = sunrises[i+1];
    sunrises[SUN_MEMORY_SIZE-1] = millis(); // this is a sunrise
    isDay = true; // it is now definitely day
  }
  else if (!isBright && isDay) { // if you see no light when you had previously thought it to be day
    if (sunsetCandidate == -1) // if there is no sunset candidate
      sunsetCandidate = millis(); // start considering that this might be a sunset
    else { // if there is a candidate, how long have we been considering it?
      if (millis() - sunsetCandidate >= MIN_NIGHT_LENGTH) { // A while?
        for (int i = 0; i < SUN_MEMORY_SIZE-1; i ++)
          sunsets[i] = sunsets[i+1];
        sunsets[SUN_MEMORY_SIZE-1] = sunsetCandidate; // I think it's a true sunset.
        sunsetCandidate = -1; // It is a candidate no longer.
        isDay = false;
      }
      else { // Not that long yet?
      } // Ignore. Keep waiting to see what happens next.
    }
  }
  else if (isBright && isDay) { // if you see light and already thought it was day
    sunsetCandidate = -1; // then I guess any sunset candidate you were considering is now definitely a fake.
  }
}

struct main(bool firstRun){
  if(firstRun == true){
    set_up();
  }
  checkForSunwend()
  struct pho_data{
    sunsets;
    sunrises;
  }
  return pho_data;
}
