class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'}': '{', ']': '[', ')': '('}   # closing → opening map
        stack = []

        for ch in s:
            if ch in mp.values():              # opening bracket → push
                stack.append(ch)
            elif not stack or mp[ch] != stack.pop():  # closing → must match top
                return False

        return not stack                       # valid only if nothing left unmatched