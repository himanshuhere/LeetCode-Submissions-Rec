class Solution:
    def ladderLength(self, beg: str, end: str, words: List[str]) -> int:
        #BFS neetcode
        if end not in words:
            return 0
        
        g = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                patt = word[:i] + "*" + word[i+1:]
                g[patt].append(word)
        print(g)
        
        #BFS, not djiktra bcs weight is 1 and undirected, will rise from origin and see the shortest way to final word
        q = deque([beg])
        vis = set([beg])        #needed as might be multiple duplicate words/patt
        level = 1               #count this word you added to new as one
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                
                if word == end:
                    return level
                
                for i in range(len(word)):
                    patt = word[:i] + "*" + word[i+1:]
                    for nei in g[patt]:
                        if nei not in vis:
                            vis.add(nei)
                            q.append(nei)
            level += 1
            
        return 0                    #bahut to error aaya yaha pe.lvel return kar rha tha