n=int(input())
lst=list(map(int,input().split()))
mx=0
c=0
for i in lst:
    if i==1:c+=1
    else:
        mx=max(mx,c)
        c=0
if c:mx=max(mx,c)
print(mx)
