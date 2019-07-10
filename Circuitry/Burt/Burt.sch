EESchema Schematic File Version 4
LIBS:Burt-cache
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
L power:+5V #PWR?
U 1 1 5D2E0611
P 4975 3875
F 0 "#PWR?" H 4975 3725 50  0001 C CNN
F 1 "+5V" H 4990 4048 50  0000 C CNN
F 2 "" H 4975 3875 50  0001 C CNN
F 3 "" H 4975 3875 50  0001 C CNN
	1    4975 3875
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D?
U 1 1 5D18A19A
P 6275 3875
F 0 "D?" H 6268 4091 50  0000 C CNN
F 1 "LED" H 6268 4000 50  0000 C CNN
F 2 "" H 6275 3875 50  0001 C CNN
F 3 "~" H 6275 3875 50  0001 C CNN
	1    6275 3875
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D18F2FE
P 5975 3875
F 0 "R?" V 5768 3875 50  0000 C CNN
F 1 "R" V 5859 3875 50  0000 C CNN
F 2 "" V 5905 3875 50  0001 C CNN
F 3 "~" H 5975 3875 50  0001 C CNN
	1    5975 3875
	0    1    1    0   
$EndComp
$Comp
L Device:LED D?
U 1 1 5D19383C
P 6275 4200
F 0 "D?" H 6268 4416 50  0000 C CNN
F 1 "LED" H 6268 4325 50  0000 C CNN
F 2 "" H 6275 4200 50  0001 C CNN
F 3 "~" H 6275 4200 50  0001 C CNN
	1    6275 4200
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D193842
P 5975 4200
F 0 "R?" V 5768 4200 50  0000 C CNN
F 1 "R" V 5859 4200 50  0000 C CNN
F 2 "" V 5905 4200 50  0001 C CNN
F 3 "~" H 5975 4200 50  0001 C CNN
	1    5975 4200
	0    1    1    0   
$EndComp
$Comp
L Device:LED D?
U 1 1 5D195D15
P 6275 4525
F 0 "D?" H 6268 4741 50  0000 C CNN
F 1 "LED" H 6268 4650 50  0000 C CNN
F 2 "" H 6275 4525 50  0001 C CNN
F 3 "~" H 6275 4525 50  0001 C CNN
	1    6275 4525
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D195D1B
P 5975 4525
F 0 "R?" V 5768 4525 50  0000 C CNN
F 1 "R" V 5859 4525 50  0000 C CNN
F 2 "" V 5905 4525 50  0001 C CNN
F 3 "~" H 5975 4525 50  0001 C CNN
	1    5975 4525
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5D19812D
P 5625 3875
F 0 "#PWR?" H 5625 3625 50  0001 C CNN
F 1 "GND" H 5630 3702 50  0000 C CNN
F 2 "" H 5625 3875 50  0001 C CNN
F 3 "" H 5625 3875 50  0001 C CNN
	1    5625 3875
	1    0    0    -1  
$EndComp
Wire Wire Line
	5625 3875 5825 3875
$Comp
L power:GND #PWR?
U 1 1 5D19BB8C
P 5625 4200
F 0 "#PWR?" H 5625 3950 50  0001 C CNN
F 1 "GND" H 5630 4027 50  0000 C CNN
F 2 "" H 5625 4200 50  0001 C CNN
F 3 "" H 5625 4200 50  0001 C CNN
	1    5625 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5625 4200 5825 4200
$Comp
L power:GND #PWR?
U 1 1 5D19E020
P 5625 4525
F 0 "#PWR?" H 5625 4275 50  0001 C CNN
F 1 "GND" H 5630 4352 50  0000 C CNN
F 2 "" H 5625 4525 50  0001 C CNN
F 3 "" H 5625 4525 50  0001 C CNN
	1    5625 4525
	1    0    0    -1  
$EndComp
Wire Wire Line
	5625 4525 5825 4525
Text Notes 5525 3525 0    50   ~ 0
Programming LEDs
Text Notes 5325 1025 0    50   ~ 0
CMOS Image Sensor\nMode: global shutter\nInput: 5V Vdd\nOutput: Digital VIDEO_S
Text Notes 7000 6750 0    118  ~ 24
BURT 
Text Label 5925 6550 2    50   ~ 0
TEMP
Text Label 5925 6650 2    50   ~ 0
VID
Text Label 5925 6750 2    50   ~ 0
CRYSTAL
$Comp
L Device:R_Small R?
U 1 1 5D25A247
P 1575 2025
F 0 "R?" V 1771 2025 50  0001 C CNN
F 1 "82" V 1650 2025 50  0000 C CNN
F 2 "" H 1575 2025 50  0001 C CNN
F 3 "~" H 1575 2025 50  0001 C CNN
	1    1575 2025
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_Small R?
U 1 1 5D25AB70
P 5025 2275
F 0 "R?" V 5221 2275 50  0001 C CNN
F 1 "100" V 5129 2275 50  0000 C CNN
F 2 "" H 5025 2275 50  0001 C CNN
F 3 "~" H 5025 2275 50  0001 C CNN
	1    5025 2275
	0    -1   -1   0   
$EndComp
$Comp
L Burt-rescue:LT1818-Custom U?
U 1 1 5D25B2EA
P 5425 2375
F 0 "U?" H 5475 2100 50  0000 L CNN
F 1 "LT1818" H 5475 2200 50  0000 L CNN
F 2 "" H 5425 2375 50  0001 C CNN
F 3 "" H 5475 2575 50  0001 C CNN
	1    5425 2375
	1    0    0    -1  
$EndComp
Wire Wire Line
	4875 1875 4875 2275
Wire Wire Line
	4875 2275 4925 2275
$Comp
L power:-5V #PWR?
U 1 1 5D2701C2
P 5325 2800
F 0 "#PWR?" H 5325 2900 50  0001 C CNN
F 1 "-5V" H 5340 2973 50  0000 C CNN
F 2 "" H 5325 2800 50  0001 C CNN
F 3 "" H 5325 2800 50  0001 C CNN
	1    5325 2800
	-1   0    0    1   
$EndComp
Wire Wire Line
	4875 1375 4950 1375
$Comp
L Burt-rescue:74HC541-Custom U?
U 1 1 5D287D5C
P 2025 2025
F 0 "U?" H 2000 2540 50  0000 C CNN
F 1 "74HC541" H 2000 2449 50  0000 C CNN
F 2 "" H 1675 2775 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/74HC_HCT541.pdf" H 1675 2775 50  0001 C CNN
	1    2025 2025
	1    0    0    -1  
$EndComp
NoConn ~ 2325 2425
NoConn ~ 2325 2525
NoConn ~ 2325 2625
NoConn ~ 2325 2725
NoConn ~ 1675 2625
NoConn ~ 1675 2525
NoConn ~ 1675 2425
NoConn ~ 1675 2325
$Comp
L Device:R_Small R?
U 1 1 5D298138
P 1350 1925
F 0 "R?" V 1546 1925 50  0001 C CNN
F 1 "82" V 1425 1925 50  0000 C CNN
F 2 "" H 1350 1925 50  0001 C CNN
F 3 "~" H 1350 1925 50  0001 C CNN
	1    1350 1925
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1150 1925 1250 1925
Wire Wire Line
	1150 2025 1475 2025
Wire Wire Line
	1450 1925 1675 1925
Text Label 4950 1175 0    50   ~ 0
ST
Text Label 4950 1375 0    50   ~ 0
CLK
Wire Wire Line
	4875 1175 4950 1175
