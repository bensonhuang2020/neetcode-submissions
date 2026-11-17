class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = {}
        truster = {}

        for i in range(1, n+1):
            trusted[i] = []
            truster[i] = []

        for trustee, person_trusted in trust:
            trusted[person_trusted].append(trustee)
            truster[trustee].append(person_trusted)
        
        for person in trusted:
            if len(trusted[person]) == n - 1 and len(truster[person]) == 0:
                return person
        return -1

        


        