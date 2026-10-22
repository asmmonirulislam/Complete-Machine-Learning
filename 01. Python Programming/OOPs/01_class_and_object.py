class BankAccount():
    def __init__(self, name, acc_no, phone, address, bank_balance):
        self.name=name
        self.acc_no=acc_no
        self.phone=phone
        self.address=address
        self.bank_balance=bank_balance
        
    def addBalance(self, amount):
        prev_balance=self.bank_balance
        self.bank_balance+=amount
        print(f"{prev_balance} + {amount} = {self.bank_balance}")
        
    def creditBalance(self, amount):
        prev_balance = self.bank_balance
        self.bank_balance-=amount
        print(f"{prev_balance} - {amount} = {self.bank_balance}")
    
    def getInfo(self):
        print(f"Name: {self.name}\nAccount No: {self.acc_no}\nBank Balance: {self.bank_balance}")
        

sayem = BankAccount("A S M Monirul Islam", 3982, "01401411046", "Mirpur, Dhaka", 120000)
sayem.addBalance(25000)
sayem.creditBalance(11500)
sayem.getInfo()  