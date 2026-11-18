def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ValueError("Division by zero is not allowed.")
        return first_number / second_number
    raise ValueError("Invalid operator. Use +, -, *, or /.")


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Simple Calculator")
    print("Enter 'q' to quit.")

    while True:
        first_number = input("First number (or q): ").strip()
        if first_number.lower() == "q":
            break

        try:
            first_number = float(first_number)
        except ValueError:
            print("Please enter a valid number.")
            continue

        operator = input("Operator (+, -, *, /): ").strip()
        if operator.lower() == "q":
            break
        if operator not in {"+", "-", "*", "/"}:
            print("Invalid operator. Use +, -, *, or /.")
            continue

        second_number = read_number("Second number: ")

        try:
            result = calculate(first_number, operator, second_number)
            print(f"Result: {result}")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()