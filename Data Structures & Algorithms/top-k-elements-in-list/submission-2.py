class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = defaultdict(int)

        for n in nums:
            freqs[n] += 1

        pairs = []

        for key, v in freqs.items():
            pairs.append([key, v])

        list.sort(pairs, key=lambda x: x[1], reverse=True)

        res = list(map(lambda x: x[0], pairs))

        return res[:k]