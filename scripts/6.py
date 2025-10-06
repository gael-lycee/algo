jour = 1
total_jours = 5

while jour <= total_jours:
    print(f"Jour :  {jour}")

    if jour == 3:
        meteo = "pluie"

    elif jour == 5:
        meteo = "nuageux"

    else:
        meteo = "ensoleillé"



    if meteo == "pluie":
        print("  Il pleut, l'élève révise à la maison.")

    elif meteo == "ensoleillé":
        print("  Il fait beau, l'élève révise dans le jardin.")

    else:
        print("  Il fait nuageux, l'élève révise à la bibliothèque.")

    for lecon in range(1, 4):
        print("    → Leçon", lecon, "révisée.")


        
    jour += 1

print("Toutes les révisions sont terminées !")
