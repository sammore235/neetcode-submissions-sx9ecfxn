class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_string_1 = "".join(sorted(list(s))) 
        sorted_string_2 = "".join(sorted(list(t)))
        if sorted_string_1 == sorted_string_2:
            return True
        else:
            return False