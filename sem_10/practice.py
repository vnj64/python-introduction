# print([input().lower() for _ in range(int(input()))])
# print(*[i**2 for i in range(10) if (i ** 2)%10 != 4], sep="\n")
# print(*[i**2 for i in range(1, int(input()) + 1)], sep="\n")
# lst = []

# for i in range(1, int(input())+1):
#     lst.append(i**2)

# sdkfjsd13123198ugegrnfdhu234y23g 82934uf!
# 131231982342382934
print(*[i for i in list(input()) if i.isdigit()], sep="")