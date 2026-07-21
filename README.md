# Minimum Spanning Tree (MST) using Prim's and Kruskal's Algorithms

## 📌 Project Overview

This project implements two popular graph algorithms:

- Prim's Algorithm
- Kruskal's Algorithm

Both algorithms are used to find the **Minimum Spanning Tree (MST)** of a weighted undirected graph.

The project also compares their execution time and performance.

---

## 🎯 Objective

To implement Prim's and Kruskal's algorithms in Python to find the Minimum Spanning Tree (MST) of a weighted undirected graph and compare their performance.

---

## 📚 What is a Minimum Spanning Tree?

A Minimum Spanning Tree (MST) is a subset of the edges of a connected weighted graph that:

- Connects all vertices
- Contains no cycles
- Has the minimum possible total edge weight

---

## 🔹 Prim's Algorithm

Prim's Algorithm starts from any vertex and repeatedly selects the minimum weight edge that connects a visited vertex to an unvisited vertex until all vertices are included.

### Advantages

- Efficient for dense graphs
- Simple implementation using an adjacency matrix

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(V²) |
| Average | O(V²) |
| Worst | O(V²) |

---

## 🔹 Kruskal's Algorithm

Kruskal's Algorithm sorts all edges by weight and repeatedly adds the smallest edge that does not create a cycle.

### Advantages

- Efficient for sparse graphs
- Uses Union-Find for cycle detection

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(E log E) |
| Average | O(E log E) |
| Worst | O(E log E) |

---

## 💻 Technologies Used

- Python
- Visual Studio Code
- GitHub

---

## ▶️ Sample Input

Number of Vertices

5

Adjacency Matrix

0 2 0 6 0

2 0 3 8 5

0 3 0 0 7

6 8 0 0 9

0 5 7 9 0

---

## ✅ Sample Output

Prim's MST

0 - 1 = 2

1 - 2 = 3

1 - 4 = 5

0 - 3 = 6

Total Cost = 16

Kruskal's MST

0 - 1 = 2

1 - 2 = 3

1 - 4 = 5

0 - 3 = 6

Total Cost = 16

---

## 📂 Project Structure

Minimum-Spanning-Tree/

├── mst_algorithms.py

├── README.md

└── index.html

---

## ▶️ How to Run

```bash
python mst_algorithms.py
```

---

## 📊 Comparison

| Algorithm | Suitable For |
|------------|--------------|
| Prim's | Dense Graphs |
| Kruskal's | Sparse Graphs |

---

## 🎯 Conclusion

Both Prim's and Kruskal's algorithms generate the same Minimum Spanning Tree.

Prim's algorithm is generally preferred for dense graphs, whereas Kruskal's algorithm performs better on sparse graphs.

---

## 👩‍💻 Author

Bhargavi