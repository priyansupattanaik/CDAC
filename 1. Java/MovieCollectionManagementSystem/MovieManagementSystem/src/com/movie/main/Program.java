package com.movie.main;

import java.util.Scanner;

import com.movie.managers.MovieManager;

public class Program {
	
	public static void main(String [] args) {
		
		Scanner sc = new Scanner(System.in);
		
		MovieManager manager = new MovieManager();
		
		int choice;
		
		do {
				System.out.println("1) Add Movies");
				System.out.println("2) View All Movies");
				System.out.println("3) Search Movie by ID");
				System.out.println("4) Update Movie");
				System.out.println("5) Delete Movie");
				System.out.println("6) Sort Movies by Title");
				System.out.println("7) Sort Movies by Director");
				System.out.println("8) Sort Movies by Rating");
				System.out.println("9) Sort Movies by Release Year");
				System.out.println("10) Exit");
				
				System.out.print("Enter choice: ");
	            choice = sc.nextInt();

	            switch (choice) {

	                case 1: manager.addMovie(); break;
	                case 2: manager.viewMovies(); break;
	                case 3: manager.searchMovie(); break;
	                case 4: manager.updateMovie(); break;
	                case 5: manager.deleteMovie(); break;
	                case 6: manager.sortByTitle(); break;
	                case 7: manager.sortByDirector(); break;
	                case 8: manager.sortByRating(); break;
	                case 9: manager.sortByReleaseYear(); break;
	                case 10: System.out.println("Exiting..."); break;
	                default: System.out.println("Invalid choice");
						
	            }

        } while (choice != 11);

        sc.close();
    }
}
