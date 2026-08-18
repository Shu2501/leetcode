class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        counts = {}
        best_length = 0

        for right in range(len(s)):

            if s[right] not in counts:
                counts[s[right]] = 0

            counts[s[right]] += 1
            
            most_frequent = max(counts.values())

            while (right - left + 1) - most_frequent > k:
                counts[s[left]] -= 1
                left += 1

                most_frequent = max(counts.values())

            window_length = right - left + 1
            best_length = max(best_length, window_length)

        return best_length


