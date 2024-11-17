def min_time_to_escape(N, H, D, S, P):
    # If running directly is possible without dying
    time_to_exit = D / S
    health_loss = time_to_exit * P
    if N >= health_loss:
        return time_to_exit

    # If healing can't offset storm damage, escape is impossible
    if H <= P:
        return -1.0

    # Use binary search to find the minimum time to escape
    low, high = 0, 10**6  # Arbitrary large value for upper bound
    while high - low > 1e-4:  # Precision up to 0.1 seconds
        mid = (low + high) / 2
        health = N - mid * P
        distance = mid * S
        if health + (mid - distance / S) * (H - P) >= 0 and distance >= D:
            high = mid
        else:
            low = mid

    return round(high, 3)


def main():
    # Read number of test cases
    T = int(input())
    results = []

    for _ in range(T):
        # Read inputs for each test case
        N, H, D, S, P = map(int, input().split())
        result = min_time_to_escape(N, H, D, S, P)
        results.append(result)

    # Print results for all test cases
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
