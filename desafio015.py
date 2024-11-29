km = int( input ("Qual a quantidade de Km percorridos por um carro alugado? "))
dias = float(input("Por quantos dias? "))

carro = ( km * 60 ) + ( dias * 0.15)

print("O preço a ser pago pelo carro é R$ {:.2f}" .format(carro))