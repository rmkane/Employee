namespace Example {
  using System;
  
  class Employee {
    // public string Name { get; protected set; }
    private string _name;
    public string Name {
      get { return _name; }
      protected set { _name = value; }
    }
    
    // public float Salary { get; protected set; }
    private float _salary;
    public float Salary {
      get { return _salary; }
      protected set { _salary = value; }
    }
     
    public Employee(String name, float salary) {
     Name = name;
     Salary = salary;
    }
    
    public void displayEmployee() {
     Console.WriteLine(String.Format("Name: {0}, Salary: ${1:f}", Name, Salary));
    }
    
    static void Main(String[] args) {
     Employee emp1 = new Employee("Bob", 75000f);
     Employee emp2 = new Employee("Joe", 50000f);
     emp1.displayEmployee();
     emp2.displayEmployee();
    }
  }
}