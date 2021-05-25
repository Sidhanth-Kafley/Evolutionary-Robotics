import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import numpy as np

class ROBOT:

    def __init__(self, solutionID):

        self.robot = p.loadURDF("body.urdf")
        self.solutionID = solutionID
        self.nn = NEURAL_NETWORK("brain"+str(self.solutionID)+".nndf")
        cmd = "rm brain"+ str(solutionID)+".nndf"
        os.system(cmd)
        self.timestep = 0

    def Prepare_To_Sense(self):

        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):

        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):

        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                self.motors[jointName].Set_Value(self.robot, desiredAngle)

    def Think(self):

        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        timeStepCounter = 0
        average = []
        for i in range(1000):
            frontLowerLeg = self.sensors["FrontLowerLeg"].values[i]
            backLowerLeg = self.sensors["BackLowerLeg"].values[i]
            rightLowerLeg = self.sensors["RightLowerLeg"].values[i]
            lefttLowerLeg = self.sensors["LeftLowerLeg"].values[i]
            sum = frontLowerLeg + backLowerLeg + rightLowerLeg + lefttLowerLeg
            mean = sum/4
            average.append(mean)

        numTimeSteps = 0
        numNegativeOnes = 0
        for x in average:
            if x == -1:
                numNegativeOnes+=1
                if numNegativeOnes > numTimeSteps:
                    numTimeSteps = numNegativeOnes
            else:
                numNegativeOnes = 0

        f = open("tmp" + str(self.solutionID) + ".txt", "w")

        f.write(str(numTimeSteps))
        os.system("mv tmp"+str(self.solutionID)+".txt fitness"+str(self.solutionID)+".txt")
        f.close()
