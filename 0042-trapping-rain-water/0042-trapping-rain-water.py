from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculates how much rainwater can be trapped in an elevation map.
        
        Approach: Two Pointers
        Time Complexity: O(N) - single pass through the array.
        Space Complexity: O(1) - constant extra space.
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]

        return total_water


# Alternative Dynamic Programming / Prefix Max Approach (O(N) Space)
class SolutionDP:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total_water = 0
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - height[i]

        return total_water


# --- Quick local testing ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ans1 = sol.trap(height1)
    print("Example 1 Input:", height1)
    print("Example 1 Output:", ans1, "| Expected: 6")

    # Example 2
    height2 = [4, 2, 0, 3, 2, 5]
    ans2 = sol.trap(height2)
    print("\nExample 2 Input:", height2)
    print("Example 2 Output:", ans2, "| Expected: 9")
