class Solution:
    def dfs(self, node, color, visited, graph):
        visited[node] = color

        for adj in graph[node]:
            if visited[adj] == -1:
                if not self.dfs(adj, 1 - color, visited, graph):
                    return False
            elif visited[adj] == color:
                return False

        return True

    def isBipartite(self, V, edges):
        graph = [[] for _ in range(V)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [-1] * V

        
        if not self.dfs(0, 0, visited, graph):
            return False

        return True