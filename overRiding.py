class Employee:
    def setTheNumberOfWorkingHours(self):
        self.numberOfWorkingHours=40
    def displayTheNumberOfWorkingHours(self):
        print('the number of working hours is',self.numberOfWorkingHours)

employee =Employee()
employee.setTheNumberOfWorkingHours()
employee.displayTheNumberOfWorkingHours()
