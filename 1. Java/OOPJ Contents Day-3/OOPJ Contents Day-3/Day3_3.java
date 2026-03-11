class Test
{
    static int counter;

    static
    {
        counter=0;
    }
    public Test()
    {
       counter++;
    }
}
class TestThis
{
    public static void main(String[] args) {

        new Test();
        new Test();
        new Test();
        System.out.println("No. of Instance: "+Test.counter);
    }
}