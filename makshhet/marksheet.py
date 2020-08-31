#A simple mark sheet by using if else
print("Enter marks of 5 subjects")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
#individually to checkout Pass or Fail
if a >= 33 and b >= 33 and c >=33 and d >= 33 and e >= 33:
    print("Result : PASS")
    per = (a+b+c+d+e)/5
    print("percentage: ", per)
    if per >= 80:
        print("GRADE A")
    elif per >= 70:
        print("GRADE B")
    elif per >= 60:
        print("GRADE C")
    else:
        print("GRADE D")
else:
    print("RESULT: FAIL")



