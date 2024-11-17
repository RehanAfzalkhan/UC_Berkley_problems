def find_optimal_bridge_height(T, test_cases):
    results = []

    for test in test_cases:
        B, N, S = test['B'], test['N'], test['S']
        max_height = max(S)
        min_danger = float('inf')
        optimal_height = 0

        # Compute prefix sums for heights below and above each bridge height
        below_danger = [0] * (max_height + 2)
        above_cost = [0] * (max_height + 2)

        for h in range(1, max_height + 2):
            below_danger[h] = below_danger[h - 1]
            above_cost[h] = above_cost[h - 1]
            for height in S:
                if height < h:
                    below_danger[h] += h - height
                if height >= h:
                    above_cost[h] += height - h

        # Iterate through all possible bridge heights
        for bridge_height in range(max_height + 1):
            danger = below_danger[bridge_height]
            cost = above_cost[bridge_height]
            
            # Check constraints
            if cost <= B:
                if danger < min_danger or (danger == min_danger and bridge_height < optimal_height):
                    min_danger = danger
                    optimal_height = bridge_height

        results.append(optimal_height)

    return results


# Input processing
if __name__ == "__main__":
    T = int(input())
    test_cases = []

    for _ in range(T):
        B, N = map(int, input().split())
        S = list(map(int, input().split()))
        test_cases.append({'B': B, 'N': N, 'S': S})

    # Solve the problem
    results = find_optimal_bridge_height(T, test_cases)

    # Output results
    for result in results:
        print(result)
