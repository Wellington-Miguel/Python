populacao = int(input())
amostra =[]
homem = 0
mulher =0
for pessoas in range(populacao):
    sexo= int(input())
    amostra.append(sexo)
for sexo in amostra:
    if (sexo ==1): 
        homem+=1
    else:
        mulher+=1
print(homem,'\n',mulher)