Text Label 2450 2125 0    50   ~ 0
ST
Text Label 2450 2025 0    50   ~ 0
CLK
Wire Wire Line
	2325 2025 2450 2025
Wire Wire Line
	2325 2125 2450 2125
Wire Wire Line
	1675 2125 1500 2125
Wire Wire Line
	1675 2225 1500 2225
Text Label 1500 2125 2    50   ~ 0
trig
Text Label 1500 2225 2    50   ~ 0
eos
Text Label 2450 2225 0    50   ~ 0
TRIG
Text Label 2450 2325 0    50   ~ 0
EOS
Wire Wire Line
	2325 2225 2450 2225
Wire Wire Line
	2325 2325 2450 2325
Text Label 4950 1275 0    50   ~ 0
trig
Text Label 4975 1675 0    50   ~ 0
eos
Wire Wire Line
	4875 1275 4950 1275
Wire Wire Line
	4875 1675 4975 1675
$Comp
L Device:C_Small C?
U 1 1 5D2B8788
P 5575 1975
F 0 "C?" H 5650 1825 50  0000 R CNN
F 1 "0.1uF" H 5650 1725 50  0000 R CNN
F 2 "" H 5575 1975 50  0001 C CNN
F 3 "~" H 5575 1975 50  0001 C CNN
	1    5575 1975
	-1   0    0    1   
$EndComp
Wire Wire Line
	5325 2075 5325 1875
$Comp
L power:+5V #PWR?
U 1 1 5D2BA5C3
P 5325 1875
F 0 "#PWR?" H 5325 1725 50  0001 C CNN
F 1 "+5V" H 5340 2048 50  0000 C CNN
F 2 "" H 5325 1875 50  0001 C CNN
F 3 "" H 5325 1875 50  0001 C CNN
	1    5325 1875
	1    0    0    -1  
$EndComp
Wire Wire Line
	5325 1875 5575 1875
Connection ~ 5325 1875
$Comp
L power:GNDA #PWR?
U 1 1 5D2BBF07
P 5575 2075
F 0 "#PWR?" H 5575 1825 50  0001 C CNN
F 1 "GNDA" H 5580 1902 50  0000 C CNN
F 2 "" H 5575 2075 50  0001 C CNN
F 3 "" H 5575 2075 50  0001 C CNN
	1    5575 2075
	1    0    0    -1  
$EndComp
Wire Wire Line
	5125 2475 5125 2900
Wire Wire Line
	5125 2900 5800 2900
Wire Wire Line
	5800 2900 5800 2375
Wire Wire Line
	5725 2375 5800 2375
Connection ~ 5800 2375
Wire Wire Line
	5800 2375 5875 2375
$Comp
L Device:R_Small R?
U 1 1 5D2C090C
P 5975 2375
F 0 "R?" V 5800 2500 50  0000 C CNN
F 1 "51" V 5875 2500 50  0000 C CNN
F 2 "" H 5975 2375 50  0001 C CNN
F 3 "~" H 5975 2375 50  0001 C CNN
	1    5975 2375
	0    1    1    0   
$EndComp
$Comp
L Device:C_Small C?
U 1 1 5D2C14C6
P 6175 2475
F 0 "C?" H 6267 2521 50  0000 L CNN
F 1 "22pF" H 6267 2430 50  0000 L CNN
F 2 "" H 6175 2475 50  0001 C CNN
F 3 "~" H 6175 2475 50  0001 C CNN
	1    6175 2475
	1    0    0    -1  
$EndComp
Wire Wire Line
	6075 2375 6175 2375
Connection ~ 6175 2375
Wire Wire Line
	6175 2375 6500 2375
$Comp
L power:GNDA #PWR?
U 1 1 5D2C4872
P 6175 2575
F 0 "#PWR?" H 6175 2325 50  0001 C CNN
F 1 "GNDA" H 6180 2402 50  0000 C CNN
F 2 "" H 6175 2575 50  0001 C CNN
F 3 "" H 6175 2575 50  0001 C CNN
	1    6175 2575
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 5D2C5995
P 3925 950
F 0 "#PWR?" H 3925 800 50  0001 C CNN
F 1 "+5V" H 3940 1123 50  0000 C CNN
F 2 "" H 3925 950 50  0001 C CNN
F 3 "" H 3925 950 50  0001 C CNN
	1    3925 950 
	1    0    0    -1  
$EndComp
Wire Wire Line
	3925 950  3925 1175
Wire Wire Line
	3925 1175 3975 1175
Wire Wire Line
	3925 950  3650 950 
Connection ~ 3925 950 
$Comp
L Device:CP_Small C?
U 1 1 5D2CC923
P 3475 1050
F 0 "C?" H 3200 925 50  0000 L CNN
F 1 "22uF" H 3200 1025 50  0000 L CNN
F 2 "" H 3475 1050 50  0001 C CNN
F 3 "~" H 3475 1050 50  0001 C CNN
	1    3475 1050
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR?
U 1 1 5D2CE15C
P 3475 1150
F 0 "#PWR?" H 3475 900 50  0001 C CNN
F 1 "GNDA" H 3450 975 50  0000 C CNN
F 2 "" H 3475 1150 50  0001 C CNN
F 3 "" H 3475 1150 50  0001 C CNN
	1    3475 1150
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C?
U 1 1 5D2CE6F1
P 3650 1050
F 0 "C?" H 3475 1350 50  0000 L CNN
F 1 "0.1uF" H 3475 1250 50  0000 L CNN
F 2 "" H 3650 1050 50  0001 C CNN
F 3 "~" H 3650 1050 50  0001 C CNN
	1    3650 1050
	1    0    0    -1  
$EndComp
Connection ~ 3650 950 
Wire Wire Line
	3650 950  3475 950 
$Comp
L power:GNDA #PWR?
U 1 1 5D2CF851
P 3650 1150
F 0 "#PWR?" H 3650 900 50  0001 C CNN
F 1 "GNDA" H 3655 977 50  0000 C CNN
F 2 "" H 3650 1150 50  0001 C CNN
F 3 "" H 3650 1150 50  0001 C CNN
	1    3650 1150
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 5D2D6313
P 2925 950
F 0 "#PWR?" H 2925 800 50  0001 C CNN
F 1 "+5V" H 2940 1123 50  0000 C CNN
F 2 "" H 2925 950 50  0001 C CNN
F 3 "" H 2925 950 50  0001 C CNN
	1    2925 950 
	1    0    0    -1  
$EndComp
Wire Wire Line
	2925 950  2650 950 
$Comp
L Device:CP_Small C?
U 1 1 5D2D631D
P 2475 1050
F 0 "C?" H 2350 1350 50  0000 L CNN
F 1 "22uF" H 2350 1250 50  0000 L CNN
F 2 "" H 2475 1050 50  0001 C CNN
F 3 "~" H 2475 1050 50  0001 C CNN
	1    2475 1050
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR?
U 1 1 5D2D6323
P 2475 1150
F 0 "#PWR?" H 2475 900 50  0001 C CNN
F 1 "GNDA" H 2450 975 50  0000 C CNN
F 2 "" H 2475 1150 50  0001 C CNN
F 3 "" H 2475 1150 50  0001 C CNN
	1    2475 1150
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C?
U 1 1 5D2D6329
P 2650 1050
F 0 "C?" H 2600 1350 50  0000 L CNN
F 1 "0.1uF" H 2600 1250 50  0000 L CNN
F 2 "" H 2650 1050 50  0001 C CNN
F 3 "~" H 2650 1050 50  0001 C CNN
	1    2650 1050
	1    0    0    -1  
