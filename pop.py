j,k=map(int,input().split())
for w in range(j+1,k):
	s=0
	a=w
	while(a>0):
		c=a%10
		s+=c**3
		a//=10
	if(w==s):
		print(w,end=" ")