import random as rnd
import os
import math

#a)
l = []
for j in range(0, 1000):
    l.append(rnd.randint(-10, 10))
random_elements = []
for j in range(0, 50):
    random_elements.append(l[rnd.randint(0, 999)])
print(random_elements)


#b)
def indentify_working_dir():
    print("Your working directory: ", os.getcwd())
    print("All Files: ", os.listdir())


indentify_working_dir()

#c)
print(math.pi)
for char in str(math.pi):
    if char != "." and int(char) % 2 == 0:
        print(char)

#d)
def binomial_coefficient(n, k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

