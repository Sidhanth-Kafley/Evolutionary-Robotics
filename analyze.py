import numpy as np
import matplotlib.pyplot

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()
