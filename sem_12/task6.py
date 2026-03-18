def count_words_by_length(text: str, n: int) -> int:
    arr = text.split()
    count = 0
    for i in arr:
        if len(i) == n:
            count += 1
    
    return count

print(count_words_by_length("привет я камиль", 6))