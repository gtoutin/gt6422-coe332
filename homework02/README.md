# Animon!

Animon is Homework 1, except the new feature is to turn ```read_animals.py``` into an imitation Pokemon game.

## Installation

Pull down the Docker image from Docker Hub with  
```docker pull gctoutin/homework02:1.0```  
after that, run it with
```docker run gctoutin/homework02:1.0```  
The files can be found in the ```/code/``` folder.

## Usage

### 1. Generate Animon species.
Before playing the game, you must generate a set of 20 animal species. These are the species that the game will pull from to generate random encounters. When you want new animals, run this script again to generate different.
The Python script is executable from the command line.

```generate_animals.py```

### 2. Catch Animon.
Now it's time to play! You need to catch animon before you can have a collection. Run ```read_animals.py``` and choose the catch option. A random animal will be chosen from the ones previously generated. The more arms + legs it has, the harder it will be to catch.

```read_animals.py```

### 3. View Animon.
To see your animals, run ```read_animals.py``` and choose the see your animals option. All the animals' information will be shown.

## Unit Testing
Unit testing for ```name_animal()``` within ```read_animals.py``` is available. To run it, run ```test_read_animal.py``` on the command line.

The fastest way to test it without editing code is to choose the see (s) option. To avoid doing this, go to ```read_animals.py``` and comment out ```main()``` at the bottom of the code.

## License
[MIT](https://choosealicense.com/licenses/mit/)
