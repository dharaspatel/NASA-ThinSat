/*  ________________________________________________
    Description: header file for Joe.c (all function declarations)
    Author: Dhara Patel
    ________________________________________________*/

#ifndef Joe_h
#define Joe_h

private:

public:
  float calibrateTime(DateTime);
  struct pho_data readPhotocells(bool);
  struct position getPosition(DateTime, struct pho_data);
  int calc_state(struct position);
  bool sendData(UserDataStruct_t);
  void readSD(char[], char[]);
  int16_t readMag();
  bool launch(int);
  void pyrolysis();
  void melt(int);
  size_t readImg();
  size_t readTemp();
#endif
