# := is a warlus operator that allows to assign values to variables as part of an expression
if (n := len([1,2,3,4,5,6])) > 3: 
    print(f"List is so long ({n} elements, expected < 3)") # List is so long (6 elements, expected < 3)