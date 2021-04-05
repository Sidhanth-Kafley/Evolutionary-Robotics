import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                self.motors[jointName].Set_Value(self.robot, desiredAngle)

    def Think(self):

        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):

        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        os.system("mv tmp"+str(self.solutionID)+".txt fitness"+str(self.solutionID)+".txt")
        f.close()
