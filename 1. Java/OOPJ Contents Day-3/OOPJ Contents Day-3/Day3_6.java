class TestArray
{
    public static void main(String[] args) {
        int arr[]=new int[10];

        for(int i=0;i<10;i++)
        {
            arr[i]=i*123;
        }


        for(int i=0;i<10;i++)
        {
            System.out.println(arr[i]);
        }
        int sum=0;
        for(int i=0;i<10;i++)
        {
            sum=sum+arr[i];
        }

        System.out.println("Array Sum: "+sum);
    }
    public static void main1(String[] args) {
        int arr[]=new int[10];

        arr[0]=10;
        arr[1]=20;
        arr[2]=30;
        arr[3]=40;
        arr[4]=50;
        arr[5]=60;
        arr[6]=70;
        arr[7]=80;
        arr[8]=90;
        arr[9]=100;

        System.out.println(arr[5]);

        for(int i=0;i<10;i++)
        {
            System.out.println(arr[i]);
        }

    }
}