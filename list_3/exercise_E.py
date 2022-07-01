pressure = []
controller = True
text=''
while controller:
  pressure_now=input()
  pressure_now=int(pressure_now)
  if(pressure_now==0):break
  pressure.append(pressure_now)

for index in pressure:
  if index > pressure[0]:
    text='ALARME'
  else: text='O Havai pode dormir tranquilo'