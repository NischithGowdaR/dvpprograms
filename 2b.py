def bin2dec(n):
    return int(n, 2)

def oct2hex(n):
    return hex(int(n, 8))

bnum = input("Enter a binary number: ")
b2d = bin2dec(bnum)
print("Decimal number is:", b2d)

onum = input("Enter an octal number: ")
o2h = oct2hex(onum)
print("Hexadecimal number is:", o2h)