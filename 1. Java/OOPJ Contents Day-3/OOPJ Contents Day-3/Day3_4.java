import java.util.Scanner;

class Student
{
    int RollNo;
    String Name;
    int Age;
    float Fees;

    public Student()
    {

    }

    void AddStudent()
    {
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter RollNo: ");
        this.RollNo=sc.nextInt();
        System.out.println("Enter Age: ");
        this.Age=sc.nextInt();
        System.out.println("Enter Fees: ");
        this.Fees=sc.nextFloat();
        System.out.println("Enter Name: ");
        this.Name=sc.next();
    }
    void UpdateStudent()
    {
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter Age: ");
        this.Age=sc.nextInt();
        System.out.println("Enter Fees: ");
        this.Fees=sc.nextFloat();
        System.out.println("Enter Name: ");
        this.Name=sc.next();
    }
    void PrintRecord()
    {
        System.out.println("Roll No: "+this.RollNo+" Name: "+this.Name+" Age: "+this.Age+" Fees: "+this.Fees);
    }
}
class TestStudent
{
    public static void main(String[] args) {
        Student s1=new Student();
        s1.PrintRecord();

        s1.AddStudent();
        System.out.println("The Original Record is: ");
        s1.PrintRecord();
        s1.UpdateStudent();
        System.out.println("The Updated Record is: ");
        s1.PrintRecord();
    }
}