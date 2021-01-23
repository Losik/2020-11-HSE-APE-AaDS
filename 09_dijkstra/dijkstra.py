from heapq import heappop, heappush


def read_adjacency_list(vertices_count: int, edges_count: int):
    """Reads a weighted adjacency list from input"""
    # Our vertex indices start with 1 so we just create an
    # array that contains one more element. This prevemts us
    # from gainig an IndexError when accessing the last vertex.
    adjacency_list = [[] for _ in range(vertices_count + 1)]
    for _ in range(edges_count):
        # Edges are weighted
        from_vertex, to_vertex, weight = map(int, input().split())
        # Edges are unordered
        adjacency_list[from_vertex].append((to_vertex, weight))
        adjacency_list[to_vertex].append((from_vertex, weight))

    return adjacency_list


def dijkstra(from_vertex: int, to_vertex: int, adjacency_list: list):
    """
    Finds shortest path from from-vertex to to_vertex. If a path exists
    returns the a tuple of best distrance and best path. Otherwise
    returns None, None
    """

    # Best known distances
    best_distances = [None] * len(adjacency_list)

    # For the known best paths we store previous
    # parents[u] stores previous vertex in the best
    # path from from_vertex to u
    parents = [None] * len(adjacency_list)

    # On each iteration we consider new paths to vertices.
    # We put distance, dst_vertex and previous vertex of
    # such path in a min-heap. Note that shorter paths
    # will be at the top of our heap due to the fact that
    # tuples are compared elementwise.
    paths_heap = [(0, from_vertex, None)]

    # While there are still paths in our priority queue (heap)
    while paths_heap:
        # We pick the shortest path
        distance, vertex, parent = heappop(paths_heap)

        # Vertices in our heap can be repeated with different
        # distances or parent vertices. So we check if we already
        # know the best distance to a dst_vertex of the path.
        # If so, just ignoring such path
        if best_distances[vertex] is None:

            # The best path from the distance heap to yet unprocessed
            # vertex is the best pathoverall. Updating best_distances
            # and parent vertex
            best_distances[vertex] = distance
            parents[vertex] = parent

            # In this particular implementation we want to know the best
            # path till to_vertex. So we can stop our algorithm prematurely
            # when we meet out desired vertex. If you don't stop here the
            # algorithm will find best distances to all vertices from
            # the from_vertex
            if vertex == to_vertex:
                break

            # Considering path that go through vertex as a previous vertex
            # and adding them to our paths_heap
            for adjacent_vertex, weight in adjacency_list[vertex]:
                heappush(paths_heap, (distance + weight, adjacent_vertex, vertex))
    else:
        # While-else loop is a bit tricky. Else block is
        # executed in and only if we exited the loop NOT by
        # a break statement.
        # We exit by a break statement only if we find 
        # an optimal path from from_vertex to to_vertex. If no
        # break occured - there is no such path 
        return None, None

    # If a path exists we restore it (just for the sake of restoring it).
    # We restore the path starting from the last vertex and moving backwards.
    # Such path is reversed so we will have to reverse it back to gain
    # a normal one.
    reverse_path = []
    path_vertex = to_vertex
    while path_vertex is not None:
        reverse_path.append(path_vertex)
        path_vertex = parents[path_vertex]

    # reversed returns a list_reverseiterator object which is not
    # a list. Fixing this
    return best_distances[to_vertex], list(reversed(reverse_path))


def main():
    # Reading our input 
    vertices_count, edges_count = map(int, input().split())
    adjacency_list = read_adjacency_list(vertices_count, edges_count)
    from_vertex, to_vertex = map(int, input().split())

    # Finding best distance and best path
    best_distance, best_path = dijkstra(from_vertex, to_vertex, adjacency_list)

    # Returning out answer 
    print(-1 if best_distance is None else best_distance)


# This code is executed if and only if you run your script as
# an entry point and no timporting it as a module
if __name__ == '__main__':
    main()
