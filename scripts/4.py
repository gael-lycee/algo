#boucle for scripte 2

a=eval('entrer un nombre : ')
b=int(input('entrer un nombre entier : '))
c=int(input('entrer un autre nombre entier : '))

for i in range (b,c):
  a=a**7
  a=a+i

print(a)
