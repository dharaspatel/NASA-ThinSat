/**
 *  @file   TSLPB.h
 *
 *  @author Nicholas Counts
 *
 *  @version     0.6.0
 *
 *  @date   06/12/18
 *
 *  @brief  Function prototypes, includes, and definitions for TSLPB Arduino
 *          interface
 *
 */

 /* 2018 Counts Engineering */


#ifndef TSLPB_h
#define TSLPB_h


#include "Arduino.h"

#include "avr/sleep.h"
#include "Wire.h"

#include <SoftwareSerial.h>

#include "NSL_ThinSat.h"
#include "ThinSat_DataPacket_generic.h"
#include "MPU9250_REGS.h"

#define TSL_DIAGNOSTIC_BAUD 9600    ///< TSLPB diagnostic serial port baud rate

#define TSL_NSL_BUS_STATUS_PIN 4    ///< NSL Serial Busy Line monitoring pin
#define TSL_NSL_BUS_RX_PIN 3        ///< Pin for software serial connectino to NSL Serial Bus
#define TSL_NSL_BUS_TX_PIN 5        ///< Pin for software serial connectino to NSL Serial Bus


#define TSL_ADC A7                  ///< ADC reading the MUX_Output
#define TSL_MUX_A 7                 ///< Mux A - TSLPB pin number
#define TSL_MUX_B 8                 ///< Mux B - TSLPB pin number
#define TSL_MUX_C 9                 ///< Mux C - TSLPB pin number
#define TSL_MUX_RESPONSE_TIME 10    ///< 10 miliseconds to change

#define TSL_SENSOR_READY_TIMEOUT 100    ///< number of milliseconds to wait for an I2C device to become ready






/*!
 * @brief TSLPB Analog Sensor Selection Enum
 */
typedef enum
{
    Solar   = 0b000,                ///< 0b000 (Solar Sensor)
    IR      = 0b001,                ///< 0b001 (IR)
    TempInt = 0b010,                ///< 0b010 (Temp Int)
    TempExt = 0b011,                ///< 0b011 (Temp Ext)
    Current = 0b100,                ///< 0b100 (Current)
    Voltage = 0b101                 ///< 0b101 (Vcc)
} TSLPB_AnalogSensor_t;


/*!
 * @brief   TSLPB Digital Sensor Address enum. Used by TSLPB private methods to
 *          communicate with the digital sensors over I2C.
 *
 * @note    May be used by client code to access any of the I2C devices on the
 *          TSLPB. (with caution!)
 */
typedef enum
{
    DT1_ADDRESS = 0x4A,             ///< LM75A
    DT2_ADDRESS = 0x4C,             ///< LM75A
    DT3_ADDRESS = 0x4D,             ///< LM75A
    DT4_ADDRESS = 0x48,             ///< LM75A
    DT5_ADDRESS = 0x49,             ///< LM75A
    DT6_ADDRESS = 0x4B,             ///< LM75A
    IMU_ADDRESS = 0x69,             ///< MPU-9250
    MAG_ADDRESS = 0x0C,             ///< MAGNETOMETER I2C Address (slave on the MPU-9250)
    MEM_ADDR ESS = 0x50,             ///< EEPROM I2C Address for the Microchip 24LC256

} TSLPB_I2CAddress_t;

/*!
 * @brief   TSLPB Digital Sensor selection Enum. Used as arguments for
 *          TSLPB::readDigitalSensor() and TSLPB::readDigitalSensorRaw()
 */
typedef enum
{
    DT1,                            ///< Select LM75A DT1
    DT2,                            ///< Select LM75A DT2
    DT3,                            ///< Select LM75A DT3
    DT4,                            ///< Select LM75A DT4
    DT5,                            ///< Select LM75A DT5
    DT6,                            ///< Select LM75A DT6
    Accelerometer_x,                ///< Select MPU-9250 Accelerometer x-axis
    Accelerometer_y,                ///< Select MPU-9250 Accelerometer y-axis
    Accelerometer_z,                ///< Select MPU-9250 Accelerometer z-axis
    Gyroscope_x,                    ///< Select MPU-9250 Gyroscope x-axis
    Gyroscope_y,                    ///< Select MPU-9250 Gyroscope y-axis
    Gyroscope_z,                    ///< Select MPU-9250 Gyroscope z-axis
    Magnetometer_x,                 ///< Select MPU-9250 Magnetometer x-axis
    Magnetometer_y,                 ///< Select MPU-9250 Magnetometer y-axis
    Magnetometer_z,                 ///< Select MPU-9250 Magnetometer z-axis
    IMU_Internal_Temp               ///< Select MPU-9250 Internal Temperature
} TSLPB_DigitalSensor_t;


