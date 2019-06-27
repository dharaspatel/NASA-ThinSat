/*  ________________________________________________
    Description: main file that defines all functions called in both burt and bill
    Author: Dhara Patel
    ________________________________________________*/



//begins I2C interface and RTC clock
void begin(){
  Wire.begin();
  Clock.setClockMode(false);
}

//syncs time to altitude estimate based on sunrise/set data to get location and alt
float sync(){
//returns accurate position
}

//orient burt properly
void orient(){

}

//calculates the state of the sat based on the position
int calc_state(){

}
