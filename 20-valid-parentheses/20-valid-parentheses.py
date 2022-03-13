class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ele in s:
            if ele in "{([":
                stack.append(ele)
            elif ele in "}])":
                if len(stack)==0:
                    return False
                elif stack[-1]=="{"and ele!="}":
                    return False
                elif stack[-1]=="("and ele!=")":
                    return False
                elif stack[-1]=="["and ele!="]":
                    return False
                elif stack[-1]=="{"and ele=="}":
                    stack.pop()
                elif stack[-1]=="("and ele==")":
                    stack.pop()
                elif stack[-1]=="["and ele=="]":
                    stack.pop()
                    
        if len(stack)!=0:
            return False
        else:
            return True
                
                    