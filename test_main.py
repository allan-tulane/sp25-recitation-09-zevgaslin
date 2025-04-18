from main import *

def test_mst_from_points():
    points = [('a', 5, 10), #(city_name, x-coord, y-coord)
              ('b', 7, 12),
              ('c', 2, 3),
              ('d', 12, 3),
              ('e', 4, 6),
              ('f', 6, 7)]
    tree = mst_from_points(points)
    # check that the weight of the MST is correct.
    assert round(sum(e[0] for e in tree), 2) == 19.04

def test_prim():    
    ###TODO
    graph = {
            's': {('a', 4), ('b', 8)},
            'a': {('s', 4), ('b', 2), ('c', 5)},
            'b': {('s', 8), ('a', 2), ('c', 3)}, 
            'c': {('a', 5), ('b', 3), ('d', 3)},
            'd': {('c', 3)},
            'e': {('f', 10)}, # e and f are in a separate component.
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