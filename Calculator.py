def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)


def main():
    print("Welcome to the Python Calculator!")
    print("Enter an expression or type 'quit' to exit.")

    while True:
        expression = input(">>> ")

        if expression.lower() == 'quit':
            print("Goodbye!")
            break

        result = calculate(expression)
        print("Result:", result)


if __name__ == "__main__":
    main()
    
