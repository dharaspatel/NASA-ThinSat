#include "TSLPB.h"

/*
 *	Instructions for use:
 *		1. Launch the Arduino Serial Plotter
 *		2. Set paud rate to 9600 (TSL_DIAGNOSTIC_BAUD from TSLPB.h)
 *		3. Move the TSLPB around and watch the plots update!
 */

TSLPB pb;
ThinsatPacket_t missionData;

void setup() {
  // put your setup code here, to run once:
  pb.begin();
}

void loop() {

  Serial.print(pb.readDigitalSensor(Accelerometer_x));
  Serial.print(",");
  Serial.print(pb.readDigitalSensor(Accelerometer_y));
  Serial.print(",");
  Serial.println(pb.readDigitalSensor(Accelerometer_z));

}
