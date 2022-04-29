a= int(input())
b= int(input())
c= int(input())
soma1= b+c
soma2= a+c
soma3= a+b
sub1= b-c
sub2= a-c
sub3= a-b
if(sub1<a and a<soma1):
    if(sub2<b and b<soma2):
        if(sub3<c and c<soma3): print('Forma triangulo')
        else:print('Nao forma triangulo')
    else:print('Nao forma triangulo')
else: print('Nao forma triangulo')
