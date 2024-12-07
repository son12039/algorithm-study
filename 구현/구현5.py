n,m = map(int,input().split())
s = int(input())
ck = [[] for _ in range(n)]
print(ck)
re = []
t = 0
for _ in range(m):
    x,y = map(int,input().split())
    print(x,y,"시작")
    if not ck[x-1] and y == 1:
        print("없네")
        ck[x-1] = t
    elif not ck[x-1] and y == 0:
        print("있네")
        print(ck[x-1] , s , t)
        if ck[x-1] and ck[x-1] + s <= t:
            re.append(x) 
        else :
            ck[x-1] = None
        t += 1
print(ck)
for i,ii in enumerate(ck):
    if ii:
        print(i+1,"엑")
