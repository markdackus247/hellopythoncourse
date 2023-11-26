"""
Author: Mark Dackus
Date: 26-11-2023
Script: Arrays
"""
import os
import datetime

# Haal de datum en tijd van vandaag op en sla deze op in de variable today.
vandaag_datumtijd = datetime.date.today()

# Verander het formaat naar YYYY-MM-DD. Sla
# Bijvoorbeeld 2023-11-26
vandaag_datum = vandaag_datumtijd.strftime("%Y-%m-%d")

gebruiker = {
    "username": "administrator",
    "firstname": "Gerard",
    "lastname": "Hoeven",
    "creationDate": vandaag_datum
}

print("Gebruikersnaam: ", gebruiker["username"])
print("Voornaam: ", gebruiker["firstname"])
print("Achernaam: ", gebruiker["lastname"])
print("Aanmaakdatum: ", gebruiker["creationDate"])

gebruiker["username"] = "admin"
print("Nieuwe gebruikersnaam: ", gebruiker["username"])