peixes=int(input())
preco=int(input())
total=preco*peixes
if(total < 500 ):print('Paciencia Firmino!')
elif(total >= 500 and total < 1800):print('Vara de Bambu')
elif(total >= 1800 and total < 7500):print('Vara de Fibra de Vidro')
elif(total >= 7500):print('Vara de Iridio')