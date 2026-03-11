class Employee{

int EmpID;
String Name;

Employee(){

    EmpID = 0;
    Name = "Priyansu";
}
    Employee(int EmpID, String Name){

this.EmpID = EmpID;
this.Name = Name;

    }

    void PrintData(){

        System.out.println("EmpId: " + this.EmpID + " | Name: " + this.Name);
    }
}

public class TestEmployee {
    public static void main(String[] args) {
        // Calls the Default Constructor [7]
        Employee e1 = new Employee(); 
        
        // Calls the Parameterized Constructor [7]
        Employee e2 = new Employee(101, "Priya"); 
        
        e1.PrintData();
        e2.PrintData();
    }
}