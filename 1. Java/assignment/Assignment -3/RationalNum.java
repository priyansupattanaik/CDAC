import java.util.Scanner;

class RationalNumber
{
    int numerator;
    int denominator;
    
    public RationalNumber(int numerator, int denominator)
    {
        this.numerator = numerator;
        this.denominator = denominator;
    }
    
    public RationalNumber add(RationalNumber r)
    {
        int newNumerator = (this.numerator * r.denominator) + (r.numerator * this.denominator);
        int newDenominator = this.denominator * r.denominator;
        return simplify(newNumerator, newDenominator);
    }
    
    public RationalNumber subtract(RationalNumber r)
    {
        int newNumerator = (this.numerator * r.denominator) - (r.numerator * this.denominator);
        int newDenominator = this.denominator * r.denominator;
        return simplify(newNumerator, newDenominator);
    }
    
    public RationalNumber multiply(RationalNumber r)
    {
        int newNumerator = this.numerator * r.numerator;
        int newDenominator = this.denominator * r.denominator;
        return simplify(newNumerator, newDenominator);
    }
    
    public RationalNumber divide(RationalNumber r)
    {
        int newNumerator = this.numerator * r.denominator;
        int newDenominator = this.denominator * r.numerator;
        return simplify(newNumerator, newDenominator);
    }
    
    public RationalNumber simplify(int num, int den)
    {
        int smallest = num;
        if (den < num)
        {
            smallest = den;
        }
        
        int gcd = 1;
        for (int i = 1; i <= smallest; i++)
        {
            if (num % i == 0 && den % i == 0)
            {
                gcd = i;
            }
        }
        
        num = num / gcd;
        den = den / gcd;
        
        return new RationalNumber(num, den);
    }
    
    public void display()
    {
        System.out.println(this.numerator + "/" + this.denominator);
    }
}

class RationalNum
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter the first rational number:");
        System.out.print("Numerator: ");
        int num1 = sc.nextInt();
        System.out.print("Denominator: ");
        int den1 = sc.nextInt();
        
        System.out.println("Enter the second rational number:");
        System.out.print("Numerator: ");
        int num2 = sc.nextInt();
        System.out.print("Denominator: ");
        int den2 = sc.nextInt();
        
        System.out.print("Enter the arithmetic operation (+,-,*,/): ");
        String op = sc.next();
        
        RationalNumber r1 = new RationalNumber(num1, den1);
        RationalNumber r2 = new RationalNumber(num2, den2);
        RationalNumber result = new RationalNumber(0, 1);
        
        if (op.equals("+"))
        {
            result = r1.add(r2);
        }
        else if (op.equals("-"))
        {
            result = r1.subtract(r2);
        }
        else if (op.equals("*"))
        {
            result = r1.multiply(r2);
        }
        else if (op.equals("/"))
        {
            result = r1.divide(r2);
        }
        
        System.out.print("Result: ");
        result.display();
    }
}