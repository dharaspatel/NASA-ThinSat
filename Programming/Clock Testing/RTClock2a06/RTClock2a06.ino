/* 
 *  Method 2a 
 *  
 *  This method will use the Arduino PCF8523 RTC to track time.
 *  
 *  The accuracy of this time will be tracked over a period of 
 *  3 days using signals from DCF77 that outputs UTC time. 
 */


//includes and declarations 
  #include "RTClib.h"
  #include "DCF77.h"
  #include "Time.h"

  #define dcf_pin 2
  #define dcf_interrupt 0

//  RTC_PCF8523 rtc; 
//  DCF77 dtc = DCF77(dcf_pin, dcf_interrupt);
//
//  long errors;
//  long elapsed;
//  time_t utc_time;
//  time_t rtc_time;
//
//  #if defined(ARDUINO_ARCH_SAMD)
//    #define Serial SerialUSB
//  #endif
//  
//
////setup that runs only once  
//void setup(){
//  //setting up the serial terminal 
//    Serial.begin(9600);
//    while( !Serial){
//      ; //waiting to connect 
//    }
//    
//  //setting up the dcf signal for utc time 
//    dtc.Start();
//    
//    utc_time = dtc.getUTCTime();
//    while(utc_time == 0){
//      utc_time = dtc.getUTCTime();
//    }
//
//  //setting up the arduino rtc
//    rtc.begin();
//    
//    //syncing it to the utc time so that they start off the same 
//    rtc.adjust(DateTime(utc_time.year(), utc_time.month(), utc_time.day(), utc_time.hour(), utc_time.minute(), utc_time.second()));
//  
//  //setting up elapsed time to timebox this experiment to 3 days 
//    elapsed = millis();
//}
//
//
////loop that runs continuously to allow for change and response 
//void loop(){
//  //continuously receiving updated UTC 
//    delay(1000); //idk why 
//    utc_time = dtc.getUTCTime();
//    
//  //continuously updating rtc 
//    rtc_time = rtc.now().unixtime(); //the unixtime makes sure rtc_time is a time_t type
//        
//  //checking for error and saving error for analysis
//    error();
//}
//
////returns the difference between UTC coming from DCF77 and arduino RTC
//long error(DateTime rtc_time, time_t utc_time){
//
//  //convert both times to total number of milliseconds 
//  long rtc_total = rtc_time.second() + rtc.
//  long utc_total = 
//
//  //returning the difference in milliseconds 
//  return DateTime()
//}
//
//
////displays the utc time
//void utcDisplay(time_t utc_time){
//  
//}
//
////displays the rtc time
//void rtcDisplay(DateTime rtc_time){
//  
//}
