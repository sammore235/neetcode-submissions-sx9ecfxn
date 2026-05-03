class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dt = []
        for i in range(0, len(temperatures)-1):
            for j in range(i+1,len(temperatures)):
                if temperatures[i]<temperatures[j]:
                    k = j -i 
                    #print(k)
                    dt.append(k)
                    break
                elif j == len(temperatures)-1:
                    #print(j)
                    #print("Inside the last loop")
                    dt.append(0)
                else:
                    continue
        
        if len(temperatures)==len(dt):
            return dt
        else:
            dt.append(0)
        #print(dt)
        
        return dt