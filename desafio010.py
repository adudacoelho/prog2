# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar considere $ 1 dólar = R$ 3,27
d = float(input("Quanto money do you have na carteira? R$ "))

cd = ( d / 3.27)

print ("Você pode comprar $ {:.2f} dólares com esse dinheiro." .format(cd))
