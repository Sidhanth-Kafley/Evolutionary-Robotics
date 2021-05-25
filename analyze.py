import numpy as np
import matplotlib.pyplot

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
targetAnglesValuesBackLeg = np.load('data/targetAngles_backLeg.npy')
targetAnglesValuesFrontLeg = np.load('data/targetAngles_frontLeg.npy')
x = np.linspace(-np.pi, np.pi, 1000)
#matplotlib.pyplot.plot(backLegSensorValues, linewidth=3)
#matplotlib.pyplot.plot(frontLegSensorValues)
#matplotlib.pyplot.legend()
matplotlib.pyplot.plot(x, np.sin(targetAnglesValuesBackLeg))
matplotlib.pyplot.plot(x, np.sin(targetAnglesValuesFrontLeg))
matplotlib.pyplot.plot.xlabel('Generations')
matplotlib.pyplot.plot.ylabel('Fitness Value')
matplotlib.pyplot.show()
