class question28 {
 public static void main(String[] args) {
    
    Byte s1 = Byte.valueOf((byte) 120);

    byte b = s1.byteValue();
    short s = s1.byteValue();
    int i = s1.intValue();
    long l = s1.longValue();
    float f = s1.longValue();
    double d = s1.longValue();

    System.out.println("byte: " +b);
    System.out.println("short: " +s);
    System.out.println("int: " +i);
    System.out.println("long: " +l);
    System.out.println("float: " +f);
    System.out.println("double: " +d);
}   
}
