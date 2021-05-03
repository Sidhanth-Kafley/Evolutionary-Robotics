import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:

    def __init__(self, solutionID):

        self.robot = p.loadURDF("body.urdf")
        self.solutionID = solutionID
        self.nn = NEURAL_NETWORK("brain"+str(self.solutionID)+".nndf")
        cmd = "rm brain"+ str(solutionID)+".nndf"
        os.system(cmd)

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

        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        zCoordinateOfLinkZero = positionOfLinkZero[2]

        stateOfLinkOne = p.getLinkState(self.robot,1)
        positionOfLinkOne = stateOfLinkOne[0]
        zCoordinateOfLinkOne = positionOfLinkOne[2]


        stateOfLinkTwo = p.getLinkState(self.robot,2)
        positionOfLinkTwo = stateOfLinkTwo[0]
        zCoordinateOfLinkTwo = positionOfLinkTwo[2]

        stateOfLinkThree = p.getLinkState(self.robot,3)
        positionOfLinkThree = stateOfLinkThree[0]
        zCoordinateOfLinkThree = positionOfLinkThree[2]
        # basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        # basePosition = basePositionAndOrientation[0]
        # zPosition = basePosition[2]

        sum = zCoordinateOfLinkZero + zCoordinateOfLinkOne + zCoordinateOfLinkTwo + zCoordinateOfLinkThree
        mean = sum/4

        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(mean))
        os.system("mv tmp"+str(self.solutionID)+".txt fitness"+str(self.solutionID)+".txt")
        f.close()
