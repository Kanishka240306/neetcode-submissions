class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array=sorted(nums)
        ans=[]
        for i in range(len(sorted_array)-2):
            if i > 0 and sorted_array[i] == sorted_array[i-1]:
                continue
            left=i+1
            right=len(sorted_array)-1
            while left<right:
                curr_sum=sorted_array[i]+sorted_array[left]+sorted_array[right]
                if curr_sum<0:
                    left+=1
                elif curr_sum>0:
                    right-=1
                else:
                    ans.append([sorted_array[i],sorted_array[left],sorted_array[right]])
                    left+=1
                    right-=1
                    while left<right and sorted_array[left]==sorted_array[left-1]:
                        left+=1
                    while left<right and sorted_array[right]==sorted_array[right+1]:
                        right-=1
        return ans