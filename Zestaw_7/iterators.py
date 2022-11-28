import itertools
import random

binary = [0,1]
directions = ["N" , "E" , "W" , "S"]
days_of_week = [0,1,2,3,4,5,6]

iter_binary = itertools.cycle(binary)
iter_directions = iter(lambda: random.choice(directions) , 1)
iter_days_of_week = itertools.cycle(days_of_week)

for i in range (50):
    print(str(next(iter_binary)) + " " + str(next(iter_directions)) + " " + str(next(iter_days_of_week)))

