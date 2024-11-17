# def min_calico_sets(T, test_cases):
#     # Map of letters to their equivalent rotatable forms
#     rotatable = {
#         "C": "C",
#         "I": "I",
#         "L": "L",
#         "O": "O",
#         "N": "C",
#         "A": "A",
#         "B": "B",
#         "D": "D",
#         "E": "E",
#         "F": "F",
#         "G": "G",
#         "H": "H",
#         "J": "J",
#         "K": "K",
#         "M": "M",
#         "P": "P",
#         "Q": "Q",
#         "R": "R",
#         "S": "S",
#         "T": "T",
#         "U": "U",
#         "V": "V",
#         "W": "W",
#         "X": "X",
#         "Y": "Y",
#         "Z": "Z",
#     }

#     # Count available letters in one set of CALICO blocks
#     block_count = {}
#     for letter in rotatable.values():
#         block_count[letter] = block_count.get(letter, 0) + 1

#     results = []
#     for s in test_cases:
#         # Count required letters in the target string
#         required = {}
#         for char in s:
#             if char not in rotatable:
#                 results.append(-1)
#                 break
#             key = rotatable[char]
#             required[key] = required.get(key, 0) + 1
#         else:
#             # Calculate the number of sets needed
#             sets_needed = 0
#             for key, count in required.items():
#                 if key not in block_count:
#                     results.append(-1)
#                     break
#                 sets_needed = max(
#                     sets_needed, (count + block_count[key] - 1) // block_count[key]
#                 )
#             else:
#                 results.append(sets_needed)

#     return results


# # Reading input
# if __name__ == "__main__":
#     T = int(input().strip())
#     test_cases = [input().strip() for _ in range(T)]
#     results = min_calico_sets(T, test_cases)
#     for result in results:
#         print(result)
# import math


# def min_calico_sets():
#     # Input: Number of test cases
#     T = int(input().strip())
#     test_cases = [input().strip() for _ in range(T)]

#     # Rotatable letter equivalence
#     rotatable = {
#         "N": "C"  # N can be formed by rotating C
#     }

#     # Block composition (1 block for each A-Z, plus rotatable mappings)
#     block_count = {chr(i): 1 for i in range(65, 91)}  # A-Z
#     for base, equivalent in rotatable.items():
#         block_count[equivalent] += block_count.get(base, 0)

#     results = []

#     for s in test_cases:
#         required = {}
#         possible = True

#         # Count required letters in the string
#         for char in s:
#             # Handle rotatable letters
#             if char in rotatable:
#                 char = rotatable[char]

#             if char not in block_count:
#                 possible = False
#                 break

#             required[char] = required.get(char, 0) + 1

#         if not possible:
#             results.append(-1)
#             continue

#         # Calculate minimum sets needed
#         max_sets = 0
#         for char, count in required.items():
#             max_sets = max(max_sets, math.ceil(count / block_count[char]))

#         results.append(max_sets)

#     # Output results
#     for result in results:
#         print(result)


# # Main execution
# if __name__ == "__main__":
#     min_calico_sets()
import math


def min_calico_sets():
    # Input: Number of test cases
    T = int(input().strip())
    test_cases = [input().strip() for _ in range(T)]

    # Mapping rotatable letters to their base equivalents
    rotatable = {"N": "C"}  # 'N' can be treated as 'C' in CALICO blocks

    # Block composition: One of each letter (A-Z)
    block_count = {chr(i): 1 for i in range(65, 91)}  # A-Z

    # Merge rotatable counts into base letters
    for source, target in rotatable.items():
        block_count[target] += 1  # Add the rotatable to the base letter count

    results = []

    for s in test_cases:
        required = {}
        possible = True

        # Count required letters for the target string
        for char in s:
            # Convert rotatable letters to their base form
            if char in rotatable:
                char = rotatable[char]

            # If a letter cannot be formed using CALICO blocks
            if char not in block_count:
                possible = False
                break

            # Count the number of each letter required
            required[char] = required.get(char, 0) + 1

        if not possible:
            results.append(-1)
            continue

        # Calculate the minimum sets needed
        max_sets = 0
        for char, count in required.items():
            # Ceiling division to calculate sets for each letter
            sets_needed = math.ceil(count / block_count[char])
            max_sets = max(max_sets, sets_needed)

        results.append(max_sets)

    # Output the results
    for result in results:
        print(result)


# Main execution
if __name__ == "__main__":
    min_calico_sets()
