# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/11/30
# Gets the input for a symbol and two numbers,
# Then uses an IF..ELSE statement to calculate
# The two numbers with the symbol. Uses functions
# And parameters with different types to do this.


# Function to make the different calculations
def calculate(symbol, number_1, number_2):
    # Setting the calculation answer to 0
    calculation = 0

    # IF ELSE statement to determine the type of calculation based on the symbol
    if symbol == "+":
        calculation = number_1 + number_2
    elif symbol == "-":
        calculation = number_1 - number_2
    elif symbol == "*":
        calculation = number_1 * number_2
    elif symbol == "/":
        calculation = number_1 / number_2
    elif symbol == "%":
        calculation = number_1 % number_2
    else:
        print("Please enter a valid symbol!")
    # Returning the calculation back to main() to be then displayed
    return calculation


def main():

    # Title of the program
    print("Calculator\n")

    # User Input for the symbol and two numbers
    symbol_user_input = input("Enter your symbol (+,-,*,/,%):")
    number_user_input_1_string = input("Enter your first number: ")
    number_user_input_2_string = input("Enter your second number: ")

    # Try Catch to make sure the input is valid
    try:
        number_user_input_1 = float(number_user_input_1_string)
        number_user_input_2 = float(number_user_input_2_string)
    except Exception:
        print("Please enter a valid number!")
    else:
        # IF ELSE to make sure the symbol input is valid
        if (
            symbol_user_input == "+"
            or symbol_user_input == "-"
            or symbol_user_input == "*"
            or symbol_user_input == "/"
            or symbol_user_input == "%"
        ):
            answer = calculate(
                symbol_user_input, number_user_input_1, number_user_input_2
            )
            # Displaying the answer*
            print(
                "{} {} {} = {}".format(
                    number_user_input_1, symbol_user_input, number_user_input_2, answer
                )
            )
        else:
            print("Please enter one of those 5 symbols!")


if __name__ == "__main__":
    main()
