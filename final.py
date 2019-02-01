import dxl
import time
import math
from whatup import *

# coords
# x = int(input("x:"))
# y = int(input("y:"))

x,y=udharja()
print (x,y)
a = dxl.get_available_ports()
print(a)
d = dxl.dxl(a[0], 1000000)
print(d.scan(10))


# lengths
a2 = 9.3
a4 = 10.6


# value of r
r = math.sqrt(pow(x, 2) + pow(y, 2))
print(r)
# equation 1
pa = float((pow(a2, 2) + pow(r, 2) - pow(a4, 2)) / (2 * a2 * r))
print (pa)
p1 = math.acos(pa) * (180 / 3.14)
# equation 2
pb = (y / x)
p2 = math.atan(pb) * (180 / 3.14)
# equation 3
pc = (pow(a4, 2) + pow(a2, 2) - pow(r, 2)) / (2 * a2 * a4)
print(pc)
p3 = math.acos(pc) * (180 / 3.14)

# angles
m = p2 - p1
n = 180 - p3

# writing angles
m3 = int(219 + (m * 3.413))
m4 = int(512 + (n * 3.413))


# dictionary writting values to motors corresponding to the motor ID
dictionary = {1: 2122, 2: 3076, 3: m3, 4: m4, 5: 202}
# zero for 1 is in 2122 and zero position for 2 is in 2068
# zero for 3-7 are in 512
d.speed(1, 40)
d.speed(2, 40)
d.speed(3, 40)
d.speed(4, 40)
d.speed(5, 40)
d.speed(6, 40)
d.speed(7, 40)

# sync-write command
d.set_goal_position(dictionary)

# for a time interval between commands use: time.sleep(seconds)

# setting torque to zero(not very necessary)
# d.set_torque({k: 0 for k in range(1, 8)})

# prints done after all commands are executed
print("done")