logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
continued = "n"
while True:
    if continued == "n":
        num1 = int(input("what's the first Number"))
        operation = input('What do you want to do?\n+\n-\n*\n/')
        num2 = int(input("What's the second number"))
        if operation == '/':
            answer = num1 /num2
        if operation == '+':
            answer = num1 +num2
        if operation == '-':
            answer = num1 -num2
        if operation == '*':
            answer = num1 *num2
        print(f'{num1}{operation}{num2} = {answer}')
        continued = input(f"type 'y' to continue from {answer} or type 'n' to start a new calculation")
    elif continued == 'y':
        num1 = answer
        operation = input('What do you want to do?\n+\n-\n*\n/')
        num2 = int(input("What's the second number"))
        if operation == '/':
            answer = num1 / num2
        if operation == '+':
            answer = num1 + num2
        if operation == '-':
            answer = num1 - num2
        if operation == '*':
            answer = num1 * num2
        print(f'{num1}{operation}{num2} = {answer}')
        continued = input(f"type 'y' to continue from {answer} or type 'n' to start a new calculation")