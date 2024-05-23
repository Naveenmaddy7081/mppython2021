
# this code is risky code
# because it may contain run time error
# then will i do
# for this use try except mechanism
# finally always executes weather exception occurs or not
# there is only one finally

# try-except
# try-except-finally recommended
# try-finally
try:
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
    print("a=",a," b=",b)
    d=a/b
    print("Divi=",d)
    #print("thanks for using this program")

except ZeroDivisionError:
    print("Value of b can not be zero")

except ValueError:
    print("You have enter a character not a number")

except Exception:
    print("Something Went Wrong")

finally:
    print("thanks for using this program")

