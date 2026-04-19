num1 = float(input("Enter first number : "))
operator = input(" + , - , * , / ")
num2 = float(input("Enter second number : "))
if operator == "+" :
    result = num1 + num2
elif operator == "-" :
    result = num1 - num2
elif operator == "*": 
    result = num1 * num2 
elif operator == "/": 
    result = num1 / num2
else :
    print("result")
    #program that prints square root
import math # square root of a number 
num3 = float(input("Enter number : "))
Result = math.sqrt(num3)
print(Result)
import random # random number btw 1 and 100
num4 = random.randint(1, 100)
print (num4) 
