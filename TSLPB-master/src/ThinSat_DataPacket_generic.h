/**
 *  @file   ThinSat_DataPacket_generic.h
 *
 *  @author Nicholas Counts
 *
 *  @date   06/20/18
 *
 *  @brief  Defines the standard data structure used to store the user's payload
 *          data, and the union that is used to transmit the data to the NSL
 *          Mothership. Users must define ThinSat_DataPacket_custom_h, write 
 *          their own UserDataStruct_t definition, and include the 
 *          ThinsatPacket_t union typedef.
 *
 */

/* 2018 Counts Engineering */

#include "NSL_Thinsat.h"

#ifndef USERSTRUCT


/*!
 * @brief   A generic data structure to hold any data the user intends to
 *          send back to Earth.
 *
 * @note    This is a sample UserDataStruct_t. It was developed to be used by
 *          ThinSat participants who do not want to make their own 
 *          UserDataStruct_t. Each field is simply the byte position (1-based)
 *          from 1 to 35. Users will need to split multi-byte data appropriately
 *          and will need to type cast their data when storing it in this
 *          structure.
 *
 * @note    We recommend adding comments that show the expected ranges and units
 *          of any data being put into a field. This will ensure that you can
 *          translate the data later.
 *
 * @warning The struct must be NSL_PACKET_SIZE bytes in total size.
 *          The first member must always be called "header" and have a size of
 *          NSL_PACKET_HEADER_LENGTH
 *
 */
typedef struct UserDataStruct_t{
    char            header[NSL_PACKET_HEADER_LENGTH];
    int8_t          b1;       ///<  b1  (Generic packet byte  1 of 35 )
    int8_t          b2;       ///<  b2  (Generic packet byte  2 of 35 )
    int8_t          b3;       ///<  b3  (Generic packet byte  3 of 35 )
    int8_t          b4;       ///<  b4  (Generic packet byte  4 of 35 )
    int8_t          b5;       ///<  b5  (Generic packet byte  5 of 35 )
    int8_t          b6;       ///<  b6  (Generic packet byte  6 of 35 )
    int8_t          b7;       ///<  b7  (Generic packet byte  7 of 35 )
    int8_t          b8;       ///<  b8  (Generic packet byte  8 of 35 )
    int8_t          b9;       ///<  b9  (Generic packet byte  9 of 35 )
    int8_t          b10;      ///<  b10 (Generic packet byte 10 of 35 )
    int8_t          b11;      ///<  b11 (Generic packet byte 11 of 35 )
    int8_t          b12;      ///<  b12 (Generic packet byte 12 of 35 )
    int8_t          b13;      ///<  b13 (Generic packet byte 13 of 35 )
    int8_t          b14;      ///<  b14 (Generic packet byte 14 of 35 )
    int8_t          b15;      ///<  b15 (Generic packet byte 15 of 35 )
    int8_t          b16;      ///<  b16 (Generic packet byte 16 of 35 )
    int8_t          b17;      ///<  b17 (Generic packet byte 17 of 35 )
    int8_t          b18;      ///<  b18 (Generic packet byte 18 of 35 )
    int8_t          b19;      ///<  b19 (Generic packet byte 19 of 35 )
    int8_t          b20;      ///<  b20 (Generic packet byte 20 of 35 )
    int8_t          b21;      ///<  b21 (Generic packet byte 21 of 35 )
    int8_t          b22;      ///<  b22 (Generic packet byte 22 of 35 )
    int8_t          b23;      ///<  b23 (Generic packet byte 23 of 35 )
    int8_t          b24;      ///<  b24 (Generic packet byte 24 of 35 )
    int8_t          b25;      ///<  b25 (Generic packet byte 25 of 35 )
    int8_t          b26;      ///<  b26 (Generic packet byte 26 of 35 )
    int8_t          b27;      ///<  b27 (Generic packet byte 27 of 35 )
    int8_t          b28;      ///<  b28 (Generic packet byte 28 of 35 )
    int8_t          b29;      ///<  b29 (Generic packet byte 29 of 35 )
    int8_t          b30;      ///<  b30 (Generic packet byte 30 of 35 )
    int8_t          b31;      ///<  b31 (Generic packet byte 31 of 35 )
    int8_t          b32;      ///<  b32 (Generic packet byte 32 of 35 )
    int8_t          b33;      ///<  b33 (Generic packet byte 33 of 35 )
    int8_t          b34;      ///<  b34 (Generic packet byte 34 of 35 )
    int8_t          b35;      ///<  b35 (Generic packet byte 35 of 35 )

};

#endif


/*!
 * @brief   A union of the UserDataStruct_t payloadData and a byte array that is
 *          used to send the user's mission data to the NSL Mothership.
 *
 * @warning DO NOT MODIFY THIS UNION UNLESS YOU REALLY REALLY KNOW WHAT YOU ARE
 *          DOING. This datatype is used in the public method
 *          TSLPB::pushDataToNSL(ThinsatPacket_t data) and changing this union
 *          may break that functionality.
 */
typedef union ThinsatPacket_t {
    UserDataStruct_t payloadData;
    byte NSLPacket[sizeof(UserDataStruct_t)];
};


