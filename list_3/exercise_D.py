enemy = input()
enemy=int(enemy)
base=2
text =''
controller = True
while controller:
  base = base*2
  if (base==enemy):
    text='Dattebayo'
    controller=False
    break
  elif (base>enemy): 
    text='Tururuuu'
    controller = False 
    break
print(text)