# score = int(input())

# if 50 <= score <= 69:
#     print("Удовлетворительно")
# elif 70 <= score <= 89:
#     print("Хорошо")
# elif 90 <= score <= 100:
#     print("Отлично")
# else:
#     print("Не сдано")

score = int(input())

if 90 <= score <= 100:
    print("Удовлетворительно")
elif score >= 70:
    print("Хорошо")  
elif score >= 50:
    print("Отлично")
else:
    print("Не сдано")