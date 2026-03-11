class StringDemo
{
    public static void main(String[] args) {
        String str1="Malkeet";
        String str2="Singh";
        String str3=new String("Malkeet");



        System.out.println(str3.hashCode());
        System.out.println(str1.hashCode());

        if(str1.equals(str3))
        {
            System.out.println("Same");
        }
        else
        {
            System.out.println("Different");
        }
    }
}