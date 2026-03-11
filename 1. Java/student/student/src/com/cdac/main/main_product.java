package com.cdac.main;
import java.util.Scanner;

import com.cdac.manager.product_manager;

public class main_product {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		product_manager pm = new product_manager();

	     
	      int choice;
	      do{
	         System.out.println("        ");
	         System.out.println("==========================================");
	         System.out.println("press 1 to Add the product : ");
	         System.out.println("press 2 to View All Products : ");
	         System.out.println("press 3 to Search Product by ID : ");
	         System.out.println("press 4 to Update Product : ");
	         System.out.println("press 5 to Delete Product : ");
	         System.out.println("press 6 to Sort Products by Name : ");
	         System.out.println("press 7 to Sort Products by Price : ");
	         System.out.println("press 8 to Sort Products by Quantity : ");
	         System.out.println("press 9 to  Sort Products by Rating : ");
	         System.out.println("press 10 for exit !!! ");
	         

	         System.out.println("Enter your option : ");
	         choice =sc.nextInt();
	         
	         switch(choice){
	            case 1:{
	                   pm.AddProduct();
	               break;
	            }
	            case 2:{
	                   pm.ViewAllProducts();
	               break;
	            }
	            case 3:{
	            	            
	                    pm.SearchByID();
	               break;
	            }
	            case 4:{
	            		pm.UpdateProduct();
	                      
	               break;
	              
	            }
	            case 5:
	            {
	            	pm.DeleteProduct();
	            	break;
	            }
	            case 6:{
	              pm.SortbyName();
	               break;
	            }
	            case 7:{
		               pm.SortbyPrice();
		               break;
		            }
	            case 8:{
		               pm.SortbyQuantity();
		               break;
		            }
	            case 9:{
		               pm.SortbyRating();
		               break;
		            }
	            case 10:{
		               System.out.println("Exit!!!!!!!!");
		               break;
		            }
	            default:{
	               System.out.println("Invalid Choice");
	               break;
	            }

	         }

	      }while(choice != 10);

	}

}