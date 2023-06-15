import networkx as nx
import matplotlib.pyplot as plt

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

# Set the layout using spring_layout
pos = nx.spring_layout(family_tree, seed=42, k=0.8)

# Invert the y-coordinates of the nodes for one generation
for node, (x, y) in pos.items():
    if node.endswith('a'):  # Modify the condition based on the generation you want to invert
        pos[node] = (x, -y)

# Define genetic names
genetic_names = ['John', 'Mary', 'Tom', 'Emily', 'David', 'Emma', 'Michael', 'Olivia']

# Assign genetic names to nodes
genetic_name_mapping = {}
for i, node in enumerate(family_tree.nodes):
    genetic_name_mapping[node] = genetic_names[i % len(genetic_names)]

# Define relationships
relationship_mapping = {
    'Root': '',
    'Roota': 'Parent',
    'Rootb': 'Parent',
    'Rootaa': 'Grandparent',
    'Rootab': 'Grandparent',
    'Rootba': 'Grandparent',
    'Rootbb': 'Grandparent',
    'Rootaaa': 'Great-Grandparent',
    'Rootaab': 'Great-Grandparent',
    'Rootaba': 'Great-Grandparent',
    'Rootabb': 'Great-Grandparent',
    'Rootbaa': 'Great-Grandparent',
    'Rootbab': 'Great-Grandparent',
    'Rootbba': 'Great-Grandparent',
    'Rootbbb': 'Great-Grandparent',
}

# Combine edge labels for multiple edges
combined_relationship_mapping = {}
for u, v, data in family_tree.edges(data=True):
    edge_key = (u, v)
    if edge_key in combined_relationship_mapping:
        combined_relationship_mapping[edge_key] += ', ' + relationship_mapping[v]
    else:
        combined_relationship_mapping[edge_key] = relationship_mapping[v]

# Draw the graph with genetic names and combined relationship types
plt.figure(figsize=(8, 8))
nx.draw(family_tree, pos, labels=genetic_name_mapping, node_size=2000, font_size=10, node_shape='s', node_color='lightblue', edge_color='gray')
nx.draw_networkx_edge_labels(family_tree, pos, edge_labels=combined_relationship_mapping, font_size=8)
plt.axis('off')
plt.show()
