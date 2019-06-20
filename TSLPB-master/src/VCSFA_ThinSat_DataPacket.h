/**
 *  @file   VCSFA_ThinSat_DataPacket.h
 *
 *  @author Nicholas Counts
 *
 *  @date   06/20/18
 *
 *  @brief  Defines the custom data structure used to store the user's payload
 *          data, and the union that is used to transmit the data to the NSL
 *          Mothership.
 *
 */

/* 2018 Counts Engineering */

#define USERSTRUCT

#include "NSL_ThinSat.h"

/*!
 * @brief   A user-customizable structure to hold any data the user intends to
 *          send back to Earth.
 *
 * @note    This is a sample UserDataStruct_t. It was developed for the VCSFA
 *          ThinSat custom payload. Some of the fields are for external sensors
 *          and some of the fields are for TSLPB sensors.
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
    int16_t         quatw;      ///<  1 -  2 (value from -4000 to 4000) 4.000 (unitless)
    int16_t         quatx;      ///<  3 -  4 (value from -1000 to 1000) 1.000 (unitless)
    int16_t         quaty;      ///<  5 -  6 (value from -1000 to 1000) 1.000 (unitless)
    int16_t         quatz;      ///<  7 -  8 (value from -1000 to 1000) 1.000 (unitless)
    int16_t         bnomagx;    ///<  9 - 10 (value from -20480 to 20470) 2047.0 uT (from BNO)
    int16_t         bnomagy;    ///< 11 - 12 (value from -20480 to 20470) 2047.0 uT
    int16_t         bnomagz;    ///< 13 - 14 (value from -20480 to 20470) 2047.0 uT
    uint8_t         bnoCal;     ///< 15      (sys, gyro, accel, mag) 01010101b
    unsigned long   bmePres;    ///< 16 - 19 (values from 0 to 1010000) 101000.0 Pa
    int16_t         bmeTemp;    ///< 20 - 21 (values from -1000 to 1000) 100.0 C
    uint16_t        tslTempExt; ///< 22 - 23 (10 bits 0-1023) ADC Raw Counts
    uint16_t        tslVolts;   ///< 24 - 25 (10 bits 0-1023) ADC Raw Counts
    uint16_t        tslCurrent; ///< 26 - 27 (10 bits 0-1023) ADC Raw Counts
    int16_t         tslMagXraw; ///< 28 - 29 Raw value (2's compliment form) -0x7FF8 to 0x7FF8
    int16_t         tslMagYraw; ///< 30 - 31 Raw value (2's compliment form) -0x7FF8 to 0x7FF8
    int16_t         tslMagZraw; ///< 32 - 33 Raw value (2's compliment form) -0x7FF8 to 0x7FF8
    uint16_t        solar;      ///< 34 - 35 (10 bits 0-1023) ADC Raw Counts
};

