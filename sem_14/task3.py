def perfect_square(s):
    parts = s.split(",")
    if len(parts) != 4:
        return "invalid input"

    for part in parts:
        if not part.isdigit():
            return "invalid input"

    numbers = []
    for part in parts:
        numbers.append(int(part))

    for i in range(3):
        if numbers[i] + 1 != numbers[i + 1]:
            return "not consecutive"

    square = numbers[0] * numbers[1] * numbers[2] * numbers[3] + 1
    root = int(square ** 0.5)
    return [square, root]
