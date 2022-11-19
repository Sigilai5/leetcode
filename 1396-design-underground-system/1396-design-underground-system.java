class UndergroundSystem {
    
    Map<Integer,Journey> journeys;
    Map<String,Average> averages;
 
    public UndergroundSystem() {   
       journeys = new HashMap();
       averages = new HashMap();
    }
    
    public void checkIn(int id, String stationName, int t) {
      journeys.put(id, new Journey(id,stationName,t));
    }
    
    public void checkOut(int id, String stationName, int t) {
      Journey arrival = journeys.get(id);
      journeys.remove(id);
        
      double timeDiff = t - arrival.t;
        
      String startEnd =  arrival.stationName + "," + stationName; 
        
        
      Average average = averages.containsKey(startEnd) ? averages.get(startEnd) : new Average();
       
      average.updateAverage(timeDiff);
        
      averages.put(startEnd,average);  
        
    }
    
   double getAverageTime(String startStation, String endStation) {
        String startEnd = startStation + "," + endStation;
        return averages.get(startEnd).getAverage();
       
    }
    

    class Journey {
        private int id;
        private String stationName;
        private int t;
        
        
        public Journey(int id, String stationName, int t){
            this.id = id;
            this.stationName = stationName;
            this.t =  t;
        }
 
    }
    
    
    class Average {
        private int customerCount = 0;
        private double totalTime = 0;
        
        public void updateAverage(double timeTaken){
            totalTime += timeTaken;
            customerCount  += 1;
            
        }
        
        public double getAverage(){
            return totalTime / customerCount;
        }
        
        
    }

    

 
    
    
}


//Nairobi -> Mombasa -> Average time: Time taken in total for all customers/number of customers
//Nairobi -> Mombasa -> Jack ->2 -> Brian -> 3
//Average -> 5/2 -> 2.5
