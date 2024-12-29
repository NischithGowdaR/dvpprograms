count = 0
num = int(input("Enter a number: "))
val = str(num)
rev = val[::-1]

if val == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

for i in range(10):
    if val.count(str(i)) > 0:
        print(f"{str(i)} appears {val.count(str(i))} times")