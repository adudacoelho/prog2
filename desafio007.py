#desevolva um programa que leia as duas notas de um aluno, calcule e mostre a sua 

n1 = float(input("Digite a sua nota: "))
n2 = float(input("Digite a sua segunda nota: "))

soma = n1 + n2

média = soma // 2

print ("Sua média é: {:.1f}" .format(média))