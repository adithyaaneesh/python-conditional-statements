a=int(input("Enter num1 : "))
b=int(input("Enter num2 : "))
result=input("Enter the operator '+','-','*','/': ")

if (result=='+'):
    print(f"{a+b}")
elif (result=='-'):
    print(f"{a-b}")
elif (result=='*'):
    print(f"{a*b}")
elif (result=='/'):
    print(f"{a/b}")
else:
    print("Hey Fool..!! Enter valid operator")