import networkx as nx

# Tạo đồ thị G (chú ý: bạn cần thay đổi đồ thị này theo hình ảnh của bạn)
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 4), (1, 6), (1,8), (1,9), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7), (6, 8), (6, 9), (7, 8), (8, 9)])

# Tìm cliques có số đỉnh lớn nhất
max_cliques = list(nx.find_cliques(G))
largest_clique = max(max_cliques, key=len)

print("Clique có số đỉnh lớn nhất:", largest_clique)
print("Số đỉnh trong clique:", len(largest_clique))
