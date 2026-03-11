class Employee
{
    int EmpId;          //Non-Static Field, Instance Field
    String Name;
    float Salary;
    static String DeptName;     //Static Field, Class Level Field
    static String CompanyName;

    void PrintData()            //Non-Static Method, Instance Method
    {
        System.out.println("EmpId: "+EmpId);
        System.out.println("Emp Name: "+Name);
        System.out.println("Emp Dept: "+Employee.DeptName);
    }
    static void PrintStaticData()   //Static Method, Class Level method
    {
        System.out.println(Employee.DeptName);
        System.out.println(Employee.CompanyName);
    }
}

class EmployeeTest 
{
    public static void main(String[] args) {
        Employee e1=new Employee();
        e1.EmpId=101;           //Accessing instance field with instance ref variable
        e1.Name="Malkeet";
        e1.Salary=365736.89f;
        Employee.DeptName="CSE";        //Accessing static field with className, Static Way
        Employee.CompanyName="CDAC Mumbai";

        e1.PrintData();         //Calling non-static method with class ref variable
        Employee.PrintStaticData(); //Callimg static method with className, Static way
    }
}
