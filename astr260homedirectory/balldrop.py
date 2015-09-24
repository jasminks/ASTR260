#Date: 9/3/14

import math
h=float(input("Input height you are dropping the ball from:"))
t=float(input("Input the time you want to know ball's position:"))

x=(0.5*(-9.81))*(t*t)+h

print("the height of the ball is ",x," at time t")
