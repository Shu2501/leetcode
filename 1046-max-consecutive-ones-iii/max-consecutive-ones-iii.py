class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0 
        zeroes = 0
        best_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1

                left += 1

            window_length = right-left+1
            best_length = max(best_length, window_length)

        return best_length


                