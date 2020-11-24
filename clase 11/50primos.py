def primo(n):
	primo = True
	if(n<2):
		primo=False
	i=2
	while(primo and i<(n//2)+1):
		if(n%i==0):
			primo=False
		i=i+1
	return primo

n=50

i=1
primos=[]

cant=0
while (cant <=n):
	if (primo(i)):
	   primos.append(i)
	   cant=cant+1
	i=i+1

print(primos)