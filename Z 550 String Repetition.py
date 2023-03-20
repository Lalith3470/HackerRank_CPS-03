s=input()
ln=len(s)
st=""
for i in range(len(s)//2+1):
    st+=s[i]
    x=st*(len(s)//(i+1))
    if x==s:print(st);exit()
print(s)
