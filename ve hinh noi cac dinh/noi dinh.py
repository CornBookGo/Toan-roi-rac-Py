import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị
G = nx.Graph()

# Thêm các đỉnh vào đồ thị
G.add_nodes_from([1, 2, 3, 4, 5])

# Thêm các cạnh nối các đỉnh
canh = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
G.add_edges_from(canh)

# Vẽ đồ thị
pos = nx.spring_layout(G)  # Xác định vị trí các đỉnh
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_color='black', edge_color='gray')

# Hiển thị đồ thị
plt.show()
