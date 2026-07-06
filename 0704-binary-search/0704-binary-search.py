class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(nums,low,high):
            if low>high:
                return -1

            mid=(low+high)//2
            if nums[mid]==target:
                return mid

            elif nums[mid]<target:
                return bs(nums,mid+1,high)
            else:
                return bs(nums,low,mid-1)

        return bs(nums,0,len(nums)-1)
