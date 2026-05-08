class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        tickets.sort()
        for n1, n2 in tickets:
            adj[n1].append(n2)
        
        res = ['JFK']
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True 
    
            if node not in adj:
                return False
            
            temp = list(adj[node])
            for i, v in enumerate(temp):
                adj[node].pop(i)
                res.append(v)
                if dfs(v):
                    return True 
                adj[node].insert(i, v)
                res.pop()
            return False
        
        dfs('JFK')
        return res

            
        