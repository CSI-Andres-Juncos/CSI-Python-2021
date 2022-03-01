import json, ssl
from pdb import Restart
import urllib.request
from Coffee import Coffee

ssl._create_default_https_context = ssl._create_unverified_context

#Here im requesting a random word from the class and pulling it here
CoffeeURL = "https://random-data-api.com/api/coffee/random_coffee"

req = urllib.request.Request(CoffeeURL)
requestData = json.loads(urllib.request.urlopen(req).read())

coffee:Coffee = Coffee(**requestData)

attemptedLetters = []

errors = 0


#Here im creating each step for the game
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

#Prints the first step, which is the start.
print(steps[0])

#This prints the random word selected but the letters are replaced with _.
print(len(coffee.blend_name)*"_")
print(coffee.blend_name)


#This function is filtering every other input that isn't a letter, making surethere are no numbers, symbols or that only 1 letter is selected, and will return an error until 1 letter is put in.
def input_function():
    while(True):
        letter = input("Input letter:")
        specialcharacter = "!@#$%^&*()+?_=,<>/"
        
        if(len(letter) != 1):
            print("Only type 1 letter")
            continue
        if (letter.isnumeric()):
            print("There are no numbers")
            continue
        if (letter in specialcharacter):
            print("Not a letter")
            continue

        # append to list of used letters
        attemptedLetters.append(letter)
        return letter

#This is the logic used for every correct letter, which verifies the inputed letter, and if it is right, it replaces the _s for the correct letter inputed. If it is wrong, then it will leave it as it is.
def printword():

    Temp:str = ""
    for letter in coffee.blend_name:
        if letter in attemptedLetters:
            Temp+= letter 
        else:
            Temp+= "_"
    print(Temp)
   

#This is the logic for every wrong letter. First it creates the variable "errors" to store the count for every wrong worc. Then, it verifies if the letter is wrong, and if it is, it will raise the errors count by 1 and print the next step.
#This will repeat until all 7 steps are passed, which will then say "GAME OVER" and reveal what the word was.
def printsteps():
    for letter in attemptedLetters:
        if letter not in coffee.blend_name:
            errors=errors+1
        if errors == 7:
            print("GAME OVER L + ratio, the word was:")
            print(coffee.blend_name)
            
    print(steps[errors])
       
while(True):
# get new word
# reset used letters

           
    #This is what keeps the game going and will repeat all loops until the game is over.
    while(True):
        input_function()
        printword()
        printsteps()
        if errors == 7:
            break

    



 



    

    