/*!
 * @brief TSLPB Digital Temperature Sensor (LMA75A) Macros
 */
#define LMA_TEMP_REG_UNUSED_LSBS        5       ///< The number of bits to be discarded (from LSb)
#define LMA_TEMP_REG_SIGN_BIT           9       ///< The bit that contains indicates the sign. 0-based
#define LMA_TEMP_REG_DEGREES_PER_LSB    0.125   ///< Temperature resolution in °C per LSb

/*!
 * @brief TSLPB Digital Temperature Sensor (LMA75A) Register Selection Enum
 */
typedef enum
{
    LM75A_TEMPERATURE   = 0x0,      ///< 0x00 Read only
    LM75A_CONFIGURATION = 0x1,      ///< 0x01 Read/Write
    LM75A_T_HYST        = 0x2,      ///< 0x02 Read/Write
    LM75A_T_OS          = 0x3,      ///< 0x03 Read/Write
    LM75A_PRODUCT_ID    = 0x7       ///< 0x07 Read only
} LM75A_REG;


/*!
 * @brief   The controller class for the TSL Payload Board. Create an instance
 *          of this class to use its member functions for accessing the onboard
 *          analog and digital sensors. Methods for communicating with the
 *          NSL Mothership are also included.
 */
class TSLPB
{

public:
    TSLPB();
    void begin();

    SoftwareSerial NSLbus;                  ///< NSL Software Serial bus object
    bool    pushDataToNSL(ThinsatPacket_t data);

    uint16_t readAnalogSensor(TSLPB_AnalogSensor_t sensorName);
    double   readDigitalSensor(TSLPB_DigitalSensor_t sensor);
    uint16_t readDigitalSensorRaw(TSLPB_DigitalSensor_t sensor);

    uint8_t TSLPB::getMemByte(uint16_t reg);
    void    TSLPB::putMemByte(uint16_t reg, uint8_t data);

    template<class TYPE> void TSLPB::readMemVar(word reg, TYPE& result) {
        const uint8_t n = sizeof(result);
        union ReadUnion{
            TYPE  dt;
            byte  b[n];
        };
        ReadUnion data;
        for (uint8_t i = 0; i < n; i++) {
            data.b[n - 1 - i] = TSLPB::getMemByte(reg + i);
        }
        result = data.dt;
    };

    template<class TYPE> void TSLPB::writeMemVar(word reg, TYPE varToWrite) {
        const uint8_t n = sizeof(varToWrite);
        union WriteUnion{
            TYPE  dt;
            byte  b[n];
        };
        WriteUnion data;
        data.dt = varToWrite;
        data.b[0] += 0x00;
        for (uint8_t i = 0; i < n; i++) {
            TSLPB::putMemByte(data.b[n - 1 - i], reg + i);
        }
    };

    void    sleepUntilClearToSend();   // NOT IMPLEMENTED
    bool    isClearToSend();

    bool    isMagnetometerOverflow = false; ///< Overflow status of magnetometer registers

private:

    bool    read16bitRegister(TSLPB_I2CAddress_t i2cAddress, const uint8_t reg, uint16_t& response);
    bool    write8bitRegister(TSLPB_I2CAddress_t i2cAddress, const uint8_t reg, uint8_t data);
    uint8_t read8bitRegister (TSLPB_I2CAddress_t i2cAddress, const uint8_t reg);
    void    InitTSLAnalogSensors();
    void    InitTSLDigitalSensors();
    void    wakeOnSerialReady();
    void    sleepWithWakeOnSerialReady();
    void    waitForMagReady();
    void    clearNSLbus();

    TSLPB_I2CAddress_t getDeviceAddress(TSLPB_DigitalSensor_t sensorName);

};


#endif /* TSLPB_h */
