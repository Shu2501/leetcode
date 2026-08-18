class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = {}
        s2_count = {}

        for char in s1:
            if char not in s1_count:
                s1_count[char] = 0

            s1_count[char] += 1

        for i in range(len(s1)):
            if s2[i] not in s2_count:
                s2_count[s2[i]] = 0

            s2_count[s2[i]] += 1

        if s1_count == s2_count:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]

            left += 1

            if s2[right] not in s2_count:
                s2_count[s2[right]] = 0

            s2_count[s2[right]] += 1
            
            if s1_count == s2_count:
                return True

        return False

        
        