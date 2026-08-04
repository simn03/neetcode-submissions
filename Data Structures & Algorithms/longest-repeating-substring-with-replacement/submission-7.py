class Solution:


    def characterReplacement(self, s: str, k: int) -> int:

        def mostFreq(l: int, r: int) -> int:
            freqs = [0] * 26
            max_freq = 0
            for i in range(l, r + 1):
                idx = ord(s[i]) - ord('A')
                freqs[idx] += 1
                max_freq = max(max_freq, freqs[idx])

            return max_freq

        l = 0
        r = 0

        largest = 0

        while l <= r < len(s):

            window_size = r - l + 1
            freq = mostFreq(l, r)

            if window_size - freq <= k:
                largest = max(largest, window_size)
                r += 1
            else:
                l += 1


        return largest
            

            

                

            