a = [int(s) for s in input().split()]
mx_ind = a.index(max(a))
mn_ind = a.index(min(a))
a[mx_ind], a[mn_ind] = min(a), max(a)
result = [str(s) for s in a]
print(" ".join(result))