class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # n=len(nums)
        # nums.sort()
        # last_smaller=float("inf")
        # count=0
        # largest=1
        # if n==0:
        #     return 0
        # for i in range(0,n):
        #     if nums[i]-1==last_smaller:
        #         count+=1
        #         last_smaller=nums[i]

        #     elif last_smaller!=nums[i]:
        #         count=1
        #         last_smaller=nums[i]

        #     largest=max(largest,count)
        # return largest
        n=len(nums)
        my_set=set()
        for i in range(0,n):
            my_set.add(nums[i])

        longest=0
        for num in my_set:
            if num-1 not in my_set:
                x=num
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1

                longest=max(longest,count)
        return longest


        