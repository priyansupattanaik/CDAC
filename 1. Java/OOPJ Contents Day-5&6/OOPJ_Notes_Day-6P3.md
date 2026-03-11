# OOPJ Notes Day-6 Part-3

## Collection, Collections and Collection Framework in Java

- Menu-Driving programs to Manage Employee Record by using ArrayList with options like Insert a Record, Update Record, Delete Record, View All record.

```java
 public class Employee
 {
  public int EmpId;
  public String Name;
  private double Salary;
  public int Age;
  public String DeptName;

  public double getSalary() {
   return Salary;
  }

  public void setSalary(double salary) {
   Salary = salary;
  }

  public Employee() {

  }

  public Employee(int empId, String name, double salary, int age, String deptName) {

   EmpId = empId;
   Name = name;
   Salary = salary;
   Age = age;
   DeptName = deptName;
  }
  @Override
  public String toString() {
   return "EmpId=" + EmpId + ", Name=" + Name + ", Salary=" + Salary + ", Age=" + Age + ", DeptName="
     + DeptName;
  }
 }
 //Creating Comparator to sort Employee by EmpId
 public class SortByEmpId implements Comparator<Employee>
 {

  @Override
  public int compare(Employee o1, Employee o2) {
   if(o1.EmpId>o2.EmpId)
   {
    return 1;
   }
   if(o1.EmpId<o2.EmpId)
   {
    return -1;
   }
   return 0;
  }

 }
 public class EmployeeManager
 {
  Vector<Employee> ev;
  
  public EmployeeManager() {
   ev=new Vector<Employee>();
   
   ev.add(new Employee(110, "Ankush", 112090.0, 22, "AI"));
   ev.add(new Employee(10, "Sahil", 1120.89, 32, "GenAI"));
  }
  
  public void AddEmployee()
  {
   Scanner scan=new Scanner(System.in);
   Employee e=new Employee();
   System.out.println("Enter EmpId");
   e.EmpId=scan.nextInt();
   System.out.println("Enter Name");
   e.Name=scan.next();
   System.out.println("Enter Salary");
   //e.Salary=scan.nextDouble();  //NOT OK
   double sal=scan.nextDouble();
   e.setSalary(sal);
   //e.setSalary(scan.nextDouble()); //OK
   System.out.println("Enter Age");
   e.Age=scan.nextInt();
   System.out.println("Enter Dept Name");
   e.DeptName=scan.next();
   ev.add(e);
   System.out.println("Employee Added Successfully");
  }
  
  public void PrintEmployees()
  {
   Enumeration<Employee> en=ev.elements();
   
   while(en.hasMoreElements())
   {
    System.out.println(en.nextElement());
   }
  }
  
  public void UpdateEmployee()
  {
   Scanner scan=new Scanner(System.in);
   System.out.println("Enter Employee Id");
   int eid=scan.nextInt();
   
   boolean flag=false;
   for(Employee e:ev)
   {
    if(eid==e.EmpId)
    {
     flag=true;
     System.out.println("Enter Age");
     e.Age=scan.nextInt();
     System.out.println("Enter Dept Name");
     e.DeptName=scan.next();
     System.out.println("Employee Updated Successfully");
     break;
    }
   }
   if(flag==false)
   {
    System.out.println("Record Not Found");
   }
  }

  public void DeleteEmployee()
  {
   Scanner scan=new Scanner(System.in);
   System.out.println("Enter EmpId");
   int eid=scan.nextInt();
   
   ListIterator<Employee> lit=ev.listIterator();
   boolean flag=false;
   /*
   while(lit.hasNext())
   {
    if(eid==lit.next().EmpId)
    {
     flag=true;
     Employee e=lit.next();
     ev.remove(e);
     System.out.println("Employee Deleted Successfully");
     break;
    }
   }*/
   for(Employee e:ev)
   {
    if(eid==e.EmpId)
    {
     flag=true;
     ev.remove(e);
     System.out.println("Employee Deleted Successfully");
     break;
    }
   }
   if(flag==false)
   {
    System.out.println("Record Not Found");
   }
  }

  //Using Comparator to Sort Employees by EmpId
  public void SortByEmpId()
  {
   Collections.sort(ev, new SortByEmpId());
   for(Employee e:ev)
   {
    System.out.println(e);
   }
  }
 }
 public class EmployeeManagement {

 public static void main(String[] args) {
  
  Scanner scan=new Scanner(System.in);
  
  EmployeeManager em=new EmployeeManager();  
  int choice=0;
  
  do
  {
   System.out.println("=====================Employee Management======================");
   System.out.println("Press 1 to Add Employee");
   System.out.println("Press 2 to View All Employee");
   System.out.println("Press 3 to Update Employee");
   System.out.println("Press 4 to Delete Employee");
   System.out.println("Press 5 to Sort By EmpId");
   System.out.println("Press 6 to Exit");
   System.out.println("=====================Employee Management======================");
   System.out.println("Please Enter Your Choice");
   choice=scan.nextInt();
   
   switch (choice) {
   case 1:
   {
    em.AddEmployee();
    break;
   }
   case 2:
   {
    em.PrintEmployees();
    break;
   }
   case 3:
   {
    em.UpdateEmployee();
    break;
   }
   case 4:
   {
    em.DeleteEmployee();
    break;
   }
   case 5:
    em.SortByEmpId();
    break;
   case 6:
   {
    System.out.println("Exiting Program");
    break;
   }
   default:
    System.out.println("Invalid Choice");
    break;
   }
  }while(choice!=6);

 }
}
```

