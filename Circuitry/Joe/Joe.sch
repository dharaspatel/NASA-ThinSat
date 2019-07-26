EESchema Schematic File Version 4
LIBS:Joe-cache
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
Text Notes 625  650  0    50   ~ 0
Real Time Clock
Wire Wire Line
	1150 1250 1150 1150
Wire Wire Line
	1000 1150 1150 1150
Wire Wire Line
	2450 1750 2750 1750
Wire Wire Line
	2750 1600 2750 1750
Connection ~ 2750 1750
Wire Wire Line
	2750 1750 3250 1750
Wire Wire Line
	2750 775  2750 1300
Wire Wire Line
	1950 1250 1950 900 
Wire Wire Line
	1950 900  2175 900 
Text Notes 8900 1775 0    50   ~ 0
Microcontroller
Text Notes 4125 650  0    50   ~ 0
NSL Connector
$Comp
L power:GND #PWR025
U 1 1 5D1611BB
P 5950 1175
F 0 "#PWR025" H 5950 925 50  0001 C CNN
F 1 "GND" H 5955 1002 50  0000 C CNN
F 2 "" H 5950 1175 50  0001 C CNN
F 3 "" H 5950 1175 50  0001 C CNN
	1    5950 1175
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR023
U 1 1 5D1639D7
P 4175 1175
F 0 "#PWR023" H 4175 925 50  0001 C CNN
F 1 "GND" H 4180 1002 50  0000 C CNN
F 2 "" H 4175 1175 50  0001 C CNN
F 3 "" H 4175 1175 50  0001 C CNN
	1    4175 1175
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 775  1850 775 
Wire Wire Line
	1850 775  1850 1250
$Comp
L MCU_Microchip_ATmega:ATmega32U4-MU U9
U 1 1 5D1491C0
P 10025 4150
F 0 "U9" H 9675 6450 50  0000 C CNN
F 1 "ATmega32U4-MU" H 9225 6450 50  0000 C CNN
F 2 "Package_DFN_QFN:QFN-44-1EP_7x7mm_P0.5mm_EP5.2x5.2mm" H 10025 4150 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Datasheet.pdf" H 10025 4150 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/microchip-technology/ATMEGA32U4-MU/ATMEGA32U4-MU-ND/1914603" H 10025 4150 50  0001 C CNN "Part URL"
	1    10025 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	10125 2350 10025 2350
Text Label 5650 1475 0    50   ~ 0
TX
Text Label 4450 1475 2    50   ~ 0
RX
$Comp
L Connector_Generic:Conn_02x03_Counter_Clockwise J1
U 1 1 5D200FC5
P 3350 3250
F 0 "J1" H 2800 3725 50  0000 C CNN
F 1 "Conn_02x03_Counter_Clockwise" H 3350 3825 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical" H 3350 3250 50  0001 C CNN
F 3 "~" H 3350 3250 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/sullins-connector-solutions/GRPB032VWVN-RC/S9015E-03-ND/1786453" H 3350 3250 50  0001 C CNN "Part URL"
	1    3350 3250
	1    0    0    -1  
$EndComp
Text Label 10825 2850 0    50   ~ 0
MOSI
Text Label 10825 2950 0    50   ~ 0
MISO
Text Label 10825 2750 0    50   ~ 0
SCK
$Comp
L power:GND #PWR035
U 1 1 5D207379
P 10025 6200
F 0 "#PWR035" H 10025 5950 50  0001 C CNN
F 1 "GND" H 10030 6027 50  0000 C CNN
F 2 "" H 10025 6200 50  0001 C CNN
F 3 "" H 10025 6200 50  0001 C CNN
	1    10025 6200
	1    0    0    -1  
$EndComp
Text Label 2950 3150 2    50   ~ 0
MISO
Text Label 2950 3350 2    50   ~ 0
SCK
Text Label 3850 3250 0    50   ~ 0
RST
Wire Wire Line
	2725 3250 2725 3175
Text Label 3850 3350 0    50   ~ 0
MOSI
$Comp
L power:GND #PWR020
U 1 1 5D212296
P 4050 3250
F 0 "#PWR020" H 4050 3000 50  0001 C CNN
F 1 "GND" H 4055 3077 50  0000 C CNN
F 2 "" H 4050 3250 50  0001 C CNN
F 3 "" H 4050 3250 50  0001 C CNN
	1    4050 3250
	1    0    0    -1  
$EndComp
Text Notes 2750 2625 0    50   ~ 0
Programming Header
Text Label 10850 3950 0    50   ~ 0
SDA
Text Label 725  1450 2    50   ~ 0
SCL
Text Label 725  1550 2    50   ~ 0
SDA
Text Label 3250 1450 0    50   ~ 0
CRYSTAL
Text Label 9225 2850 2    50   ~ 0
CRYSTAL
Text Label 3250 1750 0    50   ~ 0
SQW
Text Label 10850 4850 0    50   ~ 0
SQW
Wire Wire Line
	10625 2750 10825 2750
Wire Wire Line
	10625 2850 10825 2850
Wire Wire Line
	10625 2950 10825 2950
Wire Wire Line
	10625 3950 10850 3950
Wire Wire Line
	10625 4850 10850 4850
Wire Wire Line
	9225 2850 9425 2850
Wire Wire Line
	10025 2125 10025 2350
Wire Wire Line
	10025 5950 10025 6200
NoConn ~ 9425 3050
Text Label 900  1850 2    50   ~ 0
TMR_RST
Wire Wire Line
	3650 3250 3850 3250
Wire Wire Line
	4050 3150 4050 3250
Wire Wire Line
	3150 3150 2950 3150
Wire Wire Line
	3150 3350 2950 3350
Wire Wire Line
	10625 4550 10850 4550
