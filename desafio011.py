# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintar sabendo que cada litro de tinta pint auma área de 2m quadrados 


l = float(input("Qual a largura em metros? "))
h = float(input("Qual a altura em metros? "))

area = (l * h)  

tinta = area / 2 

print ("A quantidade de tinta necessária para pintar a sua parede é {:.1f}" .format(tinta))

