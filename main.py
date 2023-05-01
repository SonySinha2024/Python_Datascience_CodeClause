## CodeClause
## Python Development Intern
## Calculator in Python

## Calculator(Add,Subtract,Multiply,Divide,Percentage,Sum of Squares)

## Creating functions for operations

## Creating function to add
def add(x,y):
    return x + y

## Creating function to subtract
def subtract(x,y):
    return x - y

## Creating function to multiply
def multiply(x,y):
    return x * y 

## Creating function to divide
def divide(x,y):
    return x / y

## Creating function to calculate percentage
def percentage(x,y):
    return x*100/y

def SumofSuaresofEachNumber(x,y):
    return x + y

## Operation Options

print("Select operation user want to opt")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")
print("5: Percentage")
print("6: Sum of Squares of each number")

## Taking input(choice) from the user

while True:
    operation = input("Enter the Choice from the user(1/2/3/4/5/6):")
        
## Checking if one of the Options

    if operation in ('1','2','3','4','5','6'):
        try:
            FirstNumber =float(input("Enter First number:"))
            SecondNumber =float(input("Enter Second number:"))
        except ValueError:
            print("Invalid entry, Enter a number:")

## Operation Choices
        if  operation == "1":
            print ("FirstNumber",FirstNumber,"added to(+)","SecondNumber",SecondNumber,"The result is =" ,add(FirstNumber,SecondNumber))
        
        elif  operation == "2":
            print ("FirstNumber",FirstNumber, "Subtracted(-)" ,"SecondNumber",SecondNumber, "The result is =",subtract(FirstNumber,SecondNumber))
        
        elif  operation == "3":
            print ("FirstNumber",FirstNumber, "multipled(*)" ,"SecondNumber",SecondNumber, "The result is =", multiply(FirstNumber, SecondNumber))
        
        elif  operation == "4":
            print("FirstNumber",FirstNumber, "divided by(/)", "SecondNumber",SecondNumber , "The result is =", divide(FirstNumber,SecondNumber))
            
        elif operation =='5':
                print("FirstNumber",FirstNumber, "is",percentage(FirstNumber,SecondNumber), "percent(%) of", "SecondNumber",SecondNumber)
        elif operation == '6':
            print ("FirstNumber",FirstNumber," squared and added to(+)","SecondNumber",SecondNumber,"The result is =" ,SumofSuaresofEachNumber(FirstNumber*FirstNumber,SecondNumber*SecondNumber))
                