Connection ~ 1150 1150
Text Label 10850 4450 0    50   ~ 0
PHO1
Wire Wire Line
	10625 3050 10825 3050
$Comp
L Device:LED D1
U 1 1 5D18A19A
P 3475 4325
F 0 "D1" H 3468 4541 50  0000 C CNN
F 1 "LED" H 3468 4450 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric" H 3475 4325 50  0001 C CNN
F 3 "~" H 3475 4325 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/lite-on-inc/LTST-C191KFKT/160-1445-1-ND/386832" H 3475 4325 50  0001 C CNN "Part URL"
	1    3475 4325
	1    0    0    -1  
$EndComp
$Comp
L Device:R R9
U 1 1 5D18F2FE
P 3175 4325
F 0 "R9" V 2968 4325 50  0000 C CNN
F 1 "440R" V 3059 4325 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 3105 4325 50  0001 C CNN
F 3 "~" H 3175 4325 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/yageo/RC0603FR-07442RL/311-442HRCT-ND/730189" H 3175 4325 50  0001 C CNN "Part URL"
	1    3175 4325
	0    1    1    0   
$EndComp
$Comp
L Device:LED D3
U 1 1 5D195D15
P 3475 4750
F 0 "D3" H 3468 4966 50  0000 C CNN
F 1 "LED" H 3468 4875 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric" H 3475 4750 50  0001 C CNN
F 3 "~" H 3475 4750 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/lite-on-inc/LTST-C191TBKT/160-1647-1-ND/573587" H 3475 4750 50  0001 C CNN "Part URL"
	1    3475 4750
	1    0    0    -1  
$EndComp
$Comp
L Device:R R11
U 1 1 5D195D1B
P 3175 4750
F 0 "R11" V 2968 4750 50  0000 C CNN
F 1 "440R" V 3059 4750 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 3105 4750 50  0001 C CNN
F 3 "~" H 3175 4750 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/yageo/RC0603FR-07442RL/311-442HRCT-ND/730189" H 3175 4750 50  0001 C CNN "Part URL"
	1    3175 4750
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR014
U 1 1 5D19812D
P 2825 4325
F 0 "#PWR014" H 2825 4075 50  0001 C CNN
F 1 "GND" H 2830 4152 50  0000 C CNN
F 2 "" H 2825 4325 50  0001 C CNN
F 3 "" H 2825 4325 50  0001 C CNN
	1    2825 4325
	1    0    0    -1  
$EndComp
Wire Wire Line
	2825 4325 3025 4325
$Comp
L power:GND #PWR016
U 1 1 5D19E020
P 2825 4750
F 0 "#PWR016" H 2825 4500 50  0001 C CNN
F 1 "GND" H 2830 4577 50  0000 C CNN
F 2 "" H 2825 4750 50  0001 C CNN
F 3 "" H 2825 4750 50  0001 C CNN
	1    2825 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	2825 4750 3025 4750
Text Label 5650 1375 0    50   ~ 0
BUSY
Text Notes 2775 4025 0    50   ~ 0
Programming LEDs
Wire Notes Line
	500  500  500  2425
Wire Notes Line
	525  2425 4000 2425
Wire Notes Line
	4000 2425 4000 500 
Wire Notes Line
	4050 2425 4050 500 
Wire Notes Line
	11175 500  8775 500 
Wire Wire Line
	725  1450 1000 1450
Wire Wire Line
	725  1550 1150 1550
Wire Wire Line
	2450 1450 2975 1450
$Comp
L Device:R R6
U 1 1 5D1CB0F1
P 1150 1400
F 0 "R6" H 1220 1446 50  0000 L CNN
F 1 "10k" H 1220 1355 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 1080 1400 50  0001 C CNN
F 3 "~" H 1150 1400 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/yageo/RT0603BRD0710KL/YAG1236CT-ND/4340589" H 1150 1400 50  0001 C CNN "Part URL"
	1    1150 1400
	1    0    0    -1  
$EndComp
Connection ~ 1150 1550
Wire Wire Line
	1150 1550 1450 1550
$Comp
L Device:R R2
U 1 1 5D1CB367
P 1000 1300
F 0 "R2" H 825 1375 50  0000 L CNN
F 1 "10k" H 825 1300 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 930 1300 50  0001 C CNN
F 3 "~" H 1000 1300 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/yageo/RT0603BRD0710KL/YAG1236CT-ND/4340589" H 1000 1300 50  0001 C CNN "Part URL"
	1    1000 1300
	1    0    0    -1  
$EndComp
Connection ~ 1000 1450
Wire Wire Line
	1000 1450 1450 1450
$Comp
L Device:CP_Small C1
U 1 1 5D1CC4E4
P 2175 1000
F 0 "C1" H 2263 1046 50  0000 L CNN
F 1 "0.1uF" H 2263 955 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 2175 1000 50  0001 C CNN
F 3 "~" H 2175 1000 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/knowles-syfer/0603Y0250104KET/1608-1305-6-ND/7383324" H 2175 1000 50  0001 C CNN "Part URL"
	1    2175 1000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR09
U 1 1 5D1CCB29
P 2175 1100
F 0 "#PWR09" H 2175 850 50  0001 C CNN
F 1 "GND" H 2180 927 50  0000 C CNN
F 2 "" H 2175 1100 50  0001 C CNN
F 3 "" H 2175 1100 50  0001 C CNN
	1    2175 1100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R7
U 1 1 5D1CCE27
P 2750 1450
F 0 "R7" H 2820 1496 50  0000 L CNN
F 1 "10k" H 2820 1405 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 2680 1450 50  0001 C CNN
F 3 "~" H 2750 1450 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/yageo/RT0603BRD0710KL/YAG1236CT-ND/4340589" H 2750 1450 50  0001 C CNN "Part URL"
	1    2750 1450
	1    0    0    -1  
