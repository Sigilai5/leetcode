class UndergroundSystem {
    
       private final String DELIMETER = ",";
       
       Map<Integer,Journey> journeys;
       Map<String,Averages> averages;

    
    public UndergroundSystem() {
       journeys = new HashMap<>();
       averages = new HashMap<>();
        
    }
    
    public void checkIn(int id, String stationName, int t) {
      journeys.put(id,new Journey(id,stationName,t));
    }
    
    public void checkOut(int id, String stationName, int t) {
      Journey getJourney = journeys.get(id);
      journeys.remove(id);
      
      int timeDifference = t - getJourney.time;  
        
      String key = getJourney.stationName + DELIMETER + stationName;
        
      Averages average = averages.containsKey(key) ? averages.get(key) : new Averages();
        
      average.updateAverage(timeDifference);
        
      averages.put(key,average);  
        
    }
    
    public double getAverageTime(String startStation, String endStation) {
       String key = startStation + DELIMETER + endStation;
       return averages.get(key).getAverages(); 
        
    }
    

   class Journey {
       private int id;
       private String stationName; 
       private int time;
       
       public Journey(int id, String stationName, int time){
           this.id = id;
           this.stationName = stationName;
           this.time = time;
       }
   }
    
    
   class Averages {
       private double totalTime = 0;
       private int totalCustomers = 0;
       
       public void updateAverage(int timeDifference){
           totalTime += timeDifference;
           totalCustomers+=1;
       }
       
       
       public double getAverages(){
           return totalTime / totalCustomers;
       }
   } 
    
    
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */