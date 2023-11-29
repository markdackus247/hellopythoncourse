"""
Author: Mark Dackus
Date: 26-11-2023
Script: Arrays
"""
cijfers_rekenen = [5.1, 8.3, 7.2, 8.1, 5.2, 9.3]
aantal_cijfers_rekenen = len(cijfers_rekenen)

cijfers_rekenen.append(5.3)
cijfers_rekenen.append(6.4)

aantal_cijfers_rekenen = len(cijfers_rekenen)

gemiddelde_rekenen = sum(cijfers_rekenen) / len(cijfers_rekenen)
gemiddelde_rekenen_een_decimaal = round(gemiddelde_rekenen, 1)

print(f"Gemiddelde: {gemiddelde_rekenen_een_decimaal}")