$EndComp
$Comp
L Device:R R8
U 1 1 5D1CD282
P 2975 1300
F 0 "R8" H 3045 1346 50  0000 L CNN
F 1 "10k" H 3045 1255 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 2905 1300 50  0001 C CNN
F 3 "~" H 2975 1300 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/yageo/RT0603BRD0710KL/YAG1236CT-ND/4340589" H 2975 1300 50  0001 C CNN "Part URL"
	1    2975 1300
	1    0    0    -1  
$EndComp
Connection ~ 2975 1450
Wire Wire Line
	2975 1450 3250 1450
$Comp
L Device:C_Small C2
U 1 1 5D1CE9C8
P 3500 875
F 0 "C2" H 3592 921 50  0000 L CNN
F 1 "0.1uF" H 3592 830 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3500 875 50  0001 C CNN
F 3 "~" H 3500 875 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/knowles-syfer/0603Y0250104KET/1608-1305-6-ND/7383324" H 3500 875 50  0001 C CNN "Part URL"
	1    3500 875 
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR018
U 1 1 5D1CEDF2
P 3500 975
F 0 "#PWR018" H 3500 725 50  0001 C CNN
F 1 "GND" H 3505 802 50  0000 C CNN
F 2 "" H 3500 975 50  0001 C CNN
F 3 "" H 3500 975 50  0001 C CNN
	1    3500 975 
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR07
U 1 1 5D1CF616
P 1950 2050
F 0 "#PWR07" H 1950 1800 50  0001 C CNN
F 1 "GND" H 1955 1877 50  0000 C CNN
F 2 "" H 1950 2050 50  0001 C CNN
F 3 "" H 1950 2050 50  0001 C CNN
	1    1950 2050
	1    0    0    -1  
$EndComp
Text Notes 550  2625 0    50   ~ 0
Photocells
$Comp
L Device:R R1
U 1 1 5D20BD9F
P 975 3675
F 0 "R1" H 1045 3721 50  0000 L CNN
F 1 "1k" H 1045 3630 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 905 3675 50  0001 C CNN
F 3 "~" H 975 3675 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/yageo/RT0603DRD071KL/311-1.0KDCT-ND/1035738" H 975 3675 50  0001 C CNN "Part URL"
	1    975  3675
	1    0    0    -1  
$EndComp
Text Label 1175 3300 2    50   ~ 0
PHO1
Wire Wire Line
	1175 3300 1175 3525
$Comp
L power:GND #PWR01
U 1 1 5D215ECB
P 975 3825
F 0 "#PWR01" H 975 3575 50  0001 C CNN
F 1 "GND" H 980 3652 50  0000 C CNN
F 2 "" H 975 3825 50  0001 C CNN
F 3 "" H 975 3825 50  0001 C CNN
	1    975  3825
	1    0    0    -1  
$EndComp
Connection ~ 1175 3525
Wire Wire Line
	975  3525 1175 3525
Wire Wire Line
	2150 3525 2150 3300
$Comp
L Device:R R3
U 1 1 5D222394
P 1000 4800
F 0 "R3" H 1070 4846 50  0000 L CNN
F 1 "1k" H 1070 4755 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 930 4800 50  0001 C CNN
F 3 "~" H 1000 4800 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/yageo/RT0603DRD071KL/311-1.0KDCT-ND/1035738" H 1000 4800 50  0001 C CNN "Part URL"
	1    1000 4800
	1    0    0    -1  
$EndComp
Text Label 1200 4425 2    50   ~ 0
PHO2
Wire Wire Line
	1200 4425 1200 4650
$Comp
L power:GND #PWR02
U 1 1 5D22239D
P 1000 4950
F 0 "#PWR02" H 1000 4700 50  0001 C CNN
F 1 "GND" H 1005 4777 50  0000 C CNN
F 2 "" H 1000 4950 50  0001 C CNN
F 3 "" H 1000 4950 50  0001 C CNN
	1    1000 4950
	1    0    0    -1  
$EndComp
Connection ~ 1200 4650
Wire Wire Line
	1000 4650 1200 4650
Wire Wire Line
	2175 4650 2175 4425
$Comp
L Device:R R4
U 1 1 5D224EF4
P 1025 5950
F 0 "R4" H 1095 5996 50  0000 L CNN
F 1 "1k" H 1095 5905 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 955 5950 50  0001 C CNN
F 3 "~" H 1025 5950 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/yageo/RT0603DRD071KL/311-1.0KDCT-ND/1035738" H 1025 5950 50  0001 C CNN "Part URL"
	1    1025 5950
	1    0    0    -1  
$EndComp
Text Label 1225 5575 2    50   ~ 0
PHO3
Wire Wire Line
	1225 5575 1225 5800
$Comp
L power:GND #PWR03
U 1 1 5D224EFD
P 1025 6100
F 0 "#PWR03" H 1025 5850 50  0001 C CNN
F 1 "GND" H 1030 5927 50  0000 C CNN
F 2 "" H 1025 6100 50  0001 C CNN
F 3 "" H 1025 6100 50  0001 C CNN
	1    1025 6100
	1    0    0    -1  
$EndComp
Connection ~ 1225 5800
Wire Wire Line
	1025 5800 1225 5800
Wire Wire Line
	2200 5800 2200 5575
$Comp
L Device:R R5
U 1 1 5D229459
P 1050 7100
F 0 "R5" H 1120 7146 50  0000 L CNN
F 1 "1k" H 1120 7055 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 980 7100 50  0001 C CNN
F 3 "~" H 1050 7100 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/yageo/RT0603DRD071KL/311-1.0KDCT-ND/1035738" H 1050 7100 50  0001 C CNN "Part URL"
	1    1050 7100
	1    0    0    -1  
