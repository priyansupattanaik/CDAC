package com.cdac.main;

import java.util.Scanner;

class Person{
	
	String Name;
	int Age;
	String EmailID;
	long MobileNo;
	
	void AcceptRecord(){
		
		Scanner sc = new Scanner(System.in)
				
				System.out.println("Enter Name: ");
		this.Name = sc.next();
		
		System.out.println("Enter Age: ");
		this.Age = sc.next();
		
		System.out.println("Email ID: ");
		this.EmailID = sc.next();
		
		System.out.println("Enter Mobile No: ");
		this.MobileNo = sc.nextLong();
		
//		void PrintRecord() {
//			System.out.println("Name: " +this.Name+" Phone No: "+this.MobileNo);
//		}
	}
	
}

public class Program {
	
	

}
