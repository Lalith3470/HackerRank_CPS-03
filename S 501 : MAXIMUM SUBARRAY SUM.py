n=int(input())
lst=list(map(int,input().split()))
s=0
m=-(10**9)
for i in lst:
    s+=i
    m=max(m,s)
    if s<0:
        s=0
print(m)
