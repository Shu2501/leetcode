class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        current_vowels = 0

        for char in s[:k]:
            if char in 'aeiou':
                current_vowels += 1
        
        best_vowels = current_vowels

        n = len(s)

        for i in range(k,n):
            if s[i-k] in "aeiou":
                current_vowels -= 1

            if s[i] in "aeiou":
                current_vowels += 1

            if current_vowels > best_vowels:
                best_vowels = current_vowels

        return best_vowels
        