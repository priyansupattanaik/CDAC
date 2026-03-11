class Student
{
    int RollNo;
    String Name;

    void Show()
    {
        System.out.println(RollNo);
        System.out.println(Name);
    }
}
class TestStudent
{
    public static void main(String[] args) {
        Student s1=new Student();
        s1.RollNo=101;
        s1.Name="Malkeet";

        Student s2=new Student();
        s2.RollNo=102;
        s2.Name="Aditya";

        s1.Show();
        s2.Show();
    }
}