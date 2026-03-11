class question20 {

    public static void main (String[] args){

        float F1 = 3.25f;
        float F2 = 6.37f;

        float Min_Value = Float.min(F1, F2);
        float Max_Value = Float.max(F1, F2);

        float sum = Float.sum(F1, F2);

        System.out.println("Minimum Value:" + Min_Value);
        System.out.println("Maximum Value:" + Max_Value);
        System.out.println("Sum:" + sum);

    }
    
}
