class Counter {

    int count;
    static int totalObject = 0;


    Counter(){
        totalObject++;
    }

void show(){
        System.out.println("Count: " +count);
        System.out.println("Total Object: " +totalObject);
}
    

public static void main(String[] args){

    Counter c = new Counter();

    c.count = 5;

    c.show();
    }
}
