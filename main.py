class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        if len(s)==1: return 1
        
        hashTable = [False,]*95
        maxLen = 0
        l, r = 0, 1
        hashTable[ord(s[l])-32] = True
        while r<len(s):
            if hashTable[ord(s[r])-32]:
                maxLen = max(maxLen, r-l)
                while hashTable[ord(s[r])-32]:
                    hashTable[ord(s[l])-32] = False
                    l+=1
                    
            else:
                hashTable[ord(s[r])-32] = True
                maxLen = max(maxLen, r-l+1)
                r+=1
                
            
                
        return maxLen
