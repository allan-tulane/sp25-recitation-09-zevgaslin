from collections import defaultdict
from heapq import heappush, heappop
from math import sqrt


def prim(graph):
    """
    Returns a list of MSTs (as sets of (weight, node, parent)), one per connected component.
    """

    def prim_helper(visited, frontier, tree):
        if len(frontier) == 0:
            return tree
        else:
            weight, node, parent = heappop(frontier)
            if node in visited:
                return prim_helper(visited, frontier, tree)
            else:
                print('visiting', node)
                # record this edge in the tree
                tree.add((weight, node, parent))
                visited.add(node)
                for neighbor, w in graph[node]:
                    heappush(frontier, (w, neighbor, node))
                    # compare with dijkstra:
                    # heappush(frontier, (distance + weight, neighbor))

                return prim_helper(visited, frontier, tree)

    forests = []
    cities = set(graph.keys())
    explored = set()
    forests = []
    while explored < cities:
        frontier = []
        tree = set()
        source = next(iter(cities - explored))
        heappush(frontier, (0, source, source))
        prim_helper(explored, frontier, tree)
        forests.append(tree)

    return forests


def test_prim():
    graph = {
        's': {('a', 4), ('b', 8)},
        'a': {('s', 4), ('b', 2), ('c', 5)},
        'b': {('s', 8), ('a', 2), ('c', 3)},
        'c': {('a', 5), ('b', 3), ('d', 3)},
        'd': {('c', 3)},
        'e': {('f', 10)},  # e and f are in a separate component.
        'f': {('e', 10)}
    }

    trees = prim(graph)
    assert len(trees) == 2
    # since we are not guaranteed to get the same order
    # of edges in the answer, we'll check the size and
    # weight of each tree.
    len1 = len(trees[0])
    len2 = len(trees[1])
    assert min([len1, len2]) == 2
    assert max([len1, len2]) == 5

    sum1 = sum(e[0] for e in trees[0])
    sum2 = sum(e[0] for e in trees[1])
    assert min([sum1, sum2]) == 10
    assert max([sum1, sum2]) == 12
    ###


def mst_from_points(points):
    """
    Return the minimum spanning tree for a list of points, using euclidean distance 
    as the edge weight between each pair of points.
    See test_mst_from_points.

    Params:
      points... a list of tuples (city_name, x-coord, y-coord)

    Returns:
      a list of edges of the form (weight, node1, node2) indicating the minimum spanning
      tree connecting the cities in the input.
    """
    graph = {}
    for point in points:
        name = point[0]
        graph[name] = []
    n = len(points)
    for i in range(n):
        name1 = points[i][0]
        for j in range(i + 1, n):
            name2 = points[j][0]
            w = euclidean_distance(points[i], points[j])
            graph[name1].append((name2, w))
            graph[name2].append((name1, w)) 
    edges = list(prim(graph)[0])
    def sort_key(edge):
        return (edge[0], edge[1], edge[2])
    edges.sort(key=sort_key)

    return edges


def euclidean_distance(p1, p2):
    return sqrt((p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


def test_euclidean_distance():
    assert round(euclidean_distance(('a', 5, 10), ('b', 7, 12)), 2) == 2.83


def test_mst_from_points():
    points = [
        ('a', 5, 10),  #(city_name, x-coord, y-coord)
        ('b', 7, 12),
        ('c', 2, 3),
        ('d', 12, 3),
        ('e', 4, 6),
        ('f', 6, 7)
    ]
    tree = mst_from_points(points)
    # check that the weight of the MST is correct.
    assert round(sum(e[0] for e in tree), 2) == 19.04
