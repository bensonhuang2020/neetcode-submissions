class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        cur_loc = -1
        for op in operations:
            if op == '+':
                res.append(res[cur_loc] + res[cur_loc-1])
                cur_loc += 1
            elif op == "C":
                res.pop()
                cur_loc -= 1
            elif op == "D":
                res.append(res[cur_loc] * 2)
                cur_loc += 1
            else:
                res.append(int(op))
                cur_loc += 1
        return sum(res)