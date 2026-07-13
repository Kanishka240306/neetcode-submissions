class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={']':'[', '}': '{', ')':'('}
        for i in s:
            if i not in pairs:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                
                top=stack[-1]
                if top != pairs[i]:
                    return False
                stack.pop()
        return len(stack)==0