#Peça ao usuário que digite seu peso e altura e imprima o IMC (Índice de Massa Corporal).

peso = int(input("digite seu peso"))

altura = float(input("digite a sua altura"))

imc = (peso / (altura * altura))

print(f"seu IMC é {imc}")