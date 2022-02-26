def plural():
    first_number = input("Type Your First Number: ")
    second_number = input("Type Your Second Number: ")
    calc = float(first_number) + float(second_number)
    print("Your Result is: " + str(calc))

def subtract():
    first_number = input("Type Your First Number: ")
    second_number = input("Type Your Second Number: ")
    calc = float(first_number) - float(second_number)
    print("Your Result is: " + str(calc))
def multiplie():
    first_number = input("Type Your First Number: ")
    second_number = input("Type Your Second Number: ")
    calc = float(first_number) * float(second_number)
    print("Your Result is: " + str(calc))
def divide():
    first_number = input("Type Your First Number: ")
    second_number = input("Type Your Second Number: ")
    calc = float(first_number) / float(second_number)
    remainder = float(first_number) % float(second_number)
    print("Your Result is: " + str(calc))
    print("Remainder of The Division: " + str(remainder))
print("Welcome To My Basic Calculator! \n What Operate Do You Want? \n 1.( + ) \n 2.( - ) \n 3.( % ) \n 4.( X or * )")
choose = input("Write The Number of Your Choice: ")
if choose == "1":
    plural()
elif choose == "2":
    subtract()
elif choose == "3":
    divide()
elif choose == "4":
    multiplie()

