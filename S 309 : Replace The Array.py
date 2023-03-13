n=int(input())
ar=list(map(int,input().split()))
dp=[0]*n
mx=0
for i in range(n-1,-1,-1):
    dp[i]=mx
    mx=max(mx,ar[i])
print(*dp)
