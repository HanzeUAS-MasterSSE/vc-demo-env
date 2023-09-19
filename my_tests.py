#%%
import datetime

class Employee:

    number_of_employees = 0
    bonus_amount = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = int(pay)
        Employee.number_of_employees += 1

    # Converts a function into a property
    @property
    def full_name(self):
        return f'{self.first} {self.last}'
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print(f"{self.first} {self.last} - Deleted.")
        self.first = None
        self.last = None
    
    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@matrix.com"

    # def apply_bonus(self, bonus=bonus_amount):
    #     self.bonus = bonus
    #     self.pay = int(self.pay * self.bonus)

    def apply_bonus(self):
        self.pay = int(self.pay * self.bonus_amount)

    def __repr__(self) -> str:
        return f"Employee('{self.first}','{self.last}',{self.pay})"
    
    def __str__(self) -> str:
        return f"{self.first} {self.last}"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.full_name)

    # Class methods affect the class itself (not an instance)
    @classmethod
    def set_bonus_amount(cls, amount):
        cls.bonus_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # Does not receive the self or class as an argument
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

class Developer(Employee):
    bonus_amount = 1.10

    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay),
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('---> ', emp.full_name)

emp_1_str = 'Felipe-Martins-1000'
emp_2_str = 'Joanes-Burgo-2000'
emp_3_str = 'James-Bond-1007'

emp_1 = Employee.from_string(emp_1_str)
emp_2 = Employee.from_string(emp_2_str)
emp_3 = Employee.from_string(emp_3_str)

dev_1 = Developer("Mister", "Anderson", 10000, 'Binary')
dev_2 = Developer("George", "LaForge", 20000, 'LCARS')
dev_3 = Developer("Allan", "Turing", 30000, "Enigma")
print(dev_1.email)
print(dev_1.prog_lang)

mgr_1 = Manager('Karen', 'Komplainer', 10000000, [dev_1, dev_2, dev_3])
mgr_1.print_emp()

print(emp_1)
print(emp_1.__repr__())

#%%
# print(help(Developer))

# print()
# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))
# print()
# print(issubclass(Developer, Employee))
# %%
# emp_1 = Employee("Felipe", "Martins", 1000)
# emp_2 = Employee("Joanes", "Burgo", 2000)

# print(Employee.__dict__)
# print(emp_1.__dict__)
# print(emp_2.__dict__)

# print(emp_1.full_name)
# print(Employee.full_name(emp_2))

# emp_1.set_bonus_amount(1.10)

# print(emp_1.pay)
# emp_1.apply_bonus()
# print(emp_1.pay)

# print(emp_2.pay)
# emp_2.apply_bonus()
# print(emp_2.pay)

# print(emp_1.full_name + ", " + emp_1.email)
# print(emp_2.full_name + ", " + emp_2.email)
# print(emp_3.full_name + ", " + emp_3.email)

# my_date = datetime.date(2023, 9, 17)

# Employee.is_workday(my_date)

