from ast import Num


mm=0
dm=0
dam=0
hm=0
km=0
num=0
print("Bienvenido")
print("Digite el numero en centimetros:")
num=int(input())
mm=num*10
dm=num/10
dam=(dm/10)/10
hm=dam/10
km=hm/10
print("La conversion es igual a:" ,"milimetros",mm , "decimetros", dm,"decametros" ,dam, "hectometros",hm,"kilometros", km)
