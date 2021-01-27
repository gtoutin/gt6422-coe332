# Author: Gabrielle Toutin
# Date: 1/27/2021
# Homework 1

import json
import random


with open('animals.json', 'r') as f:
    animals = json.load(f)

animal = random.choice(animals['animals'])    # choose a random animal


# print out animal body parts

print("Here comes a beast!")
print("It has the head of a " + animal["head"] + " and the body of a " + animal["body"] + "!")
print("Its " + str(animal['arms']) + " arms flail and its " + str(animal['legs']) + " legs shake the ground.")
print("It shows its anger with its " + str(animal['tail']) + " tails!")