$EndComp
Connection ~ 2650 950 
Wire Wire Line
	2650 950  2475 950 
$Comp
L power:GNDA #PWR?
U 1 1 5D2D6331
P 2650 1150
F 0 "#PWR?" H 2650 900 50  0001 C CNN
F 1 "GNDA" H 2655 977 50  0000 C CNN
F 2 "" H 2650 1150 50  0001 C CNN
F 3 "" H 2650 1150 50  0001 C CNN
	1    2650 1150
	1    0    0    -1  
$EndComp
$Comp
L Device:CP_Small C?
U 1 1 5D2DA6C8
P 5800 1975
F 0 "C?" H 5900 1975 50  0000 L CNN
F 1 "22uF" H 5900 2050 50  0000 L CNN
F 2 "" H 5800 1975 50  0001 C CNN
F 3 "~" H 5800 1975 50  0001 C CNN
	1    5800 1975
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR?
U 1 1 5D2E0360
P 5800 2075
F 0 "#PWR?" H 5800 1825 50  0001 C CNN
F 1 "GNDA" H 5805 1902 50  0000 C CNN
F 2 "" H 5800 2075 50  0001 C CNN
F 3 "" H 5800 2075 50  0001 C CNN
	1    5800 2075
	1    0    0    -1  
$EndComp
Wire Wire Line
	5575 1875 5800 1875
Connection ~ 5575 1875
Wire Wire Line
	5325 2675 5325 2725
Connection ~ 5325 2725
Wire Wire Line
	5325 2725 5325 2800
$Comp
L Device:CP_Small C?
U 1 1 5D2EF06B
P 4700 2825
F 0 "C?" H 4400 2775 50  0000 L CNN
F 1 "22uF" H 4400 2850 50  0000 L CNN
F 2 "" H 4700 2825 50  0001 C CNN
F 3 "~" H 4700 2825 50  0001 C CNN
	1    4700 2825
	1    0    0    -1  
$EndComp
Wire Wire Line
	4700 2725 4875 2725
$Comp
L Device:C_Small C?
U 1 1 5D2F2A7D
P 4875 2825
F 0 "C?" H 4950 2675 50  0000 R CNN
F 1 "0.1uF" H 4950 2575 50  0000 R CNN
F 2 "" H 4875 2825 50  0001 C CNN
F 3 "~" H 4875 2825 50  0001 C CNN
	1    4875 2825
	-1   0    0    1   
$EndComp
Connection ~ 4875 2725
Wire Wire Line
	4875 2725 5325 2725
$Comp
L power:GNDA #PWR?
U 1 1 5D2F36CA
P 4700 2925
F 0 "#PWR?" H 4700 2675 50  0001 C CNN
F 1 "GNDA" H 4675 2750 50  0000 C CNN
F 2 "" H 4700 2925 50  0001 C CNN
F 3 "" H 4700 2925 50  0001 C CNN
	1    4700 2925
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR?
U 1 1 5D2F3AFF
P 4875 2925
F 0 "#PWR?" H 4875 2675 50  0001 C CNN
F 1 "GNDA" H 4880 2752 50  0000 C CNN
F 2 "" H 4875 2925 50  0001 C CNN
F 3 "" H 4875 2925 50  0001 C CNN
	1    4875 2925
	1    0    0    -1  
$EndComp
Text Label 6500 2375 0    50   ~ 0
VID
$Comp
L Device:C_Small C?
U 1 1 5D2FA214
P 5175 1575
F 0 "C?" H 5250 1750 50  0000 L CNN
F 1 "1uF" H 5250 1675 50  0000 L CNN
F 2 "" H 5175 1575 50  0001 C CNN
F 3 "~" H 5175 1575 50  0001 C CNN
	1    5175 1575
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR?
U 1 1 5D2FA21A
P 5175 1675
F 0 "#PWR?" H 5175 1425 50  0001 C CNN
F 1 "GNDA" H 5180 1502 50  0000 C CNN
F 2 "" H 5175 1675 50  0001 C CNN
F 3 "" H 5175 1675 50  0001 C CNN
	1    5175 1675
	1    0    0    -1  
$EndComp
Wire Wire Line
	4875 1475 5175 1475
$Comp
L Device:C_Small C?
U 1 1 5D3098AB
P 3675 1475
F 0 "C?" H 3450 1500 50  0000 L CNN
F 1 "1uF" H 3400 1425 50  0000 L CNN
F 2 "" H 3675 1475 50  0001 C CNN
F 3 "~" H 3675 1475 50  0001 C CNN
	1    3675 1475
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR?
U 1 1 5D3098B1
P 3675 1575
F 0 "#PWR?" H 3675 1325 50  0001 C CNN
F 1 "GNDA" H 3680 1402 50  0000 C CNN
F 2 "" H 3675 1575 50  0001 C CNN
F 3 "" H 3675 1575 50  0001 C CNN
	1    3675 1575
	1    0    0    -1  
$EndComp
Wire Wire Line
	3975 1375 3675 1375
$Comp
L power:GNDA #PWR?
U 1 1 5D320EE7
P 3825 1775
F 0 "#PWR?" H 3825 1525 50  0001 C CNN
F 1 "GNDA" H 3830 1602 50  0000 C CNN
F 2 "" H 3825 1775 50  0001 C CNN
F 3 "" H 3825 1775 50  0001 C CNN
	1    3825 1775
	1    0    0    -1  
$EndComp
Wire Wire Line
	3825 1775 3975 1775
$Comp
L Device:CP_Small C?
U 1 1 5D32E5FF
P 3250 2500
F 0 "C?" H 2950 2450 50  0000 L CNN
F 1 "22uF" H 2950 2525 50  0000 L CNN
F 2 "" H 3250 2500 50  0001 C CNN
F 3 "~" H 3250 2500 50  0001 C CNN
	1    3250 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3250 2400 3425 2400
$Comp
L Device:C_Small C?
U 1 1 5D32E606
P 3425 2500
F 0 "C?" H 3500 2350 50  0000 R CNN
F 1 "0.1uF" H 3500 2250 50  0000 R CNN
F 2 "" H 3425 2500 50  0001 C CNN
F 3 "~" H 3425 2500 50  0001 C CNN
	1    3425 2500
	-1   0    0    1   
$EndComp
$Comp
L power:GNDA #PWR?
U 1 1 5D32E60E
P 3250 2600
F 0 "#PWR?" H 3250 2350 50  0001 C CNN
F 1 "GNDA" H 3225 2425 50  0000 C CNN
F 2 "" H 3250 2600 50  0001 C CNN
F 3 "" H 3250 2600 50  0001 C CNN
	1    3250 2600
	1    0    0    -1  
$EndComp
$Comp
L power:GNDA #PWR?
U 1 1 5D32E614
P 3425 2600
F 0 "#PWR?" H 3425 2350 50  0001 C CNN
F 1 "GNDA" H 3430 2427 50  0000 C CNN
F 2 "" H 3425 2600 50  0001 C CNN
F 3 "" H 3425 2600 50  0001 C CNN
	1    3425 2600
	1    0    0    -1  
$EndComp
Connection ~ 3425 2400
Wire Wire Line
	3425 2400 3650 2400
$Comp
L power:+5V #PWR?
U 1 1 5D358444
P 3650 2275
F 0 "#PWR?" H 3650 2125 50  0001 C CNN
F 1 "+5V" H 3665 2448 50  0000 C CNN
F 2 "" H 3650 2275 50  0001 C CNN
F 3 "" H 3650 2275 50  0001 C CNN
	1    3650 2275
	1    0    0    -1  
