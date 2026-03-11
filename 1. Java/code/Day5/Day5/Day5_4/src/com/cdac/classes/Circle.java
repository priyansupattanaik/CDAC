package com.cdac.classes;

import com.cdac.interfaces.ICircle;

public class Circle extends Shape implements ICircle
{
	double Radius;
	
	public double getRadius() {
		return Radius;
	}




	public void setRadius(double radius) {
		Radius = radius;
	}


	public Circle() {
		super();
	}


	public Circle(double radius) {
		super();
		Radius = radius;
	}




	public void CalculateArea()
	{
		this.Area=Math.PI*this.Radius*this.Radius;
	}


}
