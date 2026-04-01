"""Graph Algorithms.

Implementation and tests for graph traversal and pathfinding algorithms:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Detecting cycles in an undirected graph
- Checking if a graph is connected
"""

import pytest
from collections import deque


class Graph:
    """An undirected graph represented as an adjacency list."""

    def __init__(self):
        self._adjacency = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph if it doesn't already exist."""
        if vertex not in self._adjacency:
            self._adjacency[vertex] = []

    def add_edge(self, u, v):
        """Add an undirected edge between vertices u and v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self._adjacency[u].append(v)
        self._adjacency[v].append(u)

    def vertices(self):
        """Return a list of all vertices."""
        return list(self._adjacency.keys())

    def neighbors(self, vertex):
        """Return neighbors of a vertex."""
        return self._adjacency.get(vertex, [])

    def bfs(self, start):
        """Breadth-First Search traversal starting from a given vertex.

        Returns nodes in the order they were visited.
        """
        if start not in self._adjacency:
            return []
        visited = set()
        order = []
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in sorted(self._adjacency[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        """Depth-First Search traversal starting from a given vertex.

        Returns nodes in the order they were visited.
        """
        if start not in self._adjacency:
            return []
        visited = set()
        order = []

        def _dfs_recursive(node):
            visited.add(node)
            order.append(node)
            for neighbor in sorted(self._adjacency[node]):
                if neighbor not in visited:
                    _dfs_recursive(neighbor)

        _dfs_recursive(start)
        return order

    def has_cycle(self):
        """Return True if the undirected graph contains a cycle."""
        visited = set()

        def _dfs_cycle(node, parent):
            visited.add(node)
            for neighbor in self._adjacency[node]:
                if neighbor not in visited:
                    if _dfs_cycle(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for vertex in self._adjacency:
            if vertex not in visited:
                if _dfs_cycle(vertex, None):
                    return True
        return False

    def is_connected(self):
        """Return True if all vertices are reachable from any starting vertex."""
        if not self._adjacency:
            return True
        start = next(iter(self._adjacency))
        reachable = set(self.bfs(start))
        return reachable == set(self._adjacency.keys())


# -- Fixtures --

@pytest.fixture
def simple_graph():
    """A simple connected graph:
        1 - 2 - 3
        |       |
        4 - - - 5
    """
    g = Graph()
    for edge in [(1, 2), (2, 3), (3, 5), (4, 5), (1, 4)]:
        g.add_edge(*edge)
    return g


@pytest.fixture
def tree_graph():
    """A tree (no cycles):
        1
       / \\
      2   3
     / \\
    4   5
    """
    g = Graph()
    for edge in [(1, 2), (1, 3), (2, 4), (2, 5)]:
        g.add_edge(*edge)
    return g


@pytest.fixture
def disconnected_graph():
    """Two disconnected components: {1,2,3} and {4,5}."""
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(4, 5)
    return g


# -- BFS Tests --

def test_bfs_visits_all_vertices(simple_graph):
    result = simple_graph.bfs(1)
    assert sorted(result) == [1, 2, 3, 4, 5]


def test_bfs_starts_from_given_vertex(simple_graph):
    result = simple_graph.bfs(1)
    assert result[0] == 1


def test_bfs_on_tree(tree_graph):
    result = tree_graph.bfs(1)
    assert result[0] == 1
    assert sorted(result) == [1, 2, 3, 4, 5]


def test_bfs_single_vertex():
    g = Graph()
    g.add_vertex(1)
    assert g.bfs(1) == [1]


def test_bfs_nonexistent_start():
    g = Graph()
    assert g.bfs(99) == []


# -- DFS Tests --

def test_dfs_visits_all_vertices(simple_graph):
    result = simple_graph.dfs(1)
    assert sorted(result) == [1, 2, 3, 4, 5]


def test_dfs_starts_from_given_vertex(simple_graph):
    result = simple_graph.dfs(1)
    assert result[0] == 1


def test_dfs_on_tree(tree_graph):
    result = tree_graph.dfs(1)
    assert sorted(result) == [1, 2, 3, 4, 5]


def test_dfs_single_vertex():
    g = Graph()
    g.add_vertex(42)
    assert g.dfs(42) == [42]


def test_dfs_nonexistent_start():
    g = Graph()
    assert g.dfs(99) == []


# -- Cycle Detection Tests --

def test_graph_with_cycle_detected(simple_graph):
    assert simple_graph.has_cycle() is True


def test_tree_has_no_cycle(tree_graph):
    assert tree_graph.has_cycle() is False


def test_single_edge_no_cycle():
    g = Graph()
    g.add_edge(1, 2)
    assert g.has_cycle() is False


def test_triangle_has_cycle():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    assert g.has_cycle() is True


def test_empty_graph_no_cycle():
    g = Graph()
    assert g.has_cycle() is False


# -- Connectivity Tests --

def test_connected_graph(simple_graph):
    assert simple_graph.is_connected() is True


def test_disconnected_graph(disconnected_graph):
    assert disconnected_graph.is_connected() is False


def test_single_vertex_is_connected():
    g = Graph()
    g.add_vertex(1)
    assert g.is_connected() is True


def test_empty_graph_is_connected():
    g = Graph()
    assert g.is_connected() is True


def test_two_vertex_connected():
    g = Graph()
    g.add_edge(1, 2)
    assert g.is_connected() is True
