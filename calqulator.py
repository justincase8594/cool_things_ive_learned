while True:
    print("""
    Options:
    'add' to add two numbers.
    'sub' to subtract two numbers.
    'mult' to multiply two numbers.
    'div' to divide two numbers.
    'quit' to end program.
    """)
    user_input = input(':')

    if user_input == 'quit':
        break
    elif user_input == 'add':
        num1 = float(input('enter a number: '))
        num2 = float(input('enter another number: '))
        result = str(num1 + num2)
        print(result)
    elif user_input == 'sub':
        num1 = float(input('enter a number: '))
        num2 = float(input('enter another number: '))
        result = str(num1 - num2)
        print(result)
    elif user_input == 'mult':
        num1 = float(input('enter a number: '))
        num2 = float(input('enter another number: '))
        result = str(num1 * num2)
        print(result)
    elif user_input == 'div':
        num1 = float(input('enter a number: '))
        num2 = float(input('enter another number: '))
        result = str(num1 / num2)
        print(result)
    else:
        print("unkown input")
