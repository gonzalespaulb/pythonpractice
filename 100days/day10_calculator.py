operation_type = input("What operation to perform?\n+\n-\n/\nx\n")

def operation (first_num, second_num): 

    if operation_type == "+":
        return first_num + second_num
    if operation_type == "-":
        return first_num - second_num
    if operation_type == "/":
        return first_num / second_num
    if operation_type == "x":
        return first_num * second_num    
    
first_num = int(input("Enter first number.\n"))
second_num = int(input("Enter second number.\n"))
    
while True: 

    result = operation(first_num, second_num)

    print(result)
    
    continue_operation = input("Would you like to continue further? y or n\n").lower()

    if continue_operation == "y": 
        operation_type = input("What operation to perform?\n+\n-\n/\nx\n")
        first_num = result
        second_num = int(input("Enter a number.\n"))
        continue
    else: 
        break