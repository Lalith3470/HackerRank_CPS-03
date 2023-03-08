n=int(input())
lst=list(map(int, input().split()))
i=0
puca=garu=0
while len(lst)>1:
    mx=max(lst[i],lst[-1])
    puca+=mx
    if lst[i]==mx:
        lst=lst[1:]
    else:lst.pop()
    mx2=max(lst[i],lst[-1])
    garu+=mx2
    if mx2==lst[i]:
        lst=lst[1:]
    else:lst.pop()
if lst:puca+=lst[0]
if puca>=garu:print("Pucca")
else:
    print("Garu")
