/*  ________________________________________________
    Description:
    Author: Dhara Patel
    ________________________________________________*/

//include statements
#include "TSLPB.h"
#include "myDataPacketStructure.h"

//define statements
TSLBP tslpb;
UserDataStruct_t missionData;

//for analog sensors --> uint16_t varName
//for digital sensors --> uint16_t varName (for raw) and double varName
uint16_t        photodiodeFt; //data from photodiode on front face of joe
uint16_t        photodiodeBk; //data from photodiode on back face of joe
uint16_t        photodiodeTp; //data from photodiode on top face of joe
unit16_t        photodiodeBt; //data from photodiode on bottom face of joe

uint16_t        temp; //data from temperature sensor for pyrolysis located on burt

uint16_t        spectrometer; //data from spectrometer located on burt

void begin(){
  tslbp.begin();
}

void loop(){
  //read data from all sensors
  readData();

  //store data in payload
  storeData();

  //send sensors' data from payload to bus
  sendData();

}

void readData(){
  //varName = tslpb.readAnalogSensor(Value) or readDigitalSensor(Value) or readDigitalSensorRaw(Value)
  //varName was defined in define statements at the top
  tslSolar = tslbp.readAnalogSensor(Solar);
  tslTempInt = tslbp.readAnalogSensor(TempInt);
  tslTempExt = tslbp.readAnalogSensor(TempExt);
//   tslAccX, tslAccY, tslAccZ = tslbp.readDigitalSensorRaw(Accelerometer_x, Accelerometer_y, Accelerometer_z);
//   tslGyrX, tslGyrY, tslGyrZ = tslbp.readDigitalSensorRaw(Gyroscope_x, Gyroscope_y, Gyroscope_z);

//we also need it to read time! and occasionally send back time data

}

void storeData(){
  //missionData.payloadData.byteName = varName
  missionData.payloadData.solar = tslSolar;
  missionData.payloadData.tempint = tslTempInt;
  missionData.payloadData.tempext = tslTempExt;
}

void sendData(){
  while (!tslpb.isClearToSend()){
    delay(100);
  }

  tslpb.pushDataToNSL(missionData);
}
