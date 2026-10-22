# Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.

age : int = 25 # if I type age and then put a . then it will automatically recommend all the integer functions
name : str = "A S M Monirul Islam"

def person(name: str, age: int) -> str:
    print(f"Hello {name}, your age is {age}")

person("A S M Monirul Islam", 24) # Hello A S M Monirul Islam, your age is 24