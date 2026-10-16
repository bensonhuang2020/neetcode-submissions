class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        usable_triplets = []
        # if there is ever a larger value, it's not usable because it would always make the array value larger than the target value.
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                usable_triplets.append(triplet)
        has_first = has_second = has_third = False
        # from the remaining values, we know that every triplet remaining either has 1 of the triplet values or is less than that. either way, it can be used.
        for remaining in usable_triplets:
            # for the triplets remaining, it's usable if it's a match.
            if remaining[0] == target[0]:
                has_first = True

            if remaining[1] == target[1]:
                has_second = True

            if remaining[2] == target[2]:
                has_third = True

        return has_first and has_second and has_third

        