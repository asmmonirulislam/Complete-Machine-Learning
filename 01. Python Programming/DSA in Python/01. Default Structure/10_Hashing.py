class Hash:
    def __init__(self):
        self.user = {}  # A Python dictionary is implemented as a hash table
        
    def insert_user(self, email, password):
        if email in self.user:
            print(f"{email} is already registered!")
            return
        self.user[email]=password
        print(f"{email} added as an user")
    
    def delete_user(self, email, password):
        if email in self.user:
            if password==self.user[email]:
                self.user.pop(email)
                print(f"Deleted!")
            else:
                print(f"{email} does not exists")
        
    def change_password(self, email, old_pass=None, new_pass=None):
        if email in self.user:
            if not new_pass:
                print("Enter your old password") if not old_pass==self.user[email] else print("Enter your new password")
                return
            if old_pass == self.user[email]:
                self.user.update({email: new_pass})
                print(f"Password Updated for {email}")
            else:
                print(f"Invalid Password!")
        else:
            print(f"{email} does not exists")
        
    def check_user(self, email, password):
        if email in self.user:
            print(f"Hello user!\nYour email: {email}\nYour Password: {self.user[email]}") if password==self.user[email] else print(f"Invalid Password!")
        else:
            print(f"{email} does not exists!")

user = Hash()
user.insert_user("asmmonirulislam.personal@gmail.com", "1234")
user.insert_user("asmmonirulislam.work@gmail.com", "1234")
user.change_password("asmmonirulislam.work@gmail.com", "1234", "123456")
user.check_user("asmmonirulislam.work@gmail.com", "123456")
user.delete_user("asmmonirulislam.personal@gmail.com", "1234")