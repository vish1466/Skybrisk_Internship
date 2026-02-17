# Week 1 : Hands-On Practice
# Scope : Temperature Converter, Calculator

import operator

def temp_conv():
    print("Which temperature conversion do you require?")
    pref = str(input("A.°C -> °F \t B.°F -> °C 1 \n"))

    if((pref == 'A') or (pref == 'a')):
        temp_celc = float(input("Enter Temperature in Celsius : "))
        print("Temperature in Fahrenheit:", (temp_celc * 9/5) + 32, "°F")

    elif((pref == 'B') or (pref == 'b')):
        temp_fahr = float(input("Enter Temperature in Fahrenheit : "))
        print("Temperature in Celsius:", (temp_fahr - 32) * (5/9), "°C")

def calculator():
    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '**' : operator.pow,
        '//' : operator.floordiv,
        '%' : operator.mod
    }
    print("Available operations:", ", ".join(ops.keys()))

    print("Enter the operation you would like to perform (only one operator) : ")

    mid = str(input())

    num1 = float(input("Enter number (a) : "))
    num2 = float(input("Enter number (b) : "))

    if((mid in ('/','//','%')) and (num2 == 0)):
        print("Undefined, division with 0 is not possible")

    print("Final Output : ", ops[mid](num1, num2))


def main():
    while True:
        print("1. Temperature Converter (Fahrenheit and Celsius)")
        print("2. Calculator (two numbers, single operator)")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            temp_conv()
        elif choice == "2":
            calculator()
        elif choice == "3":
            print("...Exiting script...")
            break
        else: print("Invalid Input, Select within (1-3)")


if __name__ == "__main__":
    main()

