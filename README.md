[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)

## Textile Drawing Machine
Textile Drawing Machine  has been designed by Eugenia Morpurgo (mechanics and electronics), Florent Noel (software), with the help of Sami Sabik and Come Turrata. 
TDM has been developed for the project Digital Wax Print, a self initiated research project, carried out by The Future Continuous,  a designed studio made by Olivia De Gouveia and Eugenia Morpurgo.

More information abut Digital Wax Print can be found [here.](http://digitalwaxprint.com/)
More information abut The Future Continuous can be found [here](http://www.thefuturecontinuous.com/).

### Machine

The machine is a custom build inspired by different projects, like this one [here](https://openbuilds.com/threads/cnc-sand-and-spraycalk-drawmaschine.8927/#post-52036)

### Firmware

The machine is powered by an arduino MEGA and a RAMPS 1.4.

The firmware used is Marlin v1.1.1 [here] (https://github.com/MarlinFirmware/Marlin/archive/1.1.x.zip)
It has been modified to fit the needs of this machine. The files can be found under the firmware directory of this repository.

### G-code generation and controlling the machine

The machine is controlled using G-code. To send the G-code instrucions to the machine several software can be used. One very suitable option is to use Pronterface [here] (http://www.pronterface.com/).

To generate the G-code instructions for the machine, the python software contours can be used. It takes a png as input and ouput the corresponding G-code. It can be found under the contour directory of this repository.

To streamline the all process of generating the code, a frontend can be launched. It offers a web page with some basic G-code instructions that can be used to calibrate the machine and an interface where it is possible to upload the png file and convert them to G-code. 

