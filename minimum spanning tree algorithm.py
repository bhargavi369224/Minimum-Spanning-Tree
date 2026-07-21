import time

# -----------------------------
# Prim's Algorithm
# -----------------------------
def prim(graph, vertices):
    selected = [False] * vertices
    selected[0] = True

    edges = 0
    total_cost = 0

    print("\nPrim's Minimum Spanning Tree")
    print("Edge \tWeight")

    while edges < vertices - 1:
        minimum = float('inf')
        x = 0
        y = 0

        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if (not selected[j]) and graph[i][j]:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x} - {y}\t{graph[x][y]}")
        total_cost += graph[x][y]
        selected[y] = True
        edges += 1

    print("Total Cost =", total_cost)


# -----------------------------
# Kruskal's Algorithm
# -----------------------------
parent = []

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b

def kruskal(graph, vertices):
    global parent
    parent = [i for i in range(vertices)]

    edges = []

    for i in range(vertices):
        for j in range(i + 1, vertices):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    edges.sort()

    total_cost = 0

    print("\nKruskal's Minimum Spanning Tree")
    print("Edge \tWeight")

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            print(f"{u} - {v}\t{weight}")
            total_cost += weight

    print("Total Cost =", total_cost)


# -----------------------------
# Main Program
# -----------------------------
vertices = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix:")

graph = []

for i in range(vertices):
    row = list(map(int, input().split()))
    graph.append(row)


# Prim
start = time.perf_counter()
prim(graph, vertices)
end = time.perf_counter()

prim_time = end - start

print("Execution Time:", prim_time, "seconds")


# Kruskal
start = time.perf_counter()
kruskal(graph, vertices)
end = time.perf_counter()

kruskal_time = end - start

print("Execution Time:", kruskal_time, "seconds")


# Comparison
print("\nPerformance Comparison")
print("-------------------------")
print("Prim's Time     :", prim_time, "seconds")
print("Kruskal's Time  :", kruskal_time, "seconds")