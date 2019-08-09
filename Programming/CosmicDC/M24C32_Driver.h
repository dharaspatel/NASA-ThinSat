#ifndef __M24C32__
#define __M24C32__

#include "i2cmaster.h"

// Driver class for the M24C32 EEProm. In the default co
class M24C32
{
public:

M24C32 (uint8_t chip_enable_address, uint8_t  wc_mask, volatile uint8_t *wc_port, volatile uint8_t *wc_ddr);
~M24C32();

private:
	void  set_write_ctrl(bool val);
};





#endif