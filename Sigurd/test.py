import numpy as np

# Given values
theta1 = 95     # Vinkel mellom positiv x-akse og "overarm" i grader
l1 = 60        # Lengde til overarm [cm]
theta2 = -100   # Vinkel mellom overarm og underarm i grader
l2 = 50        # Lengde til underarm [cm]




# Test for case one: without converting first
test1 = l2*np.cos( (np.pi/180)*(theta1+theta2) )

print(test1)


# Test for case two: converting first
# Convert angles to radians
theta1_rad = np.pi/180*theta1
theta2_rad = np.pi/180*theta2

# Original equations
test2 = l2 * np.cos(theta1_rad + theta2_rad)
print(test2)


