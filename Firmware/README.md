## Firmware

The firmware used for driving the RepRap board is [Marlin](http://marlinfw.org/).

### Marlin 1.1.1

#### Configuration.h changes

- Endstop Settings

|original value                                |value                                      |
|----------------------------------------------|-------------------------------------------|
|//#define ENDSTOPPULLUP_XMAX                  |#define ENDSTOPPULLUP_XMAX                 |
|//#define ENDSTOPPULLUP_YMAX                  |#define ENDSTOPPULLUP_YMAX                 |
|//#define ENDSTOPPULLUP_ZMAX                  |#define ENDSTOPPULLUP_ZMAX                 |
|//#define ENDSTOPPULLUP_XMIN                  |#define ENDSTOPPULLUP_XMIN                 | 
|//#define ENDSTOPPULLUP_YMIN                  |#define ENDSTOPPULLUP_YMIN                 |
|//#define ENDSTOPPULLUP_ZMIN                  |#define ENDSTOPPULLUP_ZMIN                 |
|//#define ENDSTOPPULLUP_ZMIN_PROBE            |#define ENDSTOPPULLUP_ZMIN_PROBE           |
|#define Y_MIN_ENDSTOP_INVERTING false         |#define Y_MIN_ENDSTOP_INVERTING true       |
|#define X_MAX_ENDSTOP_INVERTING false         |#define X_MAX_ENDSTOP_INVERTING true       |
|#define Y_MAX_ENDSTOP_INVERTING false         |#define Y_MAX_ENDSTOP_INVERTING true       |
|#define Z_MIN_PROBE_ENDSTOP_INVERTING false   |#define Z_MIN_PROBE_ENDSTOP_INVERTING true |

- Movement Settings

|original value                                              |value                                                         |
|------------------------------------------------------------|--------------------------------------------------------------| 
|#define DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 4000, 500 } |#define DEFAULT_AXIS_STEPS_PER_UNIT  { 3.3333, 13.9, 8, 500 } | 
|#define DEFAULT_MAX_FEEDRATE          { 300, 300, 5, 25 }   |#define DEFAULT_MAX_FEEDRATE          { 300, 300, 300, 25 }   |

- Axis settings

|original value                                              |value                               |
|------------------------------------------------------------|------------------------------------|
|#define INVERT_Z_DIR false                                  |#define INVERT_Z_DIR true           |
|#define X_MAX_POS 1400                                      |#define X_MAX_POS 1280              |
|#define Y_MAX_POS 2000                                      |#define Y_MAX_POS 3000              |
|#define Z_MAX_POS 200                                       |#define Z_MAX_POS 4                 |

- Homing settings

|original value                                              |value                               |
|------------------------------------------------------------|------------------------------------|
|#define HOMING_FEEDRATE_XY (50*60)                          |#define HOMING_FEEDRATE_XY (100*60) |

#### Configuration_adv.h changes

|original value            |value                               |
|--------------------------|------------------------------------|
|#define X_HOME_BUMP_MM 5  |#define X_HOME_BUMP_MM 10           |


### how to install 

- download the firmware 1.1.1 on the marlin github repository [firmware](https://github.com/MarlinFirmware/Marlin/releases)
- copy over the modified Configuration.h and Configuration_avd.h files
- flash the firmware using the Arduino IDE

### Marlin 1.1.9

#### Configuration.h changes

- Endstop Settings

|original value                                |value                                      |
|----------------------------------------------|-------------------------------------------|
|//#define ENDSTOPPULLUP_XMAX                  |#define ENDSTOPPULLUP_XMAX                 |
|//#define ENDSTOPPULLUP_YMAX                  |#define ENDSTOPPULLUP_YMAX                 |
|//#define ENDSTOPPULLUP_ZMAX                  |#define ENDSTOPPULLUP_ZMAX                 |
|//#define ENDSTOPPULLUP_XMIN                  |#define ENDSTOPPULLUP_XMIN                 | 
|//#define ENDSTOPPULLUP_YMIN                  |#define ENDSTOPPULLUP_YMIN                 |
|//#define ENDSTOPPULLUP_ZMIN                  |#define ENDSTOPPULLUP_ZMIN                 |
|//#define ENDSTOPPULLUP_ZMIN_PROBE            |#define ENDSTOPPULLUP_ZMIN_PROBE           |
|#define Y_MIN_ENDSTOP_INVERTING false         |#define Y_MIN_ENDSTOP_INVERTING true       |
|#define X_MAX_ENDSTOP_INVERTING false         |#define X_MAX_ENDSTOP_INVERTING true       |
|#define Y_MAX_ENDSTOP_INVERTING false         |#define Y_MAX_ENDSTOP_INVERTING true       |
|#define Z_MIN_PROBE_ENDSTOP_INVERTING false   |#define Z_MIN_PROBE_ENDSTOP_INVERTING true |

- Movement Settings

|original value                                              |value                                                         |
|------------------------------------------------------------|--------------------------------------------------------------| 
|#define DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 4000, 500 } |#define DEFAULT_AXIS_STEPS_PER_UNIT  { 3.3333, 13.9, 8, 500 } | 
|#define DEFAULT_MAX_FEEDRATE          { 300, 300, 5, 25 }   |#define DEFAULT_MAX_FEEDRATE          { 300, 300, 300, 25 }   |

- Axis settings

|original value                                              |value                               |
|------------------------------------------------------------|------------------------------------|
|#define INVERT_Z_DIR false                                  |#define INVERT_Z_DIR true           |
|#define X_BED_SIZE 1400                                     |#define X_BED_SIZE 1280              |
|#define Y_BED_SIZE 2000                                     |#define Y_BED_SIZE 3000              |
|#define Z_MAX_POS 200                                       |#define Z_MAX_POS 4                 |

- Homing settings

|original value                                              |value                               |
|------------------------------------------------------------|------------------------------------|
|#define HOMING_FEEDRATE_XY (50*60)                          |#define HOMING_FEEDRATE_XY (100*60) |

#### Configuration_adv.h changes

|original value            |value                               |
|--------------------------|------------------------------------|
|#define X_HOME_BUMP_MM 5  |#define X_HOME_BUMP_MM 10           |


### how to install 

- download the firmware 1.1.9 on the marlin github repository [firmware](https://github.com/MarlinFirmware/Marlin/releases)
- copy over the modified Configuration.h and Configuration_avd.h files
- flash the firmware using the Arduino IDE
