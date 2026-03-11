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
        
        Student arr[]=new Student[5];
        for(int i=0;i<5;i++)
        {
            arr[i]=new Student();
        }

        for(int i=0;i<5;i++)
        {
            arr[i].PrintRecord();
        }
        for(int i=0;i<5;i++)
        {
            arr[i].AddStudent();
        }
        for(int i=0;i<5;i++)
        {
            arr[i].PrintRecord();
        }
        Scanner sc =new Scanner(System.in);
        int rn;
        System.out.println("Enter the RollNo: ");
        rn=sc.nextInt();

        boolean flag=false;
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i].RollNo==rn)
            {
                flag=true;
                arr[i].UpdateStudent();
                System.out.println("Record Updated Successfully");
                arr[i].PrintRecord();
                break;
            }
        }
        if(flag==false)
        {
            System.out.println("Record Not Found");
        }
        
    }
}
