class Test
{
    int Num1;
    int Num2;

    public Test()
    {

    }
    public Test(int Num1, int Num2)
    {
        this.Num1=Num1;
        this.Num2=Num2;
    }

    void Show()
    {
        System.out.println("Num1: "+this.Num1);
        System.out.println("Num2: "+this.Num2);
    }
}
class TestThis
{
    public static void main(String[] args) {

        Test t1=new Test();
        Test t2=new Test(100, 200);

        t1=t2;      //Shallow Copy

        t1.Num1=10;

        t2.Show();

        t2=null;  //Nullyfying the instance

        t2.Show();  //t2.Show(&this)
    }
}