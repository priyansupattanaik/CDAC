abstract class Shape
{
    double Area;
    double Perimeter;
    public Shape()
    {
       
    }
    abstract void CalculateArea();
    
    abstract void CalculatePerimeter();
   
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
class TestAbstractClass
{
    public static void main(String[] args) {
        Circle c1=new Circle();

        c1.Radius=100;
        c1.CalculateArea();
        c1.PrintArea();
    }
}