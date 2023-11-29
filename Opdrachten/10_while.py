"""
Author: Mark Dackus
Date: 26-11-2023
Script: while
"""
tafel_van = 10
invoer_juist = False
while not invoer_juist:
    tafel_van_input = input("Van welk getal wil je het tafeltje: (tussen 1 en 100): ")
    if (tafel_van_input.isdigit()):
        tafel_van = int(tafel_van_input)
        invoer_juist = True

start = 0
while (start < 10):
    start = start + 1
    antwoord = start * tafel_van
    print(f"{start} x {tafel_van} = {antwoord}")