class Solution:
    def isValid(self, s: str) -> bool:
        holding = []
        valid_dict = {")" : "(", "]" : "[", "}" : "{"}
        valid_keys = valid_dict.keys()
        for x in s:
            if x in valid_keys:
                if not holding or holding.pop()!=valid_dict[x]:
                    return False
            else:
                holding.append(x)
        return len(holding) == 0
