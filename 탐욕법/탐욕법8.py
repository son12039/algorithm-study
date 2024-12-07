n = int(input())
l = sorted([int(input()) for _ in range(n)], reverse=True)
re = 0
for index,i in enumerate(l):
    re = max(re,i * (index+1))
print(re)

"""
3
10
11
60
//
4
3
3
3
2217
"""