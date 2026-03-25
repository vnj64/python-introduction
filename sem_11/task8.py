def is_valid_triangle(side1: int, side2: int, side3: int) -> bool:
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        print(True)
    else:
        print(False)

print(is_valid_triangle(3, 3, 3))
n = is_valid_triangle(3, 3, 3)
print(n)