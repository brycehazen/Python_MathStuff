
c = 10000 #set price

Interest = int(input("Enter interest rate: ")) # Read the interest value
Interest = Interest / 100

#Set the resale value and annual revenue as two list
ResaleValue = [10000, 9000, 5000, 3000, 0]
AnnualRevenue = [500, 600, 1000, 1200, 1500]
PV_Resale = []
PV_Annual = []

# Calculate the PV of resale value
for i in range(0, 5):
    PresentValue = (ResaleValue[i]) * (1 / ((1 + Interest)**10))
    PV_Resale.append(PresentValue)


for i in range(0, 5): # Calculate the PV of annual revenue
    Revenue = 0
    
    for j in range (1, 10):
        PresentValue = (AnnualRevenue[i]) * 1/ ((1 + Interest)**j)
        Revenue = Revenue + PresentValue
    
    PV_Annual.append(Revenue)

Total = []


for i in range(0, 5): # Calculate total PV
    Total.append(PV_Resale[i] + PV_Annual[i])

# Print table
print("Resale amount\t\tAnnual revenue\t\tPV of resale\t\tPV of revenue \t\tTotal PV")

for i in range(0, 5):
    print(str(Revenue[i]) + "\t\t" + str(AnnualRevenue[i]) + "\t\t" + str(PV_Resale[i]) + "\t\t" + str(PV_Annual[i]) + "\t\t" + str(Total[i]) + "\n")