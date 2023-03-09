def val(lst,k):
    lo=0
    hi=len(lst)-1
    while lo<=hi:
        mid=(hi+lo)//2
        if lst[mid]==k:
            return 1
        elif lst[mid]>k:hi=mid-1
        else:lo=mid+1
    
n=int(input())
lst=list(map(int,input().split()))
k=int(input())
lst.sort()
c=0
for i in lst:
    if val(lst,k-i):c+=1
print(c)
