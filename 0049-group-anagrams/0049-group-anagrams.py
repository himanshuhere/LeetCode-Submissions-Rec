class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        #key wud be sorted verson of strings, so for example
        #tan, nat, ant has key sorted is ant so map[ant] = [tan, nat, ant]
        #or mat[ant].values()
        
        big_map = dict()
        for strs in arr:
            freq_map = dict()
            for i in range(len(strs)):
                ch = strs[i]
                freq_map[ch] = freq_map.get(ch,0)+1
                
            if tuple(sorted(freq_map.items())) not in big_map.keys():
                l = []
                l.append(strs)
                big_map[tuple(sorted(freq_map.items()))]= l
            else:
                l = big_map[tuple(sorted(freq_map.items()))]
                l.append(strs)

        res = []
        for i in big_map.values():
            res.append(i)
        return res

        #or use hash instead sorting and make them key yes bro yes. I can show you my own hashing techniq
        def gethash(s):
            #,ake sure to not change hash as per the pos, so d^m-1, nope, things are not sorted its anagram, hash but normal
            p = 392113
            d = 3267113  #space
            m = len(s)-1
            hash_ = 0
            for i, c in enumerate(s):
                hash_ = (hash_ + ord(c)*ord((c.upper()))*d)%p
                m -= 1
            return hash_
        #not working formanyu cases
        
        m = defaultdict(list)
        for s in strs:
            shash_ = gethash(s)
            m[shash_].append(s)
        return m.values()
    
        
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