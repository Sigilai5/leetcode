class Solution(object):
    def twoSum(self, arr, target):
        final = []
        for i in range(len(arr) - 1):
            for j in range(i+1,len(arr)):
                if arr[i] + arr[j] == target:
                    final.append(i)
                    final.append(j)
        return final
                
                
                
                    
        
        
                    
                    
            
       
                    
                              
            
