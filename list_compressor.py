def compress_list(lst):
    compressed = []
    current_sum = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            current_sum += lst[i]
        else:
            compressed.append(current_sum)
            current_sum = lst[i]
    compressed.append(current_sum)
    return compressed
a =input("Enter a list of numbers separated by space: ")
lst = list(map(int, a.split()))
print(compress_list(lst))