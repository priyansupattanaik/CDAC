package com.cdac.main;

import java.util.TreeSet;

class Student implements Comparable<Student>
{
	int RollNo;
	String Name;
	float Fees;
	
	public Student() {
		super();
	}

	public Student(int rollNo, String name) {
		super();
		RollNo = rollNo;
		Name = name;
	}

	@Override
	public String toString() {
		return "Student [RollNo=" + RollNo + ", Name=" + Name + "]";
	}

	@Override
	public int compareTo(Student o) {
		
		//return Integer.compare(this.RollNo, o.RollNo);
		
		//return this.Name.compareTo(o.Name);
		
		//return Float.compare(this.Fees, o.Fees);
		
		if(this.RollNo>o.RollNo)
		{
			return 1;
		}
		if(this.RollNo<o.RollNo)
		{
			return -1;
		}
		return 0;
	}
	
	
}


public class Program {

	public static void main(String[] args) {
		TreeSet<String> tset=new TreeSet<String>();
		
		tset.add("Zeenat");
		tset.add("Raj");
		tset.add("Abhishiek");
		tset.add("Abhishiek");
		
		System.out.println(tset);
		
		
		TreeSet<Integer> iset=new TreeSet<Integer>();
		
		iset.add(200);
		iset.add(20);
		iset.add(10);
		iset.add(1);
		iset.add(200);
		iset.add(20);
		iset.add(10);
		iset.add(1);

		
		System.out.println(iset);
		
		
		
		TreeSet<Student> sset=new TreeSet<Student>();
		
		sset.add(new Student(110, "Malkeet"));
		sset.add(new Student(1, "Zeenat"));
		sset.add(new Student(10, "Aditya"));
		sset.add(new Student(2, "Rahul"));
		
		
		System.out.println(sset);
		
	}

}