$EndComp
Text Label 1250 6725 2    50   ~ 0
PHO4
Wire Wire Line
	1250 6725 1250 6950
$Comp
L power:GND #PWR04
U 1 1 5D229462
P 1050 7250
F 0 "#PWR04" H 1050 7000 50  0001 C CNN
F 1 "GND" H 1055 7077 50  0000 C CNN
F 2 "" H 1050 7250 50  0001 C CNN
F 3 "" H 1050 7250 50  0001 C CNN
	1    1050 7250
	1    0    0    -1  
$EndComp
Connection ~ 1250 6950
Wire Wire Line
	1050 6950 1250 6950
Wire Wire Line
	2225 6950 2225 6725
Wire Notes Line
	525  2475 2600 2475
Wire Notes Line
	2600 2475 2600 7750
Wire Notes Line
	2600 7750 500  7750
Wire Notes Line
	500  7750 500  2475
Connection ~ 2750 775 
Wire Wire Line
	2975 775  3500 775 
Wire Notes Line
	3975 500  500  500 
Wire Wire Line
	2975 775  2975 1150
Connection ~ 2975 775 
Wire Wire Line
	2750 775  2975 775 
Text Notes 7025 6775 0    118  ~ 24
JOE LOFTUS
Wire Wire Line
	10625 4450 10850 4450
Wire Wire Line
	10625 4250 10850 4250
Text Label 10850 5550 0    50   ~ 0
PHO2
Text Label 10825 2650 0    50   ~ 0
PHO3
Text Label 10850 4250 0    50   ~ 0
PHO4
Text Label 4775 2925 2    50   ~ 0
TEMP
Wire Wire Line
	9425 2650 9225 2650
Text Label 9225 2650 2    50   ~ 0
RST
Text Label 10825 3350 0    50   ~ 0
TMR_RST
Wire Wire Line
	10625 3350 10825 3350
Text Label 10850 3850 0    50   ~ 0
SCL
Wire Wire Line
	10625 3850 10850 3850
Wire Wire Line
	9925 5950 10025 5950
Connection ~ 10025 5950
NoConn ~ 4450 1275
Wire Wire Line
	900  1850 1450 1850
Wire Wire Line
	1150 1150 1150 975 
$Comp
L power:+3V3 #PWR05
U 1 1 5D2D733F
P 1150 975
F 0 "#PWR05" H 1150 825 50  0001 C CNN
F 1 "+3V3" H 1165 1148 50  0000 C CNN
F 2 "" H 1150 975 50  0001 C CNN
F 3 "" H 1150 975 50  0001 C CNN
	1    1150 975 
	1    0    0    -1  
$EndComp
$Comp
L Device:C C3
U 1 1 5D33F6A0
P 8950 3400
F 0 "C3" H 9065 3446 50  0000 L CNN
F 1 "1uF" H 9065 3355 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 8988 3250 50  0001 C CNN
F 3 "~" H 8950 3400 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/murata-electronics-north-america/GCM188R71C105KA64D/490-5241-1-ND/1979252" H 8950 3400 50  0001 C CNN "Part URL"
	1    8950 3400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR031
U 1 1 5D3400A3
P 8950 3550
F 0 "#PWR031" H 8950 3300 50  0001 C CNN
F 1 "GND" H 8955 3377 50  0000 C CNN
F 2 "" H 8950 3550 50  0001 C CNN
F 3 "" H 8950 3550 50  0001 C CNN
	1    8950 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	8950 3250 9425 3250
$Comp
L Device:C C4
U 1 1 5D3463CF
P 8950 4100
F 0 "C4" H 9065 4146 50  0000 L CNN
F 1 "1uF" H 9065 4055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 8988 3950 50  0001 C CNN
F 3 "~" H 8950 4100 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/murata-electronics-north-america/GCM188R71C105KA64D/490-5241-1-ND/1979252" H 8950 4100 50  0001 C CNN "Part URL"
	1    8950 4100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR032
U 1 1 5D3463D5
P 8950 4250
F 0 "#PWR032" H 8950 4000 50  0001 C CNN
F 1 "GND" H 8955 4077 50  0000 C CNN
F 2 "" H 8950 4250 50  0001 C CNN
F 3 "" H 8950 4250 50  0001 C CNN
	1    8950 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	8950 3950 9425 3950
Text Label 10850 4150 0    50   ~ 0
RX
Text Label 10850 4050 0    50   ~ 0
TX
Wire Wire Line
	10625 4050 10850 4050
Wire Wire Line
	10625 4150 10850 4150
Wire Wire Line
	10625 5150 10850 5150
Wire Wire Line
	10625 5250 10850 5250
Wire Wire Line
	10625 5350 10850 5350
Wire Wire Line
	10625 5450 10850 5450
Wire Wire Line
	10625 3150 10825 3150
Wire Wire Line
	10625 3250 10825 3250
Text Label 5650 1275 0    50   ~ 0
STBY
Text Label 10825 3550 0    50   ~ 0
STBY
Wire Wire Line
	10625 3550 10825 3550
Wire Wire Line
	3725 6025 3925 6025
Text Label 3725 6125 0    50   ~ 0
WC
Text Label 3725 6225 0    50   ~ 0
SCL
Text Label 3725 6325 0    50   ~ 0
SDA
$Comp
L power:GND #PWR017
U 1 1 5D2C2E70
P 2900 6325
F 0 "#PWR017" H 2900 6075 50  0001 C CNN
F 1 "GND" H 2905 6152 50  0000 C CNN
F 2 "" H 2900 6325 50  0001 C CNN
F 3 "" H 2900 6325 50  0001 C CNN
	1    2900 6325
	1    0    0    -1  
$EndComp
Wire Wire Line
	3075 6325 2900 6325
