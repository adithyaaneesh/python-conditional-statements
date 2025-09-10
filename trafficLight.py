# signal = ["red" , "green" , "yellow"]
signal = str(input("Enter the traffic light : "))

if (signal=="red"):
    print("Red for Stop")
elif(signal=="yellow"):
    print("Yellow for Get Ready")
elif(signal=="green"):
    print("Green for Go")
else:
    print("Enter valid values")