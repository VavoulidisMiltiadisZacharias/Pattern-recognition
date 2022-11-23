#QUESTION_1 - PDFs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from scipy.stats import multivariate_normal

#Discrete values for biolocigal indices of healthy
healthy1, healthy2 = np.mgrid[-4.0:6.0:30j, -4.0:6.0:30j]

# Need an (N, 2) array of (x, y) pairs.
healthy = np.column_stack([healthy1.flat, healthy2.flat])

#mean values- healthy
muHealthy = np.array([0.4, 0.8])

#Fill covariance matrix with correct data - healthy
sigmaHealthy = np.array([np.sqrt(1.5), np.sqrt(0.8)]) #Need to give as parameters the sqrt of covariance matrix
covarianceHealthy = np.diag(sigmaHealthy**2)

#Pdf for healthy
zHealthy = multivariate_normal.pdf(healthy, mean=muHealthy, cov=covarianceHealthy)
zHealthy = zHealthy.reshape(healthy1.shape)


#Discrete values for biolocigal indices of unhealthy
unhealthy1, unhealthy2 = np.mgrid[-4.0:6.0:30j, -4.0:6.0:30j]

# Need an (N, 2) array of (x, y) pairs.
unhealthy = np.column_stack([unhealthy1.flat, unhealthy2.flat])

#mean values- unhealthy
muUnhealthy = np.array([1.5, 2.7])

#Fill covariance matrix with correct data - healthy
sigmaUnhealthy = np.array([np.sqrt(0.375), np.sqrt(0.2)]) #Need to give as parameters the sqrt of covariance matrix
covarianceUnhealthy = np.diag(sigmaUnhealthy**2)

#Pdf for healthy
zUnhealthy = multivariate_normal.pdf(unhealthy, mean=muUnhealthy, cov=covarianceUnhealthy)
zUnhealthy = zUnhealthy.reshape(unhealthy1.shape)


#Plot the figures
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(healthy1,healthy2,zHealthy)
#ax.plot_wireframe(x,y,z)
ax.set_title('Healthy pdf')
ax.set_xlabel('Index_1 values')
ax.set_ylabel('Index_2 values')
ax.set_zlabel('Probability')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(unhealthy1,unhealthy2,zUnhealthy)
#ax.plot_wireframe(x,y,z)
ax.set_title('Unhealthy pdf')
ax.set_xlabel('Index_1 values')
ax.set_ylabel('Index_2 values')
ax.set_zlabel('Probability')
plt.show()



#QUESTION_2 - TOTAL PROBABILITY

#A priori probabilities
pw1 = 0.95
pw2 = 0.05

#Calculate total probability
zTotalHealthy = zHealthy*pw1
zTotalUnhealthy = zUnhealthy*pw2

totalProbability = zTotalHealthy + zTotalUnhealthy

#Plot total probability
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(healthy1,healthy2,totalProbability)
#ax.plot_wireframe(x,y,z)
ax.set_title('Total probability')
ax.set_xlabel('Index_1 values')
ax.set_ylabel('Index_2 values')
ax.set_zlabel('Probability')
plt.show()



#QUESTION_3 A POSTERIORY PROBABILITIES

#Calculate a posteriori probabilities
aPosterioriHealthy = zTotalHealthy/totalProbability
aPosterioriUnhealthy = zTotalUnhealthy/totalProbability

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(healthy1,healthy2,aPosterioriHealthy)
#ax.plot_wireframe(x,y,z)
ax.set_title('A posteriori healthy')
ax.set_xlabel('Index_1 values')
ax.set_ylabel('Index_2 values')
ax.set_zlabel('Probability')
plt.show()

#Plot a posteriori probabilities
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(unhealthy1,unhealthy2,aPosterioriUnhealthy)
#ax.plot_wireframe(x,y,z)
ax.set_title('A posteriori unhealthy')
ax.set_xlabel('Index_1 values')
ax.set_ylabel('Index_2 values')
ax.set_zlabel('Probability')
plt.show()



#QUESTION_4 - ERROR

#Initialize the error
error = 0

for i in range(aPosterioriHealthy.shape[0]):
    for j in range(aPosterioriHealthy.shape[1]):
        
        #Choose the smallest probability each time and calculate the error
        if aPosterioriHealthy[i, j] > aPosterioriUnhealthy[i, j]:
            error = error + aPosterioriUnhealthy[i, j] * totalProbability[i, j] * 0.3 * 0.3
        else:
            error = error + aPosterioriHealthy[i, j] * totalProbability[i, j] * 0.3 * 0.3

            
#Print the error
print(f'Error is: {error:.4f}')


