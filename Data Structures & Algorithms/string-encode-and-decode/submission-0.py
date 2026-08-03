
class Solution:
    delimiter = "|||"

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i, s in enumerate(strs):
            if (i != 0): 
                res += self.delimiter
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        return s.split(self.delimiter)
