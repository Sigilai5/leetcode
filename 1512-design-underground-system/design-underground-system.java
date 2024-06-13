class UndergroundSystem {
    private Map<Integer,Journey> journey;
    private Map<String,Average> averages;

    public UndergroundSystem() {
        this.journey = new HashMap<>();
        this.averages = new HashMap<>();
    }
    
    public void checkIn(int id, String stationName, int t) {
        this.journey.put(id,new Journey(stationName,t));        
    } 
    
    public void checkOut(int id, String stationName, int t) {
        int timeDif = t - this.journey.get(id).t;
        String stations = this.journey.get(id).stationName + "->" + stationName;

        Average average = this.averages.containsKey(stations) ? this.averages.get(stations) : new Average();

        average.updateAverage(timeDif);

        this.averages.put(stations,average);

        this.journey.remove(id);
        
    }
    
    public double getAverageTime(String startStation, String endStation) {
        String stations = startStation + "->" + endStation;
        return this.averages.get(stations).getAverage();
        
    }


    class Journey {
        String stationName;
        int t;

        public Journey(String stationName,int t){
            this.stationName = stationName;
            this.t = t;

        }

    }

    class Average{
        double totalTime = 0;
        int customers = 0;

        private void updateAverage(int timeDif){
            totalTime+=timeDif;
            customers+=1;
        }

        private double getAverage(){
            double averageTime = totalTime/customers;

            return averageTime;
        }


    }
}

// SC -> O(M+N)
// TC -> O(1)

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */

 // Customer -> id (station-checkin,time)
 // Stations -> stations(total time, no customers)