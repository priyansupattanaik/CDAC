package com.cdac.manager;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import com.cdac.model.Product;


public class product_manager{
	
	ArrayList<Product> plist ;
	
	
	public product_manager(){
		
		plist = new ArrayList<Product>();
		
		plist.add(new Product(101, "Laptop", 10, "12-01-2024", 55000.50f, "4.5", "Electronics"));
		plist.add(new Product(102, "Mobile Phone", 25, "05-03-2024", 25000.00f, "4.3", "Electronics"));
		plist.add(new Product(103, "Headphones", 50, "20-02-2024", 1999.99f, "4.2", "Accessories"));
		plist.add(new Product(104, "Smart Watch", 15, "18-01-2024", 7999.50f, "4.4", "Electronics"));
		plist.add(new Product(105, "Office Chair", 8, "10-12-2023", 4500.75f, "4.1", "Furniture"));
		plist.add(new Product(106, "Notebook", 100, "01-02-2025", 120.00f, "4.0", "Stationery"));
		plist.add(new Product(107, "Pen Set", 200, "15-01-2025", 250.50f, "3.9", "Stationery"));
		plist.add(new Product(108, "Water Bottle", 60, "22-11-2024", 350.00f, "4.2", "Accessories"));
		plist.add(new Product(109, "Backpack", 30, "30-10-2024", 1800.00f, "4.3", "Bags"));
		plist.add(new Product(110, "Keyboard", 40, "14-03-2024", 950.00f, "4.4", "Computer Accessories"));
	}
	
	Product p = new Product();
	
	public void AddProduct() {
		Scanner sc=new Scanner(System.in);
//		Product p = new Product();
		System.out.println("Enter the Product Id");
		p.setProductId(sc.nextInt());
		System.out.println("Enter the Product Name");
		p.setname(sc.next());

		System.out.println("Enter the Product Quantitiy");
		p.setQuantity(sc.nextInt());
		

		System.out.println("Enter the Product ManufactureDate");
		p.setManufactureDate(sc.next());

		System.out.println("Enter the Product price ");
		p.setPrice(sc.nextFloat());

		System.out.println("Enter the Product Rating");
		p.setRating(sc.next());

		System.out.println("Enter the Product Category");
		p.setCategory(sc.next());

		plist.add(p);

		System.out.println("Product Record Added Successfully");

	}
	
	
	public void ViewAllProducts() {
		plist.stream().forEach(p->System.out.println(p));

		
	}
	
	public void SearchByID() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the product Id: ");
		int SearchId=sc.nextInt();
		plist.stream().filter(p->p.getProductId()== SearchId).forEach(System.out :: println);

	}
	
	
	public void  UpdateProduct(){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the product Id: ");
		int SearchId=sc.nextInt();
		boolean flag = true;
		
		for( Product p : plist) {
			
			if (p.getProductId() == SearchId) {
				flag = false;
				
				System.out.println("Enter the Product Name");
				p.setname(sc.next());

				System.out.println("Enter the Product Quantitiy");
				p.setQuantity(sc.nextInt());
				

				System.out.println("Enter the Product ManufactureDate");
				p.setManufactureDate(sc.next());

				System.out.println("Enter the Product price ");
				p.setPrice(sc.nextFloat());

				System.out.println("Enter the Product Rating");
				p.setRating(sc.next());

				System.out.println("Enter the Product Category");
				p.setCategory(sc.next());

				plist.add(p);

				System.out.println("Product Record Added Successfully");	
				break;
				
			}
		}
		if (flag == true) {
			System.out.println("Record not found!!!");
			
		}
		
		
	}
	
    public void  DeleteProduct(){
    	Scanner sc = new Scanner(System.in);
		System.out.println("Enter the product Id: ");
		int SearchId=sc.nextInt();
		boolean flag = true;
		
		for( Product p :plist) {
			
			if (p.getProductId() == SearchId) {
				flag = false;
				plist.remove(p);
				System.out.println("Product Record Deleted Successfully");	
				break;
			}
		}
		
		plist.remove(p);
		if (flag == true) {
			System.out.println("Record not found!!!");
			
		}
	}
    
    public void  SortbyName(){
    	plist.stream().sorted((p1,p2)->p1.getname().compareTo(p2.getname())).forEach(System.out :: println);
		
	}

    public void  SortbyPrice(){
     Collections.sort(plist, (p1,p2)->Float.compare(p1.getPrice(), p2.getPrice()));
		
		for(Product p:plist)
		{
			System.out.println(p);
		}

	
    }
    
    public void  SortbyQuantity(){
     Collections.sort(plist, (p1,p2)->Integer.compare(p1.getQuantity(), p2.getQuantity()));
		
		for(Product p:plist)
		{
			System.out.println(p);
		}

	
    }
    
    public void  SortbyRating(){
    	plist.stream().sorted((p1,p2)->p1.getRating().compareTo(p2.getRating())).forEach(System.out :: println);
    }
    

}