class question16 {

public static void main(String[] args){

    long a = 1500000L;
String X = Long.toString(a);

System.out.println("Long to String:" + X);

        String binary  = Long.toBinaryString(a);
        String octal   = Long.toOctalString(a);
        String hexadecimal     = Long.toHexString(a);

System.out.println("Binary value:" + binary);
System.out.println("Octal Value:" + octal);
System.out.println("Hexadecimal Value:" + hexadecimal);

}

    
}
