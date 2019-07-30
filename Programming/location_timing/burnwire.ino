

//int numpins = 2;
//int pins[2] = {12, 13};

int numpins = 1;
int pins[1] = {13};
int on = 0;
void setup() {
  for (int i = 0; i < numpins; i++) {
    pinMode(pins[i], OUTPUT);
  }
  Serial.begin(9600);
}


void loop() {
  if (Serial.available() > 0) {
    on = Serial.read() - 48;
    if (on == 1) {
      Serial.print("On\n");
      for (int i = 0; i < numpins; i++) {
        digitalWrite(pins[i], HIGH); // sets voltage to 3.7V
        Serial.print("Voltage set to 3.7V for pin : \n");
        Serial.print(pins[i]);
        Serial.print("\n");
        //delay(5000); // 5 seconds
        delay(6000); // 6 seconds
        //delay(10000); // 10 seconds
        digitalWrite(pins[i], LOW);
        Serial.print("Now set voltage to 0V\n");
        delay(1000); // delay 1 second
      }
      Serial.print("Off\n");
      //Serial.end();
    }
  }
}

//void loop() {
//  if (Serial.available() > 0) {
//    on = Serial.read() - 48;
//    if (on == 1) {
//      Serial.print("On\n");
//      for (int i = 0; i < numpins; i++) {
//        digitalWrite(pins[i], HIGH); // sets voltage to 3.7V
//        Serial.print("Voltage set to 3.7V for pin : \n");
//        Serial.print(pins[i]);
//        Serial.print("\n");
//      }
//      //Serial.print("Voltage set to 3.7V\n");
//      delay(10000); // 10 seconds
//      Serial.print("Now set voltage to 0V\n");
//      for (int i = 0; i < numpins; i++) {
//        digitalWrite(pins[i], LOW);
//      }
//      Serial.print("Off\n");
//      //Serial.end();
//    }
//  }
//}
//for (int i = 0; i < 8; i++) {
//  digitalWrite(pins[i], HIGH);
//}
