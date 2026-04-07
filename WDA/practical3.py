import numpy as np

pages = ["page1", "page2", "page3", "page4"]
A = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
], dtype=float)

for i in range(len(pages)):
    if A[i].sum() != 0:
        A[i] /= A[i].sum()
    else:
        A[i] = np.ones(len(pages)) / len(pages)

pr = np.ones(len(pages)) / len(pages)
d = 0.85

for _ in range(100):
    pr = (1 - d)/len(pages) + d * np.dot(pr, A)

for i, p in enumerate(pages):
    print(f"{p}: {pr[i]:.4f}")