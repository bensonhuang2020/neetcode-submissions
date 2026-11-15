class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum = odd_cnt = even_cnt = res = 0
        modu = 10 ** 9 + 7

        for n in arr:
            cur_sum += n
            if cur_sum % 2:
                # every previous sub_array that was even turns odd in this case
                res = (res + 1 + even_cnt) % modu
                odd_cnt += 1
            else:
                res = (res + odd_cnt) % modu
                even_cnt += 1
        return res