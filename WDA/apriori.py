# =============================
# Apriori Algorithm (Frequent Itemsets + Association Rules)
# =============================

from itertools import combinations

# -----------------------------
# a. Transaction Dataset
# -----------------------------
transactions = [
    {"milk", "bread", "butter"},
    {"bread", "butter"},
    {"milk", "bread"},
    {"milk", "butter"},
    {"bread", "butter"},
]

min_support = 2
min_confidence = 0.6

# -----------------------------
# Support Function
# -----------------------------
def get_support(itemset):
    count = sum(1 for t in transactions if itemset.issubset(t))
    return count

# -----------------------------
# b. Generate Frequent Itemsets
# -----------------------------
items = set().union(*transactions)

# L1 (single items)
L = [{item} for item in items if get_support({item}) >= min_support]
freq_itemsets = L.copy()

k = 2

while L:
    candidates = [set(c) for c in combinations(set().union(*L), k)]
    new_L = []

    for c in candidates:
        if get_support(c) >= min_support and c not in new_L:
            new_L.append(c)

    freq_itemsets.extend(new_L)
    L = new_L
    k += 1

# -----------------------------
# Generate Association Rules
# -----------------------------
rules = []

for itemset in freq_itemsets:
    if len(itemset) < 2:
        continue

    for i in range(1, len(itemset)):
        for antecedent in combinations(itemset, i):
            antecedent = set(antecedent)
            consequent = itemset - antecedent

            support_itemset = get_support(itemset)
            support_antecedent = get_support(antecedent)

            confidence = support_itemset / support_antecedent

            if confidence >= min_confidence:
                rules.append((antecedent, consequent, confidence))

# -----------------------------
# c. Display Results
# -----------------------------
print("\nFrequent Itemsets:\n")
for itemset in freq_itemsets:
    print(itemset, "Support:", get_support(itemset))

print("\nAssociation Rules:\n")
for rule in rules:
    print(f"{rule[0]} => {rule[1]} (Confidence: {rule[2]:.2f})")