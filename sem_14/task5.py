def word_value(arr):
    result = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(arr)):
        total = 0

        for letter in arr[i]:
            if letter != " ":
                total += alphabet.find(letter) + 1

        result.append(total * (i + 1))

    return result