Text Label 10850 4350 0    50   ~ 0
WC
Wire Notes Line
	2650 2475 4150 2475
Wire Notes Line
	4150 2475 4150 3825
Wire Notes Line
	4150 3825 2650 3825
Wire Notes Line
	2650 3825 2650 2475
Wire Notes Line
	2650 3875 4150 3875
Wire Notes Line
	4150 3875 4150 5375
Wire Notes Line
	4150 5375 2650 5375
Wire Notes Line
	2650 3875 2650 5375
$Comp
L Custom:DF12-20DS-Custom U7
U 1 1 5D782D20
P 5050 1525
F 0 "U7" H 5050 2200 50  0000 C CNN
F 1 "DF12-20DS" H 5050 2109 50  0000 C CNN
F 2 "Custom:DF12-20DS-0.5V(86)" H 5050 2125 50  0001 C CNN
F 3 "" H 5050 2125 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/hirose-electric-co-ltd/DF12-20DS-0.5V-86/H5214CT-ND/948727" H 5050 1525 50  0001 C CNN "Part URL"
	1    5050 1525
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 1175 5950 1175
Wire Wire Line
	4450 1175 4175 1175
Wire Wire Line
	4450 1075 4175 1075
Wire Wire Line
	4175 1075 4175 1000
Wire Wire Line
	5650 1075 5950 1075
Wire Wire Line
	5950 1075 5950 1025
$Comp
L power:+5V #PWR024
U 1 1 5D7BEF66
P 5950 1025
F 0 "#PWR024" H 5950 875 50  0001 C CNN
F 1 "+5V" H 5965 1198 50  0000 C CNN
F 2 "" H 5950 1025 50  0001 C CNN
F 3 "" H 5950 1025 50  0001 C CNN
	1    5950 1025
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR022
U 1 1 5D7BFD46
P 4175 1000
F 0 "#PWR022" H 4175 850 50  0001 C CNN
F 1 "+3V3" H 4190 1173 50  0000 C CNN
F 2 "" H 4175 1000 50  0001 C CNN
F 3 "" H 4175 1000 50  0001 C CNN
	1    4175 1000
	1    0    0    -1  
$EndComp
Wire Notes Line
	4050 2425 6200 2425
Wire Notes Line
	6200 2425 6200 500 
Wire Notes Line
	6200 500  4050 500 
$Comp
L Connector:Micro_SD_Card J4
U 1 1 5D33A763
P 7700 1500
F 0 "J4" H 7650 2217 50  0000 C CNN
F 1 "Micro_SD_Card" H 7650 2126 50  0000 C CNN
F 2 "Connector_Card:microSD_HC_Wuerth_693072010801" H 8850 1800 50  0001 C CNN
F 3 "http://katalog.we-online.de/em/datasheet/693072010801.pdf" H 7700 1500 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/wurth-electronics-inc/693072010801/732-3820-1-ND/3124605" H 7700 1500 50  0001 C CNN "Part URL"
	1    7700 1500
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR030
U 1 1 5D33B7A8
P 8500 2100
F 0 "#PWR030" H 8500 1850 50  0001 C CNN
F 1 "GND" H 8505 1927 50  0000 C CNN
F 2 "" H 8500 2100 50  0001 C CNN
F 3 "" H 8500 2100 50  0001 C CNN
	1    8500 2100
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR027
U 1 1 5D33BC9C
P 6800 1500
F 0 "#PWR027" H 6800 1350 50  0001 C CNN
F 1 "+3V3" V 6815 1628 50  0000 L CNN
F 2 "" H 6800 1500 50  0001 C CNN
F 3 "" H 6800 1500 50  0001 C CNN
	1    6800 1500
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR026
U 1 1 5D33D19A
P 6600 1700
F 0 "#PWR026" H 6600 1450 50  0001 C CNN
F 1 "GND" H 6605 1527 50  0000 C CNN
F 2 "" H 6600 1700 50  0001 C CNN
F 3 "" H 6600 1700 50  0001 C CNN
	1    6600 1700
	0    1    1    0   
$EndComp
Text Label 6800 1400 2    50   ~ 0
MOSI
Text Label 6800 1300 2    50   ~ 0
~CS_SD
Text Label 6800 1600 2    50   ~ 0
SCK
Text Label 6800 1800 2    50   ~ 0
MISO
Wire Wire Line
	6600 1700 6800 1700
NoConn ~ 6800 1900
NoConn ~ 6800 1200
Text Label 10850 5050 0    50   ~ 0
~CS_SD
Wire Wire Line
	10625 3650 10850 3650
Wire Wire Line
	3075 6225 2900 6225
Wire Wire Line
	2900 6225 2900 6325
Connection ~ 2900 6325
Wire Wire Line
	3075 6125 2900 6125
Wire Wire Line
	2900 6125 2900 6225
Connection ~ 2900 6225
Wire Wire Line
	3075 6025 2900 6025
Wire Wire Line
	2900 6025 2900 6125
Connection ~ 2900 6125
$Comp
L power:+3V3 #PWR021
U 1 1 5D3707C8
P 3925 6025
F 0 "#PWR021" H 3925 5875 50  0001 C CNN
F 1 "+3V3" H 3940 6198 50  0000 C CNN
F 2 "" H 3925 6025 50  0001 C CNN
F 3 "" H 3925 6025 50  0001 C CNN
	1    3925 6025
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR06
U 1 1 5D372C37
P 1850 775
F 0 "#PWR06" H 1850 625 50  0001 C CNN
F 1 "+3V3" H 1865 948 50  0000 C CNN
F 2 "" H 1850 775 50  0001 C CNN
F 3 "" H 1850 775 50  0001 C CNN
	1    1850 775 
	1    0    0    -1  
