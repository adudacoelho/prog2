def main():
    salario = float(input( "Qual o seu salário: " ))
    
    aumento = 15*salario / 100

    nsalario = salario + aumento
    
    print ("Seu novo preço, com 15% de aumento é: {:.0f}." .format(nsalario))
    
main()
