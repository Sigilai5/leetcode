class UndergroundSystem {
    Map<Integer,Journey> journeys;   //Check in time
    Map<String,Average> averages;           //Record total time and number of customers
    
  
    
    public UndergroundSystem() {   
       journeys = new HashMap();
       averages = new HashMap(); 
    }
    
    public void checkIn(int id, String stationName, int t) {
        journeys.put(id,new Journey(id,stationName,t));
    }
    
    public void checkOut(int id, String stationName, int t) {
    Journey journey = journeys.get(id);
    journeys.remove(id);      //Journey is complete
        
    int timeDifference = t - journey.t;
        
    String keyStation = journey.stationName + "," + stationName;    
        
    Average average = averages.containsKey(keyStation) ? averages.get(keyStation) : new Average();   
        
    average.updateAverage(timeDifference);  
        
    averages.put(keyStation,average);    
        
    }
    
    public double getAverageTime(String startStation, String endStation) {
      String keyStation = startStation + "," + endStation;  
      return averages.get(keyStation).getAverage();  
        
        
    }
    
    class Journey {
        private int id;
        private String stationName;
        private int t;
        
        public Journey(int id, String stationName, int t){
            this.id = id;
            this.stationName = stationName;
            this.t = t;
        }
        
    }
    
    
    class Average {
        private double totalTime = 0;
        private int customerCount = 0;
        
        public void updateAverage(int timeDifference){
            totalTime += timeDifference;
            customerCount++;
            
        }
        
        public double getAverage(){
            return totalTime / customerCount;
        }
        
    }
 
    
    
}




// Your UndergroundSystem object will be instantiated and called as such:
// obj = UndergroundSystem()
// obj.checkIn(id,stationName,t)
// obj.checkOut(id,stationName,t)
// param_3 = obj.getAverageTime(startStation,endStation)


//A->B  3 
//A->B  2
//A->B  4

//A->C

//A->C


//Average->(3+2+4)/3 -> 3