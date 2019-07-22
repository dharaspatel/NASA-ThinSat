/*
 *  Method 2a
 *
 *  This method will use the Arduino PCF8523 RTC to track time.
 *
 *  The accuracy of this time will be tracked over a period of
 *  3 days using signals from DCF77 that outputs UTC time.
 */

//includes and declarations
  #include <EEPROM.>

  #include <RTClib.h>

  #include <Time.h>
  #include <TimeLib.h>

  #include <DCF77.h>

  #define dcf_pin 2
  #define dcf_interrupt 0
  #define addr 0

  DCF77 dtc = DCF77(dcf_pin, dcf_interrupt);
  EEPROM eeprom;

  long errors;
  long elapsed;

void setup() {
  //setting up the serial terminal
    Serial.begin(9600);
    while( !Serial){
      //waiting to connect
    }

  //setting up the dcf signal for utc time
    dtc.Start();
    setTime(dtc.getUTCTime());

  //setting up the arduino rtc
    rtc.begin();

    //syncing it to the utc time so that they start off the same
    rtc.adjust(DateTime(year(), month(), day(), hour(), minute(), second()));

  //setting up elapsed time to timebox this experiment to 3 days
    elapsed = 0;

  //print to confirm initial state
  Serial.println("Real time: " + getTime());
  Serial.println("Arduino time: " + rtc.now().unixtime())

}

void loop() {
  //for the duration of the experiment (3 days)...
  while(elapsed <= 25920000){
      elapsed = millis();

      //continuously receiving updated UTC and syncing it
        delay(1000); //this might not be neccessary
        time_t dtc_time = dtc.getUTCTime();
        setTime(dtc_time);

      //continuously updating rtc
        time_t rtc_time = rtc.now().unixtime(); //the unixtime makes sure rtc_time is a time_t type

      //checking for error and saving error for analysis later
        store(error(rtc_time, dtc_time));

      //Display the times to Serial for debugging
        Serial.println("Real time: " + dtc_time);
        Serial.println("Arduino time: " + rtc_time);

        //Serial.print(elapsed);
        Serial.println("Elapsed time: " + elapsed);
  }

}

//returns the difference between UTC coming from DCF77 and arduino RTC
long error(time_t rtc_time, time_t dtc_time){

 //how should we compare and return error?

 //returning the difference in milliseconds
 return DateTime()
}

//stores the error in the Arduino's eeprom
void store(long val){
  eeprom.write(addr, val);
  addr = addr + 1;
}
