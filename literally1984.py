import sys


def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)


def generate_visible_houses(limit):
    """Generate all visible house coordinates sorted by Manhattan distance and x-coordinate."""
    visible_houses = []
    seen = set()

    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            g = gcd(x, y)
            reduced_x = x // g
            reduced_y = y // g
            if (reduced_x, reduced_y) not in seen:
                seen.add((reduced_x, reduced_y))
                visible_houses.append(
                    (x, y, x + y)
                )  # Store x, y, and Manhattan distance

    visible_houses.sort(
        key=lambda coord: (coord[2], coord[0])
    )  # Sort by Manhattan distance, then x
    return [(x, y) for x, y, _ in visible_houses]


def find_coordinates(addresses, limit=100):
    """Find coordinates for a list of addresses."""
    max_address = max(addresses)
    # Estimate limit based on the maximum address (it grows logarithmically)
    estimate_limit = int(max_address**0.5) + 1
    limit = max(limit, estimate_limit)

    visible_houses = generate_visible_houses(limit)

    # Ensure we have enough houses generated
    while len(visible_houses) < max_address:
        limit *= 2
        visible_houses = generate_visible_houses(limit)

    return [visible_houses[address - 1] for address in addresses]


# Reading the input from standard input
input_data = sys.stdin.read().strip().splitlines()

t = int(input_data[0])  # Number of test cases
addresses = list(map(int, input_data[1:]))

# Compute results
results = find_coordinates(addresses)

# Write the output to standard output
for x, y in results:
    print(f"{x} {y}")
