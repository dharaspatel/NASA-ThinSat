/*  ________________________________________________
    Description:
    Author: Dhara Patel
    ________________________________________________*/

#define USERSTRUCT

#include "NSL_ThinSat.h"

typedef struct UserDataStruct_t{
    char            header[NSL_PACKET_HEADER_LENGTH]; //the first struct member must be the NSL_PACKET_HEADER_LENGTH
    uint16_t        solar;
    uint16_t        tempint;
    uint16_t        tempext;
  
};
