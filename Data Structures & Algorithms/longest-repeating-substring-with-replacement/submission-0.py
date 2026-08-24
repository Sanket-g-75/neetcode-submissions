class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        s has only uppercase english characters
        can choose upto k characters of string and replace them with any other uppercase
        After atmost k replacements, return longest substring length that contains only one distinct character

        '''

        l = 0
        count = {}
        maxlen = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l +=1
            
            maxlen = max(maxlen,r-l+1)
        return maxlen
                

                
