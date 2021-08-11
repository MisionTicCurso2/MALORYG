

print("Hola buenas tarde le escribimos por parte de la omg y que queremos sabeer su masa corporal , a continuacion escribira su peso actual ")

mensaje_Entrante = input()

resPeso = int(mensaje_Entrante)
print("su altura")
mensaje_Entrante = input()
resPesoAltura =  resPeso / float(mensaje_Entrante)

print ("su masa corporal" , resPesoAltura)

intervaloN = 24.9 
sobrePeso = 25.0


if(intervaloN >= 24.9 and sobrePeso == 25.0):

  print ("masa corporal estado normal")

else:
   print("El usuario tiene sobrepeso")
   



 