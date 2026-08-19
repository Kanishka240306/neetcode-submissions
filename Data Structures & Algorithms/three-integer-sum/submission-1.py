class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_num= sorted(nums)
        answer=[]
        for i in range(len(s_num)-2):
            if i>0 and s_num[i]==s_num[i-1]:
                continue
            left=i+1
            right=len(s_num)-1
            while left<right:
                total=s_num[left]+s_num[right]
                target=-s_num[i]
                if total>target:
                    right-=1
                elif total<target:
                    left+=1
                else:
                    answer.append([s_num[i], s_num[left], s_num[right]])
                    left+=1
                    right-=1
                    while left<right and s_num[left]==s_num[left-1]:
                        left+=1
                    while left<right and s_num[right]==s_num[right+1]:
                        right-=1
                            
        return answer