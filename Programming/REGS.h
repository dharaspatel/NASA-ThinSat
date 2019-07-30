 /*  ________________________________________________
    Description: contains all register addesses
    Author: Dhara Patel

    6-25:
    sendToBUS()
    readMag()
    send email to jack with all code + info about radar location
    ________________________________________________*/


/*___ATMEGA PIN ADDRESSES___

     input = data to atmega
     output = data from atmega
     addesses are defined in order of pin number on atmega */

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
#define SER_ADDR PORTB6 //output serial for burn wires --30
#define STBY_ADDR PORTC6 //output for standby for NSL BUS --31
#define CS_IMG_ADDR PORTC7 //output to burt for image sensor --32
#define TEMP_ADDR PINE2 //input from burt's temperature sensor --33
#define PHO2_ADDR PINF7 //input from photodiode 2 --36
#define IN2_ADDR PORTF6 //output to motordriver on burt --37
#define IN1_ADDR PORTF5 //output to motordriver on burt --38
#define RCLK_ADDR PORTF4 //output of register clock for shift regs on burt --39
#define SRCLK_ADDR PORTF1 //output of serial clock for shift regs on burt --40
#define CS_SD_ADDR PORTF0 //chip select for SD SPI communication --41

/*___DEVICE ADDRESSES___*/
#define DCF_ADDR D0h //device address for dcf77
#define EEPROM_ADDR A //device address for eeprom

/*___DS3231 PIN ADDRESSES___*/
#define SEC_ADDR 0x0h
#define MIN_ADDR 0x1h
#define HOUR_ADDR 0x2h
#define DATE_ADDR 0x4h
#define MON_ADDR 0x5h
#define YEAR_ADDR 0x6h

/*___SENSOR ADDRESSES___*/
#define MAG_ADDRESS 0x0C //this is on the IMU on the bus side...

/*BURN WIRE PIN INFO:
  motor design:
    A - F ==> launchers
    G - H, A2 - B2 ==> pyrolysis

  rifle design
    A - H ==> launchers
    A2 - D2 ==> pyrolysis
*/
