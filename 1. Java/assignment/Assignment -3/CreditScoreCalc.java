import java.util.Scanner;

class CreditScoreCalculator
{
    int creditHistory;
    double creditUtilization;
    
    public CreditScoreCalculator()
    {
        this.creditHistory = 0;
        this.creditUtilization = 0;
    }
    
    public CreditScoreCalculator(int creditHistory, double creditUtilization)
    {
        this.creditHistory = creditHistory;
        this.creditUtilization = creditUtilization;
    }
    
    public void setCreditHistory(int creditHistory)
    {
        this.creditHistory = creditHistory;
    }
    
    public void setCreditUtilization(double creditUtilization)
    {
        this.creditUtilization = creditUtilization;
    }
    
    
    public int getCreditHistory()
    {
        return this.creditHistory;
    }
    
    public double getCreditUtilization()
    {
        return this.creditUtilization;
    }
   
    
    public int calculateCreditScore()
    {
        int creditScore;
        
        if (this.creditUtilization < 30)
        {
            creditScore = (this.creditHistory * 15) + (int)(this.creditUtilization * 30) + 55;
        }
        else
        {
            creditScore = (this.creditHistory * 15) + (int)(this.creditUtilization * 30) + 35;
        }
        
        return creditScore;
    }
}

class CreditScoreCalc
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter credit history: ");
        int history = sc.nextInt();
        
        System.out.println("Enter credit utilization percentage: ");
        double utilization = sc.nextDouble();
    
        
        CreditScoreCalculator csc = new CreditScoreCalculator(history, utilization);
        
        int score = csc.calculateCreditScore();
        
        System.out.println("Calculated Credit Score: " + score);
    }
}