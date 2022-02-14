from contextlib import nullcontext
from http.client import responses
import json, ssl
from operator import contains
import numbers
import os
from pathlib import Path
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
        letter = input("Imput letter")

        if(len(letter) != 1):
            print("Not a letter")
            continue
        if (letter.isdigit()):
            print("error")
            continue
        return letter




    

    

    

