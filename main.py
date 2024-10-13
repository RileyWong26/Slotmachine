import random
'''
Advanced logic
Looking trhough rows and columns,
nested lists
'''


#BET INFO
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#INFO ON SLOT MACHINE
ROWS = 3
COLS = 3

symbol_count = {
    "🍊": 2,
    "🍇": 4,
    "🍒": 6,
    "🍓": 8
}
symbol_value = {
    "🍊": 5,
    "🍇": 4,
    "🍒": 3,
    "🍓": 2
}
def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            #If no break this runs
            winnings += values[symbol] *bet
            winning_lines.append(line+ 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =  []
    for symbol, symbol_count in symbols.items():
        #Unused variable so use _
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        #Copy a list
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slow_machine(columns):
    '''
    Way we wrote our colums is
    [a,b,c]
    [b,a,c]
    [c,a,a]
    we want it like
    [a,b,c]
    [b,a,a]
    [c.c.c] basically flip it on side.
    known as transposing
    :param columns:
    :return:
    '''
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            #CHeck if its the last element, if its not add the pipe seperator
            if i != len(columns) - 1:
                print(column[row], "|", end="")
            else:
                print(column[row])

def deposit():
    '''
take in users money
'''
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    '''
    take in users money
    '''
    while True:
        lines = input(f"Enter the number of lines to bet on(1-{MAX_LINES})?")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= 1:
                break
            else:
                print(f"Amount must be between {MAX_LINES} - 1.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    '''
    take in users money
    '''
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MAX_BET>= amount >= MIN_BET:
                break
            else:
                print(f"Amount must be between {MAX_BET} - {MIN_BET}.")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        totalbet = bet * lines
        if totalbet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines.  Total bet is equal to: ${totalbet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slow_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(winning_lines)
    print(f"You won ${winnings}.")
    print(f"You won on:",
          *winning_lines)  # Pass every line.  Splat operator.  So you dont have to break down with for loop
    return winnings - totalbet
def main():
    balance =  deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play(q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
main()