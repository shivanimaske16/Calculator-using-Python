def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error!Division by zero."
    else:
        return x/y
def exit_all():
    print("Exit the Calculator")
    exit()

ch={'1':add,'2':subtract,'3':multiply,'4':divide,'5':exit_all}

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")

while True:
    choice=input("Enter Your choice: ")

    if choice in ch:
        if choice=='5':
            ch[choice]()
        else:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))

            result= ch[choice](num1, num2)
            print("Result:",result)
    else:
        print("Invalid Input")
