# For å jobbe med første del av notatboken trenger vi disse bibliotekene
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle


# Given values
theta1 = 95     # Vinkel mellom positiv x-akse og "overarm" i grader
l1 = 60        # Lengde til overarm [cm]
theta2 = -100   # Vinkel mellom overarm og underarm i grader
l2 = 50        # Lengde til underarm [cm]

# Convert angles to radians
theta1_rad = np.deg2rad(theta1)
theta2_rad = np.deg2rad(theta2)

# Original equations
xend = l1 * np.cos(theta1_rad) + l2 * np.cos(theta1_rad + theta2_rad)
yend = l1 * np.sin(theta1_rad) + l2 * np.sin(theta1_rad + theta2_rad)
endepunkt_underarm = [xend, yend]


#Analytical solution for partial derivatives. Dette ble også gjort for hånd

# Partial derivatives of xend and yend  with respect to theta1
dx_dtheta1 = -l1 * np.sin(theta1_rad) - l2 * np.sin(theta1_rad + theta2_rad)
# Partial derivative of xend with respect to theta2
dx_dtheta2 = -l2 * np.sin(theta1_rad + theta2_rad)

# Output the partial derivatives at utgangsposisjon-values
print(f"Partial derivative of x with respect to theta1: {dx_dtheta1:.2f}" )
print(f"Partial derivative of x with respect to theta2: {dx_dtheta2:.2f}" )







# Numerical solution for partial derivatives    dx/dtheta1 and dx/dtheta2

# Create list for theta1 ∈ [0, π], with 180 elements
theta1_list = np.linspace(0, 180, 180)
#Create list for theta2 ∈ [-π, π], with 360 elements
theta2_list = np.linspace(-180, 180, 360)


#dx/dtheta1:

#  THETA2 = konstant -100 degrees (i radianer)
theta2 = (np.pi/180)*(-100)

# Create list for x-values for each theta1
x_koordinat_sluttposisjon = []
for theta1 in theta1_list:
    # Convert angles to radians
    theta1_rad = np.pi/180*theta1
    theta2_rad = np.pi/180*theta2
    # Original equations
    xend = l1 * np.cos(theta1_rad) + l2 * np.cos(theta1_rad + theta2_rad)
    #yend = l1 * np.sin(theta1_rad) + l2 * np.sin(theta1_rad + theta2_rad)
    x_koordinat_sluttposisjon.append(xend)


# make graph with x_koordinat_sluttposisjon as y-values and theta1_list as x-values

plt.plot(theta1_list, x_koordinat_sluttposisjon)
plt.xlabel("θ_1 ∈ [0, 180°]")
plt.ylabel("x_koordinat_sluttposisjon")
plt.title("θ_2 er konstant =  -100°")
plt.grid(True)
plt.show()




