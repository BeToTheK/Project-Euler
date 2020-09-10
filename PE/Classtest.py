class Employee:
    r_amount=2
    count=0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

        Employee.count+=1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def a_raise(self):
        self.pay=int(self.pay*self.r_amount)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.r_amount=amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp1=Employee('brittany', 'burke', 500)
emp2=Employee('brian','kresge',1000)
emp_str_0= 'John-Doe-8888'
emp_str_1= 'Big-Dong-666'

new_emp=Employee.from_string(emp_str_0)
import datetime
my_date=datetime.date(2018,7,7)

#print Employee.fullname(emp1)
Employee.a_raise(emp1)
print(Employee.count)
print(emp1.r_amount)
print(new_emp.fullname())
print(Employee.is_workday(my_date))
