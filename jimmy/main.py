from jimmy.vehicle import Vehicle
from jimmy.sensors.ir.vl53l0x import VL53L0XSensor


robot = Vehicle()
robot.attach_sensor(VL53L0XSensor(), 'front')
