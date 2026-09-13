class StudentRecord:
    def __init__(self):
        self.student = {}
    def A(self):
        name = input("Enter the name of the Student: ")
        if name in self.student:
            print(f"{name} already exists")
            return
        mark = int(input("Enter mark: "))
        self.student[name]=mark
        print(f"\nRecord Added\n")
    def B(self):
        name = input("Enter the name of the student: ")
        if not name in self.student:
            print(f"{name} not found")
            return
        mark = int(input("Enter mark to update: "))
        self.student[name]=mark
        print(f"\nMark Updated\n")
    def C(self):
        name = input("Enter the name of the student: ")
        if not name in self.student:
            print(f"{name} not found")
            return
        print(f'\n{name} - {self.student[name]}\n')
    def D(self):
        if not self.student:
            print(f"\nStudent not added yet\n")
            return
        for key, val in self.student.items():
            print(f"{key} - {val}")
        print()

def main():
    obj = StudentRecord()
    while True:
        cmd = input("\nA (Add a student)\nB (Update Mark)\nC (Search Student)\nD (View All)\nQ (Exit)\nEnter a command: ").lower()
        match cmd:
            case 'a':
                obj.A()
            case 'b':
                obj.B()
            case 'c':
                obj.C()
            case 'd':
                obj.D()
            case 'q':
                break
            case _:
                print('Invalid Command')

if __name__ == "__main__":
    main()