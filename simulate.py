import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
backLegSensorValues = np.zeros(100)
frontLegSensorValues = np.zeros(100)
pyrosim.Prepare_To_Simulate("body.urdf")
for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = ...,
    maxForce = ...)
    time.sleep(1/60)
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()

