class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # we need to do an initial comparison of hand size and group size. if we get a remainder, this means that there are numbers that are left over.
        if len(hand) % groupSize != 0:
            return False
        nums = {}
        # alternatively, we could do something like nums = Counter(hand)
        for x in hand:
            nums[x] = 1 + nums.get(x, 0)
        # sorting here let's us start from the minimum since it must be in order
        hand.sort()
        for num in hand:
            # for each num in hand, if it exists in the dictionary, that means it's not 0. 
            if nums[num]:
                for i in range(num, num + groupSize):
                    # this is the subsequent check for if the key even exists for groupSize numbers, non-inclusive since we start at num
                    if not nums.get(i):
                        return False
                    # if it exists, decrement the marker to show that we're counting it.
                    nums[i] -= 1
        return True
