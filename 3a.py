s = input("Enter the sentence: ")
w = d = u = l = 0

x = s.split()
w = len(x)

for i in s:
    if i.isdigit():
        d += 1
    elif i.isupper():
        u += 1
    elif i.islower():
        l += 1

print("Number of words:", w)
print("Number of digits:", d)
print("Number of uppercase letters:", u)
print("Number of lowercase letters:", l)