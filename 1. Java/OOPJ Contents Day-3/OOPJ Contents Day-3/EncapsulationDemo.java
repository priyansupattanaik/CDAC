class Test
{
    private int Num1;
    int Num2;

    int getNum1()           //Getter
    {
        return this.Num1;
    }

    void setNum1(int Num1)  //Setter
    {
        this.Num1=Num1;
    }
    public Test()
    {

    }

    public Test(int Num1, int Num2)
    {
        this.Num1=Num1;
        this.Num2=Num2;
    }

    void ShowData()
    {
        System.out.println("Num1: "+this.Num1+" Num2: "+this.Num2);
    }
}

class TestEncap
{
    public static void main(String[] args) {
        Test t=new Test();

        t.setNum1(1000);
        t.Num2=900;

        t.ShowData();


        System.out.println("Num1 printed vy Getter: "+t.getNum1());
    }
}