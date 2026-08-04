class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        next_node = (s[0], 0)

        while next_node:

            usage = 0

            start = next_node[1]
            prev = next_node[0]
            next_node = None

            curr = 0

            for i in range(start, len(s)):
                c = s[i]

                if c == prev:
                    curr += 1
                    continue

                if next_node == None:
                    next_node = (c, i)

                if usage < k:
                    curr += 1
                    usage += 1
                    continue
                print(prev, i, "moving on to next_node")
                break
            
            additional = min(k - usage, start)
            print(prev, additional)

            longest = max(longest, curr + additional)

            if usage < k and start + curr == len(s):
                break
        
        return longest

            

                

            