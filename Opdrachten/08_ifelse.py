"""
Author: Mark Dackus
Date: 26-11-2023
Script: if else
"""
import random

a = random.randint(0, 10)
b = random.randint(0, 10)

print("Getal a: ", a)
print("Getal b: ", b)

if (a > b):
    print("Cijfer b is hoger a.")
else:
    print("Cijfer b is lager a.")

c = random.uniform(0, 10)
c = round(c, 1)
c_is_het_kleinste = True

print("Getal c: ", c)

if (c > a):
    print("c is groter dan a")
    c_is_het_kleinste = False

if (c > b):
    print("c is groter dan b")
    c_is_het_kleinste = False

if (c == a) and (c == b):
    print("Alle getallen zijn hetzelfde")
