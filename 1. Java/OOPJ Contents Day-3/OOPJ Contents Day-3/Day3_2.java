class Test
{
    int Num1;
    int Num2;
    int Num3;

    public Test()
    {
        System.out.println("Am Cons with Zero Args");
    }
    public Test(int Num1)
    {
        this(); //Expicitly it will call cons with zero args
        this.Num1=Num1;
        System.out.println("Am Cons with One Args");
    }
    public Test(int Num1, int Num2)
    {
        this(1);//Expicitly it will call cons with 1 args
        this.Num1=Num1;
        this.Num2=Num2;
        System.out.println("Am Cons with Two Args");
    }
    public Test(int Num1, int Num2, int Num3)
    {
        this(1,2);  //Expicitly it will call cons with 2 args
        this.Num1=Num1;
        this.Num2=Num2;
        this.Num3=Num3;
        System.out.println("Am Cons with Three Args");
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

      //  Test t=new Test();      //Cons with Zero Args
          

          Test t=new Test(1,2,3);
    }
}