import sys,os,signal
from calculator_art import logo

# Function to handle the CTRL+C signal
def signal_handler(sig, frame):
    print("\nCTRL+C detected. Exiting gracefully...")
    # Add any cleanup code or actions you want to perform before exiting.
    sys.exit(0)

# Set the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def divide(n1,n2):
    return n1 / n2
def multiply(n1,n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def start_calculations():
    clear_console()
    print(logo)
    number_1 = float(input("What's the first number?: "))
    continue_operating = 0
    while continue_operating == 0:
        chosen_operation = input("Pick an operation: add → '+' , subtract → '-' , multiply → '*' or divide → '/': ")
        number_2 = float(input("What's the next number?: "))

        calculation = operations[chosen_operation]
        answer = calculation(number_1,number_2)

        print("%0.2f %s %0.2f = %0.2f" %(number_1,chosen_operation,number_2,answer))

        continue_choice = input("Type 'y' to continue, 'c' to reset the calculator or any other key to finish the program: ").lower()
        continue_operating =  0 if continue_choice == "y" else 1 if continue_choice == "c" else 2 
        number_1 = answer
    if continue_operating == 1:
        return True
    return False

def main():
    try:
        print("Starting...")
        while start_calculations():
            None
        exit
    except Exception as e:
        print("Please, introduce valid characters to the program. This will be reported!")

main()