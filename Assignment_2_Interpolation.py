def interpolate(x, y, hour): #function taking user input to find interval, slope and then calculate interpolation
    
    i0 = 0 
    i1 = 0
    i2 = 0
    
    for points in x: # loop through array and increment each after if statement iteration
        i0 = i0 + 1 
        
        if points >= hour: # find interval 
            i1 = i0-2
            i2 = i0-1
            
            break # once found, break out to calculate interpolation
  
    m = (y[i2] - y[i1]) / (x[i2] - x[i1]) # m is slope
    
    NonMeasured = y[i1] + (m * (hour - x[i1])) #  linear interpolation formula
    
    return NonMeasured 

def main():
    
    x_points = [0, 1, 2, 5, 7, 8, 10 ,12 ,15] # time in hours
    y_points = [0, 0.4, 0.6, 1.3, 2.1, 2.9, 3.4, 3.7, 3.9] # Rainfall in inches
    
    hour = float(input("Enter an hour between 0 and 15: ")) # input from user is the hour
    
    NonMeasured = interpolate(x_points, y_points, hour)
    
    print(NonMeasured)

main()