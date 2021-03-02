import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
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
amplitude_backLeg = np.pi/4
frequency_backLeg = 10
phaseOffset_backLeg = 0
n = np.linspace(-np.pi, np.pi, 1000)
targetAngles_backLeg = np.sin(frequency_backLeg * n + phaseOffset_backLeg) * amplitude_backLeg
amplitude_frontLeg = np.pi/4
frequency_frontLeg = 40
phaseOffset_frontLeg = np.pi
targetAngles_frontLeg = np.sin(frequency_frontLeg * n + phaseOffset_frontLeg) * amplitude_frontLeg
#np.save('data/targetAngles_backLeg.npy', targetAngles_backLeg)
#np.save('data/targetAngles_frontLeg.npy', targetAngles_frontLeg)
#exit();
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = targetAngles_backLeg[i],
    maxForce = 30)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = targetAngles_frontLeg[i],
    maxForce = 30)
    time.sleep(1/800)
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()

