min,max = input().split()
min=int(min)
max=int(max)
controller=0
for index in range(min,max):
    for teste in range(2,index-1):
        if index%teste==0:
            break
        else:
             if (teste==index-1):
                controller+=1
            
        
        
            
