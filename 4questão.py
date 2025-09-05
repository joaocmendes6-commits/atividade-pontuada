import os
os.system
("cls")

kg_morango = float(input("Digite a quantidade de morangos (kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (kg): "))


if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20


if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50


total = preco_morango + preco_maca


peso_total = kg_morango + kg_maca
if peso_total > 10 or total > 15.00:
    total *= 0.90  # aplica 10% de desconto


print(f"Valor a pagar: R$ {total:.2f}")
