# escreva um programa que leia o valor em metros e exiba convertido em centímetros e milímetros 


m = float(input("Digite o valor em metros: "))

print ("Em centímetros é: {:.0f}cm\nEm milímetros é: {:.0f}mm " .format(m * 100 , m * 1000))