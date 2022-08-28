#!/usr/bin/env python3

def dfs_traversal(graph, initial_node):
    stack = [initial_node]
    visited = set([initial_node])
    res = []
    while stack:
        curr_node = stack.pop()
        res.append(curr_node) 
        for edge in graph[curr_node][::-1]:
            if edge not in visited:
                stack.append(edge)
                visited.add(edge)
    
    return res
