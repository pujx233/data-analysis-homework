num = int(input())
m = list(map(int, input().split()))
max_m = max(m)
min_m = min(m)
index_1 = m.index(max_m)
index_2 = m.index(min_m)
tmp = abs(index_1 - index_2)
print(tmp + max(min(index_2, index_1), num - max(index_2, index_1) - 1))
