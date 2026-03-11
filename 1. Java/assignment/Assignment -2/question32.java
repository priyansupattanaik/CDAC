class question32 {

    public static void main(String[] args) {
        
        Short S1 = Short.valueOf((short)93);

        byte b = S1.byteValue();
        short s = S1.shortValue();
        int i = S1.intValue();
        long l = S1.longValue();
        float f = S1.floatValue();
        double d = S1.doubleValue();

        System.out.println("Byte: " +b);
        System.out.println("Short: " +s);
        System.out.println("Int: " +i);
        System.out.println("Long: " +l);
        System.out.println("Float: " +f);
        System.out.println("Double: " +d);

    }
    
}
