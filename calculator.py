print("     WELCOME TO MY CALCULATOR APP       ")
print("This program helps you do basic math operations.")
print("You can do multiple calculations until you choose to exit.\n")

continue_calc = True

while continue_calc:
    print("\n--- New Calculation ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers only!")
        continue 
    
    
    print("\nPlease choose an operation:")
    print("1. Addition (+)          - Adds two numbers")
    print("2. Subtraction (-)       - Subtracts second from first")
    print("3. Multiplication (*)    - Multiplies the numbers")
    print("4. Division (/)          - Divides first by second")
    print("5. Exit Program")
    
    choice = input("\nEnter your choice (1/2/3/4/5): ").strip()

    if choice == '1':
        result = num1 + num2
        operation_symbol = '+'
        print(f"\nResult: {num1} {operation_symbol} {num2} = {result}")
        
    elif choice == '2':
        result = num1 - num2
        operation_symbol = '-'
        print(f"\nResult: {num1} {operation_symbol} {num2} = {result}")
        
    elif choice == '3':
        result = num1 * num2
        operation_symbol = '*'
        print(f"\nResult: {num1} {operation_symbol} {num2} = {result}")
        
    elif choice == '4':
        if num2 == 0:
            print("\nError: Division by zero is not possible! Please try again.")
        else:
            result = num1 / num2
            operation_symbol = '/'
            print(f"\nResult: {num1} {operation_symbol} {num2} = {result:.4f}")  # showing 4 decimal places for division
    
    elif choice == '5':
        print("\nThank you for using my calculator! Goodbye 👋")
        continue_calc = False  # This will stop the loop
        break
        
    else:
        print("\nInvalid option selected! Please choose a number between 1 to 5.")
        continue 
  
    if continue_calc:
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again == 'no' or again == 'n':
            print("\nThank you for using the calculator. Have a great day!")
            continue_calc = False
        elif again != 'yes' and again != 'y':
            print("I didn't understand that. Assuming you want to continue...")


print("PROGRAM ENDED SUCCESSFULLY ")
