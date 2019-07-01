/*  ________________________________________________
    Description: file that controls all data reading, storing, and sending
    Author: Dhara Patel
    ________________________________________________*/

/*___INCLUDES___*/
#include "TSLPB.h"
#include "myDataPacketStructure.h"

/*___DECLARATIONS FOR ALL SATELLITES___*/
TSLBP tslpb;
UserDataStruct_t missionData;

                                                                                  //for analog sensors --> uint16_t varName
                                                                                  //for digital sensors --> uint16_t varName (for raw) and double varName
/*___DECLARATIONS FOR SENSORS ON JOE___*/
uint16_t        pho1; //photodiode on front face of joe
uint16_t        pho2; //photodiode on back face of joe
uint16_t        pho3; //photodiode on top face of joe
unit16_t        pho4; //photodiode on bottom face of joe

/*___DECLARATIONS FOR SENSORS ON BURT___*/
uint16_t        temp1; //internal temperature sensor
uint16_t        temp2; //external temperature sensor
uint16_t        spec; //spectrometer for uv, ir, rgb data on pyrolysis

/*___DECLARATIONS FOR SENSORS ON JOE___*/




void begin(){
  tslbp.begin();
}

void loop(){
  switch (trigger) {
    case 1:
      pyrolysis_data();

    case 2:
      launch_data();
  }
}

void pyrolysis_data(){
  /*
    FUNCTION: Collects and stores data from all sensors for pyrolysis experiment
    PARAMETERS: None
    RETURN: None
  */
  readData(pho1);
  readData(pho2);
  readData(pho3);
  readData(pho4);

  storeData(pho1);
  storeData(pho2);
  storeData(pho3);
  storeData(pho4);
}

void readData(uint16_t sensor){
  /*
    FUNCTION: Reads raw digital signal from given sensor
    PARAMETERS: sensor
    RETURN: None
  */                                                                              //varName = tslpb.readAnalogSensor(Value) or readDigitalSensor(Value) or readDigitalSensorRaw(Value)
                                                                                  //varName was defined in define statements at the top
  tslpho1 = tslbp.readDigitalSensorRaw(sensor);

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
