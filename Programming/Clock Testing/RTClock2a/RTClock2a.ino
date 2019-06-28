
//Method 2a: This method uses the rtc already on the arduino to keep track of real time 
            //a problem with this may be that it is very inaccurate (this program is currently testing that) 
            //to avoid a gradual increase in inaccuracy, we can have the program only start time when it receives a signal from the BUS 

//includes and declarations 
// Date and time functions using a DS1307 RTC connected via I2C and Wire lib
#include <Wire.h>
#include "RTClib.h"
//RTC_PCF8523 rtc; //declaring the rtc clock as the var "rtc"
//
//#if defined(ARDUINO_ARCH_SAMD)
//// for Zero, output on USB Serial console, remove line below if using programming port to program the Zero!
//   #define Serial SerialUSB
//#endif

#include "Time.h";
#include "DCF77.h";
//DCF77 dcf;
//
//int evalPeriod = 60*60*24*3; //we will be testing change in error for a period of 3 days 
//
//void setup() {
//  Serial.begin(57600);
//  //wait until  BUS signal is received (faking the signal for now) 
//  delay(1000);
//  digitalWrite(A4,1);
//  Serial.println("BUS signal received. Now beginning experiment!");
//
//  if (1 == digitalRead(A4){
//  //start arduino time (could also set to manually maybe to predicted launch time?) 
//    rtc.begin();
//
//    //print start time
//    Serial.print("The arduino time is "); 
//    Serial.print(rtc.now().hour(), DEC);
//    Serial.print(':');
//    Serial.print(rtc.now().minute(), DEC);
//    Serial.print(':');
//    Serial.print(rtc.now().second(), DEC);
//    
//  //obtain UTC using DCF77 library wait till time updates correctly
//  dtc.Start();
//  long utcTime = dtc.getTime();
//  while(utcTime != 0){
//    utcTime = dtc.getTime();
//  }
//
//  //normalize them so that we can track change in difference between them
//    long error = 
//  }
//}
//
//void loop() {
//  //for the evalPeriod keep testing 
//  tic = millis();
//  while(tic !=evalPeriod){
//    //print times 
//  
//    //calculate difference between real and arduino 
//  
//    //store difference to analyze later 
//  }
//}
