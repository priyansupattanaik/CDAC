package com.cdac.main;

enum MyMath
{
	Add,Sub,Div,Mul;
}

public class Program {

	public static void main(String[] args) {
		
		System.out.println("Add: "+MyMath.Add.ordinal());
		System.out.println("Sub: "+MyMath.Sub.ordinal());
		System.out.println("Mul: "+MyMath.Mul.ordinal());
		
		System.out.println("Add Value: "+MyMath.Add.name());
		
		
		Integer a1=10;
	}

}
