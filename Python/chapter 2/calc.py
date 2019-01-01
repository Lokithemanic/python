print ("Welcome to MyCalc Version 0.20")
print ("")

a = input("Enter first digit: ")

b = input("Enter Second digit: ")

c = input("Choose one of the maths operation: ")
    #1 + for Addition
    #2 - for Substration
    #3 * for Multiplition
    #4 / for Division")

if c == "+" :
    result = float(a) + float(b)

elif c ==  "-" :
    result = float(a) - float (b)

elif c == "*" :
    result = float(a) * float(b)

elif c == "/" :
    result = float(a) / float(b)

else :
    print ("Entered value is not valid")
    print ("Try again.")

print (result)

print ("see you later")
