def add():
    return first_number + second_number


def subtract():
    return first_number - second_number


def multiply():
    return first_number * second_number


def divide():
    return first_number / second_number


print("Select operation.")
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

while True:
    try:
        command = int(input('Choose operation(1/2/3/4): '))
    except ValueError:
        print('Choose a valid operation')
        continue
    if command == 1 or command == 2 or command == 3 or command == 4:
        try:
            first_number = float(input('Enter your first number: '))
            second_number = float(input('Enter your second number: '))
        except ValueError:
            print('Invalid number. Please enter a valid number')
            continue
        result = 0
        if command == 1:
            result = add()
        elif command == 2:
            result = subtract()
        elif command == 3:
            result = multiply()
        elif command == 4:
            try:
                first_number / second_number or second_number / first_number
            except ZeroDivisionError:
                print("Can't divide by 0. Try again: ")
                continue

        print(f'Result: {result}')

        next_calculation = input('Would you like to do a new calculation (yes/no): ')
        if next_calculation == 'no' or next_calculation == 'n' or next_calculation == 'N' or next_calculation == 'NO':
            break
    else:
        print('Invalid input')
