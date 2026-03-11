class Student       //Blueprint of real world entity known as object (Student)
{
    int RollNo;     //Field, Non-Static
    String Name;    //Field, Non-Static

    void Show()     //Method, Non-Static
    {
        System.out.println(RollNo);
        System.out.println(Name);
    }

}
class Test
{
    public static void main(String[] args) {
        System.out.println("Hello");
        int Num1;
        int Number=100;    //Local Variable, Initialization, LHS data type Declaration

        Num1=200;
        Num1=900;       //Re-assigment
        new Student();      //To create an object/instance of any class, Anonymous object

        Student s;          //To create ref variable of the class, here s is ref variable of class student

        Student s1=new Student();
        s1.Name="Malkeet";       //Accessing class field with the help of class ref variable
        s1.RollNo=101;

        s1.Show();                 //Calling Class method with the help of class ref variable

        Student s2=new Student();
        Student s3=new Student();
    }
}