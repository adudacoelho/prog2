def main():

    km = float(input("Qual a quantidade de km percorridos pelo carro? "))
    dias = int(input("Qual a quantidade de dias pelo qual ele foi alugado? "))

    preço = (60 * dias) + (0.15 * km)

    print("O total a pagar é de R${:.2f}" .format(preço))
    
main()
