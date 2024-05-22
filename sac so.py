import networkx as nx
import matplotlib.pyplot as plt

# Tạo một đồ thị vô hướng bất kỳ
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 4), (1, 6), (1, 8), (1, 9), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (5, 11), (6, 7), (6, 8), (6, 9), (7, 8), (7, 10), (7, 11), (8, 9), (8, 10), (8, 11), (9, 10), (10, 11)])

# Tính số đồ thị sắc số
chromatic_number = nx.coloring.greedy_color(G, strategy="largest_first")
num_colors = max(chromatic_number.values()) + 1
print("Số đồ thị sắc số:", num_colors)

# Vẽ đồ thị
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=list(chromatic_number.values()), cmap=plt.cm.rainbow, node_size=500)
plt.title("Đồ thị với sắc số")
plt.show()