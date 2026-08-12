class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:
            
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            
            else:
                if len(stack) == 0:
                    return False

                opening = stack.pop()

                if(opening == '(' and char != ')') or (opening == '{' and char != '}') or (opening == '[' and char != ']'):
                    return False
        
        return len(stack) == 0