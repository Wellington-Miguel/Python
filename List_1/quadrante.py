total, amigo_frente, amigo_direta, amigo_esquerda, amigo_tras = input().split()
amigos_total=int(amigo_frente) + int(amigo_direta) + int(amigo_esquerda) + int(amigo_tras)
inimigos_total=int(int(total)-amigos_total)
print(inimigos_total)