class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
#         grid = [[False]*n for _ in range(n)]
#         #lets dig first
#         for r, c in dig:
#             grid[r][c] = True
        
#         #now check every complete art is digged or not
#         ans = 0
#         for r1,c1,r2,c2 in artifacts:
#             alluncovered = True
#             for i in range(r1, r2+1):
#                 for j in range(c1, c2+1):
#                     if grid[i][j] == False:
#                         alluncovered = False
#                         break
#                 if not alluncovered:
#                     break
#             if alluncovered:
#                 ans+=1
        
#         return ans
    
    
        #not matrix, use anything liner like map
        s=set()
        for r, c in dig:
            s.add((r,c))
        
        #now check every complete art is digged or not
        ans = 0
        for r1,c1,r2,c2 in artifacts:
            alluncovered = True
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if (i,j) not in s:
                        alluncovered = False
                        break
            if alluncovered:
                ans+=1
        
        return ans
    
    
    
    
        
        #fucker noob you
        ans=0
        for i in range(len(artifacts)):
            r1,c1 = artifacts[i][0], artifacts[i][1]
            r2,c2 = artifacts[i][2], artifacts[i][3]
            art=[]
            al=0
            if r1==r2==c1==c2:
                art.append([r1,c1])
                al=1
            elif r1==r2 and c1+1==c2:
                art.append([r1,c1])
                art.append([r2,c2])
                al=2
            elif r1+1==r2 and c1==c2:
                art.append([r1,c1])
                art.append([r2,c2])
                al=2
            elif r1+1==r2 and c1+1==c2:
                art.append([r1,c1])
                art.append([r1,c1+1])
                art.append([r1+1,c1])
                art.append([r2,c2])
                al=4
            elif r1==r2 and c1+3==c2:
                art.append([r1,c1])
                art.append([r1,c1+1])
                art.append([r1,c1+2])
                art.append([r1,c2+3])
                al=4
            elif r1+3==r2 and c1==c2:
                art.append([r1,c1])
                art.append([r1+1,c1])
                art.append([r1+2,c1])
                art.append([r1+3,c2])
                al=4
            elif r1==r2 and c1+2==c2:
                art.append([r1,c1])
                art.append([r1,c1+1])
                art.append([r1,c1+2])
                al=3
            elif r1+2==r2 and c1==c2:
                art.append([r1,c1])
                art.append([r1+1,c1])
                art.append([r1+2,c1])
                al=3
                
            c=0
            #print(art, dig)
            for a in art:
                if a in dig:
                    ans.append(a)
        return len(set(ans))
                
                
                