// This script needs to:
// 1) use RTC to match up sunrise to lookup table
// 2) use day length and night length to update location forecast (loop every orbit)
// 3) determine timing for launchers / deorbit / pyrolysis

// Given:
// * Photocell data: time of last sunset, time of last sunrise, orbital period
// * RTC value
// * Lookup tables: Time, forecasted latitude, longitude and altitude of sunrise and sunset
// * Parameters (for updating location given day and night length)

float RTCdata[3] = {9718.62, 12938.19, 15055.634}; //time of last last sunrise, time of last sunset, time of last sunrise

float sunrisedata[6] [4] = {
  {4386.006999900565, 51.50681885531415, 29.32911849721807, 231.1965262353242},
  {9727.614999935031, 51.52552725975358, 7.010603810552084, 231.0698421742627},
  {15069.10999986576, 51.54413994381702, -15.30235531923493, 230.8692341692504},
  {20410.39800031576, 51.56404134952468, -37.61344627634696, 230.6269498370393},   
  {25751.35200036457, 51.58434569662798, -59.92675377245475, 230.4275178456792},
  {31091.95399977034, 51.60314282567107, -82.24111839407341, 230.2964362403609},
};

float shift[3][3][3] = {
  {
    {1.21097247e+00, -5.02760593e-01, 4.99429467e-01},
    {4.51013107e+01, -7.65556717e+01, -2.27936432e+02},
    {3.91181030e+01, -2.39536092e+02, -7.77920586e+02}
  },
  {
    {-10.15165921, 7.2143677, 22.30823809},
    {-223.92845256, 138.1156475, 416.61120306},
    {20.25181539, -163.83472914, -565.52555243},
  },
  {
    {-27.65226351, 9.01331709, 32.25895315},
    {-600.43674847, 55.51576793, 248.40489914},
    {-85.29471328, -2928.12684892, -8820.42099321},
  },
};

int index = 0;
float latitude;
float longitude;
float altitude;

void setup() {
  // Read lookup table from SD card (TO DO)
  Serial.begin(9600);
  float day_length = RTCdata[1] - RTCdata[0]; // sunset - sunrise
  float night_length = RTCdata[2] - RTCdata[1]; // sunrise - sunset

  // find closest time to look up table
  int count = sizeof(sunrisedata)/sizeof(sunrisedata[0]);
  for (int i = 0; i <= count; i++) {
    if (abs(sunrisedata[i][0] - RTCdata[2]) < abs(sunrisedata[index][0] - RTCdata[2]) ) {
      index = i;
    }
  }

  // get current location from lookup table
  latitude = sunrisedata[index][1];
  longitude = sunrisedata[index][2];
  altitude = sunrisedata[index][3];

  // use day length and night length to update location forecast
}

void loop() {
}
