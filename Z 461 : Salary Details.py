from operator import itemgetter
n=int(input())
l=[]
for i in range(n):
    a,b=map(str,input().split())
    l.append([a,int(b)])
l.sort(key=itemgetter(1,0))
for i in l:
    print(*i)
