def search(l,i):
    lo=0
    hi=len(l)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if l[mid]==i:
            return 1
        elif l[mid]<i:
            lo=mid+1
        else:
            hi=mid-1
    return 0
    
n=int(input())
l=list(map(int, input().split()))  
l.sort()
m=int(input())
ls=list(map(int,input().split()))
for i in ls:
    if search(l,i):print("Happy Halloween!")
    else:print("Tricky!")
