# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input("Digite um número: "))

# dobro = n * 2
# triplo = n * 3
# # rq = n**2
# rq = n ** (1/2)

print("Seu dobro é: {}\nSeu triplo é: {}\nSua raiz quadrada é: {:.0f}" .format(n * 2, n * 3, n ** (1/2)))
