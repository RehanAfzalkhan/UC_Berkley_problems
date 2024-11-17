def determine_shape(grid, n, m):
    # Get all the "#" coordinates
    hash_coords = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == "#"]

    if not hash_coords:
        return "Invalid Input"

    # Bounding box for the shape
    min_x = min(x for x, _ in hash_coords)
    max_x = max(x for x, _ in hash_coords)
    min_y = min(y for _, y in hash_coords)
    max_y = max(y for _, y in hash_coords)

    # Check if it's a rectangle
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) not in hash_coords:
                break
        else:
            continue
        break
    else:
        return "ferb"

    # Check if it's a triangle
    # A triangle must form an isosceles right triangle
    for x, y in hash_coords:
        if not (
            (x + 1, y) in hash_coords
            or (x, y + 1) in hash_coords
            or (x + 1, y + 1) in hash_coords
        ):
            return "phineas"

    # If neither a rectangle nor triangle is detected
    return "Invalid Shape"


def main():
    # Read number of test cases
    t = int(input())
    results = []

    for _ in range(t):
        n, m = map(int, input().split())
        grid = [input().strip() for _ in range(n)]
        results.append(determine_shape(grid, n, m))

    # Print results
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
