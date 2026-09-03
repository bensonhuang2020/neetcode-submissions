class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def summer(curr, index, total):
                nonlocal res
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    curr.append(candidates[i])
                    new_total = total + candidates[i]
                    if new_total == target:
                        res.append(curr[:])
                    elif new_total < target:
                        summer(curr, i + 1, new_total)
                    curr.pop()

        summer([], 0, 0)
        return res