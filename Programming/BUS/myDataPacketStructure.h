/*  ________________________________________________
    Description:
    Author: Dhara Patel
    ________________________________________________*/

#include "NSL_Thinsat.h"

#ifndef USERSTRUCT //if the user struct is defined...

typedef struct UserDataStruct_t{
    char            header[NSL_PACKET_HEADER_LENGTH]; //the first struct member must be the NSL_PACKET_HEADER_LENGTH

    //uint16_t        photodiodeFt; //data from photodiode on front face of joe
    //uint16_t        photodiodeBk; //data from photodiode on back face of joe
    //uint16_t        photodiodeTp; //data from photodiode on top face of joe
    //unit16_t        photodiodeBt; //data from photodiode on bottom face of joe

    uint16_t        temp; //data from temperature sensor for pyrolysis located on burt

    uint16_t        spectrometer; //data from spectrometer located on burt

    int16_t         magnetometer_x; //raw magnetometer x axis
    int16_t         magnetometer_y; //raw magnetometer y axis
    int16_t         magnetometer_z; //raw magnetometer z axis
};

#endif

typedef union ThinsatPacket_t {
    UserDataStruct_t payloadData;
    byte NSLPacket[sizeof(UserDataStruct_t)];
};
