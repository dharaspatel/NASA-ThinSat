# NASA-ThinSat
---

This GitHub is a collection of 1) pcb design and logic 2) location determination 3) event triggering for mission NG13. 3 satellites will be launched - Joe Loftus, Burt Cour-Palais, Bill Rochelle. For more detail, see the GitHub Wiki.

--- 
## Joe Loftus 

Joe (also named *Cosmic DC*) has an Atmega, clock, power, and downlink capability. It keeps track of time to trigger melt wires to activate launchers and pyrolysis.

---
## Burt Cour-Palais

Burt (also named *Lt. Surge*) executes pyrolysis and launches the 4 launchers at the command of Joe. It also collects data on pyrolysis using the temperature sensor and CMOS image sensor.

---
## Bill Rochelle

Bill (also named *Fall Out Boy*), unlike Burt, has its own clock, Atmega, and downlink capability. In the next mission Bill will prove it *can* deorbit by executing all protocalls without propelant to deorbit. 
