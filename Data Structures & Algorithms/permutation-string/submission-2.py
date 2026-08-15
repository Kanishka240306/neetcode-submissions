class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        window_count={}
        s1_count={}
        for ch in s1:
            if ch in s1_count:
                s1_count[ch]+=1
            else:
                s1_count[ch]=1
        for right in range(0,len(s2)):
            if s2[right] in window_count:
                window_count[s2[right]]+=1
            else:
                window_count[s2[right]]=1
            if right-left+1>len(s1):
                window_count[s2[left]]-=1
                if window_count[s2[left]]==0:
                    del window_count[s2[left]]
                left+=1
            if window_count==s1_count:
                return True
        return False