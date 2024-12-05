n,m = map(int, input().split())
l = sorted([int(input()) for _ in range(n)], reverse=True)
c = 0
for i in l:
    c += m//i
    m %= i
    if m == 0:
        print(c)
        break

