class Solution {
    public String intToRoman(int num) {
        Map<Integer,String> numRoman = new LinkedHashMap<>();

        numRoman.put(1000,"M");
        numRoman.put(900,"CM");
        numRoman.put(500,"D");
        numRoman.put(400,"CD");
        numRoman.put(100,"C");
        numRoman.put(90,"XC");
        numRoman.put(50,"L");
        numRoman.put(40,"XL");
        numRoman.put(10,"X");
        numRoman.put(9,"IX");
        numRoman.put(5,"V");
        numRoman.put(4,"IV");
        numRoman.put(1,"I");

        StringBuilder result = new StringBuilder();

        for (Map.Entry<Integer, String> entry : numRoman.entrySet()){ 
            while(num >= entry.getKey()){
                num -= entry.getKey();
                result.append(entry.getValue());
            }
        }
 
        return result.toString();
        
        
    }
}

// SC -> O(N)
// TC -> O(N)