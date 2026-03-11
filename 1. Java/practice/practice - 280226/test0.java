class rectangle {

    float length;
    float width;

    float calculateArea(){

        return length * width;
    }
    
    float calculatePerimeter(){

        return 2*(length + width);
    }

    public static void main(String[] args) {
        
        rectangle rect = new rectangle();

        rect.length = 23;
        rect.width = 43;

        float area = rect.calculateArea();
        System.out.println("Area of Rectangle:" + area);

        float perimeter = rect.calculatePerimeter();
        System.out.println("Perimeter of Rectangle:" + perimeter);

    }
}
