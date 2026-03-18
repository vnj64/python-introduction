def all_unique(text: str) -> bool:
    for ch in text:
        if text.count(ch) > 1:
            return False
    return True