import uuid
import networkx as nx
import matplotlib.pyplot as plt
import time

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000000"
        self.id = str(uuid.uuid4())

def build_tree(arr):
    if not arr:
        return None

    nodes = [Node(key) for key in arr]

    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def update_color_and_draw(tree_root, node, color):
    node.color = color
    draw_tree(tree_root)
    time.sleep(1)

def generate_color(index, total_steps):
    intensity = int(255 * (index / total_steps))
    hex_color = "#{:02x}{:02x}{:02x}".format(intensity, 150 + intensity // 3, 255 - intensity)
    return hex_color

def dfs(tree_root):
    stack = [tree_root]
    step = 0
    total_steps = count_nodes(tree_root)
    visited = set()

    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.add(node)
            color = generate_color(step, total_steps)
            update_color_and_draw(tree_root, node, color)
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def bfs(tree_root):
    queue = [tree_root]
    step = 0
    total_steps = count_nodes(tree_root)
    visited = set()

    while queue:
        node = queue.pop(0)
        if node and node not in visited:
            visited.add(node)
            color = generate_color(step, total_steps)
            update_color_and_draw(tree_root, node, color)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

tree_array = [10, 7, 5, 3, 2, 4, 1]

tree_root = build_tree(tree_array)

method = input("Виберіть метод обходу (DFS або BFS): ").strip().lower()

if method == "dfs":
    dfs(tree_root)
elif method == "bfs":
    bfs(tree_root)
else:
    print("Невірний вибір методу.")
