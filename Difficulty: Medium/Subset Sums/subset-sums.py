class Solution:
    def solve(self,ind,total,nums,result):
        if ind>=len(nums):
            result.append(total)
            return
        self.solve(ind+1,total+nums[ind],nums,result)
        self.solve(ind+1,total,nums,result)
	def subsetSums(self, nums):
	    result=[]
	    self.solve(0,0,nums,result)
	    return result
	     
		# code here
		