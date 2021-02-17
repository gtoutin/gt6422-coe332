#!/usr/bin/env python3
# Homework 2
# Gabrielle Toutin
# 2/15/2021

import unittest
from read_animals import nameAnimal
 

class TestAnimals(unittest.TestCase):
    def test_nameAnimal(self):
        animal = {"head": "snake", "body": "guinea-quetzal", "arms": 7, "legs": 3, "tail": 10}
        self.assertEqual(nameAnimal(animal, "Charlie")['name'], "Charlie")
        self.assertEqual(nameAnimal(animal, 1234)['name'], 1234)
        self.assertRaises(TypeError, nameAnimal, animal, )	# test for error if no name passed


if __name__ == '__main__':
    unittest.main()
