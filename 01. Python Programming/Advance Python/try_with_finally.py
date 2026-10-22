try:
    num = int(input("Enter an integer: "))
    print(num)
except Exception as e:
    print(e)
finally:
    print("Hello I am inside finally block")
    
    
# input: Enter an integer: 4
# Output:
# 4
# Hello I am inside finally block


# Input: Enter an integer: sayem
# Output:
# invalid literal for int() with base 10: 'sayem'
# Hello I am inside finally block


def main1():
    try:
        num = int(input("Enter an integer: "))
        print(num)
        return
    except Exception as e:
        print(e)
        return
    print("Hey I am inside finally block") # It is never ever executed for this function
    
    
def main2():
    try:
        num = int(input("Enter an integer: "))
        print(num)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("Hey I am inside finally block")
        
main1()
# Input: Enter an integer: 4
# Output: 4
main2()
# Input: Enter an integer: 4
# Output:
# 4
# Hey I am inside finally block