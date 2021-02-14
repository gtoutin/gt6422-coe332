# Author: Gabrielle Toutin
# Date: 2/14/2021
# Homework 2

import json
import random


def loadAnimal():	# gets a dictionary of animals and returns it as a dictionary
    with open('animals.json', 'r') as f:
        animals = json.load(f)
    return animals

def getAnimal(animals):

    animal = random.choice(animals['animals'])    # choose a random animal species
    return animal

def catchRate(animal):
    tails = animal['tail']
    return (100-5*(tails-4))/100

def nameAnimal(animal, animname):
    newanimal = animal
    newanimal['name'] = animname
    return newanimal

def saveAnimals(myanimals):
    with open('MyAnimalBox.json', 'a') as f:
        json.dump(myanimals, f)


def main():	# create a pokemon game

    animals = loadAnimal()
    myanimals = []
    while True:
        print()
        animal = getAnimal(animals)
        print("A wild", animal['head'] + "-" + animal['body'], "has appeared!")
        print("It has", animal['tail'], "tails," , animal['arms'], "arms, and", animal['legs'], "legs!") 

        pursue = True
        while pursue:
        
            while pursue not in ['y','n']:
                pursue = str(input("Throw a ball? (y or n): "))
            if (pursue=='y'):
                pursue = True
            elif pursue=='n':
                pursue = False
                break


            if pursue: # if throw a ball
                catchprob = catchRate(animal)    # does the ball land? probability depends on number of legs
                if random.random() < catchprob: # if catch
                    print("Gotcha!")
                    animname = input("What would you like to name it? ") # name?
                    myanimals.append(nameAnimal(animal, animname))  # save creature into pokemon box json
                    print("Saved!")
                    break
                else:
                    print("Oh no! It jumped out!")

        quit = 'x'
        while quit not in ['y','n']:
            quit = str(input("\nEnd the game? (y or n): "))
        if quit=='y':
            quit = True
            break
        elif quit=='n':
            quit = False
    
    print("\n\nWriting animal box...")
    saveAnimals(myanimals)
    print("Animals saved to MyAnimalBox.json!")
    print("Exited.")



main()    
