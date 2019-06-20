#include "TSLPB.h"


TSLPB pb;
ThinsatPacket_t missionData;

void setup() {
  // put your setup code here, to run once:
  pb.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  pb.pushDataToNSL(missionData);
  Serial.println("This displays on the TSLPB Diagnostic Serial Port");
  
}