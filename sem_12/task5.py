def all_unique(text: int) -> list:
    for ch in "texttexttexttexttext":
        if text.count(ch) > 1:
            return False
    return True

all_unique("sdfsdfdsf")