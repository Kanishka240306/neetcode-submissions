import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        answer=right
        while left<=right:
            mid=(left+right)//2
            hours=0
            k=mid
            for pile in piles:
                hours+=math.ceil(pile/k)
                
            if hours<=h:
                answer=mid
                right=mid-1
            else:
                left=mid+1
        return answer
            