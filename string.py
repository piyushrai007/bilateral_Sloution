def rotate_string(s, k):
    k = k % len(s)
    
    if k == 0:
        return s
    
    rotated_string = ""
    for i in range(len(s)):
        rotated_string += s[(i + k) % len(s)]
    
    return rotated_string
a = input("Enter a string: ")
b = int(input("Enter a number by which you want to rotate a string: "))
print(rotate_string(a, b))

