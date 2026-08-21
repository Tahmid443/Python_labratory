def main():
    history = []
    print("\n===========================================================\n============== Welcome to python calculator ===============\n===========================================================\n\nA help guide for you to use this program:\n1.To close this program enter 1 in operator\n2.Operator Details:\n\t'+' = sum\n\t'-' = difference\n\t'*' = multiplication\n\t'/' = division\n\t'%' = modulo\n\t'^' = power\n\nDo you want to use this calculator?\n1.Yes\n2.No")
    def add(a, b):
        return f"Sum of {a} and {b} is : {a+b}\n"
    def sub(a, b):
        return f"Subtraction of {a} and {b} is: {a-b}\n"
    def mul(a, b):
        return f"Multiplication of {a} and {b} is: {a*b}\n"
    def div(a, b):
        try:
            return f"Division of {a} and {b} is: {a/b}\n"
        except ZeroDivisionError:
            return "Cannot divide by zero (Undefined)\n"
    def mod(a, b):
        try:
            return f"Modulo of {a} and {b} is: {a%b}\n"
        except ZeroDivisionError:    
            return "Cannot perform modulo by zero (Undefined)\n"
    def power(a, b):
        return f"{a} to the power {b} is: {a**b}\n"
    def save_history(result):
        with open("history.txt", "a") as file:
            file.write(result)
    def show_history():
        try:
            with open("history.txt", "r") as file:
                history = file.read()

            if history:
                print("\n===== CALCULATION HISTORY =====")
                print(history)
            else:
                print("\nNo calculation history yet.")

        except FileNotFoundError:
            print("\nNo calculation history yet.")
        
    b = int(input())
    if b == 1:
        while True:
            operator = input(f"\n______________________________________________________\nEnter operator(+, -, /, *, ^, %)[Enter H to show history] [Enter 1 to exit]: ")
            if operator == "1":
                break
            if operator == "H" or operator == "h":
                show_history()
                continue
            try:        
                operand1 = float(input("Enter your first number: "))
                operand2 = float(input("Enter your second number: "))
            except ValueError:
                print("Invalid operand!")
                continue
                
            match operator:
                case "+":
                    result = add(operand1, operand2)
                    print(result)
                    history.append(result)
                    save_history(result)
                case "-":
                    result = sub(operand1, operand2)
                    print(result)
                    history.append(result)
                    save_history(result)
                case "*":
                    result = mul(operand1, operand2)
                    print(result)
                    history.append(result)
                    save_history(result)
                case "/":
                    result = div(operand1, operand2)
                    print(result)
                    history.append(result)
                    save_history(result)
                case "%":
                    result = mod(operand1, operand2)
                    print(result)
                    history.append(result)
                    save_history(result)
                case "^":
                    result = power(operand1, operand2)
                    print(result)
                    history.append(result)
                    save_history(result)
                case _:
                    print("Invalid operator!")
                
    elif b == 2:
        print("\nOK! Have a nice day!")
    else:
        print("\nInvalid input! Try '1' or '2'.")

if __name__ == "__main__":
    main()
