#!/Users/sunnypark/anaconda3/bin/python3

import os

os.environ["FAV_RESTAURANT"] = "Taco Bell"
os.environ["FAV_SONG"] = "Crybaby"
os.environ["BIRTH_MONTH"] = "June"

FAV_RESTAURANT = input('What is your favorite restaurant?')
FAV_SONG = input('What is your favorite song?')
BIRTH_MONTH = input('What is your birth month?')

os.environ["USER_FAV_RESTAURANT"] = FAV_RESTAURANT
os.environ["USER_FAV_SONG"] = FAV_SONG
os.environ["USER_BIRTH_MONTH"] = BIRTH_MONTH

print(os.getenv("USER_FAV_RESTAURANT"))
print(os.getenv("USER_FAV_SONG"))
print(os.getenv("USER_BIRTH_MONTH"))
