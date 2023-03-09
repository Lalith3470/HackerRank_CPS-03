s=input()
n=len(s)
if n==1:print(1)
else:
    m=10**9+7
    dp=[0]*(n+1)
    dp[0]=dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]%m
        if s[i-2]<="1" or (s[i-2]=="2" and s[i-1]<'6'):
            dp[i]=(dp[i]+dp[i-2])%m
    print(dp[n]%m)
