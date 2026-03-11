class PolyTest
{
    static int Add(int a, int b)        //Method Overloading
    {
        return a+b;
    }
    static float Add(float a, float b, float c)
    {
        return a+b;
    }
    static float Add(float a, float b)
    {
        return a+b;
    }
    static double Add(double a, double b)
    {
        return a+b;
    }
    static double Add(double a, float b)
    {
        return a+b;
    }
    static double Add(float a, double b)
    {
        return a+b;
    }
    public static void main(String[] args) {
        
        System.out.println(Add(345.90, 3456.89));       //Compile-Time, Early Binding, Static Binding, Method Overloading
        System.out.println(Add(100.00f,200.89f));
    }
}
