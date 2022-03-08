canal1=[15,9,3,3,1.2,1,4.5,5,5.2,5,6.5,7.4,7.2,8,11,10,18,20,23,25,28.1,28,25,23]
canal2=[16,9,1,2,1.8,1,5.5,6,7.2,6,5.5,7.4,7.9,9,10,11,19,20,24,29,28.8,27,26,25]

max=canal1[0]
c=1
h=0
perdidos=[]
for i in range(len(canal1)):
    if canal1[i]>max:
        max=canal1[i]
        c=1
        h=i
    if canal2[i]>max:
        max=canal2[i]
        c=2
        h=i
    if(canal1[i]<canal2[i]):
        perdidos.append(i)
print("maximo rating: ", max, "canal",c,"hora",h)
print("canal 1 perdio en los horarios", perdidos)