$EndComp
Wire Wire Line
	3650 2275 3650 2400
Wire Wire Line
	3650 2400 3975 2400
Wire Wire Line
	3975 1875 3975 2400
Connection ~ 3650 2400
$Comp
L power:GNDA #PWR?
U 1 1 5D3B6E48
P 1600 2850
F 0 "#PWR?" H 1600 2600 50  0001 C CNN
F 1 "GNDA" H 1605 2677 50  0000 C CNN
F 2 "" H 1600 2850 50  0001 C CNN
F 3 "" H 1600 2850 50  0001 C CNN
	1    1600 2850
	1    0    0    -1  
$EndComp
Wire Wire Line
	1675 2725 1600 2725
Wire Wire Line
	1600 2725 1600 2850
Text Label 1150 1925 2    50   ~ 0
CRYSTAL
$Comp
L Connector:Screw_Terminal_01x09 J?
U 1 1 5D3FE5E4
P 6125 6950
F 0 "J?" H 5475 7550 50  0000 L CNN
F 1 "Screw_Terminal_01x09" H 5475 7675 50  0000 L CNN
F 2 "" H 6125 6950 50  0001 C CNN
F 3 "~" H 6125 6950 50  0001 C CNN
	1    6125 6950
	1    0    0    -1  
$EndComp
Text Label 5925 6850 2    50   ~ 0
START_VID
$Comp
L Burt-rescue:S14739-20-Custom U?
U 1 1 5D25536A
P 4425 1525
F 0 "U?" H 4425 2340 50  0000 C CNN
F 1 "S14739-20" H 4425 2249 50  0000 C CNN
F 2 "" H 4425 2305 50  0001 C CNN
F 3 "https://www.hamamatsu.com/resources/pdf/ssd/s14739-20_kmpd1196e.pdf" H 4425 2305 50  0001 C CNN
	1    4425 1525
	1    0    0    -1  
$EndComp
Text Label 1150 2025 2    50   ~ 0
START_VID
$Comp
L Device:R_Small R?
U 1 1 5D28D225
P 2400 7075
F 0 "R?" H 2459 7121 50  0000 L CNN
F 1 "R_Small" H 2459 7030 50  0000 L CNN
F 2 "" H 2400 7075 50  0001 C CNN
F 3 "~" H 2400 7075 50  0001 C CNN
	1    2400 7075
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R?
U 1 1 5D28D9E9
P 2575 6525
F 0 "R?" H 2516 6479 50  0000 R CNN
F 1 "R_Small" H 2516 6570 50  0000 R CNN
F 2 "" H 2575 6525 50  0001 C CNN
F 3 "~" H 2575 6525 50  0001 C CNN
	1    2575 6525
	-1   0    0    1   
$EndComp
Wire Wire Line
	2400 6300 2575 6300
Wire Wire Line
	2575 6300 2575 6425
Wire Wire Line
	2400 6700 2575 6700
Wire Wire Line
	2575 6700 2575 6625
$Comp
L power:GND #PWR?
U 1 1 5D292366
P 2575 6700
F 0 "#PWR?" H 2575 6450 50  0001 C CNN
F 1 "GND" H 2580 6527 50  0000 C CNN
F 2 "" H 2575 6700 50  0001 C CNN
F 3 "" H 2575 6700 50  0001 C CNN
	1    2575 6700
	1    0    0    -1  
$EndComp
Connection ~ 2575 6700
$Comp
L Device:C_Small C?
U 1 1 5D2929F0
P 925 6400
F 0 "C?" H 725 6425 50  0000 L CNN
F 1 "4.7uF" H 600 6325 50  0000 L CNN
F 2 "" H 925 6400 50  0001 C CNN
F 3 "~" H 925 6400 50  0001 C CNN
	1    925  6400
	1    0    0    -1  
$EndComp
$Comp
L Device:D D?
U 1 1 5D29968B
P 1150 6450
F 0 "D?" V 1196 6371 50  0000 R CNN
F 1 "D" V 1105 6371 50  0000 R CNN
F 2 "" H 1150 6450 50  0001 C CNN
F 3 "~" H 1150 6450 50  0001 C CNN
	1    1150 6450
	0    -1   -1   0   
$EndComp
Wire Wire Line
	800  6300 925  6300
Connection ~ 925  6300
Wire Wire Line
	925  6300 1150 6300
Connection ~ 1150 6300
Wire Wire Line
	1150 6300 1425 6300
Wire Wire Line
	1425 6300 1425 6500
Wire Wire Line
	1425 6500 1600 6500
Connection ~ 1425 6300
Wire Wire Line
	1425 6300 1600 6300
Wire Wire Line
	2400 6900 2400 6975
Wire Wire Line
	1150 6600 1150 7350
Wire Wire Line
	1150 7350 2400 7350
Wire Wire Line
	2400 7350 2400 7175
$Comp
L power:GND #PWR?
U 1 1 5D2BE8A0
P 925 6500
F 0 "#PWR?" H 925 6250 50  0001 C CNN
F 1 "GND" H 930 6327 50  0000 C CNN
F 2 "" H 925 6500 50  0001 C CNN
F 3 "" H 925 6500 50  0001 C CNN
	1    925  6500
	1    0    0    -1  
$EndComp
Wire Notes Line
	625  3250 6750 3250
Text Label 5925 6950 2    50   ~ 0
B1
Text Label 5925 7050 2    50   ~ 0
B2
Text Label 5925 7350 2    50   ~ 0
B5
Text Label 5925 7250 2    50   ~ 0
B4
Text Label 5925 7150 2    50   ~ 0
B3
$Comp
L Device:Q_NMOS_DGS Q?
U 1 1 5D4126D2
P 10025 1025
F 0 "Q?" V 10750 950 50  0000 L CNN
F 1 "Q_NMOS_DGS" V 10825 950 50  0000 L CNN
F 2 "" H 10225 1125 50  0001 C CNN
F 3 "~" H 10025 1025 50  0001 C CNN
	1    10025 1025
	-1   0    0    1   
$EndComp
$Comp
L Device:R R?
U 1 1 5D4126D8
P 10375 1025
F 0 "R?" V 10168 1025 50  0000 C CNN
F 1 "BURNWIRE" V 10259 1025 50  0000 C CNN
F 2 "" V 10305 1025 50  0001 C CNN
F 3 "~" H 10375 1025 50  0001 C CNN
	1    10375 1025
	0    1    1    0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D4126E4
P 9450 825
F 0 "#PWR?" H 9450 675 50  0001 C CNN
F 1 "+BATT" H 9465 998 50  0000 C CNN
F 2 "" H 9450 825 50  0001 C CNN
F 3 "" H 9450 825 50  0001 C CNN
	1    9450 825 
	1    0    0    -1  
$EndComp
Wire Wire Line
	10525 1025 10800 1025
Wire Wire Line
	10800 1025 10800 975 
$Comp
L power:GND #PWR?
U 1 1 5D4126EC
P 9925 1275
F 0 "#PWR?" H 9925 1025 50  0001 C CNN
F 1 "GND" H 9930 1102 50  0000 C CNN
F 2 "" H 9925 1275 50  0001 C CNN
F 3 "" H 9925 1275 50  0001 C CNN
	1    9925 1275
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D4126F2
P 9600 975
F 0 "R?" H 9670 1021 50  0000 L CNN
F 1 "10k" H 9670 930 50  0000 L CNN
F 2 "" V 9530 975 50  0001 C CNN
F 3 "~" H 9600 975 50  0001 C CNN
	1    9600 975 
	1    0    0    -1  
