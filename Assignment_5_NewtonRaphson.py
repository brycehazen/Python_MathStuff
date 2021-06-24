import math

# Function for Newton-Raphson method
def NewtonRaphson(f, x, h, GivenValues):
    
    return (f(x + h, GivenValues) - f(x - h, GivenValues)) / (2.0 * h)

# Manning equation with oneside equal to zero
def ManningZero(y, GivenValues):
    Q, n, b, z, s = GivenValues
    A = b * y + z * y**2
    W = b + 2 * y * math.sqrt(1 + z * z)
    R = A / W
    
    NewManning = (Q * n / 1.49 / math.sqrt(s)) - A * R**(2/3)
    
    return NewManning

# Check the value of Q 
def Trapezoidal(n, b, y, z, s):
    
    A = b * y + z * y**2
    W = b + 2 * y * math.sqrt(1 + z * z)
    R = A / W
    Q = 1.49 / n * A * math.pow(R, 2.0 / 3.0) * math.sqrt(s)
    
    return Q

Q_Value = str(round(Trapezoidal(0.022, 3, 1.395, 2, 0.01), 2))
print('When Flowrate (Q) is: ' + Q_Value)

# Iterations via Newton-Raphson method finding depth 
def DepthCalulation(f, FromRange, ToRange, GivenValues):
    x_Initial = FromRange
    x_New = x_Initial + 10 * ToRange
    
    while (abs(x_Initial - x_New) > ToRange):
        y_New = f(x_New, GivenValues)
        x_Initial = x_New
        x_New = x_Initial - y_New / NewtonRaphson(f, x_Initial, ToRange, GivenValues)
    
    return x_New

# Given Values
Q = 50
n = 0.022 
b = 3
z = 2
s = 0.01 

# Accuracy range
range_1 = 0.01
range_2 = 0.01

# Calculation of the depth
Depth = str(round(DepthCalulation(ManningZero, range_1, range_2, [Q, n, b, z, s]), 2))

print('Depth approximates to: ' + Depth)

