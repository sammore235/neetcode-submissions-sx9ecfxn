class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}
        frequent_elements =[]
        for i in nums:
            my_dict[i]= my_dict.get(i, 0) + 1
        vals = list(my_dict.values())
        desc_vals = sorted(vals, reverse=True)
        last_vals = desc_vals[:k]
        list_keys =[k for k,v in my_dict.items() if v in last_vals]
        return list_keys