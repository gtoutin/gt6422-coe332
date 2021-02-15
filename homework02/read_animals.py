#!/usr/bin/env python3
# Author: Gabrielle Toutin
# Date: 2/14/2021
# Homework 2

import json
import random
import sys
import os.path as path


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
    with open('MyAnimalBox.json', 'w') as f:
        json.dump(myanimals, f)

def seeAnimals():
    doesexist = path.exists("MyAnimalBox.json")
    if not(doesexist): return False
    with open('MyAnimalBox.json', 'r') as f:
        animals = json.load(f)
    return animals


def printAnimal(animal):
    print("Name:", animal['name'])
    print("Head:", animal['head'])
    print("Body:", animal['body'])
    print("Arms:", animal['arms'])
    print("Legs:", animal['legs'])
    print("Tails:",animal['tail'])
    print()



def main():	# create a pokemon game

    animals = loadAnimal()
#    myanimals = []
    myanimals = seeAnimals()
    if not(myanimals): # if it's empty
        myanimals = []

    play = 'x'
    while play not in ['c','s']:
        play = str(input("Catch some animals or see your animals? (c or s): "))
    if (play=='c'):
        play = True
    elif play=='s':
        play = False
    else:
        return


    if not(play):	# see animals
        openanimals = seeAnimals()	# does file exist?

        if openanimals==False:
            print("You have no animals! Go catch some!")
            return
        else:
            print()
            for animal in openanimals:
                printAnimal(animal) 
            return

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
