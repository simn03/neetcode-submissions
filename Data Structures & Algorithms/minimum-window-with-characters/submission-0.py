class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        min_window = len(t)
        
        chars = defaultdict(int)
        freqs = defaultdict(int)

        for c in t:
            chars[c] += 1

        for i in range(min_window):
            c = s[i]
            freqs[c] += 1
        
        l = 0
        r = min_window - 1

        def isPerm():
            for k, v in chars.items():
                
                if freqs[k] < v:
                    return False

            return True

        res = len(s)
        resL = None
        resR = None

        while l < r < len(s):

            if isPerm():
                size = r - l

                if size < res:
                    res = size
                    resL = l
                    resR = r


                l += 1

                while s[l] not in chars:
                    l += 1

                r = l + min_window - 1

                if r >= len(s):
                    break;

                # reset freqs
                freqs = defaultdict(int)
                for i in range(l, r + 1):
                    c = s[i]
                    freqs[c] += 1

                continue;

            if res == min_window:
                break

            r += 1

            if r < len(s):
                freqs[s[r]] += 1

        if resL == None:
            return ""

        return s[resL:resR + 1]
            















