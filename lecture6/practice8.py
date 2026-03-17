def is_one_away(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1

    return diff == 1