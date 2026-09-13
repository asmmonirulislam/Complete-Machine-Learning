def Person(*args, **kwargs):
    print("Personal Details:")
    print(*args, sep="\n")
    print("Address: ")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

Person("A S M Monirul Islam", "01401411046", Holding="J12", Street="Road no 05", Area="Mirpur, Dhaka")