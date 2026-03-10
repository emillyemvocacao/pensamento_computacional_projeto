print('Qual a sua idade?')


idade = int(input())

if idade <= 18:
    print('Você é menor de idade')

elif idade <= 65:
    print('Você é adulto')

else: 
    print('Você é idoso')