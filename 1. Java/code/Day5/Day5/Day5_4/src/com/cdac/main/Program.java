package com.cdac.main;

import com.cdac.classes.Circle;

public class Program {

	public static void main(String[] args) {
		
		Circle c1=new Circle(60);
		
		c1=null;
		
		try
		{
			c1.CalculateArea();
		}
		catch(NullPointerException ex)
		{
			ex.printStackTrace();;
		}
		//c1.PrintArea();

	}

}
