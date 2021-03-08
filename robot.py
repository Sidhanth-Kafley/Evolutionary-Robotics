import pybullet as p
from sensor import SENSOR
from motor import MOTOR

class ROBOT:

    def __init__(self):
    
        self.robot = p.loadURDF("body.urdf")
        self.sensor = {}
        self.motor = {}
