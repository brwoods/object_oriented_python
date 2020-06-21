# Date: 30-DEC-2019
# Author: https://developer.ibm.com/tutorials/object-oriented-programming-in-python/
# Purpose: objects in Python, using GIT
class Employee:

    #class attributes
    status = "active"
    number_of_employee = 0

    def __init__(self, employee_id, name, age):
        self.employee_id = employee_id #instance attribute
        self.name = name #instance attribute
        self.age = age #instance attribute
        Employee.number_of_employee += 1


    # Creates model property
    @property
    def age(self):
        return self.__age

    # Create property setter
    @age.setter
    def age(self, age):
        if age < 18:
            raise Exception('An Employee\'s age cannot be lower than 18')
        elif age > 99:
            raise Exception('An Employee\'s age cannot be upper than 99')
        else:
            self.__age = age


    #class method
    def give_info(self):
        print("Name:",self.name,"\nID:",self.employee_id)

    @staticmethod
    def get_class_objective():
        message = "The objective of this Employee class is to organize employee information with more modular manner"
        print (message)
               
    # Create Class Manager that inherits Employee
class Manager(Employee):

    team_size = 10

    def set_team_size(self, team_size):
        self.team_size = team_size

    def give_info(self):
        print("Name:",self.name,"\nID:",self.employee_id,"\nTeam Size:",self.team_size)

    def calculate_salary(self, salary, bonus=None):
        if bonus is not None:
            salary += bonus
        return salary
    
    
    