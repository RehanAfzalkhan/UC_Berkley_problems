# def draw_cookie(test_cases):
#     # Process each test case
#     results = []
#     for S in test_cases:
#         result = []
#         i = 0
#         while i < len(S):
#             if S[i] == 'O':
#                 result.append("[###OREO###]")
#                 i += 1
#             elif S[i:i+2] == 'RE':
#                 result.append("[--------]")
#                 i += 2
#             elif S[i] == '&':
#                 result.append("")  # Empty line
#                 i += 1
#         results.append(result)
#     return results

# # Input reading and processing
# def main():
#     T = int(input("Enter the number of test cases: "))
#     test_cases = [input("Enter string for test case {}: ".format(i+1)) for i in range(T)]

#     # Get the results
#     results = draw_cookie(test_cases)

#     # Print the results
#     for result in results:
#         for line in result:
#             print(line)

# if __name__ == "__main__":
#     main()
def draw_cookie(test_cases):
    results = []  # To store the results for all test cases

    for S in test_cases:
        result = []  # To store the result for the current test case
        i = 0
        while i < len(S):
            if S[i] == "O":  # Token O
                result.append("[###OREO###]")
                i += 1
            elif i + 1 < len(S) and S[i : i + 2] == "RE":  # Token RE
                result.append("[--------]")
                i += 2
            elif S[i] == "&":  # Token &
                result.append("")  # Empty line
                i += 1
        results.append(result)

    return results


# Input handling
def main():
    T = int(input())  # Number of test cases
    test_cases = [input().strip() for _ in range(T)]  # List of input strings

    # Get the results
    results = draw_cookie(test_cases)

    # Print the results
    for result in results:
        for line in result:
            print(line)


if __name__ == "__main__":
    main()
