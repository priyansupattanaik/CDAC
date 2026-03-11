class question22 {

    public static void main (String[] args){

        double A = 4.8;

        String Num = Double.toString(A);
        long bits = Double.doubleToLongBits(A);


        String binary  = Long.toBinaryString(bits);    
        String octal  = Long.toOctalString(bits);   
        String hexdecimal  = Long.toHexString(bits);   

        System.out.println("Double to string value:" + Num);
        System.out.println("Binary Value:" +binary);
        System.out.println("Octal Value:" + octal);
        System.out.println("Hexadecimal Value:" + hexdecimal);
        

    }
    
}
