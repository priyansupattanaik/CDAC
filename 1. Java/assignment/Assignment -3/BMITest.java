import java.util.Scanner;

class BMICalculator {
    double height;
    double weight;
    
    public BMICalculator() {
    }
    
    public BMICalculator(double height, double weight) {
        this.height = height;
        this.weight = weight;
    }
    
    public double getHeight() {
        return height;
    }
    public double getWeight() {
        return weight;
    }

    public void setHeight(double height) {
        this.height = height;
    }
    
    
    public void setWeight(double weight) {
        this.weight = weight;
    }
    
    public double calculateBMI() {
        return weight / (height * height);
    }
}

class BMITest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter height in m: ");
        double height = sc.nextDouble();
        System.out.println("Enter weight in kg: ");
        double weight = sc.nextDouble();
        
        BMICalculator bmiCalc = new BMICalculator();
        bmiCalc.setHeight(height);
        bmiCalc.setWeight(weight);
        
        double bmi = bmiCalc.calculateBMI();
        System.out.println("BMI: " + bmi);
    }
}