class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s1) > len(s2):
            return False

        window_size = len(s1)

        chars = defaultdict(int)

        for c in s1:
            chars[c] += 1

        freqs = defaultdict(int)

        for i in range(window_size):
            c = s2[i]
            freqs[c] += 1

        # print(f"initial freqs: {freqs}")

        def isPerm():
            for k, v in chars.items():
                if v != freqs[k]:
                    return False

            return True

        for i in range(len(s2) - window_size + 1):
            if isPerm():
                return True
            
            char_start = s2[i]
            freqs[char_start] -= 1

            if i + window_size < len(s2):
                char_end = s2[i + window_size]
                freqs[char_end] += 1

            # print(f"[{i}, {i + window_size}]  freqs: {freqs}")

        return False


