n:int=4
gasolina=[4,6,7,4]
distancia=[6,5,3,5]
for line in range(n):
    i=().split(" ")
    gasolina.append(int(i[0]))
    distancia.append(int(i[1]))
bal=[]
for i in range(n):
    bal.append(gasolina[i]-distancia[i])

small=0    
for strt in range(n):
    s=bal[strt]
    i=(strt+1)%n
    while(s>=0 and i!=strt): 
        s+=bal[i]    
        i=(i+1)%n
    if(i==strt):
        small=strt
        break
        
print(small)