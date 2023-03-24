n,k=map(int,input().split())
a=list(map(int, input().split()))
d=[0]*k
for i in a:
    d[i%k]+=1
c=(d[0]*(d[0]-1))//2
for i in range(1,k//2+1):
    if i!=k-i:
        c+=d[i]*d[k-i]
if k%2==0:
    c+=d[k//2]*(d[k//2]-1)//2
print(c)
