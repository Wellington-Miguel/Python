qntPista, qntPessoas, qntAlunos=input().split()
qntPista=int(qntPista)
qntPessoas=int(qntPessoas)
qntAlunos = int(qntAlunos)
qntTotal = qntPista*qntPessoas
if(qntTotal>qntAlunos): print('S')
else: print('N')