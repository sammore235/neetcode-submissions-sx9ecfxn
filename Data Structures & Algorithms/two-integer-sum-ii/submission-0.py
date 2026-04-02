class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Indice_list=[]
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                if target == numbers[i]+numbers[j]:    
                    Indice_list.append(i+1)
                    Indice_list.append(j+1)
                    return sorted(Indice_list)
                else:
                    continue