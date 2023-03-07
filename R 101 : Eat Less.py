n=int(input())
lst=[]
while not lst:lst=list(map(int, input().split()))
c=0
val=0
for i in sorted(lst,reverse=True):
    c+=(2**val)*i
    val+=1
print(c)
