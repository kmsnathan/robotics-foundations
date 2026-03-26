class PayrollSystem:
    def calculate_payroll(self,employees):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print("")
            
            
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
        
    def calculate_payroll(self):
        return self.weekly_salary
    
class HourlyEmployee(Employee):
    def __init__(self,id, name, hours_worked, hourly_rate):
        super().__init__(id,name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate
    
class ComissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, comission):
        super().__init__(id, name, weekly_salary)
        self.comission = comission
    
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.comission
    
salary_employee = SalaryEmployee(1, "John Smith", 1500)
hourly_employee = HourlyEmployee(2, "Jane Doe", 40, 15)
comission_employee = ComissionEmployee(3, "Kevin Bacon",1000, 250)

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(
    [salary_employee,hourly_employee,comission_employee]
)