#ifndef __M24C32__
#define __M24C32__

#include "i2cmaster.h"

// Driver class for the M24C32 EEProm. In the default co
class M24C32
{
public:

M24C32 (uint8_t chip_enable_address, uint8_t  wc_mask, volatile uint8_t *wc_port, volatile uint8_t *wc_ddr);
~M24C32();

void setup();

void   write_page(uint16_t address, uint8_t *vals, uint8_t vals_size);
void   write_byte(uint16_t address, uint8_t val);

uint8_t read_byte(uint16_t address);

private:
uint8_t M24C32_MEM;
uint8_t M24C32_ADDR;
uint8_t wc_mask;
volatile uint8_t *wc_port;
volatile uint8_t *wc_ddr;

void  set_write_ctrl(bool val);
};



#endif