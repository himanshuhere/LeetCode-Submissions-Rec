class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        #Kahn Algo
        g = defaultdict(list)
        indegree = defaultdict(list)
        
        for (i, recipe) in enumerate(recipes):
            for ingredient in ingredients[i]:
                g[ingredient].append(recipe)
                
            indegree[recipe] = len(ingredients[i])
        
        q = [sup for sup in supplies]
        ans = []
        while q:
            x = q.pop()
            for k in g[x]:
                indegree[k] -= 1
                if indegree[k] == 0:
                    ans.append(k)
                    q.append(k)
        return ans