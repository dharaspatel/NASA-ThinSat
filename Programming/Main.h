/*  ________________________________________________
    Description: main file that defines all functions called in joe, burt, and bill
    Author: Dhara Patel
    ________________________________________________*/


/*___INCLUDES___*/
#include <DS3231.h>
#include <Wire.h>
#include <SD.h>
#include "TSLPB.h"
#include "myDataPacketStructure.h"

/*___ADDRESSES___*/

//input = data to atmega
//output = data from atmega
//addesses are defined in order of pin number on atmega
#define SQW_ADDR PINE6 //input of sqare wave from DCF --1
#define PHO3_ADDR PINB0 //input from photodiode 3 --8
#define TMR_RST_ADDR PORTB7 //output to reset DCF77 rtc chip --12
#define TX_ADDR PORTD2 //output data to NSL BUS --20
#define RX_ADDR PIND3 //input data from NSL BUS --21
#define WC_ADDR PORTD5 //output to write to EEPROM --22
#define PHO4_ADDR PIND4 //input from photodiode 4 --25
#define PHO1_ADDR PIND6 //input from photodiode 1 --26
#define PLED1_ADDR PORTD7 //output diagnostic led signal --27
#define PLED3_ADDR PORTB4 //output diagnostic led signal --28
#define BUSY_ADDR PINB5 //input busy signal from NSL BUS --29
//pin 30?? serial?? what?
#define STBY_ADDR PORTC6 //output for standby for NSL BUS --31
#define CS_IMG_ADDR PORTC7 //output to burt for image sensor --32
#define TEMP_ADDR PINE2 //input from burt's temperature sensor --33
#define PHO2_ADDR PINF7 //input from photodiode 2 --36
#define IN2_ADDR PORTF6 //output to motordriver on burt --37
#define IN1_ADDR PORTF5 //output to motordriver on burt --38
#define RCLK_ADDR PORTF4 //output of register clock for shift regs on burt --39
#define SRCLK_ADDR PORTF1 //output of serial clock for shift regs on burt --40
#define CS_SD_ADDR PORTF0 //chip select for SD SPI communication --41


#define DCF_ADDR D0h //device address for dcf77
#define EEPROM_ADDR A //device address for eeprom

//DCF77 REGISTER ADDRESSES
#define SEC_ADDR 0x0h
#define MIN_ADDR 0x1h
#define HOUR_ADDR 0x2h
#define DATE_ADDR 0x4h
#define MON_ADDR 0x5h
#define YEAR_ADDR 0x6h


/*___DECLARATIONS___*/
DCF77 rtc = DCF77(pin, interrupt);
EEPROM eeprom;
uint8_t pho_data[PHO1_ADDR, PHO2_ADDR, PHO3_ADDR, PHO4_ADDR];

/*_________FUNCTIONS USED IN JOE__________*/
void begin(){
  /*
    FUNCTION: Begins communication with I2C interface, starts the DS3231 Clock
    PARAMETERS: None
    RETURN: None
  */
  Wire.begin();

  Clock.setClockMode(false);
  rtc.begin();

  SD.begin(2); //cs pin = 2
  write_SD(table); //saves data table to SD card
}

DateTime getTime()
  char raw_time [7]; //array for the raw bytes
  int raw_time_counter = 0;
  Wire.requestFrom(DCF_ADDR,7); //order of bits: sec, min, hour, day, date, mon, yr
  while(Wire.avaliable()){
    raw_time[raw_time_counter] = Wire.read();
    raw_time_counter ++;
  }
  return DateTime(raw_time[6],raw_time[5],raw_time[3],raw_time[2],raw_time[1],raw_time[0])
}

float sync(DateTime time){
  /*
    FUNCTION: Allows the rtc to be corrected using sunset/sunrise data taken from photodiodes and onboard data
    PARAMETERS: rtc time given be crystal oscillator DS3231, which is not exactly accurate
    RETURN: exact position vector (latitude, longitude) defined by the exact time calculated
  */
  DateTime corrected_time =
  rtc.adjust(corrected_time);
  //TODO: Code for syncing with photodiode data
}

void sendBUS(uint8_t data){
  Wire.beginTransmission(TX_ADDR);
  Wire.write(data);
  Wire.endTransmission();
}

boolean check_busy(){
  Wire.requestFrom(BUSY_ADDR,1);
  if(Wire.read() == 'HIGH'){
    return false;
  }
  else{
    return true
  }
}

void write_SD(uint8_t data, char file_name[]){
  File data_file = SD.open(file_name, FILE_WRITE);
  data_file.println(data);
  data_file.close();
}

void read_SD(char file_name[]){
  File data_file = SD.open(file_name);
  while(data_file.avaliable()){
    return data_file.read()
  }
  data_file.close()
}

uint8_t read_photocells(){
  for(i = 0; i<4; i++){
    Wire.requestFrom(pho_data[i],1);
    while (Wire.avaliable()){
      pho_data[i] = Wire.read();
    }
  }
  return pho_data
}

uint8_t read_eeprom(int address){
  return EEPROM.read(address)
}

void write_eeprom(uint8_t data){
  
}
