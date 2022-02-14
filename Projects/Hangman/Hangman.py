from contextlib import nullcontext
from http.client import responses
import json, ssl
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

print(len(coffee.blend_name)*" _")



def input_function():
    while(True):
        letter = input("Input letter")
        string_set = set(letter)
        punctuation_set = set(letter.punctuation)

        if(len(letter) != 1):
            print("Only type 1 letter")
            continue
        if (letter.isnumeric()):
            print("There are no numbers")
            continue
        if (letter.isspace):
            print("Not a letter")
            continue
        if (string_set.intersection(punctuation_set)):
            print("Not a letter")
            continue
        return letter

print(input_function())


    

    

    

