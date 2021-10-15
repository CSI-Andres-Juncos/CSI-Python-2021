import math
from ExperimentalData import ExperimentalData

# Gun="OP-SKS"
# Caliber="7.62x39mm"
# Ammunition="MAI AP"
# Velocity_Ms=875
# Building="One World Trade Center"
# BuildingHeight_m=541.3
# gravity_Ms=9.81

#Here im calculating the time by plugging in the formula with the variables defined on top. But first, you need to import the function of the square root.
def ProjectileFunction(experimentalData:ExperimentalData):
    time_s = math.sqrt((2 * experimentalData.BuildingHeight_m) / experimentalData.gravity_Ms)
#Now that time is calculated, the variable is plugged into another formula to calculate distance, or delta x (Δx). 
    Distance_m = (experimentalData.Velocity_Ms * time_s)
    print(f"In this first part of the experiment, the distance of the projectile fired from a {experimentalData.Gun} was calculated. The caliber of the gun was {experimentalData.Caliber} and the projectile fired is a {experimentalData.Ammunition} with a speed of {experimentalData.Velocity_Ms}m/s. The building chosen for this experiment was the {experimentalData.Building} with a height of {experimentalData.BuildingHeight_m} meters. By using the formula for time, the time was {time_s} seconds. Then the time was plugged into another formula to calculate the distance, which was {Distance_m} meters")

# experimentalData ={
#     "Gun=" : "OP-SKS",
#     "Caliber" : "7.62x39mm",
#     "Ammunition" : "MAI AP",
#     "Velocity_Ms" : 875,
#     "Building=" : "One World Trade Center",
#     "BuildingHeight_m" : 541.3,
#     "gravity_Ms" : 9.81
# }

experimentalData = ExperimentalData("OP-SKS","7.62x39mm","MAI AP",875,"One World Trade Center",541.3,9.81)
ProjectileFunction(experimentalData)
