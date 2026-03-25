def solve(st: str) -> str:
    l_count = 0
    u_count = 0

    result = ""
    for i in st:
        if i.isupper() == True:
            u_count += 1
        else:
            l_count += 1
    
    for i in range(len(st)):
        if l_count > u_count:
            if st[i].isupper():
                result += st[i].lower()
            else:
                result += st[i]
    
        if l_count < u_count:
            if st[i].islower():
                result += st[i].upper()
            else:
                result += st[i]

        if l_count == u_count:
            result += st[i].lower()

    return result

print(solve("coDe"))
print(solve("CODe"))
print(solve("COde"))