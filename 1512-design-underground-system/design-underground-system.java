class UndergroundSystem {
    private HashMap<Integer,Checkin> checkins;
    private HashMap<String,Average> averages;

    public UndergroundSystem() {
        checkins = new HashMap();
        averages = new HashMap(); 
    }
    
    public void checkIn(int id, String stationName, int t) {
        checkins.put(id,new Checkin(id,stationName,t));
    }
    
    public void checkOut(int id, String stationName, int t) {
        Checkin checkin = checkins.get(id);
        String stations = checkin.stationName + "," + stationName;
        double timeDif = t - checkin.t;

        Average average = averages.containsKey(stations) ? averages.get(stations) : new Average();

        average.updateAverage(timeDif);

        averages.put(stations,average);
    }
    
    public double getAverageTime(String startStation, String endStation) {
        String stations = startStation + "," + endStation;
        return averages.get(stations).getAverage();
        
    }

    class Checkin {
        private int id;
        private String stationName;
        private int t;

        public Checkin(int id, String stationName, int t) {
            this.id = id;
            this.stationName = stationName;
            this.t = t;
        }

    }

    class Average {
        private double totalTime = 0;
        private int customers = 0;


        public void updateAverage(double timeDif){
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