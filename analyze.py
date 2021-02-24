import numpy as np
import matplotlib.pyplot

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
matplotlib.pyplot.plot(backLegSensorValues, linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
