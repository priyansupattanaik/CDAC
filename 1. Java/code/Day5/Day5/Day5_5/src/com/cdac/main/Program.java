package com.cdac.main;

import java.io.IOException;
import java.sql.SQLException;

public class Program {

static void Display() throws IOException, SQLException, NullPointerException
{
	System.out.println("Hello From Display");
}
public static void main(String[] args) {
	
	try {
		Display();
	} catch (Throwable es) {
		// TODO Auto-generated catch block
		es.printStackTrace();
	}
}
public static void main3(String[] args) {
		
		
		int Num1=100;
		int Num2=0;
		int Res=0;
		try
		{
			Res=Num1/Num2;
			System.out.println("The Res: "+Res);
		}
		catch(ArithmeticException ex)
		{
			System.out.println(ex.getMessage());
		}
		finally {
			System.out.println("Finally Block executed");
			System.out.println("All Resources released");
		}
		
		
		System.out.println("Rest of the program");
		System.out.println("Main Ends Here");
		
	}
public static void main2(String[] args) {
		
		
		int Num1=100;
		int Num2=0;
		int Res=0;
		try
		{
			Res=Num1/Num2;
			System.out.println("The Res: "+Res);
		}
		finally {
			System.out.println("Finally Block executed");
			System.out.println("All Resources released");
		}
		
		
		System.out.println("Rest of the program");
		System.out.println("Main Ends Here");
		
	}
	public static void main1(String[] args) {
		
		
		int Num1=100;
		int Num2=5;
		int Res=0;
		try
		{
			Res=Num1/Num2;
			System.out.println("The Res: "+Res);
		}
		catch(ArithmeticException ex)
		{
			System.out.println(ex.getMessage());
		}
		
		
		System.out.println("Rest of the program");
		System.out.println("Main Ends Here");
		
	}
}
