n = int(input())
l = sorted([int(input()) for _ in range(n)])
ll = l.copy()
s = []
while not s or (l and l[-1]*(len(s)+1) > min(s)*len(s)):
    s.append(l.pop())
while len(ll) > 1 and (len(ll)-1)*ll[1] >len(ll)*ll[0]:
    ll.pop(0)
print(max(len(s)*s[-1],len(ll)*ll[0]))


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