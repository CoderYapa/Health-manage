def getdate() :
    import datetime
    return datetime.datetime.now()
def Lock(n1) :
    if n1 == 1:
        n3 = int(input("Press \n 1. For Diet\n 2. For Exercise\n"))
        if n3 == 1:
          with open("Harry Diet.txt", "a") as p:
            n4=input("Enter your Diet \n")
            p.write("Harry ne khaya:" "\n")
            p.write(str([str(getdate())]) +n4+ "\n")
            print("Written Successfully")
        elif n3 == 2:
            with open("Harry Exercise.txt", "a") as p:
                n4 = input("Enter your Exercise \n")
                p.write("Harry ne ye exercise ki:" "\n")
                p.write(str([str(getdate())]) + n4 + "\n")
                print("Written Successfully")
    elif n1 == 2:
        n3 = int(input("Press \n 1. For Diet\n 2. For Exercise\n"))
        if n3 == 1:
            with open("Hammad Diet.txt", "a") as p:
                n4 = input("Enter your Diet \n")
                p.write("Hammad ne khaya:" "\n")
                p.write(str([str(getdate())]) + n4 + "\n")
                print("Written Successfully")
        elif n3 == 2:
            with open("Hammad Exercise.txt", "a") as p:
                n4 = input("Enter your Exercise \n")
                p.write("Hammad ne ye exercise ki:\n")
                p.write(str([str(getdate())]) + n4 + "\n")
                print("Written Successfully")
    elif n1 == 3:
        n3 = int(input("Press \n 1. For Diet\n 2. For Exercise\n"))
        if n3 == 1:
            with open("Rohan Diet.txt", "a") as p:
                n4 = input("Enter your Diet \n")
                p.write("Rohan ne khaya:\n")
                p.write(str([str(getdate())]) + n4 + "\n")
                print("Written Successfully")
        elif n3 == 2:
            with open("Rohan Exercise.txt", "a") as p:
                n4 = input("Enter your Exercise \n")
                p.write("Rohan ne ye exercise ki:\n")
                p.write(str([str(getdate())]) + n4 + "\n")
                print("Written Successfully")
    else:
        print("Please Enter a valid number  ")
def Retrive(n2):
    if n2 == 1:
        n3 = int(input("Press \n 1. For Diet\n 2. For Exercise\n"))
        if n3 == 1:
            with open("Harry Diet.txt") as p:
               for line in p:
                   print(line, end="")

        elif n3 == 2:
            with open("Harry Exercise.txt") as p:
                for line in p:
                    print(line, end="")
    elif n2 == 2:
        n3 = int(input("Press \n 1. For Diet\n 2. For Exercise\n"))
        if n3 == 1:
            with open("Hammad Diet.txt", "a") as p:
                for line in p:
                    print(line, end="")
        elif n3 == 2:
            with open("Hammad Exercise.txt") as p:
                for line in p:
                    print(line, end="")
    elif n2 == 3:
        n3 = int(input("Press \n 1. For Diet\n 2. For Exercise\n"))
        if n3 == 1:
            with open("Rohan Diet.txt", "a") as p:
                for line in p:
                    print(line, end="")
        elif n3 == 2:
            with open("Rohan Exercise.txt", "a") as p:
                for line in p:
                    print(line, end="")
    else:
        print("Please Enter a valid number")
print("                  Health Management System  ")
n_1=int(input("Press\n 1. For Lock\n 2. For Retrive \n"))


if n_1 == 1:
    n_2 = int(input("Press\n 1. For Harry\n 2. For Hammad \n 3. For Rohan  \n"))
    a=Lock(n_2)
    print(a)
elif n_1 == 2:
    n_2 = int(input("Press\n 1. For Harry\n 2. For Hammad \n 3. For Rohan  \n"))
    a=Retrive(n_2)
    print(a)
else:
    print("Please enter a valid number & try again" )