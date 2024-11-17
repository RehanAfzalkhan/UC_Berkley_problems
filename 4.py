def solve(N: int, H: int, D: int, S: int, P: int) -> int:
    """
    Return the minimum time needed for you to exit the storm.

    N: starting health
    H: healing per second
    D: distance out of the storm in meters
    S: running speed in meters per second
    P: storm damage per second
    """

    def is_possible(time: float) -> bool:
        # If we can't cover the distance in this time, it's impossible
        if D / S > time:
            return False

        # Calculate minimum run time needed
        min_run_time = D / S

        # Remaining time can be used for healing
        heal_time = time - min_run_time

        # Calculate final health
        total_damage = time * P  # Damage taken during entire duration
        total_healing = heal_time * H  # Healing during heal time
        final_health = N + total_healing - total_damage

        return final_health >= 0

    # First check if we can run straight out
    straight_time = D / S
    straight_damage = straight_time * P
    if N >= straight_damage:
        return int(straight_time)  # Ensure the return type is an integer

    # Binary search for minimum time needed
    left = D / S  # Minimum time needed to cover distance
    right = 100000  # Large enough upper bound for a more dynamic range

    # If impossible even with maximum time, return -1
    if not is_possible(right):
        return -1

    # Binary search for optimal time
    for _ in range(100):  # Increased iterations for better precision
        mid = (left + right) / 2
        if is_possible(mid):
            right = mid
        else:
            left = mid

    return int(left)  # Ensure the return type is an integer


def main():
    T = int(input())
    for _ in range(T):
        N, H, D, S, P = map(int, input().split())
        print(solve(N, H, D, S, P))


if __name__ == "__main__":  # Corrected the main check
    main()
