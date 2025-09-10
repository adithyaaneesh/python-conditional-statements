# Using nested if

a=293
b=151
c=632

if a>b:
    if a>c:
        print(f"{a} is greater")
    else:
        print(f"{c} is greater")
else:
    print(f"{b} is greater")

# Using if elif else

a=23
b=15
c=87
if a>b and a>c:
    print(f"{a} is greater")
elif b>a and b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")
