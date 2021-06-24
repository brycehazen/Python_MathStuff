import math 

east1, north1 = input("UTM coordinates for point A:").split()
east2, north2 = input("UTM coordinates for point B:").split()
east3, north3 = input("UTM coordinates for point C:").split()

def calcUmtAB ( north1, east1, north2, east2): # Function to Calc point A to B

    bearing1 = 0
    # Condition for each quadrant
    if (north2 > north1):
        if ( east2 > east1):
            bearing1 = int( 57.2958 * math.atan((north2 - north1) / (east2 - east1)))
        elif( east2 <  east1):
            bearing1 = int( 270 + (57.2958 * math.atan(-((north2 - north1) / (east2 - east1)))))
    elif (north2 < north1):
        if ( east2 > east1):
            bearing1 = int(90 + (57.2958 * math.atan(-((north2 - north1) / (east2 - east1)))))
        elif ( east2 <  east1):
            bearing1 = int(180 + (57.2958 * math.atan(-((north2 - north1) / (east2 - east1)))))
     
    distance1 = int( math.sqrt((north2 - north1)**2 + ( east2 - east1)**2))

    return distance1, bearing1


def calcUmtBC ( north2, east2, north3, east3): # Function to Calc point B to C
    
    bearing2 = 0
    # Condition for each quadrant
    if ( north3 > north2):
        if ( east3 > east2):
            bearing2 = int (57.2958 * math.atan((north3 - north2) / (east3 - east2)))
        elif( east3 <  east2):
            bearing2 = int(270 + (57.2958 * math.atan(-((north3 - north2) / (east3 - east2)))))
    elif (north3 < north2):
        if ( east3 > east2):
            bearing2 =int( 90 + (57.2958 * math.atan(-((north3 - north2) / (east3 - east2)))))
        elif ( east3 <  east2):
            bearing2 = int(180 + (57.2958 * math.atan(-((north3 - north2) / (east3 - east2)))))
     
    distance2 = int( math.sqrt((north3 - north2)**2 + ( east3 - east2)**2))
    
    return distance2, bearing2

distance1, bearing1 = calcUmtAB(north1, east1, north2, east2)
distance2, bearing2 = calcUmtBC(north2, east2, north3, east3)

print("From A to B is:", "{0:.2f}".format(distance1),"m", "{0:.2f}".format(bearing1),u"\N{DEGREE SIGN}")
print("From B to C is:", "{0:.2f}".format(distance2),"m", "{0:.2f}".format(bearing2),u"\N{DEGREE SIGN}")

