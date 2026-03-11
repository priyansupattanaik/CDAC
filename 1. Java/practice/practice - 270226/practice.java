class Circle {

    float radius;
    float area;

    public void calculateArea(){
        this.area = (float) 3.14 * this.radius * this.radius;

    }
}

class testCircle{
public static void main(String[] args){
    Circle A = new Circle();
    A.radius = 3.89f;

    A.calculateArea();
    System.out.println("Area of Circle:" +A.area);
}
}