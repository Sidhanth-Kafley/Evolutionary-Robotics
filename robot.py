import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim

class ROBOT:

    def __init__(self):
    
        self.robot = p.loadURDF("body.urdf")
        
        self.motor = {}
    
    def Prepare_To_Sense(self):
        
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            
    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)
            
