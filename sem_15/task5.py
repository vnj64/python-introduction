alphabet = "abcdefghijklmnopqrstuvwxyz"

def sym_sum(arr: list) -> list:
	result = []
	for i in range(len(arr)):
		count = 0
		print(arr[i])
		for sym in arr[i]:
			print(sym)
			ind = alphabet.index(sym)
			count += ind+1
		result.append(count*(i+1))
	return result

print(sym_sum(["abc", "a b c", "a", "b", "c"]))
