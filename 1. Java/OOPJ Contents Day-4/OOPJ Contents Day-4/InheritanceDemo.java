class Shape
{
    double Area;
    double Perimeter;
    public Shape()
    {
        System.out.println("Am Cons of shape");
    }
    void CalculateArea()
    {

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
        System.out.println("Am cons of Circle");
    }
    public Circle(double Radius)
    {
        this.Radius=Radius;
    }
    void CalculateArea()
    {
        this.Area=Math.PI*this.Radius*this.Radius;
    }
    void CalculatePerimeter()
    {
        this.Perimeter=2*Math.PI*this.Radius;
    }
}
class Rectangle extends Shape
{
    double Length;
    double Width;

    void CalculateArea()
    {
        this.Area=this.Length*this.Width;
    }
    void CalculatePerimeter()
    {
        this.Perimeter=2*(this.Length+this.Width);
    }
}
class TestCircle
{
    public static void main(String[] args) {
        Circle c1=new Circle(20);
        c1.CalculateArea();
        c1.CalculatePerimeter();
        c1.PrintArea();
        c1.PrintPerimeter();
    }
}
class TestRectangle
{
    public static void main(String[] args) {
        Rectangle r1=new Rectangle();
        r1.Length=10;
        r1.Width=20;
        r1.CalculateArea();
        r1.PrintArea();
    }
}
class TestCons
{
    public static void main(String[] args) {
       // Circle c1=new Circle();
        Circle c2=new Circle(300.0);
    }
}
class TestCasting
{
    public static void main(String[] args) {
       Shape s1= new Circle();       //Upcasting

    }
}