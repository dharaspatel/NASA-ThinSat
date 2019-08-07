/*  ________________________________________________
    Description: header file for Burt.c (contains all function prototypes)
    Author: Dhara Patel
    ________________________________________________*/

#ifndef Burt_h
#define Burt_h

private:

public:
  int getState(float);
  bool launchMotors();
  bool launchBurn();
  bool gasRelease();
  size_t getTemp();
  size_t getProcessedImg();

#endif
