
class Solution:
    delimiter = "|||"

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i, s in enumerate(strs):
            if (i != 0): 
                res += self.delimiter
            res += s

        

        return str(len(strs)) + self.delimiter + res

    def decode(self, s: str) -> List[str]:
        res = s.split(self.delimiter)

        if (int(res[0]) == 0):
            return []

        return res[1:]
