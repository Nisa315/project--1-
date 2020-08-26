#function:
def add():
    a = int(input("Enter 1st number"))
    b = int(input("Enter 2nd number "))
    c = a + b
    print("\n\tResult =", c)

 
def sub():
    a = int(input("Enter 1st number"))
    b = int(input("Enter 2nd number"))
    c = a + b
    print("\n\tResult =", c)

def mul():
    a = int(input("Enter 1st number"))
    b = int(input("Enter 2nd number"))
    c = a + b
    print("\n\tResult =", c)

def div():
    a = int(input("Enter 1st number"))
    b = int(input("Enter 2nd number"))
    c = a + b
    print("\n\tResult =", c)

print("\n----------------")
print("\n* Menu *")
print("* Menu *")
print("------------------")
print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Division")
print("5.Exit")
print("---------------")

choice = int(input("Enter your choice"))

if choice == 1:
    add()
elif choice == 2:
    sub()
elif choice == 3:
    mul()
elif choice == 4:
    div()
elif choice == 5:
    exit()
else:
    print("\n!!! Please select a choice from given options !!!")



