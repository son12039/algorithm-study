import heapq
import sys
plus = []
minus = []
data = sys.stdin.read().splitlines()
result = []
for i in range(1,int(data[0])+1):
    a = int(data[i])
    if a > 0:
        heapq.heappush(plus, a)
    elif a < 0:
        heapq.heappush(minus, -a)
    else:
        if not plus and not minus:
            result.append("0")
        elif not plus:
            result.append(str(-heapq.heappop(minus)))
        elif not minus:
            result.append(str(heapq.heappop(plus)))
        elif plus[0] >= minus[0]:
            result.append(str(-heapq.heappop(minus)))
        else:
            result.append(str(heapq.heappop(plus)))
            
sys.stdout.write("\n".join(result) + "\n")
