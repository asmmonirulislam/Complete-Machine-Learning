try:
    num = int(input("Enter an integer: "))
    print(num)
except Exception as e:
    print(e)
else:
    print("Hello I am inside else block")
    
# Input:  Enter an integer: 4
# Output:
# 4
# Hello I am inside else block



# input: Enter an integer: sayem
# Output: invalid literal for int() with base 10: 'sayem'