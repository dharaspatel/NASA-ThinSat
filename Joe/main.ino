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
}

void storeData(){
  //missionData.payloadData.byteName = varName
}

void sendData(){
  while (!tslpb.isClearToSend()){
    delay(100);
  }

  tslpb.pushDataToNSL(missionData);
}
