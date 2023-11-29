"""
Author: Mark Dackus
Date: 26-11-2023
Script: for loop
"""
# Let op! Als je dit script voor de tweede keer runt krijg je een foutmelding
# omdat de bestanden al bestaan. Verwijder dan eerst de aangemaakte bestanden.
bestanden_aan_te_maken = ["read.me", "license", "app.js"]

for bestandsnaam in bestanden_aan_te_maken:
    print("Bestandsnaam: ", bestandsnaam)
    
    with open(bestandsnaam, 'w') as f:
        f.write('Dit is het bestand ' + bestandsnaam)

# for a in range(11):
#     print(a)