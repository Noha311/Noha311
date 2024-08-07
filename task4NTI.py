class Calculation:
    
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

while True:
        print("="*30 + " HELLO TO MY 'Mini Calculator' " + "="*24)
        print("Please choose suitable option:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue
            
            if choice == '1':
                print(f"Result: {Calculation.add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {Calculation.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {Calculation.multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {Calculation.divide(num1, num2)}")
        else:
            print("Invalid choice. Please select a valid option.")


