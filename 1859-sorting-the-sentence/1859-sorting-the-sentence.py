class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        dic = {}
        for w in words:
            key, val = w[-1], w[:-1]
            dic[int(key)] = val
        dic = [val for _, val in sorted(dic.items(), key=lambda x:x[0])]
        return " ".join(dic)