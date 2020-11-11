import sympy as sym
import math

# Matrix multiplacation function
def mm(M1, M2):
    res = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                res[i][j] += M1[i][k] * M2[k][j]
    return res

# Conversion between rad and deg
def radToDeg(theta):
    return math.degrees(theta)

def degToRad(theta):
    return math.radians(theta)

# Rotation about z
def rotZ(theta):
    if (theta == degToRad(90)):
        c = 0
        s = 1
    elif (theta == degToRad(180)):
        c = -1
        s = 0
    elif (theta == degToRad(270)):
        c = 0
        s = -1
    elif (theta == 0):
        c = 1
        s = 0
    else:
        c = sym.cos(theta)
        s = sym.sin(theta)

    return [[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

# Translation in z
def transZ(z):
    return [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, z], [0, 0, 0, 1]]

# Translation in x
def transX(x):
    return [[1, 0, 0, x], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

# Rotation about x
def rotX(theta):
    if (theta == degToRad(90)):
        c = 0
        s = 1
    elif (theta == degToRad(180)):
        c = -1
        s = 0
    elif (theta == degToRad(270)):
        c = 0
        s = -1
    elif (theta == 0):
        c = 1
        s = 0
    else:
        c = sym.cos(theta)
        s = sym.sin(theta)

    return [[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]]
