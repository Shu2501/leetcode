class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        lengths = []
        
        for i in strs:
            lengths.append(len(i))
            
        print(lengths)
        print(min(lengths))

        for i in range(min(lengths)):
            for string in strs:
                if string[i] != strs[0][i]:
                    print("not matching")
                    return strs[0][:i]

        return strs[0][:min(lengths)]
        