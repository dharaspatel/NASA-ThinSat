EESchema Schematic File Version 4
EELAYER 26 0
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
L Timer_RTC:DS3231M U1
U 1 1 5D03BBFA
P 1400 1500
F 0 "U1" H 1400 1014 50  0000 C CNN
F 1 "DS3231M" H 1150 2150 50  0000 C CNN
F 2 "Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm" H 1400 900 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS3231.pdf" H 1670 1550 50  0001 C CNN
	1    1400 1500
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0101
U 1 1 5D03BD04
P 1400 1900
F 0 "#PWR0101" H 1400 1650 50  0001 C CNN
F 1 "GND" H 1405 1727 50  0000 C CNN
F 2 "" H 1400 1900 50  0001 C CNN
F 3 "" H 1400 1900 50  0001 C CNN
	1    1400 1900
	1    0    0    -1  
$EndComp
$Comp
L formula:R_10K R?
U 1 1 5D03BEF7
P 700 1150
F 0 "R?" H 770 1196 50  0000 L CNN
F 1 "R_10K" H 770 1105 50  0000 L CNN
F 2 "footprints:R_0805_OEM" H 630 1150 50  0001 C CNN
F 3 "http://www.bourns.com/data/global/pdfs/CRS.pdf" H 780 1150 50  0001 C CNN
F 4 "DK" H 700 1150 60  0001 C CNN "MFN"
F 5 "CRS0805-FX-1002ELFCT-ND" H 700 1150 60  0001 C CNN "MPN"
F 6 "https://www.digikey.com/products/en?keywords=CRS0805-FX-1002ELFCT-ND" H 1180 1550 60  0001 C CNN "PurchasingLink"
	1    700  1150
	1    0    0    -1  
$EndComp
$Comp
L formula:R_10K R?
U 1 1 5D03BF79
P 550 1150
F 0 "R?" H 620 1196 50  0000 L CNN
F 1 "R_10K" H 620 1105 50  0000 L CNN
F 2 "footprints:R_0805_OEM" H 480 1150 50  0001 C CNN
F 3 "http://www.bourns.com/data/global/pdfs/CRS.pdf" H 630 1150 50  0001 C CNN
F 4 "DK" H 550 1150 60  0001 C CNN "MFN"
F 5 "CRS0805-FX-1002ELFCT-ND" H 550 1150 60  0001 C CNN "MPN"
F 6 "https://www.digikey.com/products/en?keywords=CRS0805-FX-1002ELFCT-ND" H 1030 1550 60  0001 C CNN "PurchasingLink"
	1    550  1150
	1    0    0    -1  
$EndComp
$EndSCHEMATC
