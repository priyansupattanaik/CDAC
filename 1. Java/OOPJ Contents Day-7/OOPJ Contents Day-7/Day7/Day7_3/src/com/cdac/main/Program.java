package com.cdac.main;

import java.util.ArrayList;
import java.util.List;
import java.util.OptionalInt;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Program {

	public static void main(String[] args) {
		
	List<String> slist = new ArrayList<>();
	
	slist.add("Malkeet");
	slist.add("Sahil");
	slist.add("Akash");
	slist.add("Zoya");
	slist.add("Isha");
	
	List<Integer> lenths=slist.stream().map(String::length).collect(Collectors.toList());
	
	System.out.println(lenths);
	
	
	}

}
