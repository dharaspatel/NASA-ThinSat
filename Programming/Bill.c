/*  ________________________________________________
    Description: file that controls electronics for Bill
    Author: Dhara Patel
    ________________________________________________*/

#include <DS3231.h>
#include <Wire.h>
#include <Main.h>
#include <linterp.h>
#include <spline.h>


#define NUM_PHOTODIODES 4;
#define SUN_THRESHOLD 100;
#define MIN_NIGHT_LENGTH 10000; // minimum number of milliseconds of a night
#define SUN_MEMORY_SIZE 9
#define NUM_INTERP_POINTS 9


DS3231 Clock;

int launchDate; // the index of the day we launched (-1 if we're not sure yet)
long sunrises[SUN_MEMORY_SIZE]; // the last few sunrises
long sunsets[SUN_MEMORY_SIZE]; // the last few sunsets
long sunsetCandidate; // the last thing that might have been a sunset (we're not sure yet), or -1 if we're not considering right now
bool isBright; // is the sun visible right now?
bool isDay; // is it daytime right now?#define SUN_MEMORY_SIZE 9
int orbit; // the index of the current rise-to-rise orbit (the zeroth is the incomplete one that includes launch)


struct Location {
  float latitude;
  float longitude;
  float altitude;
}


void setup(){
  begin();

  for (int i = 0; i < SUN_MEMORY_SIZE; i ++) {
    sunrises[i] = -1;
    sunsets[i] = -1;
  }
}


void loop(){
  pos = sync();
  checkForSunwend();
  state = calc_state();

  if (state == deorbit){
    deorbit();
  }
}


/*_________FUNCTIONS USED IN BOTH BILL AND BURT__________*/

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

void checkForSunwend() {
  isBright = false;
  for (int i = 0; i < NUM_PHOTODIODES; i ++)
    if (analogRead(PHOTODIODES[i]) > SUN_THRESHOLD)
      isBright = true; // are any of the photocells receiving?

  if (isBright && !isDay) { // if you see light when you had previously thought it to be night
    for (int i = 0; i < SUN_MEMORY_SIZE-1; i ++)
      sunrises[i] = sunrises[i+1];
    sunrises[SUN_MEMORY_SIZE-1] = millis(); // this is a sunrise // TODO: read the RTC
    isDay = true; // it is now definitely day
  }
  else if (!isBright && isDay) { // if you see no light when you had previously thought it to be day
    if (sunsetCandidate == -1) // if there is no sunset candidate
      sunsetCandidate = millis(); // start considering that this might be a sunset // TODO: read the RTC
    else { // if there is a candidate, how long have we been considering it?
      if (millis() - sunsetCandidate >= MIN_NIGHT_LENGTH) { // A while? // TODO: read the RTC
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

void getCoordinates(long t){
  /*
    FUNCTION: Estimates the location at the given time
    PARAMETERS: t, the time of interest
    RETURN: {latitude, longitude, altitude}
    PRECONDITION: t should be in the current orbit for a semblance of accuracy
  */
  long sunsetsExp[NUM_ORBITS]; // TODO load expected observations from SD card
  long sunrisesExp[NUM_ORBITS];

  float time_0[]; // TODO load expected coordinates from SD card
  float latitude_0[];
  float longitude_0[];
  float altitude_0[];

  float latCoefs[NUM_ORBITS][NUM_INTERP_POINTS][2*SUN_MEMORY_SIZE]; // TODO load parameter coefficients
  float lonCoefs[NUM_ORBITS][NUM_INTERP_POINTS][2*SUN_MEMORY_SIZE];
  float altCoefs[NUM_ORBITS][NUM_INTERP_POINTS][2*SUN_MEMORY_SIZE];
  float rtcCoefs[NUM_ORBITS][NUM_INTERP_POINTS][2*SUN_MEMORY_SIZE];

  float latInterp[NUM_INTERP_POINTS]; // initialize parameters
  for (int k = 0; k < NUM_INTERP_POINTS; k ++)
    latInterp[k] = 0;
  float lonInterp[NUM_INTERP_POINTS];
  for (int k = 0; k < NUM_INTERP_POINTS; k ++)
    lonInterp[k] = 0;
  float altInterp[NUM_INTERP_POINTS];
  for (int k = 0; k < NUM_INTERP_POINTS; k ++)
    altInterp[k] = 0;
  float driftGuess = 0;

  for (int l = 0; l < SUN_MEMORY_SIZE; l ++) { // do the linear regression thing to get the actual parameters
    int j = orbit - SUN_MEMORY_SIZE + l;
    if (orbit - SUN_MEMORY_SIZE + l >= 0) {
      for (int k = 0; k < NUM_INTERP_POINTS; j ++) {
        latInterp[k] += latCoefs[orbit][k][2*l]   * (sunsets[l] - sunsetsExp[j]);
        latInterp[k] += latCoefs[orbit][k][2*l+1] * (sunrises[l] - sunrisesExp[j]);
        lonInterp[k] += lonCoefs[orbit][k][2*l]   * (sunsets[l] - sunsetsExp[j]);
        lonInterp[k] += lonCoefs[orbit][k][2*l+1] * (sunrises[l] - sunrisesExp[j]);
        altInterp[k] += altCoefs[orbit][k][2*l]   * (sunsets[l] - sunsetsExp[j]);
        altInterp[k] += altCoefs[orbit][k][2*l+1] * (sunrises[l] - sunrisesExp[j]);
        driftGuess += rtcCoefs[orbit][2*l]   * (sunsets[l] - sunsetsExp[j]);
        driftGuess += rtcCoefs[orbit][2*l+1] * (sunrises[l] - sunrisesExp[j]);
      }
    }
  }

  float tInterp[NUM_INTERP_POINTS];
  for (int k = 0; k < NUM_INTERP_POINTS; k ++)
    tInterp[k] = (sunrisesExp[orbit-1]-sunrisesExp[orbit])/(NUM_INTERP_POINTS-1)*k + sunrisesExp[orbit-1];

  Location loc;
  loc.latitude =
    linterp(time_0, latitude_0,  t - driftGuess) +
    spline1_c(&tInterp, &latInterp, &NUM_INTERP_POINTS, &(t - driftGuess), &loc.latitude, &1);
  loc.longitude =
    linterp(time_0, longitude_0, t - driftGuess) +
    spline1_c(&tInterp, &latInterp, &NUM_INTERP_POINTS, &(t - driftGuess), &loc.latitude, &1);
  loc.altitude =
    linterp(time_0, altitude_0,  t - driftGuess) +
    spline1_c(&tInterp, &latInterp, &NUM_INTERP_POINTS, &(t - driftGuess), &loc.latitude, &1);
  return loc;
}


float linterp(float xi[], float yi[], int ni, float xo) {
  /*
    FUNCTION: Linearly interpolates onto a sorted vector of values
    PARAMETERS: xi and yi, the given data, ni, their length, and xo, the x at which the y is desired
    RETURN: yi
    PRECONDITION: xi is sorted
  */
  int min = 0; // first, do a binary search
  int max = ni;
  while (max - min > 1) {
    guess = (max + min)/2;
    if (xo < xi[guess])
      max = guess;
    else
      min = guess;
  }
  return (xo - xi[min]) / (xi[max] - xi[min]) * (yi[max] - yi[min]) + yi[min]; // then do some multiplication
}
