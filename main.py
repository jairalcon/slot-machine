# https://www.youtube.com/watch?v=th4OBktqK1I&list=WL&index=1&t=1s
# learning python one step at a time
import random

# adding global constant that limits variable value
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# how many symbols are in each reel
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):  # looping through every row
        # look at first column gives us the first symbol
        symbol = columns[0][line]
        for column in columns:  # loop through each col and check for that symbol
            symbol_to_check = column[line]
            if symbol != symbol_to_check:  # check if symbols are not the same, check next line
                break  # check next line
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# generate outcome out slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():  # gives both key and value associated with dictionary
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []  # define columns list
    for _ in range(cols):  # generate a column for each columns we have
        column = []  # picking randomly
        # : is the slice operator in python to copy
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            # finds first instance in the list and removes it
            current_symbols.remove(value)
            column.append(value)  # add value to column

        columns.append(column)  # adding column to columns list

    return columns


def print_slot_machine(columns):  # transposing
    for row in range(len(columns[0])):  # loop through every row
        # looping through items in individual columns
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                # pipe operator to create separation and end tells print when to end line = "\n"
                print(column[row], end=" | ")
            else:
                print(column[row], end="")  # no pipe operator

        print()  # bring us to the next line


# creating function to execute block of code and return value
def deposit():
    while True:  # creating while loop
        amount = input("What would you like to deposit? $")  # prompt w/text
        if amount.isdigit():  # conditional / check if amount is a number
            amount = int(amount)  # assign number to amount
            if amount > 0:  # if amount is greater, then breaks
                break
            else:  # if not, else statement
                print("Amount must be greater than 0.")
        else:  # if it's not a number
            print("Please enter a number.")
    return amount  # returns value


# determine how many lines and how much to bet
def get_number_of_lines():
    while True:  # creating while loop
        lines = input(  # prompt w/text
            "Enter the amount of lines to bet on (1-" + str(MAX_LINES) + ")? ")  # adding string of MAX_LINES
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # checking to see if value is between 2 values
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:  # creating while loop
        # prompt w/text
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():  # conditional / check if amount is a number
            amount = int(amount)  # assign number to amount
            if MIN_BET <= amount <= MAX_BET:  # if amount is greater, then breaks
                break
            else:  # if not, else statement
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:  # if it's not a number
            print("Please enter a number.")
    return amount  # returns value


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet >= balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on", *winning_lines)  # splat/unpack operator
    return winnings - total_bet


def main():  # adding main function to start code
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break  # ends game
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
