n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
l.sort(key=lambda x:(x[1],x[0]))
re = 0
a = 0
for i in l:
    if a <= i[0]:
        a = i[1]
        re +=1
print(re)
 



"""
4
2 5
3 3
4 4
5 6
3
4 4
3 4
2 4
 """