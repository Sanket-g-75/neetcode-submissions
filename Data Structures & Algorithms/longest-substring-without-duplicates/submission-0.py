class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxlen = 0
        left = 0

        for right in range(len(s)):

            while s[right] in s[left:right]:
                left += 1

            maxlen = max(maxlen, right - left + 1)

        return maxlen