## Motor output checker/ proof of concept
## Val Coppo


##ThunderBorg setup
#import ThunderBorg
#TB = ThunderBorg.ThunderBorg() 
#TB.Init()


def start_motors():
    voltage = int(input("The Voltage ranges from 7.0V to 35.0V  \nMotor Voltage?: "))
    percent = int((voltage/35) * 100)
    if percent > 100:
        print ("voltage too high")
    elif percent < 20:
        print("Not Enough Voltage")
    else:

        #TB.SetMotors(voltage)
        print ("Voltage set to ",voltage, percent, "%", "of total motor power\n" )


def stop_motors():
    #TB.MotorsOff()  
    print("Motors Off")



while True:
    start_motors()

