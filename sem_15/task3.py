def ideal_number(st: str) -> list:
    result = []
    explic = 0

    splited = st.split(",")

    if len(splited) != 4:
        return "invalid input"

    for i in range(len(splited)):
        splited[i] = int(splited[i])
    
    for i in range(len(splited) - 1):
        if int(splited[i]) + 1 != int(splited[i+1]):
            return "not consecutive"
    
    explic = (splited[0] * splited[1] * splited[2] * splited[3]) + 1    
    result.append(explic)
    result.append(explic ** 0.5)
    return result

print(ideal_number("1,2,3,4"))