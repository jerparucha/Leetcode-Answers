class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = frequency(nums)

        for i in range(k):
            a = max(zip(freq.values(), freq.keys()))[1]
            ans.append(a)
            del freq[a]

        return ans


def frequency(nums):
    freq = {}

    for x in nums:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    return freq