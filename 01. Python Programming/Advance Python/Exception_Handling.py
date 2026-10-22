try:
    number = int(input("Enter an integer: "))
    print(number)
except Exception as e:
    print(e)
    
# Input: Enter an integer: 4
# Output: 4

# Input: Enter an integer: Sayem
# Output: invalid literal for int() with base 10: 'Sayem'