#!/usr/bin/python
import sys

class Employee(object):
  def set_name(self, value):
    self._name = value
  def get_name(self):
    return self._name
  def del_name(self):
    del self.name
  name = property(get_name, set_name, del_name, 'String')

  def set_salary(self, value):
    self._salary = value
  def get_salary(self):
    return self._salary
  def del_salary(self):
    del self.salary
  salary = property(get_salary, set_salary, del_salary, 'float')

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    
  def __repr__(self):
    return "Name: %s, Salary: $%.2f" % (self.name, self.salary)

  def displayEmployee(self):
    print self

def main():
  emp1 = Employee("Bob", 75000)
  emp2 = Employee("Joe", 50000)
  emp1.displayEmployee()
  emp2.displayEmployee()
  sys.exit(0)
  
if __name__ == '__main__':
  main();