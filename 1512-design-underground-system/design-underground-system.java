class UndergroundSystem {
    Map<Integer,Journey> journeys; 
    Map<String,Average> averages;

    public UndergroundSystem() {
        journeys = new HashMap<>();
        averages = new HashMap<>();
    }
    
    public void checkIn(int id, String stationName, int t) {
        this.journeys.put(id,new Journey(id,stationName,t));
    }
    
    public void checkOut(int id, String stationName, int t) {
        Journey journey = this.journeys.get(id);
        String stations = journey.stationName + "," + stationName;
        int timeDif = t - journey.t;

        Average average = this.averages.containsKey(stations) ? this.averages.get(stations) : new Average();

        average.updateAverage(timeDif);

        this.averages.put(stations,average);

        this.journeys.remove(id);

    }
    
    public double getAverageTime(String startStation, String endStation) {
        String stations = startStation + "," + endStation;
        return this.averages.get(stations).getAverage();
        
    }

    class Journey { 
        int id;
        String stationName;
        int t;

        public Journey(int id, String stationName,int t){
            this.id = id;
            this.stationName = stationName;
            this.t = t;
        }


    }

    class Average {
        double totalTime = 0;
        int customers = 0;

        public void updateAverage(int timeDif){
            totalTime+=timeDif;
            customers+=1;
        }

        public double getAverage(){
            return totalTime / customers;
        }

    }

}

// SC -> O(N+M)
// TC -> O(1)

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */