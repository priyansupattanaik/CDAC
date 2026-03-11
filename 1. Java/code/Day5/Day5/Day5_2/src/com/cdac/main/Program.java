package com.cdac.main;

import java.util.Scanner;

import com.cdac.Mangers.EmployeeManager;

public class Program {

	public static void main(String[] args) 
	{

		int choice;
		Scanner sc=new Scanner(System.in);
		EmployeeManager em=new EmployeeManager();
		
		
		do
		{
			System.out.println("======================Employee Management System======================");
			System.out.println("Press 1 to Add Employee");
			System.out.println("Press 2 to View All Employee");
			System.out.println("Press 3 to Update Employee");
			System.out.println("Press 4 to Delete Employee");
			System.out.println("Press 5 to Exit the Program");
			System.out.println("=======================================================================");
			System.out.println("Enter you choice");
			choice=sc.nextInt();
			
			switch (choice) 
			{
			case 1:
				em.AddEmployee();
				break;
			case 2:
				em.PrintEmployees();
				break;
			case 3:
				em.UpdateEmployee();
				break;
			case 4:
				em.DeleteEmployee();
				break;
			case 5:
				System.out.println("Exiting The Program! Bye Bye");
				break;
			default:
				System.out.println("Invalid Input");
				break;
			}
		}while(choice!=5);
		
		
		
	}
	

}
