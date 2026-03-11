package com.cdac.main;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.OptionalInt;
import java.util.stream.IntStream;

class Test
{
	private int Num1;
	private int Num2;
	
	
	private Test(int Num1, int Num2)
	{
		this.Num1=Num1;
		this.Num2=Num2;
	}

	public int getNum1() {
		return Num1;
	}

	public int getNum2() {
		return Num2;
	}
	
}

public class Program {
	
	public static void main(String[] args) throws ClassNotFoundException, NoSuchMethodException, SecurityException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException {
		
		Class<?> c1=null;
		
		c1=Class.forName("com.cdac.main.Test");
		
		Constructor<?> carr[]=c1.getDeclaredConstructors();
		for(Constructor<?> c:carr)
		{
			System.out.println(c.getName());
		}
		
		Constructor<?> con=c1.getDeclaredConstructor(int.class, int.class);
		
		con.setAccessible(true);
		
		Test t1=(Test)con.newInstance(100,200);
		
		System.out.println(t1.getNum1());
		System.out.println(t1.getNum2());
	}
}
