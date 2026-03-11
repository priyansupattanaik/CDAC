class book {

    String title;
    String author;
    int price;

    void displyaBook(){

        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Price: " + price);
    }

    public static void main(String[] args) {
        
        book book1 = new book();

        book1.title = "Grady booch";
        book1.author = "Priyansu";
        book1.price = 25000;

        System.out.println("Book Details:");
        book1.displyaBook();
    }
    
}
