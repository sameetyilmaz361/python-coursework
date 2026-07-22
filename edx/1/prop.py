import random
import math

def rand():
    return random.uniform(-1, 1)

def distance(x, y):
    sums = (x[0] - y[0])**2 + (x[1] - y[1])**2
    dist = math.sqrt(sums)
    return dist

def in_circle(x, origin = [0,0]):
    if distance(x , origin) < 1:
        return True
    else:
        return False

R = 10000
inside = []

random.seed(1)

for _ in range(R):
    point = (rand(), rand())
    
    inside.append(in_circle(point))


proportion = sum(inside) / R

print(proportion)

diff = (math.pi / 4) - proportion

print(diff)