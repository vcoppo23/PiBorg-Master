# Tank Robot Controller - Gabe Mankowski
x = 1
L = 1 #Left Motor
R = 0 # Right Motor
LS = 16 #Left Sensor
RS = 17 #Right Sensor
RPL.pinMode(LS,RPL.INPUT)
RPL.pinMode(RS,RPL.INPUT)


# Template for PiBorg code

import RoboPiLib as RoboPi

# connect to RoboPi
RoboPi.RoboPiInit(“/dev/ttyAMA0”,115200)

# Get's the controller module
from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

        
    def on_L3_up(self):
        if readingL == 1:
        RPL.servoWrite(L, 1600)
        elif readingL == 1:
        RPL.servoWrite(L, 1600)
        
        
    def on_L3_down(self):
        if readingL == 1:
        RPL.servoWrite(L, 1400)
        elif readingL == 1:
        RPL.servoWrite(L, 1400)


    def on_R3_up(self):
        if readingR == 0:
        RPL.servoWrite(R, 1400)
        elif readingR == 0:
        RPL.servoWrite(R, 1400)


    def on_R3_down(self):
        if readingR == 0:
        RPL.servoWrite(R, 1600)
        elif readingR == 0:
        RPL.servoWrite(R, 1600)


#left and right arrow plan to more turret left/right
T = 3 #turret motor



    def on_left_arrow_press(self):
        if readingT == 3:
        RPL.servoWrite(L, 1400)
        elif readingT == 3:
        RPL.servoWrite(L, 1400)

    def on_right_arrow_press(self):
        if readingT == 3:
        RPL.servoWrite(L, 1600)
        elif readingT == 0:
        RPL.servoWrite(L, 1600)
    
        

        
  
        




controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
