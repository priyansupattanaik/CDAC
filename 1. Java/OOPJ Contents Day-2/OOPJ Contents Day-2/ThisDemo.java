import java.util.Scanner;

class Test
{
    int Num1;
    int Num2;

    static int Num3;
    public Test()
    {

    }
    public Test(int Num1, int Num2)
    {
        this.Num1=Num1;
        this.Num2=Num2;
        Test.Num3=200;
    }
    public static void GetData()
    {
        //this.Num1=100;    //NOTOK
    }
    void Show()
    {
        System.out.println(this.Num1);
        System.out.println(this.Num1);
        System.out.println(this.Num2);
    }
}
class ThisTest
{
    public static void main(String[] args) {
        Test t1=new Test();
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number");
        t1.Num1=sc.nextInt();
        System.out.println("Enter a number");
        t1.Num2=sc.nextInt();
        t1.Show();
        Test.GetData();
    }
}