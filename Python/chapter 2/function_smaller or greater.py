def bog(a,b) :
    if a > b :
        return "greater"
    elif a < b :
        return "smaller"
    else :
        return "maybe its equal or you didn't enter a number"

a = input("type the number a : ")
b = input("type the number b : ")

print(bog(a,b))
