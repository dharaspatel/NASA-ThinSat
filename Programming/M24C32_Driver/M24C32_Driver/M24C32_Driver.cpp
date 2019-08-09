
#include "M24C32_Driver.h"

M24C32::M24C32(uint8_t chip_enable_address, 
			   uint8_t wc_mask, 
			   volatile uint8_t *wc_port, 
			   volatile uint8_t *wc_ddr):
			   wc_mask(wc_mask),
			   wc_port(wc_port),
			   wc_ddr(wc_ddr){
		
		M24C32_MEM =  0xA0 + chip_enable_address;
		M24C32_ADDR = 0xB0 + chip_enable_address;
		setup();
		}

void M24C32::setup(){
	*wc_ddr  |=  (1 << wc_mask); // Set Write Enable pin DDR
	set_write_ctrl(false);
	i2c_init();
}
		
void  M24C32::set_write_ctrl(bool val){
	if (val){
		*wc_port &= ~(1 << wc_mask); // Enable Write Control
	}else{
		*wc_port |=  (1 << wc_mask); // Disable Write Control
	}
}		

void M24C32::write_byte(uint16_t address, uint8_t val){
	set_write_ctrl(true);
	i2c_start_wait(M24C32_MEM+I2C_WRITE);     // set device address and write mode
	i2c_write(address&0xFF);                  // most significant address byte
	i2c_write((address>>8)&0xFF);		      // least significant address byte
	i2c_write(val);                           // write value to EEPROM
	i2c_stop();                               // set stop condition = release bus
	set_write_ctrl(false);
}

// Writes to a page of the EEPROM, allowing for a full array of up to 32 bytes
// to be sent. 
//    uint16_t address  : The start address of the write. Ensure that the most-significant
//                        address bits b16-b5 are the same in order to guarantee that all
//                        data is written sequentially. Bytes which exceed the page will
//                        "roll over" to the beginning of the page. 
void M24C32::write_page(uint16_t address, uint8_t *vals, uint8_t vals_size){
	set_write_ctrl(true);
	i2c_start_wait(M24C32_MEM+I2C_WRITE);     // set device address and write mode
	i2c_write(address&0xFF);                  // most significant address byte
	i2c_write((address>>8)&0xFF);		      // least significant address byte
	for(int i=0; i<=vals_size; i++){
	{
		i2c_write(vals[i]);
	}
	i2c_stop();
	set_write_ctrl(false);
}

uint8_t M24C32::read_byte(uint16_t address){
	uint8_t ret;
	i2c_start_wait(M24C32_MEM+I2C_WRITE);     // set device address and write mode
	i2c_write(address&0xFF);                  // write address most significant 0
	i2c_write((address>>8)&0xFF);             // write address least significant 0
	i2c_rep_start(M24C32_MEM+I2C_READ);       // set device address and read mode
	ret = i2c_readNak();                      // read one byte from EEPROM (not used)
	i2c_stop();

	return ret;
}



