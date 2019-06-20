
# Twiggs Space Lab Payload Board Driver

TSLPB is a driver class that can be used to access the sensors and devices
on the TSLPB V3 for the [ThinSat Program.](http://vaspace.org/index.php/thinsat-program)

The driver sets up all the input and output pins required for accessing the
analog sensors, and provides methods for reading both the analog and digital
sensors.

## Usage Guides and Documentation

For more detailed information about the hardware and software, look in the `extras`
folder for .pdf files containing the TSLPB and NSL ICDs, as well as some more 
in-depth technical information about this library.

The [TSLPB Wiki](https://github.com/VCSFA-MARS/TSLPB/wiki) as another good reference for getting started and understanding
the TSLPB library functions.

# Basic Usage

You will need to do the following to use this library:

1. Include tslbp.h in your program.
2. Instantiate a TSLPB object
3. Run the TSLPB::begin() method

Once these steps are complete, you may call any of the public methods to
interact with the TSL Payload Board.

## Example

``` c++
 #include "TSLPB.h"

 TSLBP tslpb;
 ThinsatPacket_t missionData;

 void setup() {
     tslpb.begin();
 }

 void loop() {
     uint16_t tslVolts   = tslpb.readAnalogSensor(Voltage);
     uint16_t tslCurrent = tslpb.readAnalogSensor(Current);
     uint16_t tslTempExt = tslpb.readAnalogSensor(TempExt);

     uint16_t tslDT1Raw  = tslpb.readTSLDigitalSensorRaw(DT1);
     double   tslDT1C    = tslpb.readTSLDigitalSensor(DT1);

     missionData.payloadData.solar = tslpb.readAnalogSensor(Solar);

     while (!tslpb.isClearToSend())
     {
         delay(100);
     }

     tslpb.pushDataToNSL(missionData);
 }

```

You probably noticed the "Voltage", "Current", etc arguments. The TSLPB
driver has two enums that allow the client to call the read methods with
human-readable code, and without worrying about keeping I2C addresses or
managing low-level mux switching.



### TSLPB_AnalogSensor_t

Use `readAnalogSensor()` with any of the following values:

* Solar   - The solar sensor
* IR      - The infrared detector
* TempInt - The TSLPB internal temperature sensor
* TempExt - The TSLPB external temperature sensor
* Current - The TSLPB power system, current sensor
* Voltage - The TSLPB power system, voltage sensor

### TSLPB_DigitalSensor_t

Use `readDigitalSensor()` with any of the following values:

* DT1               - The TSLPB LM75A DT1 Temperature Sensor
* DT2               - The TSLPB LM75A DT2 Temperature Sensor
* DT3               - The TSLPB LM75A DT3 Temperature Sensor
* DT4               - The TSLPB LM75A DT4 Temperature Sensor
* DT5               - The TSLPB LM75A DT5 Temperature Sensor
* DT6               - The TSLPB LM75A DT6 Temperature Sensor
* Accelerometer_x   - The TSLPB MPU-9250 Accelerometer x-axis
* Accelerometer_y   - The TSLPB MPU-9250 Accelerometer y-axis
* Accelerometer_z   - The TSLPB MPU-9250 Accelerometer z-axis
* Gyroscope_x       - The TSLPB MPU-9250 Gyroscope x-axis
* Gyroscope_y       - The TSLPB MPU-9250 Gyroscope y-axis
* Gyroscope_z       - The TSLPB MPU-9250 Gyroscope z-axis
* Magnetometer_x    - The TSLPB MPU-9250 Magnetometer x-axis
* Magnetometer_y    - The TSLPB MPU-9250 Magnetometer y-axis
* Magnetometer_z    - The TSLPB MPU-9250 Magnetometer z-axis
* IMU_Internal_Temp - The TSLPB MPU-9250 Internal Temperature 


# Advanced Usage

## How to Store Your Data - The DataPacket `struct`

The TSLPB uses a union of a byte array and a struct to allow you to store your 
data in semantically relevant variables. For example, if you want to save
temperature data, instead of storing the bytes directly as follows:

``` c++
long myTemp = getTemp();
byte[1] = highByte(myTemp);
byte[2] = lowByte(myTemp);
```

Then you can use:

``` c++
myData.payloadData.temp = getTemp();
```

If you don't define a custom data packet structure, the library will use the
one defined in ```ThinSat_DataPacket_generic.h```, which does not use 
semantically named fields. They are simply:

``` c++
myData.payloadData.b1;
myData.payloadData.b2;
myData.payloadData.b3;
...
myData.payloadData.b35;
```

## Creating your DataPacket struct

For the most readable code, you will want to make your own data structure. The 
VCSFA_ThinSat example includes a header file called `VCSFA_Thinsat_DataPacket.h`. 
This file defines the data structure that VCSFA used in our flight software, and 
is a useful example if you run into problems writing your own.

### What you need to do

There are three important things you need to do to make your data structure work
with the TSLPB Library.

1. Let the library know you are using a user-defined data structure
2. Make sure your data structure has the right typedef
3. Define a data structure that is the right size

If you don't know what some of this means, don't worry. We'll walk through each of
them now.

#### Let the Library know you are using a user-defined data structure

Create a new file that will hold your data structure definition. You can name it
something like `MyDataStruct.h`

The top line should read `#define USERSTRUCT`

This lets the rest of the library know to ignore the default and use yours instead.
Then, you need to let your program know about this file. Add a 
`#include "MyDataStruct.h` line in your main sketch, right above the `#include "TSLPB.h"`
line.

#### Make sure your data structure has the right typedef

The TSLPB library is expecting your data structure to be of type `UserDataStruct_t`
This is a way that the library protects you from sending the wrong kind of data
to the NSL board, and possible getting undexpected behavior. We do this with a
`typedef` statement.

Make the next lines in your `MyDataStruct.h` file look like this:

``` c++
typedef struct UserDataStruct_t{

};
```

That tells the library that you are making a data structure that will be used to store
and send data to the NSL board.

#### Define a data structure that is the right size

The NLS ThinSat boards can only accept a certain amount of data, and they expect it in 
a particular format: [header][user data]. Each packet must also be a specific length, 
and must start with a predefinied "header."

We take care of the header, but you will need to give it a place in your data struct.
Add the following line inside the `{ }` from your `typedef struct UserDataStruct_t`

``` c++
char            header[NSL_PACKET_HEADER_LENGTH];
```

Now you have 35 bytes worth of data to divide up into whatever fields make sense. When
you add up the bytes used by each of your fields (excluding the header) it must equal 35.

To help you, here is a handy chart of variable types and how much memory they use:

| Type | Description                                        | Size in Bytes |
|------|----------------------------------------------------|---------------|
bool   | True or False                                      | 1
byte   | Arbitrary Data                                     | 1
char   | A letter or symbol                                 | 1
int    | An integer from -32,768 to 32,767                  | 2
uint   | An integer from 0 to 65,535                        | 2
long   | An integer from 2,147,483,648 to 2,147,483,647     | 4
double | A floating point (decimal)                         | 4
float  | A floating point number (decimal)                  | 4

If you have a temperature that you want to represent as a number with a decimal point,
you might want to use a float. You would add a line *after* the `char header[NSL_HEADER_LENGTH];` line

``` c++
float           temp; // 4 bytes
```

**NOTE:** this is probably not the most efficient way to save a temperature. Can you think of 
a way to represent a temperature that uses fewer bytes?

Once you have added all your data fields, double check that the byte total adds up to 35!




