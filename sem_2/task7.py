school_boys = int(input())
oranges = int(input())

print(f"Количество мандаринов, которое достанется каждому: {oranges // school_boys}")
print(f"Останется в корзине: {oranges % school_boys}")