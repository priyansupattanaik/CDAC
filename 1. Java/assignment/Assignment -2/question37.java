public class question37 {

    public static void main(String[] args){

        Long L1 = Long.valueOf(642392L);

        byte b = L1.byteValue();
        short s = L1.shortValue();
        int i = L1.intValue();
        long l = L1.longValue();
        float f = L1.floatValue();
        double d = L1.doubleValue();

        System.out.println("Byte:" +b);
        System.out.println("Short:" +s);
        System.out.println("Int:" +i);
        System.out.println("Long:" +l);
        System.out.println("Float:" +f);
        System.out.println("Double:" +d);
        
    }
    
}