$EndComp
Wire Wire Line
	9600 825  9925 825 
Wire Wire Line
	9600 825  9450 825 
Connection ~ 9600 825 
Wire Wire Line
	9600 1250 9925 1250
Wire Wire Line
	9600 1125 9600 1250
Wire Wire Line
	9925 1225 9925 1250
Connection ~ 9925 1250
Wire Wire Line
	9925 1250 9925 1275
Text Label 10800 975  0    50   ~ 0
BL1
$Comp
L Device:Q_NMOS_DGS Q?
U 1 1 5D44740D
P 10025 1825
F 0 "Q?" V 10750 1750 50  0000 L CNN
F 1 "Q_NMOS_DGS" V 10825 1750 50  0000 L CNN
F 2 "" H 10225 1925 50  0001 C CNN
F 3 "~" H 10025 1825 50  0001 C CNN
	1    10025 1825
	-1   0    0    1   
$EndComp
$Comp
L Device:R R?
U 1 1 5D447413
P 10375 1825
F 0 "R?" V 10168 1825 50  0000 C CNN
F 1 "BURNWIRE" V 10259 1825 50  0000 C CNN
F 2 "" V 10305 1825 50  0001 C CNN
F 3 "~" H 10375 1825 50  0001 C CNN
	1    10375 1825
	0    1    1    0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D447419
P 9450 1625
F 0 "#PWR?" H 9450 1475 50  0001 C CNN
F 1 "+BATT" H 9465 1798 50  0000 C CNN
F 2 "" H 9450 1625 50  0001 C CNN
F 3 "" H 9450 1625 50  0001 C CNN
	1    9450 1625
	1    0    0    -1  
$EndComp
Wire Wire Line
	10525 1825 10800 1825
Wire Wire Line
	10800 1825 10800 1775
$Comp
L power:GND #PWR?
U 1 1 5D447421
P 9925 2075
F 0 "#PWR?" H 9925 1825 50  0001 C CNN
F 1 "GND" H 9930 1902 50  0000 C CNN
F 2 "" H 9925 2075 50  0001 C CNN
F 3 "" H 9925 2075 50  0001 C CNN
	1    9925 2075
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D447427
P 9600 1775
F 0 "R?" H 9670 1821 50  0000 L CNN
F 1 "10k" H 9670 1730 50  0000 L CNN
F 2 "" V 9530 1775 50  0001 C CNN
F 3 "~" H 9600 1775 50  0001 C CNN
	1    9600 1775
	1    0    0    -1  
$EndComp
Wire Wire Line
	9600 1625 9925 1625
Wire Wire Line
	9600 1625 9450 1625
Connection ~ 9600 1625
Wire Wire Line
	9600 2050 9925 2050
Wire Wire Line
	9600 1925 9600 2050
Wire Wire Line
	9925 2025 9925 2050
Connection ~ 9925 2050
Wire Wire Line
	9925 2050 9925 2075
Text Label 10800 1775 0    50   ~ 0
BL2
$Comp
L Device:Q_NMOS_DGS Q?
U 1 1 5D44AF9C
P 10050 2675
F 0 "Q?" V 10775 2600 50  0000 L CNN
F 1 "Q_NMOS_DGS" V 10850 2600 50  0000 L CNN
F 2 "" H 10250 2775 50  0001 C CNN
F 3 "~" H 10050 2675 50  0001 C CNN
	1    10050 2675
	-1   0    0    1   
$EndComp
$Comp
L Device:R R?
U 1 1 5D44AFA2
P 10400 2675
F 0 "R?" V 10193 2675 50  0000 C CNN
F 1 "BURNWIRE" V 10284 2675 50  0000 C CNN
F 2 "" V 10330 2675 50  0001 C CNN
F 3 "~" H 10400 2675 50  0001 C CNN
	1    10400 2675
	0    1    1    0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D44AFA8
P 9475 2475
F 0 "#PWR?" H 9475 2325 50  0001 C CNN
F 1 "+BATT" H 9490 2648 50  0000 C CNN
F 2 "" H 9475 2475 50  0001 C CNN
F 3 "" H 9475 2475 50  0001 C CNN
	1    9475 2475
	1    0    0    -1  
$EndComp
Wire Wire Line
	10550 2675 10825 2675
Wire Wire Line
	10825 2675 10825 2625
$Comp
L power:GND #PWR?
U 1 1 5D44AFB0
P 9950 2925
F 0 "#PWR?" H 9950 2675 50  0001 C CNN
F 1 "GND" H 9955 2752 50  0000 C CNN
F 2 "" H 9950 2925 50  0001 C CNN
F 3 "" H 9950 2925 50  0001 C CNN
	1    9950 2925
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D44AFB6
P 9625 2625
F 0 "R?" H 9695 2671 50  0000 L CNN
F 1 "10k" H 9695 2580 50  0000 L CNN
F 2 "" V 9555 2625 50  0001 C CNN
F 3 "~" H 9625 2625 50  0001 C CNN
	1    9625 2625
	1    0    0    -1  
$EndComp
Wire Wire Line
	9625 2475 9950 2475
Wire Wire Line
	9625 2475 9475 2475
Connection ~ 9625 2475
Wire Wire Line
	9625 2900 9950 2900
Wire Wire Line
	9625 2775 9625 2900
Wire Wire Line
	9950 2875 9950 2900
Connection ~ 9950 2900
Wire Wire Line
	9950 2900 9950 2925
Text Label 10825 2625 0    50   ~ 0
BL3
$Comp
L Device:Q_NMOS_DGS Q?
U 1 1 5D44F9EB
P 10100 3525
F 0 "Q?" V 10825 3450 50  0000 L CNN
F 1 "Q_NMOS_DGS" V 10900 3450 50  0000 L CNN
F 2 "" H 10300 3625 50  0001 C CNN
F 3 "~" H 10100 3525 50  0001 C CNN
	1    10100 3525
	-1   0    0    1   
$EndComp
$Comp
L Device:R R?
U 1 1 5D44F9F1
P 10450 3525
F 0 "R?" V 10243 3525 50  0000 C CNN
F 1 "BURNWIRE" V 10334 3525 50  0000 C CNN
F 2 "" V 10380 3525 50  0001 C CNN
F 3 "~" H 10450 3525 50  0001 C CNN
	1    10450 3525
	0    1    1    0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D44F9F7
P 9525 3325
F 0 "#PWR?" H 9525 3175 50  0001 C CNN
F 1 "+BATT" H 9540 3498 50  0000 C CNN
F 2 "" H 9525 3325 50  0001 C CNN
F 3 "" H 9525 3325 50  0001 C CNN
	1    9525 3325
	1    0    0    -1  
$EndComp
Wire Wire Line
	10600 3525 10875 3525
Wire Wire Line
	10875 3525 10875 3475
$Comp
L power:GND #PWR?
U 1 1 5D44F9FF
P 10000 3775
F 0 "#PWR?" H 10000 3525 50  0001 C CNN
F 1 "GND" H 10005 3602 50  0000 C CNN
F 2 "" H 10000 3775 50  0001 C CNN
F 3 "" H 10000 3775 50  0001 C CNN
	1    10000 3775
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D44FA05
P 9675 3475
F 0 "R?" H 9745 3521 50  0000 L CNN
F 1 "10k" H 9745 3430 50  0000 L CNN
F 2 "" V 9605 3475 50  0001 C CNN
F 3 "~" H 9675 3475 50  0001 C CNN
	1    9675 3475
	1    0    0    -1  
