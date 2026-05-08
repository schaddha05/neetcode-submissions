class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for n1, n2 in tickets:
            adj[n1].append(n2)
        
        for n in adj:
            adj[n].sort()
        
        path = ['JFK']
        def dfs(node):
            if len(path) == len(tickets) + 1:
                return True 
            
            for i in range(len(adj[node])):
                destination = adj[node][i]
                if destination is None:
                    continue 

                path.append(destination)
                adj[node][i] = None 
                if dfs(destination):
                    return True
                
                path.pop()
                adj[node][i] = destination
            return False
        
        dfs('JFK')
        return path

            
        