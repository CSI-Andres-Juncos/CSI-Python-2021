from contextlib import nullcontext
from http.client import responses
from itertools import count
import json, ssl
from lib2to3.pytree import LeafPattern
from operator import contains
import numbers
import os
from pathlib import Path
from string import punctuation
from tracemalloc import start
import urllib.request
from Coffee import Coffee

ssl._create_default_https_context = ssl._create_unverified_context

CoffeeURL = "https://random-data-api.com/api/coffee/random_coffee"

req = urllib.request.Request(CoffeeURL)
requestData = json.loads(urllib.request.urlopen(req).read())

coffee:Coffee = Coffee(**requestData)

attemptedLetters = []

errors = 0

steps = ["""
    |---------|
    |         |
    |         |
    |         
    |
    |
    |
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |
    |
    |
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |         I
    |         I
    |
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |         I--
    |         I
    |
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |       --l--
    |         l
    |
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |       --l--
    |         l
    |        /
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |       --l--
    |         l
    |        / \\
    |
    |
    """]

print(steps[0])

print(coffee.blend_name)

print(len(coffee.blend_name)*"_")



def input_function():
    while(True):
        letter = input("Input letter:")
        specialcharacter = "!@#$%^&*()-+?_=,<>/"
        
        if(len(letter) != 1):
            print("Only type 1 letter")
            continue
        if (letter.isnumeric()):
            print("There are no numbers")
            continue
        #if (letter.isspace()):
            #print("Not a letter")
            #continue
        if (letter in specialcharacter):
            print("Not a letter")
            continue

        # append to list of used letters
        attemptedLetters.append(letter)
        return letter

def printword():

    Temp:str = ""
    for letter in coffee.blend_name:
        if letter in attemptedLetters:
            Temp+= letter 
        else:
            Temp+= "_"
    print(Temp)
    return errors


def printsteps():
    for letter in attemptedLetters:
        if letter not in coffee.blend_name:
            errors + 1
            print(steps[errors])
           

while(True):
    input_function()
    printword()
    printsteps()



 



    

    

