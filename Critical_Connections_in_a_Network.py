import collections
class Solution(object):
    def criticalConnections(self, n, connections):
        # Create the dictionary witch represents the graph
        graph = collections.defaultdict(list)
        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])
        # convert the array into a set to make easier deletions
        sorted_connections = [tuple(sorted(connection)) for connection in connections]
        connections = set(sorted_connections)
        rank = [-2] * n

        def dfs(node, parent, depth):
            if rank[node] >= 0:
                return rank[node]

            rank[node] = depth

            min_depth = n
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                back_depth = dfs(neighbour, node, depth+1)
                # loop!
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbour))))
                min_depth = min(min_depth, back_depth)
            return min_depth
        dfs(0, -1, 0)
        return list(connections)