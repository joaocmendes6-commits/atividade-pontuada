import os
os.system ("cls")

nome=input("digite seu nome: ")
sexo=input("digite seu sexo (M/f): ").upper()
estado_civil=input("digite seu estado civil: ").upper()
tempo_casada=input("digite tempo_casada: ")

if sexo =="f" and estado_civil() == "casada":
    tempo_casada=int(input)("digite o tempo_casada (em anos, (apenas numeros: ")

else:
 tempo_casada= None


 print("nome", nome)
 print("sexo", sexo)
 print("estado_civil", estado_civil)

 if tempo_casada is not None:
     print("tempo_casada", tempo_casada,"anos: "() )

 