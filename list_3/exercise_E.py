pressure = []
controller = True
text=''
while controller:
  pressure_now=input()
  if(pressure_now==0):break
  pressure.append(pressure_now)
limit=pressure[0]
for index in pressure:
  