#!/usr/bin/env python3

def tree_to_text(tree, root_node):
    curr_path = []
    stack = []
    curr_node = root_node
    while True:
        # Go all the way to left if you are able to
        if curr_node:
            stack.append(curr_node)
            curr_node = tree[curr_node][0] if tree[curr_node] else 0
        # Cannot go further left, pop from stack and try to go right
        elif stack:
            curr_node = stack.pop()
            curr_path.append(curr_node[3:])
            curr_node = tree[curr_node][1] if tree[curr_node] else 0
        else:
            break
    return(''.join(curr_path))

