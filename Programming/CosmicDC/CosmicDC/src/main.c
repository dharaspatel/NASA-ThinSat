/**
 * \file
 *
 * \brief Empty user application template
 *
 */

/**
 * \mainpage User Application template doxygen documentation
 *
 * \par Empty user application template
 *
 * Bare minimum empty user application template
 *
 * \par Content
 *
 * -# Include the ASF header files (through asf.h)
 * -# "Insert system clock initialization code here" comment
 * -# Minimal main function that starts with a call to board_init()
 * -# "Insert application code here" comment
 *
 */

/*
 * Include header files for all drivers that have been imported from
 * Atmel Software Framework (ASF).
 */
/*
 * Support and FAQ: visit <a href="https://www.microchip.com/support/">Microchip Support</a>
 */

/* Insert system clock initialization code here (sysclk_init()). */
#ifndef F_CPU
#define F_CPU 1000000ul
#endif
	

#include <avr/io.h>
#include <asf.h>
#include <avr/delay.h>
#include <avr/portpins.h>
#include "i2cmaster.h"
//#include "M24C32_Driver.h"

#define M24C32_MEM   0xA0
#define M24C32_ADDR  0xB0
#define M24C32_WC    PD5
int main (void)
{

	DDRD  |=  (1 << PD7) ; // Set Debug LED as output
	DDRD  |=  (1 << M24C32_WC);
	PORTD &= ~(1 << M24C32_WC);
	board_init();

	/* Insert application code here, after the board has been initialized. */
	unsigned char ret = 0;

	while (1)
	{
		i2c_init();
		// write 0x75 to EEPROM address 5 (Byte Write)
		i2c_start_wait(M24C32_MEM+I2C_WRITE);     // set device address and write mode
		i2c_write(0x00);                          // most significant address byte
		i2c_write(0x05);						  // least significant address byte
		i2c_write(0x23);                          // write value 0x75 to EEPROM
		i2c_stop();                               // set stop condition = release bus
		// read previously written value back from EEPROM address 0
		i2c_start_wait(M24C32_MEM+I2C_WRITE);     // set device address and write mode
		i2c_write(0x00);                          // write address most significant 0
		i2c_write(0x05);                          // write address least significant 0
		i2c_rep_start(M24C32_MEM+I2C_READ);       // set device address and read mode
		ret = i2c_readNak();                      // read one byte from EEPROM
		//ret = 23;
		i2c_stop();
		_delay_ms(100);

		//if (ret == 0x75){
			//PORTD |= 1 << PD7; //Turns ON Debug
			//_delay_ms(100); //1 second delay
			//PORTD &= ~(1 << PD7); //Turns OFF All LEDs
			//_delay_ms(100); //1 second delay
		//}
		//else{
			//for (int i = 0; i < ret; i++)
			//{
				//PORTD |= 1 << PD7; //Turns ON Debug
				//_delay_ms(10); //1 second delay
				//PORTD &= ~(1 << PD7); //Turns OFF All LEDs
				//_delay_ms(10); //1 second delay
			//}
			//_delay_ms(2000);
		//}
		
	}
}
//
///*
 //* CosmicDC.c
 //*
 //* Created: 8/7/2019 10:04:06 AM
 //* Author : mschommer
 //*/ 
//
//
//#ifndef F_CPU
//#define F_CPU 1000000UL
//#endif
//
//#include <avr/io.h>
//#include <util/delay.h>
//#include <math.h>
//#include <stdlib.h>
//
//#include "i2cmaster/i2cmaster.h"
//
//#define M24C32_XDW5TP_MEM_ARRAY 0x50
//#define M24C32_XDW5TP_ID_PAGE 0x58
//
//
//#define Dev24C02  0x50      // device address of EEPROM 24C02, see datasheet
//
//
//int main(void)
//{
	//unsigned char ret;
	//i2c_init();                             // initialize I2C library
	//// write 0x75 to EEPROM address 5 (Byte Write)
	//i2c_start_wait(Dev24C02+I2C_WRITE);     // set device address and write mode
	//i2c_write(0x05);                        // write address = 5
	//i2c_write(0x75);                        // write value 0x75 to EEPROM
	//i2c_stop();                             // set stop conditon = release bus
	//// read previously written value back from EEPROM address 5
	//i2c_start_wait(Dev24C02+I2C_WRITE);     // set device address and write mode
	//i2c_write(0x05);                        // write address = 5
	//i2c_rep_start(Dev24C02+I2C_READ);       // set device address and read mode
	//ret = i2c_readNak();                    // read one byte from EEPROM
	//i2c_stop();
	//for(;;);
//}