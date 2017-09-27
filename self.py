class Employee:
    def callbyname(self):
        self.name="buckey"
        print(self.name)
        age =3
        print("age is ",age)

    def callbyvalue(self):
        print(self.name)

employee=Employee()
employee.callbyname()
employee.callbyvalue()
