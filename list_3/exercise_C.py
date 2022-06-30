pacientes = []
result = []
controll = True
while controll:
    init, percent = input().split()
    percent=int(percent)
    if (init=='#' or percent==0): controll=False
    else: 
        pacientes.append(init)
        if (percent<90):
            result.append('Internar')
        else: result.append('Alta')
for x in range(len(pacientes)):
    final = '{} {}'
    print(final.format(pacientes[x], result[x]))