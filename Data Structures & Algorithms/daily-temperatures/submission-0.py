class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results =  [0]* len(temperatures)
        
        monoStack = []

        for i in range(len(temperatures)):
            while monoStack and temperatures[monoStack[-1]] < temperatures[i]:
                tempIdx = monoStack.pop()
                results[tempIdx] = i - tempIdx
            monoStack.append(i)

        for i in monoStack:
            results[i] = 0
        return results 
        
            
