class Solution:
    def solve(self,nums,idx,subset,result):
        if idx>=len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[idx])
        self.solve(nums,idx+1,subset,result)
        subset.pop()
        self.solve(nums,idx+1,subset,result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.solve(nums,0,[],result)
        return result
        # n=len(nums)
        # total_subsets=1<<n
        # result=[]
        # for num in range(0,total_subsets):
        #     list=[]
        #     for i in range(0,n):
        #         if num & (1<<i)!=0:
        #             list.append(nums[i])
        #     result.append(list)
        # return result   

             