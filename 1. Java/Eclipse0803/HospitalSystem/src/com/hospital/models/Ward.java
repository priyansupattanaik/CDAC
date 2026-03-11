package com.hospital.models;

public class Ward {
    private int wardId;
    private String wardName;      // ICU, General, Emergency
    private int totalBeds;
    private int occupiedBeds;
    private double chargesPerDay;
    
    public Ward(int wardId, String wardName, int totalBeds, 
                int occupiedBeds, double chargesPerDay) {
        this.wardId = wardId;
        this.wardName = wardName;
        this.totalBeds = totalBeds;
        this.occupiedBeds = occupiedBeds;
        this.chargesPerDay = chargesPerDay;
    }
    
    // Getters and Setters...
    public int getWardId() { return wardId; }
    public void setWardId(int wardId) { this.wardId = wardId; }
    
    public String getWardName() { return wardName; }
    public void setWardName(String wardName) { this.wardName = wardName; }
    
    public int getTotalBeds() { return totalBeds; }
    public void setTotalBeds(int totalBeds) { this.totalBeds = totalBeds; }
    
    public int getOccupiedBeds() { return occupiedBeds; }
    public void setOccupiedBeds(int occupiedBeds) { this.occupiedBeds = occupiedBeds; }
    
    public double getChargesPerDay() { return chargesPerDay; }
    public void setChargesPerDay(double chargesPerDay) { this.chargesPerDay = chargesPerDay; }
    
    public int getAvailableBeds() {
        return totalBeds - occupiedBeds;
    }
    
    @Override
    public String toString() {
        return "Ward " + wardName + " (ID: " + wardId + "): " + 
               getAvailableBeds() + "/" + totalBeds + " beds available";
    }
}