$EndComp
Wire Wire Line
	9675 3325 10000 3325
Wire Wire Line
	9675 3325 9525 3325
Connection ~ 9675 3325
Wire Wire Line
	9675 3750 10000 3750
Wire Wire Line
	9675 3625 9675 3750
Wire Wire Line
	10000 3725 10000 3750
Connection ~ 10000 3750
Wire Wire Line
	10000 3750 10000 3775
Text Label 10875 3475 0    50   ~ 0
BL4
$Comp
L Device:Q_NMOS_DGS Q?
U 1 1 5D455BC0
P 7875 1025
F 0 "Q?" V 8600 950 50  0000 L CNN
F 1 "Q_NMOS_DGS" V 8675 950 50  0000 L CNN
F 2 "" H 8075 1125 50  0001 C CNN
F 3 "~" H 7875 1025 50  0001 C CNN
	1    7875 1025
	-1   0    0    1   
$EndComp
$Comp
L Device:R R?
U 1 1 5D455BC6
P 8225 1025
F 0 "R?" V 8018 1025 50  0000 C CNN
F 1 "BURNWIRE" V 8109 1025 50  0000 C CNN
F 2 "" V 8155 1025 50  0001 C CNN
F 3 "~" H 8225 1025 50  0001 C CNN
	1    8225 1025
	0    1    1    0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D455BCC
P 7300 825
F 0 "#PWR?" H 7300 675 50  0001 C CNN
F 1 "+BATT" H 7315 998 50  0000 C CNN
F 2 "" H 7300 825 50  0001 C CNN
F 3 "" H 7300 825 50  0001 C CNN
	1    7300 825 
	1    0    0    -1  
$EndComp
Wire Wire Line
	8375 1025 8650 1025
Wire Wire Line
	8650 1025 8650 975 
$Comp
L power:GND #PWR?
U 1 1 5D455BD4
P 7775 1275
F 0 "#PWR?" H 7775 1025 50  0001 C CNN
F 1 "GND" H 7780 1102 50  0000 C CNN
F 2 "" H 7775 1275 50  0001 C CNN
F 3 "" H 7775 1275 50  0001 C CNN
	1    7775 1275
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D455BDA
P 7450 975
F 0 "R?" H 7520 1021 50  0000 L CNN
F 1 "10k" H 7520 930 50  0000 L CNN
F 2 "" V 7380 975 50  0001 C CNN
F 3 "~" H 7450 975 50  0001 C CNN
	1    7450 975 
	1    0    0    -1  
$EndComp
Wire Wire Line
	7450 825  7775 825 
Wire Wire Line
	7450 825  7300 825 
Connection ~ 7450 825 
Wire Wire Line
	7450 1250 7775 1250
Wire Wire Line
	7450 1125 7450 1250
Wire Wire Line
	7775 1225 7775 1250
Connection ~ 7775 1250
Wire Wire Line
	7775 1250 7775 1275
Text Label 8650 975  0    50   ~ 0
BL5
$Comp
L power:+BATT #PWR?
U 1 1 5D46466E
P 1300 6800
F 0 "#PWR?" H 1300 6650 50  0001 C CNN
F 1 "+BATT" H 1315 6973 50  0000 C CNN
F 2 "" H 1300 6800 50  0001 C CNN
F 3 "" H 1300 6800 50  0001 C CNN
	1    1300 6800
	1    0    0    -1  
$EndComp
Wire Wire Line
	1600 6700 1600 6800
Wire Wire Line
	1600 6800 1300 6800
Wire Wire Line
	1600 6900 1600 6800
Connection ~ 1600 6800
$Comp
L Burt-rescue:A3908-Custom U?
U 1 1 5D5325EF
P 4450 6650
F 0 "U?" H 4450 7065 50  0000 C CNN
F 1 "A3908" H 4450 6974 50  0000 C CNN
F 2 "" H 4000 6500 50  0001 C CNN
F 3 "" H 4000 6500 50  0001 C CNN
	1    4450 6650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R?
U 1 1 5D538E55
P 5025 6800
F 0 "R?" H 5084 6846 50  0000 L CNN
F 1 "18k" H 5084 6755 50  0000 L CNN
F 2 "" H 5025 6800 50  0001 C CNN
F 3 "~" H 5025 6800 50  0001 C CNN
	1    5025 6800
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R?
U 1 1 5D543F60
P 5025 7100
F 0 "R?" H 4875 7075 50  0000 L CNN
F 1 "10k" H 4825 7000 50  0000 L CNN
F 2 "" H 5025 7100 50  0001 C CNN
F 3 "~" H 5025 7100 50  0001 C CNN
	1    5025 7100
	1    0    0    -1  
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D545C7D
P 3700 6500
F 0 "#PWR?" H 3700 6350 50  0001 C CNN
F 1 "+BATT" H 3715 6673 50  0000 C CNN
F 2 "" H 3700 6500 50  0001 C CNN
F 3 "" H 3700 6500 50  0001 C CNN
	1    3700 6500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3700 6500 4100 6500
Wire Wire Line
	4800 6700 5025 6700
Wire Wire Line
	5025 6900 5025 6950
Wire Wire Line
	4800 6800 4800 6950
Wire Wire Line
	4800 6950 5025 6950
Connection ~ 5025 6950
Wire Wire Line
	5025 6950 5025 7000
$Comp
L power:GNDA #PWR?
U 1 1 5D559B0F
P 4475 7300
F 0 "#PWR?" H 4475 7050 50  0001 C CNN
F 1 "GNDA" H 4480 7127 50  0000 C CNN
F 2 "" H 4475 7300 50  0001 C CNN
F 3 "" H 4475 7300 50  0001 C CNN
	1    4475 7300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5025 7200 5025 7300
Wire Wire Line
	5025 7300 4475 7300
Wire Wire Line
	4100 6800 4100 7300
Wire Wire Line
	4100 7300 4475 7300
Connection ~ 4475 7300
$Comp
L Motor:Motor_DC M?
U 1 1 5D49D045
P 3675 6900
F 0 "M?" V 3350 6925 50  0000 L CNN
F 1 "Motor_DC" V 3450 6675 50  0000 L CNN
F 2 "" H 3675 6810 50  0001 C CNN
F 3 "~" H 3675 6810 50  0001 C CNN
	1    3675 6900
	1    0    0    -1  
$EndComp
Text Label 5025 6500 0    50   ~ 0
IN1
Text Label 5025 6600 0    50   ~ 0
IN2
Wire Wire Line
	4800 6500 5025 6500
Wire Wire Line
	4800 6600 5025 6600
Wire Wire Line
	4100 6600 3675 6600
Wire Wire Line
	3675 6600 3675 6700
Wire Wire Line
	4100 6700 3900 6700
Wire Wire Line
	3900 6700 3900 7200
Wire Wire Line
	3900 7200 3675 7200
Wire Notes Line
	625  3250 625  550 
Wire Notes Line
	625  550  6750 550 
Wire Notes Line
	6750 550  6750 3250
$Comp
L Device:Q_NMOS_DGS Q?
U 1 1 5D78BB8F
P 7900 1825
F 0 "Q?" V 8625 1750 50  0000 L CNN
F 1 "Q_NMOS_DGS" V 8700 1750 50  0000 L CNN
F 2 "" H 8100 1925 50  0001 C CNN
F 3 "~" H 7900 1825 50  0001 C CNN
	1    7900 1825
	-1   0    0    1   
