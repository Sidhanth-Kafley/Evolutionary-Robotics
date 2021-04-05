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

    def __init__(self, directOrGUI):

        self.directOrGUI = directOrGUI
        if(directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):

        for t in range(1000):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            if (self.directOrGUI == "GUI"):
                time.sleep(1/1800)

    def Get_Fitness(self):

        self.robot.Get_Fitness()

    def __del__(self):

        p.disconnect()
