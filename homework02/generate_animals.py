# Authon: Gabrielle Toutin
# Date: 1/27/2021
# Homework 1



import petname
import random
import json



animals = { "animals": [] }    # initialize animals dictionary

heads = ["snake", "bull", "lion", "raven", "bunny"]    # get head choices
bodies = petname.names                       # get body choices

while len(animals["animals"]) < 20:
    head = random.choice(heads)    # choose a random head from heads list

    body1 = random.choice(bodies)  # choose 2 animals for the body
    body2 = random.choice(bodies)

    while (body1 == body2):
        body2 = random.choice(bodies)    # can't choose the same 2 animals

    body = body1 + '-' + body2    # format the body correctly

    numarms = 2 * random.randint(1,5)    # choose a number of arms
    numlegs = 3 * random.randint(1,4) # choose a number of legs
    numtails = numarms + numlegs

    animal = { "head": head, 
               "body": body, 
               "arms": numarms, 
               "legs": numlegs, 
               "tail": numtails }

    if (animal in animals["animals"]):    # no duplicates
        continue
    else:
        animals["animals"].append(animal) # add new animal to dictionary



with open('animals.json', 'w') as out:
    json.dump(animals, out, indent=2)