- Brief introduction to Comparable and Comparator Interface
  - Comparable Interface (java.lang.Comparable<T>)
    - Used to define a natural ordering for objects.
      - The class implementing Comparable must override the compareTo() method.
      - Typically used when a single sorting sequence is required (e.g., sorting employees by ID).
      - It used inside the class.
      - Uses compareTo(Object o) method for sorting
  - Comparator Interface (java.util.Comparator<T>)
    - Used for custom sorting logic.
    - Multiple comparators can be created for different sorting orders.
    - Requires overriding the compare() method.
    - It is defined outside of the class.
    - Uses compare(o1,o2) method for sorting.
    - Supports multiple sorting strategies.
    - Preferred when different sorting orders are needed.

- Implementation of Comparable for TreeSet collection for storing user-defined class instance inside TreeSet

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.TreeSet;

class Employee implements Comparable<Employee>
{
 int EmpId;
 String Name;
 double Salary;
 String DeptName;
 
 public Employee() {
  super();
 }

 public Employee(int empId, String name, double salary, String deptName) {
  super();
  EmpId = empId;
  Name = name;
  Salary = salary;
  DeptName = deptName;
 }

 @Override
 public String toString() {
  return "EmpId=" + EmpId + ", Name=" + Name + ", Salary=" + Salary + ", DeptName=" + DeptName;
 }

 @Override
 public int compareTo(Employee o) {
  if(this.Salary>o.Salary)
  {
   return 1;
  }
  if(this.Salary<o.Salary)
  {
   return -1;
  }
  return 0;
 }
}

public class ComparableDemo {

 public static void main(String[] args) {
  
  TreeSet<Employee> ts=new TreeSet<Employee>(); //To store data inside TreeSet a user defined class must implements Comparable<T>
  
  ts.add(new Employee(120, "Malkeet", 473436.89, "Education"));
  ts.add(new Employee(12, "Ankush", 3436.89, "IT"));
  ts.add(new Employee(300, "Zeenat", 147343.89, "Software"));
  ts.add(new Employee(1, "Harman", 23436.89, "Biology"));
  ts.add(new Employee(101, "Sahil", 476.89, "Marketing"));
  System.out.println("Employee data sorted according specified Natural order");
  for(Employee e:ts)
  {
   System.out.println(e);
  }
 }
}
```

- Implementation of Comparator Interface
  - Using Class
  - Using Anonymous class

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.TreeSet;

class Employee
{
 int EmpId;
 String Name;
 double Salary;
 String DeptName;
 
 public Employee() {
  super();
 }

 public Employee(int empId, String name, double salary, String deptName) {
  super();
  EmpId = empId;
  Name = name;
  Salary = salary;
  DeptName = deptName;
 }

 @Override
 public String toString() {
  return "EmpId=" + EmpId + ", Name=" + Name + ", Salary=" + Salary + ", DeptName=" + DeptName;
 }
}
//Implementing Comparator<> interface through class to sort Employee by Salary
class SortBySalaray implements Comparator<Employee>
{
 @Override
 public int compare(Employee o1, Employee o2) {
  if(o1.Salary>o2.Salary)
  {
   return 1;
  }
  if(o1.Salary<o2.Salary)
  {
   return -1;
  }
  return 0;
 }
 
}
//Implementing Comparator<> interface through class to sort Employee by Name
class SortbyName implements Comparator<Employee>
{

 @Override
 public int compare(Employee o1, Employee o2) {
  
  return o1.Name.compareTo(o2.Name);
 }
}
public class ComparableDemo { 
 public static void main(String[] args) {
 ArrayList<Employee> ts=new ArrayList<Employee>();
  
  ts.add(new Employee(120, "Malkeet", 473436.89, "Education"));
  ts.add(new Employee(12, "Ankush", 3436.89, "IT"));
  ts.add(new Employee(300, "Zeenat", 147343.89, "Software"));
  ts.add(new Employee(1, "Harman", 23436.89, "Biology"));
  ts.add(new Employee(101, "Sahil", 476.89, "Marketing"));
  
  System.out.println("Unsorted Records");
  
  for(Employee e:ts)
  {
   System.out.println(e);
  }
  
  //Implementing Comparator<> interface through anonymous to sort Employee by Name
  Comparator<Employee> sortByName=new Comparator<Employee>() {
   
   @Override
   public int compare(Employee o1, Employee o2) {
    
    return o1.Name.compareTo(o2.Name);
   }
  };
  
  Collections.sort(ts,sortByName);
  System.out.println("Records Sorted By Name");
  for(Employee e:ts)
  {
   System.out.println(e);
  }
  
  //Implementing Comparator<> interface through anonymous to sort Employee by DeptName
  Comparator<Employee> sortByDeptName=new Comparator<Employee>() {
   
   @Override
   public int compare(Employee o1, Employee o2) {
    
    return o1.DeptName.compareTo(o2.DeptName);
   }
  };
  Collections.sort(ts,sortByDeptName);
  System.out.println("Records Sorted By Dept Name");
  for(Employee e:ts)
  {
   System.out.println(e);
  }
 }
}
```

