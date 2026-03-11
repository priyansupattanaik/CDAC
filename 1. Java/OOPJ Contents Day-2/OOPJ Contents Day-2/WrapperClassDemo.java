class TestWrapper
{
    public static void main(String[] args) {
        
        int Num1=100;       //Local int variable, will get memory inside SF

        Integer a1=new Integer(Num1);       //

        a1=200;
        System.out.println("Num1="+Num1);
        System.out.println("a1="+a1);


        Integer a2=200;     //new Integer(200)

        int Num2=a2;        //UnBoxing

        System.out.println("A2="+a2);
        System.out.println("Num2="+Num2);

    }
}