$EndComp
$Comp
L Device:R R?
U 1 1 5D78BB95
P 8250 1825
F 0 "R?" V 8043 1825 50  0000 C CNN
F 1 "BURNWIRE" V 8134 1825 50  0000 C CNN
F 2 "" V 8180 1825 50  0001 C CNN
F 3 "~" H 8250 1825 50  0001 C CNN
	1    8250 1825
	0    1    1    0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D78BB9B
P 7325 1625
F 0 "#PWR?" H 7325 1475 50  0001 C CNN
F 1 "+BATT" H 7340 1798 50  0000 C CNN
F 2 "" H 7325 1625 50  0001 C CNN
F 3 "" H 7325 1625 50  0001 C CNN
	1    7325 1625
	1    0    0    -1  
$EndComp
Wire Wire Line
	8400 1825 8675 1825
Wire Wire Line
	8675 1825 8675 1775
$Comp
L power:GND #PWR?
U 1 1 5D78BBA3
P 7800 2075
F 0 "#PWR?" H 7800 1825 50  0001 C CNN
F 1 "GND" H 7805 1902 50  0000 C CNN
F 2 "" H 7800 2075 50  0001 C CNN
F 3 "" H 7800 2075 50  0001 C CNN
	1    7800 2075
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D78BBA9
P 7475 1775
F 0 "R?" H 7545 1821 50  0000 L CNN
F 1 "10k" H 7545 1730 50  0000 L CNN
F 2 "" V 7405 1775 50  0001 C CNN
F 3 "~" H 7475 1775 50  0001 C CNN
	1    7475 1775
	1    0    0    -1  
$EndComp
Wire Wire Line
	7475 1625 7800 1625
Wire Wire Line
	7475 1625 7325 1625
Connection ~ 7475 1625
Wire Wire Line
	7475 2050 7800 2050
Wire Wire Line
	7475 1925 7475 2050
Wire Wire Line
	7800 2025 7800 2050
Connection ~ 7800 2050
Wire Wire Line
	7800 2050 7800 2075
Text Label 8675 1775 0    50   ~ 0
BL6
$Comp
L Device:Q_NMOS_DGS Q?
U 1 1 5D78BBB8
P 7950 2675
F 0 "Q?" V 8675 2600 50  0000 L CNN
F 1 "Q_NMOS_DGS" V 8750 2600 50  0000 L CNN
F 2 "" H 8150 2775 50  0001 C CNN
F 3 "~" H 7950 2675 50  0001 C CNN
	1    7950 2675
	-1   0    0    1   
$EndComp
$Comp
L Device:R R?
U 1 1 5D78BBBE
P 8300 2675
F 0 "R?" V 8093 2675 50  0000 C CNN
F 1 "BURNWIRE" V 8184 2675 50  0000 C CNN
F 2 "" V 8230 2675 50  0001 C CNN
F 3 "~" H 8300 2675 50  0001 C CNN
	1    8300 2675
	0    1    1    0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D78BBC4
P 7375 2475
F 0 "#PWR?" H 7375 2325 50  0001 C CNN
F 1 "+BATT" H 7390 2648 50  0000 C CNN
F 2 "" H 7375 2475 50  0001 C CNN
F 3 "" H 7375 2475 50  0001 C CNN
	1    7375 2475
	1    0    0    -1  
$EndComp
Wire Wire Line
	8450 2675 8725 2675
Wire Wire Line
	8725 2675 8725 2625
$Comp
L power:GND #PWR?
U 1 1 5D78BBCC
P 7850 2925
F 0 "#PWR?" H 7850 2675 50  0001 C CNN
F 1 "GND" H 7855 2752 50  0000 C CNN
F 2 "" H 7850 2925 50  0001 C CNN
F 3 "" H 7850 2925 50  0001 C CNN
	1    7850 2925
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D78BBD2
P 7525 2625
F 0 "R?" H 7595 2671 50  0000 L CNN
F 1 "10k" H 7595 2580 50  0000 L CNN
F 2 "" V 7455 2625 50  0001 C CNN
F 3 "~" H 7525 2625 50  0001 C CNN
	1    7525 2625
	1    0    0    -1  
$EndComp
Wire Wire Line
	7525 2475 7850 2475
Wire Wire Line
	7525 2475 7375 2475
Connection ~ 7525 2475
Wire Wire Line
	7525 2900 7850 2900
Wire Wire Line
	7525 2775 7525 2900
Wire Wire Line
	7850 2875 7850 2900
Connection ~ 7850 2900
Wire Wire Line
	7850 2900 7850 2925
Text Label 8725 2625 0    50   ~ 0
BL7
$Comp
L Device:Q_NMOS_DGS Q?
U 1 1 5D78BBE1
P 7975 3500
F 0 "Q?" V 8700 3425 50  0000 L CNN
F 1 "Q_NMOS_DGS" V 8775 3425 50  0000 L CNN
F 2 "" H 8175 3600 50  0001 C CNN
F 3 "~" H 7975 3500 50  0001 C CNN
	1    7975 3500
	-1   0    0    1   
$EndComp
$Comp
L Device:R R?
U 1 1 5D78BBE7
P 8325 3500
F 0 "R?" V 8118 3500 50  0000 C CNN
F 1 "BURNWIRE" V 8209 3500 50  0000 C CNN
F 2 "" V 8255 3500 50  0001 C CNN
F 3 "~" H 8325 3500 50  0001 C CNN
	1    8325 3500
	0    1    1    0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D78BBED
P 7400 3300
F 0 "#PWR?" H 7400 3150 50  0001 C CNN
F 1 "+BATT" H 7415 3473 50  0000 C CNN
F 2 "" H 7400 3300 50  0001 C CNN
F 3 "" H 7400 3300 50  0001 C CNN
	1    7400 3300
	1    0    0    -1  
$EndComp
Wire Wire Line
	8475 3500 8750 3500
Wire Wire Line
	8750 3500 8750 3450
$Comp
L power:GND #PWR?
U 1 1 5D78BBF5
P 7875 3750
F 0 "#PWR?" H 7875 3500 50  0001 C CNN
F 1 "GND" H 7880 3577 50  0000 C CNN
F 2 "" H 7875 3750 50  0001 C CNN
F 3 "" H 7875 3750 50  0001 C CNN
	1    7875 3750
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D78BBFB
P 7550 3450
F 0 "R?" H 7620 3496 50  0000 L CNN
F 1 "10k" H 7620 3405 50  0000 L CNN
F 2 "" V 7480 3450 50  0001 C CNN
F 3 "~" H 7550 3450 50  0001 C CNN
	1    7550 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	7550 3300 7875 3300
Wire Wire Line
	7550 3300 7400 3300
Connection ~ 7550 3300
Wire Wire Line
	7550 3725 7875 3725
Wire Wire Line
	7550 3600 7550 3725
Wire Wire Line
	7875 3700 7875 3725
Connection ~ 7875 3725
Wire Wire Line
	7875 3725 7875 3750
Text Label 8750 3450 0    50   ~ 0
BL8
Wire Notes Line
	11150 550  11150 4075
Wire Notes Line
	11150 4075 6825 4075
Wire Notes Line
	6825 4075 6825 550 
Wire Notes Line
	6825 550  11150 550 
