import math

print("A - Create your own equation and write to a file?")
print("B - Read some equations from a chosen file by you?\n")

user_choice = str(input("Would you like to go with A or B from above?")).upper()

print(" ")

# If the user chooses choice 'a', they will be prompted to enter 2 number and an operation...
#...to create an equation
if user_choice == 'A':

    print("< This is a calculator, you will be asked to input 2 numbers and an operation to carry out. >")
    print("< For exampple: (number 1) = 3, (number 2) = 6, (operation) = +. >")
    print("< (Result) is  3 + 6 = 9. >")

    print(" ")

    # Requests for number input and will loop until a number has been entered
    # Will not accept anything other than a number
    # Prevents system from crashing from incorrect entries
    while True:
        try:
            num_1 = float(input("Please enter a number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    # Requests for 2nd number input and will loop until a number has been entered
    # Will not accept anything other than a number
    # Prevents system from crashing from incorrect entries
    while True:
        try:
            num_2 = float(input("Please enter another number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    # Requests user for operation input from the selection given below (+,-,x,/)
    # Will loop and request for correct operation input until 1 of the selection is chosen
    # Prevents crashing of system if incorrect option is chosen
    while True:

        CalcT29_file = open('CalcT29.txt', 'a')

        _oper = str(input("Please choose an operation from the following: '+', '-', 'x', '/': ")).lower()

        while _oper != '+' and _oper != '-' and _oper != 'x' and _oper != '/':
            _oper = str(input("Please choose an operation from the following: '+', '-', 'x', '/': ")).lower()

        # Addition 'if' statement
        if _oper == '+':
            _total = num_1 + num_2
            print(f'\n{num_1} + {num_2} = {_total}')
            CalcT29_file.write(f'{num_1} {_oper} {num_2} = {_total}\n')

        # Subtraction 'if' statement
        elif _oper == '-':
            _total = num_1 - num_2
            print(f'\n{num_1} - {num_2} = {_total}')
            CalcT29_file.write(f'{num_1} {_oper} {num_2} = {_total}\n')

        # Multiplication 'if' statement
        elif _oper == 'x':
            _total = num_1 * num_2
            print(f'\n{num_1} x {num_2} = {_total}')
            CalcT29_file.write(f'{num_1} {_oper} {num_2} = {_total}\n')

        # Division 'if' statement
        elif _oper == '/':

            # Below prevents a crash from a zerodevision error (can't divide a number by zero)
            # num_2 can never be zero if a numerical total is required
            # I have created a prevention to stop the system crashing if num_2 is zero
            if num_2 == 0:
                print("\nError, in this universe, you can't divide by zero!")
                print("Please travel to universe R-52 where zero division is possible!")
                CalcT29_file.write(f'{num_1} {_oper} {num_2} = ERROR\n')

            # num_1 can be zero
            # Will calculate normal division
            # Although 0 / (anything) will always be zero
            elif num_2 != 0:
                _total = round(num_1 / num_2, 2)
                print(f'\n{num_1} / {num_2} = {_total}')
                CalcT29_file.write(f'{num_1} {_oper} {num_2} = {_total}\n')

        else:
            print("Please enter a valid choice from the operators!")
        break
        CalcT29_file.close()

# If user chooses choice 'b'...
elif user_choice == 'B':

    user_file = " "

    while True:

        # Will prompt user to enter a file name
        # If file exists, will open and read the lines plus print them
        # The user does not need to add '.txt' as it is within the f string already
        # Loop will stop
        try:
            user_file = str(input("Please enter the name of the file that you want to read: "))
            CalcT29_file = open(f'{user_file}.txt', 'r+')
            for line in CalcT29_file:
                print(line)
            break

        # If file is not found, the error will be handled and will not simply crash
        # The user will be prompted again to enter the file name
        # This will loop until the user inputs a correct file name
        # The file will then close
        except FileNotFoundError:
            print("The file that you are trying to open does not exist")
            print("Please try again!\n")
            CalcT29_file.close()