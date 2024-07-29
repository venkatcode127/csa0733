import math
signal_power=eval(input("enter the radians"))
noise_power=eval(input("enter the noise"))
ratio=signal_power/noise_power
decimal=10*math.log10(ratio)
print(decimal)