$Comp
L Device:Q_NMOS_DGS Q?
U 1 1 5D81B0DC
P 10075 4875
F 0 "Q?" V 10800 4800 50  0000 L CNN
F 1 "Q_NMOS_DGS" V 10875 4800 50  0000 L CNN
F 2 "" H 10275 4975 50  0001 C CNN
F 3 "~" H 10075 4875 50  0001 C CNN
	1    10075 4875
	-1   0    0    1   
$EndComp
$Comp
L Device:R R?
U 1 1 5D81B0E2
P 10425 4875
F 0 "R?" V 10218 4875 50  0000 C CNN
F 1 "BURNWIRE" V 10309 4875 50  0000 C CNN
F 2 "" V 10355 4875 50  0001 C CNN
F 3 "~" H 10425 4875 50  0001 C CNN
	1    10425 4875
	0    1    1    0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D81B0E8
P 9500 4675
F 0 "#PWR?" H 9500 4525 50  0001 C CNN
F 1 "+BATT" H 9515 4848 50  0000 C CNN
F 2 "" H 9500 4675 50  0001 C CNN
F 3 "" H 9500 4675 50  0001 C CNN
	1    9500 4675
	1    0    0    -1  
$EndComp
Wire Wire Line
	10575 4875 10850 4875
Wire Wire Line
	10850 4875 10850 4825
$Comp
L power:GND #PWR?
U 1 1 5D81B0F0
P 9975 5125
F 0 "#PWR?" H 9975 4875 50  0001 C CNN
F 1 "GND" H 9980 4952 50  0000 C CNN
F 2 "" H 9975 5125 50  0001 C CNN
F 3 "" H 9975 5125 50  0001 C CNN
	1    9975 5125
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D81B0F6
P 9650 4825
F 0 "R?" H 9720 4871 50  0000 L CNN
F 1 "10k" H 9720 4780 50  0000 L CNN
F 2 "" V 9580 4825 50  0001 C CNN
F 3 "~" H 9650 4825 50  0001 C CNN
	1    9650 4825
	1    0    0    -1  
$EndComp
Wire Wire Line
	9650 4675 9975 4675
Wire Wire Line
	9650 4675 9500 4675
Connection ~ 9650 4675
Wire Wire Line
	9650 5100 9975 5100
Wire Wire Line
	9650 4975 9650 5100
Wire Wire Line
	9975 5075 9975 5100
Connection ~ 9975 5100
Wire Wire Line
	9975 5100 9975 5125
Text Label 10850 4825 0    50   ~ 0
BP2
$Comp
L Device:Q_NMOS_DGS Q?
U 1 1 5D81B105
P 7950 4850
F 0 "Q?" V 8675 4775 50  0000 L CNN
F 1 "Q_NMOS_DGS" V 8750 4775 50  0000 L CNN
F 2 "" H 8150 4950 50  0001 C CNN
F 3 "~" H 7950 4850 50  0001 C CNN
	1    7950 4850
	-1   0    0    1   
$EndComp
$Comp
L Device:R R?
U 1 1 5D81B10B
P 8300 4850
F 0 "R?" V 8093 4850 50  0000 C CNN
F 1 "BURNWIRE" V 8184 4850 50  0000 C CNN
F 2 "" V 8230 4850 50  0001 C CNN
F 3 "~" H 8300 4850 50  0001 C CNN
	1    8300 4850
	0    1    1    0   
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 5D81B111
P 7375 4650
F 0 "#PWR?" H 7375 4500 50  0001 C CNN
F 1 "+BATT" H 7390 4823 50  0000 C CNN
F 2 "" H 7375 4650 50  0001 C CNN
F 3 "" H 7375 4650 50  0001 C CNN
	1    7375 4650
	1    0    0    -1  
$EndComp
Wire Wire Line
	8450 4850 8725 4850
Wire Wire Line
	8725 4850 8725 4800
$Comp
L power:GND #PWR?
U 1 1 5D81B119
P 7850 5100
F 0 "#PWR?" H 7850 4850 50  0001 C CNN
F 1 "GND" H 7855 4927 50  0000 C CNN
F 2 "" H 7850 5100 50  0001 C CNN
F 3 "" H 7850 5100 50  0001 C CNN
	1    7850 5100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5D81B11F
P 7525 4800
F 0 "R?" H 7595 4846 50  0000 L CNN
F 1 "10k" H 7595 4755 50  0000 L CNN
F 2 "" V 7455 4800 50  0001 C CNN
F 3 "~" H 7525 4800 50  0001 C CNN
	1    7525 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	7525 4650 7850 4650
Wire Wire Line
	7525 4650 7375 4650
Connection ~ 7525 4650
Wire Wire Line
	7525 5075 7850 5075
Wire Wire Line
	7525 4950 7525 5075
Wire Wire Line
	7850 5050 7850 5075
Connection ~ 7850 5075
Wire Wire Line
	7850 5075 7850 5100
Text Label 8725 4800 0    50   ~ 0
BP1
Wire Notes Line
	6825 4150 6825 5525
Wire Notes Line
	6825 5525 11150 5525
Wire Notes Line
	11150 5525 11150 4175
Wire Notes Line
	11150 4175 6825 4175
$Comp
L power:+5V #PWR?
U 1 1 5D287139
P 800 6300
F 0 "#PWR?" H 800 6150 50  0001 C CNN
F 1 "+5V" H 815 6473 50  0000 C CNN
F 2 "" H 800 6300 50  0001 C CNN
F 3 "" H 800 6300 50  0001 C CNN
	1    800  6300
	1    0    0    -1  
$EndComp
$Comp
L Burt-rescue:MCP73831-DFN-Custom U?
U 1 1 5D264C9F
P 2000 6600
F 0 "U?" H 2000 7215 50  0000 C CNN
F 1 "MCP73831-DFN" H 2000 7124 50  0000 C CNN
F 2 "" H 2000 6600 50  0001 C CNN
F 3 "" H 2000 6600 50  0001 C CNN
	1    2000 6600
	1    0    0    -1  
$EndComp
$Comp
L Burt-rescue:MCP9701A-Custom U?
U 1 1 5D425D1D
P 4775 4175
F 0 "U?" H 4750 3600 50  0000 L CNN
F 1 "MCP9701A" H 4900 3600 50  0000 L CNN
F 2 "" H 4500 4325 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/20001942G.pdf" H 4500 4325 50  0001 C CNN
	1    4775 4175
	-1   0    0    1   
$EndComp
Text Label 4575 3875 2    50   ~ 0
TEMP
$Comp
L power:GND #PWR?
U 1 1 5D2E4603
P 4775 4525
F 0 "#PWR?" H 4775 4275 50  0001 C CNN
F 1 "GND" H 4780 4352 50  0000 C CNN
F 2 "" H 4775 4525 50  0001 C CNN
F 3 "" H 4775 4525 50  0001 C CNN
	1    4775 4525
	1    0    0    -1  
$EndComp
Text Notes 4250 3525 0    50   ~ 0
Temperature Sensor
Wire Notes Line
	6750 3325 5475 3325
Wire Notes Line
	5475 3325 5475 4825
Wire Notes Line
	5400 3325 4175 3325
Wire Notes Line
	4175 3325 4175 4825
Wire Notes Line
	4175 4825 5400 4825
Wire Notes Line
	5400 4825 5400 3325
Wire Wire Line
	2325 1825 2325 950 
Wire Wire Line
	2325 950  2475 950 
Connection ~ 2475 950 
Wire Notes Line
	6750 3325 6750 4825
Wire Notes Line
	6750 4825 5475 4825
$EndSCHEMATC
