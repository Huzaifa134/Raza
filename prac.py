# print("hello world")
# a = input("enter you marks")
# print(a)
# b = type(a)
# print(b)
c = int(input("enter your marks"))
b = (c/100)*100
print('your percentage is :', b, "%")
if c >= 50:
    print('your grade is B')
elif c == 50:
    print('your grade is C')
elif c >= 70:
    print("Your Grade is A")
elif c >= 80:
    print("Your Grade is A-one")
else:
    print("You are failed")
