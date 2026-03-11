class Mobile
{
    String BrandName;
    String Color;
    float Weight;
    double Price;

    public Mobile()     //Default Constructor
    {
        BrandName="Malkeet";
        Color="Blue";
        Weight=72.56f;
        Price=2672627.67;
    }

    public Mobile(String s1, String s2, float f, double d)
    {
        this.BrandName=s1;
        Color=s2;
        Weight=f;
        Price=d;
    }
    void PrintData()
    {
        System.out.println(BrandName);
        System.out.println(Color);
        System.out.println(Weight);
        System.out.println(Price);
    }
}

class ConstructorDemo {
    public static void main(String[] args) {
        Mobile m1=new Mobile();
        m1.BrandName="Apple";

        Mobile m2=new Mobile();
        m1.PrintData();
        m2.PrintData();

        Mobile m3=new Mobile("Samsung", "Red", 255.78f, 122654.89);     //Calling Paramterized
        m3.PrintData();

    }
}
