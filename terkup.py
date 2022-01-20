# File: terkup.py
# Aurh: Délczeg Ádám
# copyright: 2021, Délczeg Ádám
# Group: Ifra I N
# Date: 2021-10-30
# Github: https://github.com/adam12033
# Licenc: GNU GPL

print("Délczeg Ádám, Ifra IN")
print("2021-10-30")
print("Feladat 0301")
print("Körlapú kúp térfogata")

import math

sugarStr = input("Sugár: ")
magassagStr = input("Magasság: ")

magassag = int(magassagStr)
sugar = int(sugarStr)

terfogat= 1/3*math.pow(sugar, 2) * math.pi * magassag

print("Térfogat: %.2f" % terfogat)
