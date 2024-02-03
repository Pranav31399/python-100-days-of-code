def sum(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations_list=['+','-','*','/']

end_of_calculation=False

operand1=int(input("What's the first number?: '"))
result=0
while not end_of_calculation:
    for operator in operations_list:
        print(operator)

    operation=int(input("Pick an operation: "))
    operand2=int(input("What's the next number?: '"))
    
    if operation=='+':
        result=sum(operand1,operand2)
    elif operation=='-':
        result=subtract(operand1,operand2)
        
    elif operation=='*':
        result=multiply(operand1,operand2)
        
    else:
        result=divide(operand1,operand2)
        
    operand1=result
        
    choice=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if('n'):
        end_of_calculation=True
    
