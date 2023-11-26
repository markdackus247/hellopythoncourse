"""
Author: Niels Peters
Date: 13-11-2023
Script: Functie om het cijfer te berekenen
"""
# Deze functie berekent een cijfer en geeft dit terug.
# Je geeft het aantal behaalde punten en het maximaal aantalpunten mee.
def calculate_grade( aantal_behaalde_punten, max_aantal_punten ):
    # Minimaal cijfer is een 1.
    # Hier wordt het cijfer berekend.
    cijfer = ( 9 * aantal_behaalde_punten ) / max_aantal_punten + 1
    # Hier wordt het cijfer terug geven aan de aanvrager.
    return cijfer

# Hier wordt het cijfer berekent van een student die 37 punten behaald heeft.
# Het maximaal aantal punten is 40. Hij heeft dus 37 van de 40 punten behaald.
# Hij heeft een 9.325 behaald.
behaald_cijfer = calculate_grade(37, 40)

# Hier wordt het cijfer afgedrukt met de functie print().
# Maar het cijfer wordt eerst nog afgerond op 1 decimaal met de functie round()
print(round(behaald_cijfer, 1))
 