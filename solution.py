import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION():

    def __init__(self, nextAvailableID):

        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights*2-1
        self.myID = nextAvailableID

    def Start_Simulation(self, guiOrDirect):

        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        print("python3 simulate.py " + guiOrDirect + " "+ str(self.myID) + " &" )
        os.system("python3 simulate.py " + guiOrDirect + " "+ str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):

        fitnessFileName = "fitness"+str(self.myID)+".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.1)
        fitnessFile = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(fitnessFile.read())
        # print("\n", self.fitness)
        fitnessFile.close()
        os.system("rm fitness"+str(self.myID)+".txt")

    def Mutate(self):
        randomRow = random.randint(0, len(self.weights)-1)
        randomColumn = random.randint(0, len(self.weights[0])-1)
        self.weights[randomRow, randomColumn] = random.random()*2-1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Create_World(self):

        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        x=-3
        y=3
        z=0.5

        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])

        pyrosim.End()



    def Create_Body(self):

        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length, width, height])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "0 0.5 1", jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2, 1, 0.2])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "0 -0.5 1", jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2, 1, 0.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = "-0.5 0, 1", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1, 0.2, 0.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = "0.5 0, 1", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1, 0.2, 0.2])



        pyrosim.End()


    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name =1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Motor_Neuron(name = 5 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 6 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 7 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name = 8 , jointName = "Torso_RightLeg")

        for currentRow in range(len(self.weights)):
            for currentColumn in range(len(self.weights[0])):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()
