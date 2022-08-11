"""Restaurant rating lister."""

from ast import Or
import random
from re import X
from string import capwords

ratings_dictionary = {}
with open("scores.txt") as file:
    for line in file:
        (key, value) = line.strip().split(":")
        ratings_dictionary[key] = value


def show_current():
    for key, value in sorted(ratings_dictionary.items()):
        print(f"{key} : {value}")
    
show_current()

def what_do():
    check = input("Please select an option for the action you'd like to do:\n1 OR View - View all of the current restaurant's and their ratings\n2 OR Random - Choose a random restaurant from the list\n3 OR Add - Add a new restaurant\n4 OR Edit - Pick a store to edit it's rating\n5 OR Quit - Quit the application\n")
    check = check.lower()

    if check == '1' or check == 'view':
        show_current()        
        what_do()

    elif check == '2' or check == 'random':
        rando = random.choice(list(ratings_dictionary))
        print(f"The restaurant chosen is: \"{rando}\" and it's rating is: {ratings_dictionary[rando]}")
        print(f"{rando} : {ratings_dictionary[rando]}")
        update_rating = input("What would you like to change the rating to?\n")
        ratings_dictionary[rando] = str(update_rating)

        show_current()
        what_do()

    elif check == '3' or check == 'add':
        print("Please add another restaurant")
        new_store = input("What is the restaurant's name?\n")
        new_store = capwords(new_store)
        new_rating = input("What is the restaurant's rating? \n")

        if float(new_rating) < 0 or float(new_rating) > 5:
            print('The rating must be between 1 and 5. Let\'s start over.')
            what_do()
        elif float(new_rating) >= 0 and float(new_rating) <= 5:
            ratings_dictionary[new_store] = new_rating
            show_current()
            what_do()
        else:
            print("Something went wrong")

        show_current()
        what_do()

    elif check == '4' or check == 'edit':
        print("Please select the number correspoding to the store name.")
        for key in sorted(ratings_dictionary.keys()):
            print(f"{key}")

        change = input("Enter number here:\n")
        change = capwords(change)
        if change in ratings_dictionary:
            print(f"The current rating of {change} is: {ratings_dictionary[change]}")
            new_rating = input("What would you like to change the rating to?\n")

            if float(new_rating) < 0 or float(new_rating) > 5:
                print('The rating must be between 1 and 5. Let\'s start over.')
                what_do()

            elif float(new_rating) >= 0 and float(new_rating) <= 5:
                ratings_dictionary[change] = new_rating
                show_current()
                what_do()
            else:
                print("Something went wrong")



    elif check == '5' or check == 'quit' or check == 'exit':
        exit()

    else:
        print("Your input didn't match. Please type either \n1 or view --- 2 or random --- 3 or add --- 4 or quit")
        what_do()

what_do()