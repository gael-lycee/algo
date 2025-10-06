#boucle while avec variable et condition d'arrêt sur le solde d'un compte bancaire        scritpe 1

solde = 100


retrait = eval(input("Montant du retrait en euros : "))

while solde >= retrait:
    print("Retrait de", retrait, "euros.")

    solde = solde - retrait

    print("Solde restant :", solde, "euros.")

print("Solde insuffisant pour un nouveau retrait.")
