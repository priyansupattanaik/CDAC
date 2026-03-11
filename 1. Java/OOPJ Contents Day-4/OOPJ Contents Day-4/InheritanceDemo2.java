class Shape
{
    double Area;
    double Perimeter;
    public Shape()
    {
       
    }
    void CalculateArea()
    {
        System.out.println("Calculate Area of SHape");
    }
    void CalculatePerimeter()
    {

    }
    void PrintArea()
    {
        System.out.println(this.Area);
    }
    void PrintPerimeter()
    {
        System.out.println(this.Perimeter);
    }
}
class Circle extends Shape
{
    double Radius;

    public Circle()
    {
        
    }
    public Circle(double Radius)
    {
        this.Radius=Radius;
    }
    void CalculateArea()        //method overriding
    {
       // this.Area=Math.PI*this.Radius*this.Radius;
       System.out.println("CalculateArea of Circle");
    }
    void CalculatePerimeter()
    {
        this.Perimeter=2*Math.PI*this.Radius;
    }
}
class TestMethOverriding
{
    public static void main(String[] args) {
        Circle c1=new Circle();
        c1.CalculateArea();

        Shape s1=new Circle();
        s1.CalculateArea();
    }
}