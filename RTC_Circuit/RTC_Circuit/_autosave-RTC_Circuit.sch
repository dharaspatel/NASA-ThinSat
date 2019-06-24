EESchema Schematic File Version 4
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Timer_RTC:DS3231M U?
U 1 1 5D0BA3DC
P 2200 1800
F 0 "U?" H 1600 2900 50  0000 C CNN
F 1 "DS3231M" H 1300 2900 50  0000 C CNN
F 2 "Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm" H 2200 1200 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS3231.pdf" H 2470 1850 50  0001 C CNN
	1    2200 1800
	1    0    0    -1  
$EndComp
Text Notes 1100 600  0    50   ~ 0
Real Time Clock
$Comp
L power:+3.3V #PWR?
U 1 1 5D0BD12D
P 2100 1250
F 0 "#PWR?" H 2100 1100 50  0001 C CNN
F 1 "+3.3V" H 2115 1423 50  0000 C CNN
F 2 "" H 2100 1250 50  0001 C CNN
F 3 "" H 2100 1250 50  0001 C CNN
	1    2100 1250
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D0BEF83
P 1400 1400
F 0 "R?" H 1250 1450 50  0000 L CNN
F 1 "R" H 1250 1350 50  0000 L CNN
F 2 "" V 1330 1400 50  0001 C CNN
F 3 "~" H 1400 1400 50  0001 C CNN
	1    1400 1400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D0BFFCD
P 1600 1400
F 0 "R?" H 1670 1446 50  0000 L CNN
F 1 "R" H 1670 1355 50  0000 L CNN
F 2 "" V 1530 1400 50  0001 C CNN
F 3 "~" H 1600 1400 50  0001 C CNN
	1    1600 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	1600 1550 1600 1700
Wire Wire Line
	1600 1700 1700 1700
Wire Wire Line
	1400 1550 1400 1600
Wire Wire Line
	1400 1600 1700 1600
Wire Wire Line
	1400 1250 1600 1250
$Comp
L power:+3.3V #PWR?
U 1 1 5D0C0728
P 1600 1250
F 0 "#PWR?" H 1600 1100 50  0001 C CNN
F 1 "+3.3V" H 1615 1423 50  0000 C CNN
F 2 "" H 1600 1250 50  0001 C CNN
F 3 "" H 1600 1250 50  0001 C CNN
	1    1600 1250
	1    0    0    -1  
$EndComp
Connection ~ 1600 1250
Text Label 1150 1600 2    50   ~ 0
SCL
Wire Wire Line
	1400 1600 1150 1600
Connection ~ 1400 1600
Wire Wire Line
	1600 1700 1150 1700
Connection ~ 1600 1700
Text Label 1150 1700 2    50   ~ 0
SDA
$Comp
L power:GND #PWR?
U 1 1 5D0C4750
P 2200 2200
F 0 "#PWR?" H 2200 1950 50  0001 C CNN
F 1 "GND" H 2205 2027 50  0000 C CNN
F 2 "" H 2200 2200 50  0001 C CNN
F 3 "" H 2200 2200 50  0001 C CNN
	1    2200 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	1700 2000 1400 2000
Wire Wire Line
	1400 2000 1400 2200
Wire Wire Line
	1400 2200 2200 2200
Connection ~ 1400 2000
Wire Wire Line
	1400 2000 1150 2000
Connection ~ 2200 2200
Text Label 1150 2000 2    50   ~ 0
RST
Wire Wire Line
	2100 1400 2100 1250
$Comp
L Device:R R?
U 1 1 5D0CB013
P 2950 1400
F 0 "R?" H 2800 1450 50  0000 L CNN
F 1 "R" H 2800 1350 50  0000 L CNN
F 2 "" V 2880 1400 50  0001 C CNN
F 3 "~" H 2950 1400 50  0001 C CNN
	1    2950 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2950 1550 2950 1600
Wire Wire Line
	2950 1600 3250 1600
Wire Wire Line
	2950 1600 2700 1600
Connection ~ 2950 1600
$Comp
L Device:R R?
U 1 1 5D0CBF97
P 3150 1400
F 0 "R?" H 3200 1450 50  0000 L CNN
F 1 "R" H 3200 1350 50  0000 L CNN
F 2 "" V 3080 1400 50  0001 C CNN
F 3 "~" H 3150 1400 50  0001 C CNN
	1    3150 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 1900 3150 1900
Wire Wire Line
	3150 1900 3150 1550
Connection ~ 3150 1900
Wire Wire Line
	3150 1900 3250 1900
$Comp
L Memory_EEPROM:CAT24M01X U?
U 1 1 5D0D0209
P 4500 1200
F 0 "U?" H 4750 1750 50  0000 C CNN
F 1 "CAT24M01X" H 4400 1750 50  0000 C CNN
F 2 "Package_SO:SOIJ-8_5.3x5.3mm_P1.27mm" H 5350 950 50  0001 C CNN
F 3 "https://www.onsemi.com/pub/Collateral/CAT24M01-D.PDF" H 4500 1200 50  0001 C CNN
	1    4500 1200
	1    0    0    -1  
$EndComp
Text Notes 4150 600  0    50   ~ 0
EEPROM
$Comp
L MCU_Microchip_ATmega:ATmega32U4-MU U?
U 1 1 5D0D95A0
P 6050 2750
F 0 "U?" H 6400 4850 50  0000 C CNN
F 1 "ATmega32U4-MU" H 5900 4850 50  0000 C CNN
F 2 "Package_DFN_QFN:QFN-44-1EP_7x7mm_P0.5mm_EP5.2x5.2mm" H 6050 2750 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Datasheet.pdf" H 6050 2750 50  0001 C CNN
	1    6050 2750
	1    0    0    -1  
$EndComp
Text Notes 5600 600  0    50   ~ 0
ATMega
$EndSCHEMATC
