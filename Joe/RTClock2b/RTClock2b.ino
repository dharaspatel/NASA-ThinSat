//Method 2b: this method does not really require any analysis of real time; it uses time differences between key events and the millis function
           //a problem with this method might be making sure the release is in the location; however, it may not be a problem for pyrolysis or target release, only bill for which location really matters 

// Date and time functions using a DS1307 RTC connected via I2C and Wire lib
#include <Wire.h>
#include "RTClib.h"

#if defined(ARDUINO_ARCH_SAMD)
// for Zero, output on USB Serial console, remove line below if using programming port to program the Zero!
   #define Serial SerialUSB
#endif

//declaring the rtc clock as the var "rtc"
RTC_PCF8523 rtc;

void setup() {
  #ifndef ESP8266
  while (!Serial); // for Leonardo/Micro/Zero
#endif

  Serial.begin(57600);
  if (! rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);
  }

  if (! rtc.initialized()) {
    Serial.println("RTC is NOT running!");
    // following line sets the RTC to the date & time this sketch was compiled
    rtc.adjust(DateTime(2020, 5, 21, 5, 12, 2)); //here we could set the time to be whatever the expected launch date, time, etc. is
                                     //right now launch day is arbitrarly May 21, 2020 at 5:12:02
  }

  //ignore this is for testing: 
  pinMode(13, OUTPUT);
}

//The elapsed var will keep track of elapsed milliseconds since the start of this program 
unsigned long elapsed = millis();

void loop() {

  //First, we need to keep track of what it thinks is real time 
  //t = 0 will be when satellites first get power

  DateTime now = rtc.now();
  Serial.print("The real time is ");
  Serial.print(now.year(), DEC);
  Serial.print('/');
  Serial.print(now.month(), DEC);
  Serial.print('/');
  Serial.print(now.day(), DEC);
  Serial.print(" ");
  Serial.print(now.hour(), DEC);
  Serial.print(':');
  Serial.print(now.minute(), DEC);
  Serial.print(':');
  Serial.print(now.second(), DEC);
  Serial.println();

  //Second, we need to keep track of the time since start of power (launch?) 
  elapsed = millis();
  Serial.println(elapsed);

  //Now, we need to set events: 
  long launch = 0; //right now we are assuming we get power at launch
  long engineOff = launch + 0; //when is the engine turned off relative to the launch? 
  long ejection = 235000 + engineOff; //we know that ejection will occur 235s (235000ms) after the engine is shut off 
  
  /*the last time triggered event is target release: 
    - happens once a day 
    - need altitude and duration data to space out ejection signals equally for the span of 4 days 
  */ 
  long target = 10000; //right now we are assuming we want to release targets 1s after launch
  
  //We need to constantly check if the elapsed time (or rt depending on what data we have) is equal to the launch time 
  if (elapsed == target){
    //for now, light up an LED everytime 
    digitalWrite(13, HIGH);

    //update so that the next target is released in a day a.k.a 86400000 milliseconds later
    target += 86400000;
  }
}
