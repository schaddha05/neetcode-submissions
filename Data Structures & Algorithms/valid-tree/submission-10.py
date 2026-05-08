class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        adj = [[] for i in range(n)]
        visited = set() 
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node, prevNode): 
            if node in visited:
                return False 
            
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prevNode:
                    continue 
                if not dfs(neighbor, node):
                    return False 
            
            return True 

        return dfs(0, -1) and len(visited) == n

