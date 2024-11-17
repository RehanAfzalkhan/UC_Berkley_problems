from collections import deque


# Function to perform BFS and find the shortest path length
def bfs(start, target):
    visited = [False] * 501  # 1-indexed graph
    dist = [-1] * 501  # -1 means unvisited
    queue = deque([start])
    visited[start] = True
    dist[start] = 0

    # BFS
    while queue:
        node = queue.popleft()

        # Query neighbors of current node
        print(f"SCAN {node}")  # Send SCAN query to the judge
        response = input().strip()  # Judge returns a random neighbor of 'node'

        # The judge responds with the label of one of the neighbors
        neighbor = int(response)

        # If we haven't visited this neighbor yet
        if not visited[neighbor]:
            visited[neighbor] = True
            dist[neighbor] = dist[node] + 1
            if neighbor == target:
                return dist[neighbor]
            queue.append(neighbor)

    return dist[target]  # This should never return -1 in a connected graph


# Main function to interact with the judge and process test cases
def main():
    t = int(input())  # Number of test cases

    for _ in range(t):
        # For each test case, perform BFS to find the shortest path
        shortest_path_length = bfs(1, 500)

        # If BFS terminates and we haven't found a path, it's an error (but it should never happen)
        if shortest_path_length == -1:
            print("Error: No path found")
            exit(1)

        # Submit the result
        print(f"SUBMIT {shortest_path_length}")
        result = (
            input().strip()
        )  # Read the result from the judge (CORRECT or WRONG_ANSWER)
        if result == "WRONG_ANSWER":
            exit(1)


if __name__ == "__main__":
    main()
