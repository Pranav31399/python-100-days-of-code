operations_list=['+','-','*','/']

def sum(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def calculator():
    end_of_calculation=False

    operand1=float(input("What's the first number?: "))
    result=0
    while not end_of_calculation:
        for operator in operations_list:
            print(operator)

        operation=input("Pick an operation: ")
        
        if operation not in operations_list:
            print("Wrong operation. Program exited.")
            return
        
        operand2=float(input("What's the next number?: "))
        
        if operation=='+':
            result=sum(operand1,operand2)
        elif operation=='-':
            result=subtract(operand1,operand2)
            
        elif operation=='*':
            result=multiply(operand1,operand2)
            
        elif operation=='/':
            result=divide(operand1,operand2)
            
            
        operand1=result
            
        choice=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if(choice=='n'):
            end_of_calculation=True
            calculator()
            
calculator()
    
