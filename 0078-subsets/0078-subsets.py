class Solution:
    def func(self,nums,idx,subset):
        if idx>=len(nums):
            self.result.append(subset.copy())
            return
        subset.append(nums[idx])
        self.func(nums,idx+1,subset)
        subset.pop()
        self.func(nums,idx+1,subset)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result=[]
        self.func(nums,0,[])
        return self.result
        


        