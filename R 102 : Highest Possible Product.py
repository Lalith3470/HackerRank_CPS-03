import math
n=int(input())
lst=[]
while not lst:lst=list(map(int, input().split()))
lst.sort(reverse=True)
print(math.prod(lst[:3]))
