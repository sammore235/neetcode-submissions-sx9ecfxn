class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        ls = []
        stringlist = list(s)
        for i in range(0,len(stringlist)):
            count=0
            substring=[]
            for j in range(i,len(stringlist)):
                if stringlist[j] not in substring:
                    substring.append(stringlist[j])
                    count = count+1
                else:
                    break
            ls.append(count)
                    
        ls.sort()
        if not ls:
            return 1
        else:
            return ls[-1]

