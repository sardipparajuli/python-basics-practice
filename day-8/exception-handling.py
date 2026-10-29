# Exception handling
# exception raise line place it in try block place
# except block: statements to be exected in case of exception
# can define multiple error specific except block
# can have one one catch all except block

# try:
#     statement
# except:
#     statement

try:
    a = int(input("enter a number:"))
    print(b + 10)  # "b" is not defined
except ValueError:
    print("ValueError")
except:
    print("Except block")
    
    
    
    inp = "yes"
while inp == "yes":
    try:
        a = int(input("enter a number "))
        b = int(input("enter a number "))
        op = input("enter a operator ")

        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "/":
            print(a / b)
        elif op == "%":
            print(a % b)
        elif op == "*":
            print(a * b)
        elif op == "//":
            print(a // b)
        else:
            print("invalid operator")

    except ValueError:
        print("value error")
    except ZeroDivisionError:
        print("cannot divide by zero")
    except:
        print("error")

    inp = input("do you want to perform operations ")