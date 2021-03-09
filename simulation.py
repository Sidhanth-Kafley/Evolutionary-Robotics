from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
import time

class SIMULATION:

    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate("body.urdf")
     
    def Run(self):
    
        for i in range(10):
            p.stepSimulation()
            time.sleep(1/800)
            
            
    def __del__(self):
    
        p.disconnect()
            
            
