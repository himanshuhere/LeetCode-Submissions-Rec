class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key wud be sorted verson of strings, so for example
        #tan, nat, ant has key sorted is ant so map[ant] = [tan, nat, ant]
        #or mat[ant].values()
        
        words = {}
        for i in strs:
            #string = ''.join((sorted(i)))
            string =str(sorted(i))
            if string not in words:
                words[string] = [i]
            else:
                words[string] += [i]
        return words.values()