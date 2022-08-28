#!/usr/bin/env python3

def bfs_traversal(graph, initial_node):
    visited = set([initial_node])
    queue = [initial_node]
    res = []
    while queue:
        curr_node = queue.pop(0)
        res.append(curr_node)
        for edge in graph[curr_node]:
            if edge not in visited:
                queue.append(edge)
                visited.add(edge)

    return res


