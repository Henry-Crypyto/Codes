#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Heng-Yu Hsu

# Function to perform Kruskal's algorithm for single link k-clustering
def greedy_clustering_kruskal(distance_matrix, k):
    n = len(distance_matrix)
    parent = list(range(n))
    rank = [0] * n
    
    def find(target):
        if parent[target] != target:
            parent[target] = find(parent[target])  # Path compression
        return parent[target]
    def union(a, b):
        root_a, root_b = find(a), find(b)
        if root_a != root_b:
            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            elif rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((distance_matrix[i][j], i, j))
    edges.sort()
    
    num_clusters = n
    # Process edges in increasing order of distance
    for distance, a, b in edges:
        if find(a) != find(b):
            if num_clusters == k:
                break
            union(a, b)
            num_clusters -= 1


    
    clusters = {}
    for i in range(n):
        root = find(i)
        if root not in clusters:
            clusters[root] = []
        clusters[root].append(i)
    
    return list(clusters.values()) 

# Use this input 
distance_matrix = [
    [0, 38, 17, 28, 88, 59, 13],
    [38, 0, 52, 49, 83, 91, 59],
    [17, 52, 0, 46, 34, 77, 80],
    [28, 49, 46, 0, 5, 53, 62],
    [88, 83, 34, 5, 0, 43, 33],
    [59, 91, 77, 53, 43, 0, 27],
    [13, 59, 80, 62, 33, 27, 0]
]

# Set k=2 for number of clusters
k = 2  
clusters = greedy_clustering_kruskal(distance_matrix, k)

# Print the resulting clusters
print("Resulting Clusters:", clusters)