m1=int(input("Enter a marks of test 1 :"))
m2=int(input("Enter a marks of test 2 :"))
m3=int(input("Enter a marks of test 3 :"))
if m1<m2 and m1<m3:
    avg=(m2+m3)/2
elif m3<m2 and m3<m1:
    avg = (m2 + m1) / 2
else:
    avg=(m1+m3)/2
print("Aversge of three marks :",avg)