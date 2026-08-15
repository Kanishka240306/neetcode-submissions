class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_count={}
        left=0
        max_length=0
        max_freq=0
        for right in range(0,len(s)):
            if s[right] in window_count:
                window_count[s[right]]+=1
            else:
                window_count[s[right]]=1
            max_freq=max(max_freq, window_count[s[right]])
            while right-left+1-max_freq>k:
                window_count[s[left]]-=1
                if window_count[s[left]]==0:
                    del window_count[s[left]]

                left+=1
            
            max_length=max(max_length, right-left+1)
            
        return max_length