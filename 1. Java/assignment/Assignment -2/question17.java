class question17 {


    public static void main (String[] args){

        long a = 7463493L;
        long b = 249284L;

        long min = Long.min(a, b);
        long max = Long.max(a, b);
        long sum = Long.sum(a, b);

        System.out.println("Minimum: " + min);
        System.out.println("Maximum: " + max);
        System.out.println("Sum: " + sum);
    }
    
}
