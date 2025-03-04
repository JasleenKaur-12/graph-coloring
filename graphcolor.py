# Function to assign colors to the graph
def greedy_coloring(graph, vertices):
    # To store the color assigned to each vertex
    result = [-1] * vertices

    # Assign the first color to the first vertex
    result[0] = 0

    # Available colors (for each vertex)
    available = [False] * vertices

    # Assign colors to remaining vertices
    for u in range(1, vertices):
        # Mark all adjacent vertices as unavailable
        for i in graph[u]:
            if result[i] != -1:
                available[result[i]] = True

        # Find the first available color
        color = 0
        while color < vertices:
            if not available[color]:
                break
            color += 1
        
        # Assign the found color to the vertex
        result[u] = color

        # Reset the available array for the next iteration
        available = [False] * vertices
    
    return result

# Function to take user input and create the graph
def create_graph():
    vertices = int(input("Enter the number of vertices: "))
    
    # Check if vertices are positive
    if vertices <= 0:
        print("The number of vertices should be a positive integer.")
        return [], 0
    
    edges = int(input("Enter the number of edges: "))

    # Check if edges are non-negative
    if edges < 0:
        print("The number of edges should be a non-negative integer.")
        return [], 0

    graph = [[] for _ in range(vertices)]

    print("Enter the edges (in the format 'u v' where u and v are connected vertices):")
    
    for _ in range(edges):
        u, v = map(int, input().split())
        
        # Check if the vertices are within the valid range
        if u < 0 or u >= vertices or v < 0 or v >= vertices:
            print(f"Invalid edge input: {u} or {v} is out of bounds. Please enter a valid edge.")
            continue
        
        graph[u].append(v)
        graph[v].append(u)  # Since it's an undirected graph

    return graph, vertices

# Main function
def main():
    graph, vertices = create_graph()

    # Check if graph creation was successful
    if not graph:
        return

    # Perform greedy coloring
    colors = greedy_coloring(graph, vertices)
    
    print("\nVertex colors:")
    for v in range(vertices):
        print(f"Vertex {v} -> Color {colors[v]}")

if __name__ == "__main__":
    main()
