n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst1=list(map(int,input().split()))
lst.sort()
l=[]
for i in lst1:
    c=0
    for j in range(n):
        if lst[j]<=i:c+=1
        else:break
    l.append(c)
print(*l)
