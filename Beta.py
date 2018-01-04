from random import choice
lista=[]
x=input("Escriba el primer equipo ")
y=input("Escriba el segundo equipo ")
lista.append(x)
lista.append(y)
cosa=[1,2,3,4,5]
cosa2=[1,2,3,4,5]
resultado = choice(cosa)
resultado2=choice(cosa2)
First=choice(lista)
lista.remove(First)
second=choice(lista)
print( "El partido va a Terminar ",First,resultado, "-",resultado2, second )
