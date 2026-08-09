class Solution:
    def solve(self,index,total,subset,nums,target,result):
        if total==target:
            result.append(subset.copy())
            return
        elif total>target:
            return
        if index>=len(nums):
            return
        subset.append(nums[index])
        self.solve(index,total+nums[index],subset,nums,target,result)
        subset.pop()
        self.solve(index+1,total,subset,nums,target,result)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        self.solve(0,0,[],nums,target,result)
        return result

        