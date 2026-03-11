class Student{

 int rollNo;
 String name;
 float marks;

 void displayDetail(){

 System.out.println("Roll No: " + this.rollNo);
 System.out.println("Name: " + name);
 System.out.println("Marks: " + marks);
 }

 public static void main(String[] args) {
    
    Student stud1 = new Student();

    stud1.rollNo = 23;
    stud1.name = "Priyansu";
    stud1.marks = 9;

    System.out.println("Student Details:");
    stud1.displayDetail();

 }


}