import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
pyrosim.Prepare_To_Simulate("body.urdf")
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    min = -(math.pi)/2.0
    max = (math.pi)/2.0
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = min + (random.random() * (max - min)),
    maxForce = 30)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = min + (random.random() * (max - min)),
    maxForce = 30)
    time.sleep(1/1000)
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()

