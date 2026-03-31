class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b = sorted(nums)
        if nums==[]:
            return False
        for i in range(0,len(b)-1):
            for j in range(i+1,len(b)):
                if b[i] == b[j]:
                    return True
                else:
                    continue

        return False            