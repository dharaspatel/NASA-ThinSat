
#include "M24C32_Driver.h"

M24C32::M24C32(uint8_t chip_enable_address, 
			   uint8_t wc_mask, 
			   volatile uint8_t *wc_port, 
			   volatile uint8_t *wc_ddr){
		
		const uint8_t M2M24C32_MEM =  0xA0 + chip_enable_address;
		const uint8_t M24C32_ADDR = 0xB0 + chip_enable_address;
		*wc_ddr  |=  (1 << wc_mask); // Set Write Enable pin DDR
		*wc_port &= ~(1 << wc_mask);
	
		}