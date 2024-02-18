from codrone_edu import drone
from time import sleep
import asyncio
import open_gopro



drone = drone.Drone()
drone.pair()
drone.takeoff()
drone.land()
drone.close()
