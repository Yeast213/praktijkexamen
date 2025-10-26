# Berekener:
def pensioenBerekener(leeftijd,werkstatuut):
    lijst = [ # Lijst met alle data voor werkstatuuten en bedragen:
        {
            "medewerker": "350",
            "zelfstandige": "300",
            "ambtenaar": "370"
        },
        {
            "medewerker": "370",
            "zelfstandige": "320",
            "ambtenaar": "390"
        }
    ]
    if leeftijd>69: # Extra pensioen:
        dictionary = lijst[1]
        bedrag = dictionary[werkstatuut]
        uitvoer = (f"Je krijgt € {bedrag} per week.")
    else: # Standaard pensioen:
        if leeftijd>64:
            dictionary = lijst[0]
            bedrag = dictionary[werkstatuut]
            uitvoer = (f"Je krijgt € {bedrag} per week.")
        else: # Geen pensioen:
            tijdTotPensioen = 65 - int(leeftijd)
            uitvoer = (f"Van werken word je gelukkig, je mag nog {tijdTotPensioen} jaar genieten van je baan.")
    return uitvoer
# Invoer:
leeftijd = int(input("Wat is je leeftijd? "))
werkstatuut = input("Wat is je werkstatuut? ")
print(pensioenBerekener(leeftijd,werkstatuut))