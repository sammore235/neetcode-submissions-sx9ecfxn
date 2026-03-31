class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Indice_list=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i]+nums[j]:
                    Indice_list.append(i)
                    Indice_list.append(j)
                    return sorted(Indice_list)
                else:
                    continue
        