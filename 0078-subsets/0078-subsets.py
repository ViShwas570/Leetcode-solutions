class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        total_subsets=1<<n
        result=[]
        for num in range(0,total_subsets):
            list=[]
            for i in range(0,n):
                if num & (1<<i)!=0:
                    list.append(nums[i])
            result.append(list)
        return result        