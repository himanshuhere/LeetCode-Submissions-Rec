class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key wud be sorted verson of strings, so for example
        #tan, nat, ant has key sorted is ant so map[ant] = [tan, nat, ant]
        #or mat[ant].values()
        
        #2
        dic = defaultdict(list)
        for s in strs:
            sorteds = str(sorted(s))        #immutible string can be key not array
            dic[sorteds].append(s)
        return dic.values()
        
        #1
        # words = {}
        # for i in strs:
        #     #string = ''.join((sorted(i)))
        #     string =str(sorted(i))
        #     if string not in words:
        #         words[string] = [i]
        #     else:
        #         words[string] += [i]
        # return words.values()