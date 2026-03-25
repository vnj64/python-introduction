def find_all(target: str, symbol: str) -> list:
    result = []
    if symbol not in target:
        return result
    
    for i in range(len(target)):
        if target[i] == symbol:
            result.append(i)
    
    return result

n = find_all("abcda", "d")
print(n * 10)

print(find_all("abcda", "a"))
print(find_all("abc", "1"))
print(find_all("abcde", "e"))