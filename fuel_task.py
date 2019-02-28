# write a function that tells you if it is possible to get to the pump or not.
def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left