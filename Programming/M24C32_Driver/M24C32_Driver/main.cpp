/*
 * M24C32_Driver.cpp
 *
 * Created: 8/9/2019 10:53:46 AM
 * Author : mschommer
 */ 

/* Insert system clock initialization code here (sysclk_init()). */
#ifndef F_CPU
#define F_CPU 1000000ul
#endif


#include <avr/io.h>
#include <util/delay.h>
#include <avr/portpins.h>
#include "i2cmaster.h"
#include "M24C32_Driver.h"

#define M24C32_MEM   0xA0
//#define M24C32_ADDR  0xB0
//#define M24C32_WC    PD5
int main (void)
{					  

	M24C32 eeprom = M24C32(0x00, PD5, &PORTD, &DDRD);

	/* Insert application code here, after the board has been initialized. */

	while (1)
	{
		eeprom.write_byte(22, 42);
		eeprom.read_byte(22);
		_delay_ms(500);
	}
}