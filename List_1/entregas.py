import math

kmTotal, pedagio = input().split() 
kmValor, pedagioValor = input().split()
kmTotal= int(kmTotal) 
pedagio= int(pedagio) 
kmValor= int(kmValor) 
pedagioValor= int(pedagioValor) 
valorTotal= int((kmTotal*kmValor)+(math.floor(kmTotal/pedagio)*pedagioValor))
print(valorTotal)
