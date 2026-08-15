class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        current_sum = sum(nums[:k])
        best_sum = current_sum

        n = len(nums)
        for i in range(k,n):
            current_sum = current_sum - nums[i-k] + nums[i]

            if current_sum > best_sum:
                best_sum = current_sum

        return best_sum/k
