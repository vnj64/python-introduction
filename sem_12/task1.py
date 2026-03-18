def find_all(target: str, symbol: str) -> list:
    result = []
    for i in range(len(target)):
        if target[i] == symbol:
            result.append(i)
    return result

print(find_all("abcdeabclka1231231a", "a"))