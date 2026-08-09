class Solution:
    def  backtrack(self,index,total,subset,nums,result):
        n=len(nums)
        if total==0:
            result.append(subset.copy())
            return
        if total<0:
            return

        for i in range(index,n):
            if i>index and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            self.backtrack(i+1,total-nums[i],subset,nums,result)
            subset.pop()


    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        self.backtrack(0,target,[],nums,result)
        return result
        