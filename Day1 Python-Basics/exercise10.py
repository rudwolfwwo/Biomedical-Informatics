#import random as rnd
import math

#a)
def formula(x):
    return math.floor(math.sqrt((2+(50*x))/30))

l = [10,11,20]
#for j in range(0,10): l.append(rnd.randint(0,201)) length not given

s = {}
for e in l:
    s[e] = formula(e)
temp = ""
for e in s:
    temp += str(e) + ":" + str(s[e]) + ", "
print(temp)

#b)
heads = 35
legs = 94
chicken_legs = 2
rabbit_legs = 4
for i in range(0, heads + 1):
    if legs - i * chicken_legs - (heads - i) * rabbit_legs == 0:
        print("Chicken %i (legs: %i), Rabbits %i (legs: %i)" % (i, i * chicken_legs, heads - i, (heads - i) * rabbit_legs))
