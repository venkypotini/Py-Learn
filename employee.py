class Employee:
    empCount = 0
    def __init__(self,name, salary, phone):
        self.name = name
        self.salary = salary
        self.phone = phone
        Employee.empCount += 1
        self.id = Employee.empCount

    def display_info(self):
        print(self.name)
        print(self.id)

    def display_info2(self):
        print("I am inside info2")
        self.display_info()
        Employee.cmethod()

    @classmethod
    def cmethod(cls):
        print("I am class method")
        return cls("Ajay",100,'444')
