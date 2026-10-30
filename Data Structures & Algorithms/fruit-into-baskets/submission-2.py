class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # the approach is that we have a dictionary to keep in the number of seen fruits used as keys. we have a total that we use to track the current number of fruits (maybe something like counting_fruit is better?) and a res to have the final max. keep a sliding window approach where our window widens if we have 2 keys and we keep addign on to the total. however, if we ever get to a point where we have 3 keys, that means we have too many fruits that can't fit in the baskets, so we're going to have to move the left pointer right until we have 2 keys again. at the end, we shift the right pointer and check if the tracked number of fruit is more than our tracked max. time is O(n) since we go through all the fruit and space is O(n) for the dictionary.
        seen_fruits = {}
        res = l = 0
        for r in range(len(fruits)):
            seen_fruits[fruits[r]] = 1 + seen_fruits.get(fruits[r], 0)
            while len(seen_fruits.keys()) > 2:
                seen_fruits[fruits[l]] -= 1
                if seen_fruits[fruits[l]] == 0:
                    del seen_fruits[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
