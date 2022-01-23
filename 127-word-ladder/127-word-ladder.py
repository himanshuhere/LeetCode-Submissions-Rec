class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        #BFS neetcode
        if end not in wordList:
            return 0
        
        graph = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]       #skip j and add wildcard
                graph[pattern].append(word)
        #yes theremight be multiple duplicacy in graph but dnt worry while BFS visisted will handle
        
        vis = set([begin])
        q = deque([begin])
        res = 1
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                
                if word == end:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in graph[pattern]:
                        if neiWord not in vis:
                            vis.add(neiWord)
                            q.append(neiWord)
            res += 1            #one level +
        
        return 0