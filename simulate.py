import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from simulation import SIMULATION


simulation = SIMULATION()
simulation.Run()

#physicsClient = p.connect(p.GUI)
#p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.setGravity(0,0,-9.8)
#planeId = p.loadURDF("plane.urdf")
#robot = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")
#backLegSensorValues = np.zeros(1000)
#frontLegSensorValues = np.zeros(1000)
#pyrosim.Prepare_To_Simulate("body.urdf")
#
#n = np.linspace(-np.pi, np.pi, 1000)
#targetAngles_backLeg = np.sin(c.frequency_backLeg * n + c.phaseOffset_backLeg) * c.amplitude_backLeg
#
#targetAngles_frontLeg = np.sin(c.frequency_frontLeg * n + c.phaseOffset_frontLeg) * c.amplitude_frontLeg
#
#for i in range(1000):
#    p.stepSimulation()
#    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#    pyrosim.Set_Motor_For_Joint(
#    bodyIndex = robot,
#    jointName = "Torso_BackLeg",
#    controlMode = p.POSITION_CONTROL,
#    targetPosition = targetAngles_backLeg[i],
#    maxForce = 30)
#    pyrosim.Set_Motor_For_Joint(
#    bodyIndex = robot,
#    jointName = "Torso_FrontLeg",
#    controlMode = p.POSITION_CONTROL,
#    targetPosition = targetAngles_frontLeg[i],
#    maxForce = 30)
#    time.sleep(1/800)
#np.save('data/backLegSensorValues.npy', backLegSensorValues)
#np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
#p.disconnect()

