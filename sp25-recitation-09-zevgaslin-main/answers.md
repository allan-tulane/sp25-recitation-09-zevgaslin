# CMPS 2200 Recitation 09

## Answers

**Name:**Zev Gaslin
**Name:**Josh Haddad


Place all written answers from `recitation-09.md` here for easier grading.



- **2)**

start with n points, make one edge between every pair: so n(n−1)/2 ≈ O(n²) edges.

Sort the edges = (O(n^2 log n))
Sorting a list of O(n^2) edges takes O(n^2 log n) time.
so total max work is O(n^2 logn)


- **4)**

compute all edges between nodes: O(n^2) edges
sort all edges taes O(n^2 logn) work
