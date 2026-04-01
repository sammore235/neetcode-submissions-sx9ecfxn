class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = re.sub(r'[^a-zA-Z0-9]', '', s)
        reversetext = text[::-1]
        print(text)
        print(reversetext)
        for i in range(0,len(text)):
            if text[i].lower()==reversetext[i].lower():
                continue
            else:
                return False
        return True

