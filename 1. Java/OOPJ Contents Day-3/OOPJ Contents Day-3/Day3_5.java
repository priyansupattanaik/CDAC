class ElectricityBoard
{
    int CustomerId;
    float BillAmount;
    int NoofUnits;

    public ElectricityBoard(int CustomerId, int NoofUnits)
    {
        this.CustomerId=CustomerId;
        this.NoofUnits=NoofUnits;
    }

    void GenerateBill()
    {
        if(this.NoofUnits<=100)
        {
            this.BillAmount=this.NoofUnits*5;
        }
        if(this.NoofUnits>100 && this.NoofUnits<=200)
        {
            this.BillAmount=100*5+(this.NoofUnits-100)*7;
        }
        if(this.NoofUnits>200)
        {
            this.BillAmount=100*5+100*7+(this.NoofUnits-200)*10;
        }
    }
}
class TestElectricity
{
    public static void main(String[] args) {
        ElectricityBoard e1=new ElectricityBoard(101, 234);
        e1.GenerateBill();

        System.out.println("The Bill is: "+e1.BillAmount);
    }
}