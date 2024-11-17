def dfs(grid, i, j, N, M):
    # Stack for DFS to explore all connected land cells
    stack = [(i, j)]
    grid[i][j] = 0  # Mark the current cell as visited
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Directions: up, down, left, right

    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                grid[nx][ny] = 0  # Mark the cell as visited
                stack.append((nx, ny))


def solve(N: int, M: int, G: list[list[int]]) -> int:
    max_islands = 0
    max_height = max(max(row) for row in G)  # Maximum height in the grid

    # Try all possible heights h from 0 to max_height
    for h in range(max_height + 1):
        # Create a binary grid where 1 indicates land (height >= h) and 0 indicates submerged
        grid = [[1 if G[i][j] >= h else 0 for j in range(M)] for i in range(N)]

        # Count the islands using DFS
        island_count = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:  # Found a new island
                    dfs(grid, i, j, N, M)  # Flood the island
                    island_count += 1

        # Track the maximum number of islands
        max_islands = max(max_islands, island_count)

    return max_islands


def main():
    T = int(input())  # Read number of test cases
    for _ in range(T):
        N, M = map(int, input().split())  # Read grid dimensions
        G = [list(map(int, input().split())) for _ in range(N)]  # Read the grid heights
        print(solve(N, M, G))  # Solve the test case and print the result


if __name__ == "__main__":
    main()
