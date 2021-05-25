import numpy as np
import matplotlib.pyplot


# versionA = np.load('data/versionA.npy')
# versionAMean = np.mean(versionA, axis=0)
# vAstd = np.std(versionA, axis=1)
m1 = np.load('data/versionA1.npy')
m1s = np.mean(m1, axis=0)
m2 = np.load('data/versionA2.npy')
m2s = np.mean(m2, axis=0)
m3 = np.load('data/versionA3.npy')
m3s = np.mean(m3, axis=0)
m4 = np.load('data/versionA4.npy')
m4s = np.mean(m4, axis=0)
m5 = np.load('data/versionA5.npy')
m5s = np.mean(m5, axis=0)
#m6 = np.load('data/versionA6.npy')
#m6s = np.mean(m6, axis=0)
m7 = m1s+m2s+m3s+m4s+m5s
m=m7/5

# versionB = np.load('data/versionB.npy')
# versionBMean = np.mean(versionB, axis=0)
# vBstd = np.std(versionB, axis=1)
n1 = np.load('data/versionB1.npy')
n1s = np.mean(n1, axis=0)
n2 = np.load('data/versionB2.npy')
n2s = np.mean(n2, axis=0)
n3 = np.load('data/versionB3.npy')
n3s = np.mean(n3, axis=0)
n4 = np.load('data/versionB4.npy')
n4s = np.mean(n4, axis=0)
n5 = np.load('data/versionB5.npy')
n5s = np.mean(n5, axis=0)
#n6 = np.load('data/versionB6.npy')
#n6s = np.mean(n6, axis=0)
n7 = n1s+n2s+n3s+n4s+n5s
n=n7/5
# for col in range(versionA.shape[1]):
# lineA1 = matplotlib.pyplot.plot(versionAMean+vAstd, linewidth = 0.5, label='VersionA')
lineA2 = matplotlib.pyplot.plot(m, linewidth = 0.5, label='VersionA')
# lineA3 = matplotlib.pyplot.plot(versionAMean-vAstd, linewidth = 0.5, label='VersionA')
## for row in range(versionB.shape[0]):
# lineB1 = matplotlib.pyplot.plot(versionBMean+vBstd, label='VersionB')
lineB2 = matplotlib.pyplot.plot(n, label='VersionB')
# lineB3 = matplotlib.pyplot.plot(versionBMean-vBstd, label='VersionB')


matplotlib.pyplot.xlabel('Generations')
matplotlib.pyplot.ylabel('Fitness Value')

matplotlib.pyplot.show()
