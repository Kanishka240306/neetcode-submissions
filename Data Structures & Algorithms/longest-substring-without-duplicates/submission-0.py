class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        max_length=0
        for right in range(len(s)):
            ch=s[right]
            while ch in seen:
                seen.remove(s[left])
                left+=1
            seen.add(ch)
            max_length=max(max_length, right-left+1)
        return max_length