- Implementation of Comparator Interface: Using Lambda

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.TreeSet;
import java.util.stream.Collector;

class Employee
{
 int EmpId;
 String Name;
 double Salary;
 String DeptName;
 
 public Employee() {
  super();
 }

 public Employee(int empId, String name, double salary, String deptName) {
  super();
  EmpId = empId;
  Name = name;
  Salary = salary;
  DeptName = deptName;
 }

 @Override
 public String toString() {
  return "EmpId=" + EmpId + ", Name=" + Name + ", Salary=" + Salary + ", DeptName=" + DeptName;
 }
}
public class ImplCompByLambda { 
 public static void main(String[] args) {
  ArrayList<Employee> ts=new ArrayList<Employee>();
  
  ts.add(new Employee(120, "Malkeet", 473436.89, "Education"));
  ts.add(new Employee(12, "Ankush", 3436.89, "IT"));
  ts.add(new Employee(300, "Zeenat", 147343.89, "Software"));
  ts.add(new Employee(1, "Harman", 23436.89, "Biology"));
  ts.add(new Employee(101, "Sahil", 476.89, "Marketing"));
  
  System.out.println("Unsorted Records");
  
  for(Employee e:ts)
  {
   System.out.println(e);
  }
  
  Collections.sort(ts, (o1,o2)->o1.Name.compareTo(o2.Name));
  System.out.println("Sorted Records By Name");
  
  for(Employee e:ts)
  {
   System.out.println(e);
  }
  
  Collections.sort(ts, (o1,o2)->Double.valueOf(o1.Salary).compareTo(o2.Salary));
  
  System.out.println("Sorted Records By Salary");
  
  for(Employee e:ts)
  {
   System.out.println(e);
  }
 }
}
```

## Functional Programming in Java

- Functional Programming Overview
  - Functional Interfaces
  - An interface which have exactly one abstract method is known as Functional Interface.
  - We can implements such interfaces using:
    - A class
    - A Anonymous class
    - A Lambda expression
  - The best way to implement these interfaces is through lambda expressions.
  - Implementation of Functional interfaces through lambda expressions/methods give rise to the Functional Programming.

- Impact of Functional programming upon Collection Framework
  - Before Java 8: Collections required external iteration (e.g., using loops).
  - After Java 8: Introduced Streams API, enabling internal iteration and functional-style operations on collections.

- Explore java.util.function package : Predicate, Map, Consumer, Supplier
  - Predicate<T> – Represents a boolean-valued function. (test(T t))
  - Consumer<T> – Represents an operation that accepts a single input and returns no result. (accept(T t))
  - Supplier<T> – Represents a supplier of results. (get())
  - Function<T, R> – Represents a function that accepts one argument and produces a result. (apply(T t))
  - BiFunction<T, U, R> – Represents a function that accepts two arguments and produces a result. (apply(T t, U u))
  - UnaryOperator<T> – Represents an operation on a single operand that produces a result of the same type. (apply(T t))
  - BinaryOperator<T> – Represents an operation upon two operands of the same type, producing a result of the same type. (apply(T t1, T t2))