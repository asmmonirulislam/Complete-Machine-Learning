s1 = 'asm MoniRul Islam'
s2 = 'asmmonirulislam'
s3 = 'ASMMONIRULISLAM'
s4 = 'ASM MONIRUL ISLAM'
s5 = '0323653982@student.wub.edu.bd'

# capitalize()	Converts the first character to upper case
print(s2.capitalize())  # Asmmonirulislam

# casefold()	Converts string into lower case
print(s3.casefold())    # asmmonirulislam

# center()	Returns a centered string
print(s1.center(40))    #            asm MoniRul Islam

# count()	Returns the number of times a specified value occurs in a string
print(s1.count('a'))    # 2

# encode()	Returns an encoded version of the string
print(s1.encode())  # b'asm MoniRul Islam'

# endswith()	Returns true if the string ends with the specified value
print(s1.endswith('m')) # True

# expandtabs()	Sets the tab size of the string
print(s1.expandtabs(3)) # asm MoniRul Islam

# find()	Searches the string for a specified value and returns the position of where it was found
print(s2.find('isl'))   # 10

# index()	Searches the string for a specified value and returns the position of where it was found
print(s2.index('ulis')) # 8

# isalnum()	Returns True if all characters in the string are alphanumeric
print(s2.isalnum()) # True

# isalpha()	Returns True if all characters in the string are in the alphabet
print(s2.isalpha()) # True

# isascii()	Returns True if all characters in the string are ascii characters
print(s2.isascii()) # True

# isdecimal()	Returns True if all characters in the string are decimals
print(s2.isdecimal())   #False

# isdigit()	Returns True if all characters in the string are digits
print(s2.isdigit())     #False

# isidentifier()	Returns True if the string is an identifier
print(s2.isidentifier())    # True

# islower()	Returns True if all characters in the string are lower case
print(s2.islower())     # True

# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning