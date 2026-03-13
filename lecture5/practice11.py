arr = ["Kamil", "Maxim", "Alex"]
for i in range(len(arr)):
    # print(arr[i]) arr[i] - по сути является name на данном моменте
    for c in range(len(arr[i])):
        print(arr[i][c], end=" ")

name = "Kamil"
for c in range(len(name)):
    print(name[c])