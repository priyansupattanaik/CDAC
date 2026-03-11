package com.movie.models;

public class Movie {
	
	private int movieID;
	private String title;
	private String director;
	private String genre;
	private int rating;
	private int releaseYear;
	
	public Movie(int movieID, String title, String director, double rating, int releaseYear, String genre) {
		super();
		this.movieID = movieID;
		this.title = title;
		this.director = director;
		this.genre = genre;
		this.rating = (int) rating;
		this.releaseYear = releaseYear;
	}

	public Movie(int id, String title2, String director2, int rating2, int year) {
		// TODO Auto-generated constructor stub
	}

	public int getMovieID() {
		return movieID;
	}

	public void setMovieID(int movieID) {
		this.movieID = movieID;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getDirector() {
		return director;
	}

	public void setDirector(String director) {
		this.director = director;
	}

	public String getGenre() {
		return genre;
	}

	public void setGenre(String genre) {
		this.genre = genre;
	}

	public int getRating() {
		return rating;
	}

	public void setRating(int i) {
		this.rating = i;
	}

	public int getReleaseYear() {
		return releaseYear;
	}

	public void setReleaseYear(int releaseYear) {
		this.releaseYear = releaseYear;
	}

	@Override
	public String toString() {
		return "Movie=" + movieID + ", title=" + title + ", director=" + director + ", genre=" + genre
				+ ", rating=" + rating + ", releaseYear=" + releaseYear;
	}

	public String getD() {
		// TODO Auto-generated method stub
		return null;
	}

	public void add(Movie movie) {
		// TODO Auto-generated method stub
		
	}
	
	
	
	

}
