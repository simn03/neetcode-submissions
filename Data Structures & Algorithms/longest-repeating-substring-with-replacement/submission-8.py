class Solution:


    def characterReplacement(self, s: str, k: int) -> int:

        def getIdx(idx):
            c = s[idx]
            return ord(c) - ord('A')

        char_freqs = [0] * 26            
            
        l = 0
        r = 0

        largest = 0

        char_freqs[getIdx(0)] = 1

        while l <= r < len(s):

            window_size = r - l + 1
            freq = max(char_freqs)

            if window_size - freq <= k:
                largest = max(largest, window_size)
                r += 1
                if r < len(s):
                    char_freqs[getIdx(r)] += 1
            else:
                char_freqs[getIdx(l)] -= 1
                l += 1


        return largest
            

            

                

            