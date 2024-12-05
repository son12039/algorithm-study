n = int(input())
turn = sorted(list(map(int ,input().split())))
re= sum(i * (n-ii)for ii,i in enumerate(turn))
print(re)




