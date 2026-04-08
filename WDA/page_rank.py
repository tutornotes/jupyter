# =============================
# PageRank using Random Walk
# =============================

import numpy as np

# -----------------------------
# a. Define pages
# -----------------------------
pages = ["page1", "page2", "page3", "page4"]
n = len(pages)

# -----------------------------
# b. Define link structure (Adjacency Matrix)
# -----------------------------
# Row = current page, Column = linked page
A = np.array([
    [0, 1, 1, 0],  # page1 → page2, page3
    [0, 0, 1, 1],  # page2 → page3, page4
    [1, 0, 0, 1],  # page3 → page1, page4
    [0, 0, 0, 1]   # page4 → itself (dangling handled)
], dtype=float)

# -----------------------------
# Normalize matrix (probability transition)
# -----------------------------
for i in range(n):
    if A[i].sum() != 0:
        A[i] = A[i] / A[i].sum()
    else:
        A[i] = np.ones(n) / n   # handle dangling node

# -----------------------------
# c. Random Walk Parameters
# -----------------------------
d = 0.85   # damping factor
pr = np.ones(n) / n   # initial equal probability

# -----------------------------
# d. Iterative PageRank Update
# -----------------------------
iterations = 100

for _ in range(iterations):
    pr = (1 - d) / n + d * np.dot(pr, A)

# -----------------------------
# e. Display Final PageRank
# -----------------------------
print("\nFinal PageRank Values:\n")
for i in range(n):
    print(f"{pages[i]} : {pr[i]:.4f}")