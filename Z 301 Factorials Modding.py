a,b,m=map(int,input().split())
res=1
for i in range(b+1,a+1):
    res=(res*i)%m
print(res%m)
