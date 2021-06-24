import matplotlib.pyplot as plot

def CalculateVolume(Pressure, n, R, T): # Function calculating the Van Der Waals Equation
    
    T = (T - 32) * 0.555 + 273.15 # Convert the temperature to kelvin
    Volume = []
    
    for P in Pressure: # Iterate through Pressure array
        
        V = n*R*T / P 
        
        Volume.append(V) 
    
    return Volume 

n = 1
R = 0.0821
Pressure = [0.8, 0.9, 1.0, 1.1, 1.2]

TempInput = float(input("Enter Temp in Fahrenheit: "))

Volume = CalculateVolume(Pressure, n, R, TempInput) # Calculate list of Volumes

plot.xlabel("Pressure (atm)")
plot.ylabel("Volume (liters)")
plot.scatter(Pressure, Volume)
plot.show() # Plot graph