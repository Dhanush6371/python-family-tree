import networkx as nx
import matplotlib.pyplot as plt
import pydot

def add_family_tree(graph, root, generation):
    if generation == 0:
        graph.add_node(root, shape='square')
        return root

    parent = add_family_tree(graph, root + 'a', generation - 1)
    child = add_family_tree(graph, root + 'b', generation - 1)

    graph.add_edge(root, parent, weight=0.5)  # Reverse the edge direction
    graph.add_edge(root, child, weight=0.5)  # Reverse the edge direction

    return root

# Create an empty graph
family_tree = nx.DiGraph()

# Add the root node
root_node = add_family_tree(family_tree, 'Root', 2)

# Set the layout using pydot
pos = nx.nx_pydot.graphviz_layout(family_tree, prog='dot')

# Invert the y-coordinates of the nodes for one generation
for node, (x, y) in pos.items():
    if node.endswith('a'):  # Modify the condition based on the generation you want to invert
        pos[node] = (x, -y)

# Draw the graph
plt.figure(figsize=(8, 8))
nx.draw(family_tree, pos, with_labels=True, node_size=2000, font_size=10, node_shape='s', node_color='lightblue')
plt.axis('off')
plt.show()