$EndComp
Connection ~ 1850 775 
$Comp
L power:+3V3 #PWR012
U 1 1 5D378F26
P 2225 6725
F 0 "#PWR012" H 2225 6575 50  0001 C CNN
F 1 "+3V3" H 2240 6898 50  0000 C CNN
F 2 "" H 2225 6725 50  0001 C CNN
F 3 "" H 2225 6725 50  0001 C CNN
	1    2225 6725
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR011
U 1 1 5D3794CC
P 2200 5575
F 0 "#PWR011" H 2200 5425 50  0001 C CNN
F 1 "+3V3" H 2215 5748 50  0000 C CNN
F 2 "" H 2200 5575 50  0001 C CNN
F 3 "" H 2200 5575 50  0001 C CNN
	1    2200 5575
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR010
U 1 1 5D379B58
P 2175 4425
F 0 "#PWR010" H 2175 4275 50  0001 C CNN
F 1 "+3V3" H 2190 4598 50  0000 C CNN
F 2 "" H 2175 4425 50  0001 C CNN
F 3 "" H 2175 4425 50  0001 C CNN
	1    2175 4425
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR08
U 1 1 5D37A5AE
P 2150 3300
F 0 "#PWR08" H 2150 3150 50  0001 C CNN
F 1 "+3V3" H 2165 3473 50  0000 C CNN
F 2 "" H 2150 3300 50  0001 C CNN
F 3 "" H 2150 3300 50  0001 C CNN
	1    2150 3300
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR019
U 1 1 5D37B22F
P 2725 3175
F 0 "#PWR019" H 2725 3025 50  0001 C CNN
F 1 "+3V3" H 2740 3348 50  0000 C CNN
F 2 "" H 2725 3175 50  0001 C CNN
F 3 "" H 2725 3175 50  0001 C CNN
	1    2725 3175
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR034
U 1 1 5D37C4D1
P 10025 2125
F 0 "#PWR034" H 10025 1975 50  0001 C CNN
F 1 "+3V3" H 10040 2298 50  0000 C CNN
F 2 "" H 10025 2125 50  0001 C CNN
F 3 "" H 10025 2125 50  0001 C CNN
	1    10025 2125
	1    0    0    -1  
$EndComp
$Comp
L Connector:USB_B_Micro J3
U 1 1 5D37DE2D
P 7125 3000
F 0 "J3" H 7182 3467 50  0000 C CNN
F 1 "USB_B_Micro" H 7182 3376 50  0000 C CNN
F 2 "Connector_USB:USB_Micro-B_Molex-105017-0001" H 7275 2950 50  0001 C CNN
F 3 "~" H 7275 2950 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/molex/1050170001/WM1399CT-ND/2350885" H 7125 3000 50  0001 C CNN "Part URL"
	1    7125 3000
	1    0    0    -1  
$EndComp
Text Label 7425 3000 0    50   ~ 0
D+
Text Label 7425 3100 0    50   ~ 0
D-
Text Label 9425 3650 2    50   ~ 0
D+
Text Label 9425 3750 2    50   ~ 0
D-
Wire Wire Line
	7425 2800 7500 2800
$Comp
L power:GND #PWR028
U 1 1 5D385ECE
P 7025 3400
F 0 "#PWR028" H 7025 3150 50  0001 C CNN
F 1 "GND" H 7030 3227 50  0000 C CNN
F 2 "" H 7025 3400 50  0001 C CNN
F 3 "" H 7025 3400 50  0001 C CNN
	1    7025 3400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR029
U 1 1 5D386288
P 7125 3400
F 0 "#PWR029" H 7125 3150 50  0001 C CNN
F 1 "GND" H 7130 3227 50  0000 C CNN
F 2 "" H 7125 3400 50  0001 C CNN
F 3 "" H 7125 3400 50  0001 C CNN
	1    7125 3400
	1    0    0    -1  
$EndComp
Text Label 7500 2800 0    50   ~ 0
VBUS
$Comp
L Regulator_Linear:AP2127N-3.3 U8
U 1 1 5D3894A7
P 10025 1150
F 0 "U8" H 9525 1300 50  0000 C CNN
F 1 "AP2127N-3.3" H 9150 1300 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 10025 1375 50  0001 C CIN
F 3 "https://www.diodes.com/assets/Datasheets/AP2127.pdf" H 10025 1150 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/diodes-incorporated/AP2127N-3.3TRG1/AP2127N-3.3TRG1DICT-ND/8545775" H 10025 1150 50  0001 C CNN "Part URL"
	1    10025 1150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR033
U 1 1 5D38A5D4
P 10025 1450
F 0 "#PWR033" H 10025 1200 50  0001 C CNN
F 1 "GND" H 10030 1277 50  0000 C CNN
F 2 "" H 10025 1450 50  0001 C CNN
F 3 "" H 10025 1450 50  0001 C CNN
	1    10025 1450
	1    0    0    -1  
$EndComp
Text Label 9725 1150 2    50   ~ 0
VBUS
Text Label 9925 2350 2    50   ~ 0
VBUS
$Comp
L power:+3V3 #PWR036
U 1 1 5D38F4D1
P 10325 1150
F 0 "#PWR036" H 10325 1000 50  0001 C CNN
F 1 "+3V3" H 10340 1323 50  0000 C CNN
F 2 "" H 10325 1150 50  0001 C CNN
F 3 "" H 10325 1150 50  0001 C CNN
	1    10325 1150
	1    0    0    -1  
$EndComp
NoConn ~ 7425 3200
$Comp
L Device:Battery_Cell BT1
U 1 1 5D39BFD5
P 2575 1100
F 0 "BT1" H 2693 1196 50  0000 L CNN
F 1 "Battery_Cell" H 2693 1105 50  0000 L CNN
F 2 "Battery:BatteryHolder_Keystone_3034_1x20mm" V 2575 1160 50  0001 C CNN
F 3 "~" V 2575 1160 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/keystone-electronics/3034TR/36-3034CT-ND/4833649" H 2575 1100 50  0001 C CNN "Part URL"
	1    2575 1100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR013
