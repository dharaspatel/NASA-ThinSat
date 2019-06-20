/*  ┌──────────────────────────────────────────────────┐
    │      VCSFA Thinsat Software Template - 2019      │
    └──────────────────────────────────────────────────┘

    Description of the project
    Developed with [embedXcode](http://embedXcode.weebly.com)

    Author       Nicholas Counts
                 Counts Engineering

    Date         05/02/18 5:56 PM
    Version      0.6.0

    Copyright    © Nicholas Counts, 2018
    Licence      MIT

*/

/*  ┌──────────────────────────────────────────────────┐
 *  │    Include Custom ThinSat DataPacket Structure   │
 *  │                      NOTE:                       │
 *  │      This must be done before including the      │
 *  │                TSLPB Library header              │
 *  └──────────────────────────────────────────────────┘ */

// #include "myDataPacketStructure.h"

/*  ┌──────────────────────────────────────────────────┐
 *  │  Include Twiggs Space Lab Payload Board Library  │
 *  └──────────────────────────────────────────────────┘ */

#include "TSLPB.h"

/*  ┌──────────────────────────────────────────────────┐
 *  │   Instantiate Controller Classes and Variables   │
 *  └──────────────────────────────────────────────────┘ */

TSLPB pb;
ThinsatPacket_t data;

void setup()
{
    pb.begin();
}

void loop()
{
    // Your code goes here
    
    // Example: try to push data to NSL every 5 seconds
    
    if (pb.isClearToSend()) {
        Serial.println("Clear To Send");
        pb.pushDataToNSL(data);
    }

    delay(5000);
}