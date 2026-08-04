class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0

        char_length = {}
        char_usage = defaultdict(int)
        char_safety = {}

        for i, c in enumerate(s):

            if c not in char_length:    
                char_length[c] = [i, 0]
        
            keys = list(char_length.keys())

            for key in keys:
                if key == c:
                    char_length[key][1] += 1

                    if k != 0 and char_usage[key] == k and key not in char_safety:
                        char_safety[key] = i
                elif char_usage[key] < k:
                    char_length[key][1] += 1
                    char_usage[key] += 1
                else:
                    longest = max(longest, char_length[key][1])
                    if key in char_safety:
                        start = char_safety[key]
                        char_length[key] = [start, i - start + 1]
                        char_usage[key] = 1
                        del char_safety[key]
                    else:
                        del char_length[key]
                        char_usage[key] = 0

        for key, val in char_length.items():
            additional = min(val[0], k - char_usage[key])
            total = additional + val[1]
            longest = max(longest, total)

        return longest
            

            

                

            