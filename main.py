from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

drone.takeoff()

drone.sendControlWhile(0, 0, 0, 0, 3000)

drone.sendControlWhile(0, 0, 0, 30, 2000)

drone.set_drone_LED(255, 255, 0, 100)

#######################################################

drone.sendControlWhile(0, 30, 0, 0, 3000)

drone.sendControlWhile(30, 0, 0, 0, 3000)

drone.sendControlWhile(0, -30, 0, 0, 3000)

drone.sendControlWhile(-30, 0, 0, 0, 3000)

#######################################################

drone.sendControlWhile(0, 0, 0, 0, 1000)

drone.sendControlWhile(0, 0, 0, 30, 3000)
drone.sendControlWhile(0, 0, 0, -60, 3000)
drone.sendControlWhile(0, 0, 0, 30, 3000)
drone.sendControlWhile(0, 0, 0, -60, 3000)
drone.sendControlWhile(0, 0, 0, 30, 3000)
drone.sendControlWhile(0, 0, 0, -60, 3000)
drone.sendControlWhile(0, 0, 0, 30, 3000)

#######################################################

drone.sendControlWhile(0, 0, 0, 0, 2000)

drone.land()
drone.close()

drone.land()
drone.close()