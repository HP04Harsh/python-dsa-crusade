 # First Unique Character in a String

# ----------- Solution 1 ----------------

 class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i , char in enumerate(s):
            if s.find(char) == s.rfind(char):
                return  i
        return -1     

# ---------------- Solution 2 ----------------

 class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i] += 1 



        for i in range(len(s)):
            if freq[s[i]]==1:
                return i 

        return -1                    
       