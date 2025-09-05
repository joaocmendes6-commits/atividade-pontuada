import os
os.system
("cls")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2


print(f"Média: {media:.2f}")


if media >= 6.0:
    print("Parabéns, você foi aprovado!")
elif 4.1 <= media <= 5.9:
    print("Você está em recuperação.")
else:  # media < 4.0
    print("Você foi reprovado.")