class Solution {
    public List<String> fizzBuzz(int n) {
        // Intialize and empty array
        // loop through the range(n+1)
        // check if num/15,if so append FizzBuzz,do the same for 5 and 3
        // else append string num
        // return the array

        ArrayList<String> result = new ArrayList();

        for(int i = 1; i <= n;i++){
            if((i%15) == 0){
                result.add("FizzBuzz");
            }else if((i%5) == 0){ 
                result.add("Buzz");
            }else if((i%3) == 0){
                result.add("Fizz");
            }else{
                result.add(Integer.toString(i));
            }
        }

        return result;
        
    }
}

// SC -> O(N)
// TC -> O(N)