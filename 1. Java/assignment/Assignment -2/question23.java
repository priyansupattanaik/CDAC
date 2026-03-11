class question23 {
    
    public static void main(String[] args){

        double D1 = 3.53535;
        double D2 = 6.33434;

        double min_value = Double.min(D1, D2);
        double max_value = Double.max(D1, D2);
        double sum = Double.sum(D1, D2);

        System.out.println("Minimum Value:" + min_value);
        System.out.println("Maximum Value:" + max_value);
        System.out.println("Sum:" + sum);
    }
    
}
