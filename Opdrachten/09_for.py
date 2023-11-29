"""
Author: Mark Dackus
Date: 26-11-2023
Script: for loop
"""
bestanden_aan_te_maken = ["read.me", "license", "app.js"]

for bestandsnaam in bestanden_aan_te_maken:
    print("Bestandsnaam: ", bestandsnaam)
    
    with open(bestandsnaam, 'w') as f:
        f.write('Dit is het bestand ' + bestandsnaam)

# for a in range(11):
#     print(a)