class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        seen = set()
        best_length = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            window_length = right - left + 1
            best_length = max(best_length, window_length)

        return best_length
        