U 1 1 5D39D1C7
P 2575 1200
F 0 "#PWR013" H 2575 950 50  0001 C CNN
F 1 "GND" H 2580 1027 50  0000 C CNN
F 2 "" H 2575 1200 50  0001 C CNN
F 3 "" H 2575 1200 50  0001 C CNN
	1    2575 1200
	1    0    0    -1  
$EndComp
Wire Wire Line
	2575 900  2175 900 
Connection ~ 2175 900 
NoConn ~ 4450 1675
NoConn ~ 4450 1775
NoConn ~ 4450 1875
NoConn ~ 4450 1975
NoConn ~ 5650 1975
NoConn ~ 5650 1875
NoConn ~ 5650 1775
NoConn ~ 5650 1675
NoConn ~ 5650 1575
NoConn ~ 4450 1575
Text Label 9425 3450 2    50   ~ 0
VBUS
Text Label 10850 5250 0    50   ~ 0
RCLK
Text Label 10850 5150 0    50   ~ 0
SRCLK
Text Notes 2775 5575 0    50   ~ 0
EEPROM\n
Text Label 4775 3025 2    50   ~ 0
CS_IMG
Text Label 4775 3125 2    50   ~ 0
MOSI
Text Label 4775 3825 2    50   ~ 0
SER
Text Label 4775 3925 2    50   ~ 0
SRCLK
Text Label 4775 4025 2    50   ~ 0
RCLK
$Comp
L Timer_RTC:DS3231MZ U5
U 1 1 5D2C648B
P 1950 1650
F 0 "U5" H 675 2475 50  0000 C CNN
F 1 "DS3231MZ" H 825 2575 50  0000 C CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 1950 1150 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS3231M.pdf" H 1950 1050 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/maxim-integrated/DS3231MZ/DS3231MZ-ND/2754396" H 1950 1650 50  0001 C CNN "Part URL"
	1    1950 1650
	1    0    0    -1  
$EndComp
Text Notes 5200 2925 0    39   ~ 0
Temp Sensor Data Input
Text Notes 5200 3025 0    39   ~ 0
CS Output for Img Sensor
Text Notes 5200 3125 0    39   ~ 0
MOSI Output for Img Sensor
Text Notes 5200 3625 0    39   ~ 0
Burn Wire Output 1 for Pyrolysis
Text Notes 5200 3725 0    39   ~ 0
Burn Wire Output 2 for Pyrolysis
Text Notes 5200 3825 0    39   ~ 0
Serial Output for Shift Reg
Text Notes 5200 4025 0    39   ~ 0
Reg Clk Output for Shift Reg
Text Notes 4600 2750 0    39   ~ 0
Input = Data from Burt to Joe\nOutput = Data from Joe to Burt
Wire Notes Line
	4200 2475 6200 2475
Wire Notes Line
	6200 2475 6200 4775
Wire Notes Line
	4200 4775 4200 2475
Wire Notes Line
	2650 5425 4150 5425
Wire Notes Line
	4150 5425 4150 6650
Wire Notes Line
	4150 6650 2650 6650
Wire Notes Line
	2650 6650 2650 5425
Text Notes 6325 650  0    50   ~ 0
Data Storage: USB and SD
Wire Notes Line
	6275 500  8725 500 
Wire Notes Line
	8725 500  8725 3825
Wire Notes Line
	8725 3825 6275 3825
Wire Notes Line
	6275 3825 6275 500 
Text Label 10850 4550 0    50   ~ 0
PLED1
Wire Wire Line
	10625 2650 10825 2650
Text Label 10850 4750 0    50   ~ 0
TEMP
Wire Wire Line
	10625 4750 10850 4750
Text Label 10825 3050 0    50   ~ 0
PLED3
Wire Wire Line
	10625 5550 10850 5550
Text Label 3625 4750 0    50   ~ 0
PLED3
Text Label 3625 4325 0    50   ~ 0
PLED1
Connection ~ 10025 2350
Text Notes 8900 925  0    50   ~ 0
5V to 3.3V Regulator\n
Wire Notes Line
	11175 500  11175 6450
Wire Notes Line
	11175 6450 8775 6450
Wire Notes Line
	8775 500  8775 6450
$Comp
L Device:R_PHOTO R12
U 1 1 5D3F3BA1
P 1650 3525
F 0 "R12" V 1325 3525 50  0000 C CNN
F 1 "R_PHOTO" V 1416 3525 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x02_P2.00mm_Vertical" V 1700 3275 50  0001 L CNN
F 3 "~" H 1650 3475 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/advanced-photonix/NSL-5910/NSL-5910-ND/5436028" H 1650 3525 50  0001 C CNN "Part URL"
	1    1650 3525
	0    1    1    0   
$EndComp
$Comp
L Device:R_PHOTO R13
U 1 1 5D40B08B
P 1700 4650
F 0 "R13" V 1375 4650 50  0000 C CNN
F 1 "R_PHOTO" V 1466 4650 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x02_P2.00mm_Vertical" V 1750 4400 50  0001 L CNN
F 3 "~" H 1700 4600 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/advanced-photonix/NSL-5910/NSL-5910-ND/5436028" H 1700 4650 50  0001 C CNN "Part URL"
	1    1700 4650
	0    1    1    0   
