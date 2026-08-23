class Solution:
    def isValid(self, s: str) -> bool:
        holding = []
        valid_dict = {")" : "(", "]" : "[", "}" : "{"}
        valid_keys = valid_dict.keys()
        for x in s:
            if x in valid_keys:
                if len(holding) == 0:
                    return False
                held = holding.pop(-1)
                if valid_dict[x] != held:
                    return False
            else:
                holding.append(x)
        return len(holding) == 0
