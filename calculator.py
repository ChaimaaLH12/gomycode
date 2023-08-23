def calculator(num1,num2):
  while True:
    o =  input("Enter the operator (+, -, *, /): ")
    if o == "+" :
        return sum(num1,num2) 
    elif o == "*" :
        return num1 * num2 
    elif o == "-":
        return num1-num2
    elif o == "/":
        if num2 == 0 :
            print("You can't divide by zero !")
        else :
            return num1 / num2
    else :
        print("invalid operators")

print(calculator(3,0))