$EndComp
$Comp
L Device:R_PHOTO R14
U 1 1 5D40BCB5
P 1725 5800
F 0 "R14" V 1400 5800 50  0000 C CNN
F 1 "R_PHOTO" V 1491 5800 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x02_P2.00mm_Vertical" V 1775 5550 50  0001 L CNN
F 3 "~" H 1725 5750 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/advanced-photonix/NSL-5910/NSL-5910-ND/5436028" H 1725 5800 50  0001 C CNN "Part URL"
	1    1725 5800
	0    1    1    0   
$EndComp
$Comp
L Device:R_PHOTO R15
U 1 1 5D40F4BF
P 1750 6950
F 0 "R15" V 1425 6950 50  0000 C CNN
F 1 "R_PHOTO" V 1516 6950 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x02_P2.00mm_Vertical" V 1800 6700 50  0001 L CNN
F 3 "~" H 1750 6900 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/advanced-photonix/NSL-5910/NSL-5910-ND/5436028" H 1750 6950 50  0001 C CNN "Part URL"
	1    1750 6950
	0    1    1    0   
$EndComp
Wire Wire Line
	1175 3525 1500 3525
Wire Wire Line
	1800 3525 2150 3525
Wire Wire Line
	1200 4650 1550 4650
Wire Wire Line
	1850 4650 2175 4650
Wire Wire Line
	1225 5800 1575 5800
Wire Wire Line
	1875 5800 2200 5800
Wire Wire Line
	1250 6950 1600 6950
Wire Wire Line
	1900 6950 2225 6950
Text Label 4775 4125 2    50   ~ 0
IN1
Text Label 4775 4225 2    50   ~ 0
IN2
Text Notes 5200 4125 0    39   ~ 0
Motor Driver for Launchers Output 1
Text Notes 5200 4225 0    39   ~ 0
Motor Driver for Launchers Output 2\n
Text Notes 5200 3925 0    39   ~ 0
Serial Clk Output for Shift Reg
Text Label 4775 3225 2    50   ~ 0
MISO
Text Label 4775 3325 2    50   ~ 0
SCK
Text Label 4775 3425 2    50   ~ 0
SDA
Text Label 4775 3525 2    50   ~ 0
SCL
Text Notes 5200 3225 0    39   ~ 0
MISO Output for Img Sensor
Text Notes 5200 3325 0    39   ~ 0
SCLK Output for Img Sensor
Text Notes 5200 3425 0    39   ~ 0
SDA Output for Img Sensor
Text Notes 5200 3525 0    39   ~ 0
SCL Output for Img Sensor
$Comp
L power:+3V3 #PWR037
U 1 1 5D47F25B
P 4650 4325
F 0 "#PWR037" H 4650 4175 50  0001 C CNN
F 1 "+3V3" V 4665 4453 50  0000 L CNN
F 2 "" H 4650 4325 50  0001 C CNN
F 3 "" H 4650 4325 50  0001 C CNN
	1    4650 4325
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR038
U 1 1 5D480338
P 4650 4425
F 0 "#PWR038" H 4650 4275 50  0001 C CNN
F 1 "+5V" V 4665 4553 50  0000 L CNN
F 2 "" H 4650 4425 50  0001 C CNN
F 3 "" H 4650 4425 50  0001 C CNN
	1    4650 4425
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR039
U 1 1 5D480BD6
P 4600 4525
F 0 "#PWR039" H 4600 4275 50  0001 C CNN
F 1 "GND" H 4605 4352 50  0000 C CNN
F 2 "" H 4600 4525 50  0001 C CNN
F 3 "" H 4600 4525 50  0001 C CNN
	1    4600 4525
	1    0    0    -1  
$EndComp
NoConn ~ 4450 1375
$Comp
L Custom:UFDFPN8-MC-Custom U6
U 1 1 5D2D63AB
P 3375 6125
F 0 "U6" H 3400 6490 50  0000 C CNN
F 1 "M24C32-XDW5TP" H 3400 6399 50  0000 C CNN
F 2 "Package_SO:TSSOP-8_4.4x3mm_P0.65mm" H 3375 6125 50  0001 C CNN
F 3 "https://www.st.com/content/ccc/resource/technical/document/datasheet/80/4e/8c/54/f2/63/4c/4a/CD00001012.pdf/files/CD00001012.pdf/jcr:content/translations/en.CD00001012.pdf" H 3375 6125 50  0001 C CNN
F 4 "https://www.digikey.com/product-detail/en/stmicroelectronics/M24C32-XDW5TP/497-16068-1-ND/5476770" H 3375 6125 50  0001 C CNN "Part URL"
	1    3375 6125
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x20 J2
U 1 1 5D2D5DCB
P 4975 3825
F 0 "J2" H 5055 3817 50  0000 L CNN
F 1 "Conn_01x20" H 5055 3726 50  0000 L CNN
F 2 "Custom:62674-201121ALF" H 4975 3825 50  0001 C CNN
F 3 "~" H 4975 3825 50  0001 C CNN
	1    4975 3825
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 4325 4775 4325
Wire Wire Line
	4650 4425 4775 4425
Wire Wire Line
	4600 4525 4775 4525
NoConn ~ 4775 4625
NoConn ~ 4775 4725
NoConn ~ 4775 4825
Wire Wire Line
	10625 4350 10850 4350
Wire Wire Line
	10625 5050 10850 5050
Text Label 10850 3650 0    50   ~ 0
CS_IMG
Text Label 10825 3250 0    50   ~ 0
SER
Text Label 10825 3150 0    50   ~ 0
BUSY
Text Label 10850 5350 0    50   ~ 0
IN1
Text Label 10850 5450 0    50   ~ 0
IN2
Wire Wire Line
	2725 3250 3150 3250
Wire Wire Line
	3650 3150 4050 3150
Wire Wire Line
	3650 3350 3850 3350
NoConn ~ 4775 3625
NoConn ~ 4775 3725
$EndSCHEMATC
