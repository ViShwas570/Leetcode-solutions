class Solution:
    def backtrack(self,idx,total,subset,nums,target):
        if total==target:
        
            return True
        elif total>target:
            return False
        if idx>=len(nums):
            return False
        subset.append(nums[idx])
        curr_sum=total+nums[idx]
        pick=self.backtrack(idx+1,curr_sum,subset,nums,target)
        if pick==True:
            return True
        subset.pop()
        not_pick=self.backtrack(idx+1,total,subset,nums,target)
        return not_pick
    def checkSubsequenceSum(self, nums, target):
        return self.backtrack(0,0,[],nums,target)
        
            
        # code here