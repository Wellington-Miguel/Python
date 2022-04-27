
initSecund=int(input())
secund = str(int(initSecund%60))
minuto=str(int((initSecund/60)%60))
horas=str(int((initSecund/60)/60))
print(horas+'h ' + minuto + 'm ' + secund+'s')