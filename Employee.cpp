#include <iostream>
#include <stdio.h>
using namespace std;

class Employee {
  private:
    string name;
    float salary;
  public:
    Employee(string, float);
    void displayEmployee();
};

Employee::Employee(string name, float salary) {
  this->name = name;
  this->salary = salary;
}

void Employee::displayEmployee() {
  printf("Name: %s, Salary: $%.2f\n", this->name.c_str(), this->salary);
}

int main () {
  Employee emp1("Bob", 75000);
  Employee emp2("Joe", 50000);
  emp1.displayEmployee();
  emp2.displayEmployee();
  return 1;
}
