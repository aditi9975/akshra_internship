import random

# =========================
# TEMPLATE DEFINITIONS (Binary Search Focus)
# =========================

def random_n(min_val=5, max_val=15):
    return random.randint(min_val, max_val)

def random_choice(choices):
    return random.choice(choices)

templates = {
    "level1": {
        "TFQ": [
            lambda: {
                "question": "True or False: Binary Search is faster than Linear Search for large sorted arrays.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used on unsorted arrays.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Binary Search always checks every element in the array.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Binary Search works by dividing the array into halves.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: The array must be sorted for Binary Search to work.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the minimum value in a sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the maximum value in a sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search has a time complexity of O(log n).",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be implemented using a loop.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be implemented using recursion.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search is a type of divide and conquer algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to search for a value in a linked list efficiently.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Binary Search always finds the correct answer if the array is sorted.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the position to insert a new value in a sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can only be used on arrays with an even number of elements.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the first occurrence of a value in a sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the last occurrence of a value in a sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to count the number of times a value appears in a sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the square root of a number.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to solve some optimization problems.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search is slower than Linear Search for large sorted arrays.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Binary Search can be used on a list of strings if they are sorted.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to search in a matrix if it is sorted row-wise and column-wise.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the smallest element greater than a given value.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the largest element smaller than a given value.",
                "answer": "True"
            }
        ],
        "MCQ": [
            lambda: {
                "question": "What is the main requirement for using Binary Search?",
                "options": ["Array must be sorted", "Array must be unsorted", "Array must be empty", "Array must have only even numbers"],
                "answer": "Array must be sorted"
            },
            lambda: {
                "question": "What is the time complexity of Binary Search?",
                "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
                "answer": "O(log n)"
            },
            lambda: {
                "question": "Which of the following is NOT true about Binary Search?",
                "options": ["It works on sorted arrays", "It checks every element", "It divides the array", "It is efficient"],
                "answer": "It checks every element"
            },
            lambda: {
                "question": "How do you find the middle index in Binary Search?",
                "options": ["(low + high) // 2", "(low + high) / 2", "low + high", "high - low"],
                "answer": "(low + high) // 2"
            },
            lambda: {
                "question": "What happens if the value is not found in Binary Search?",
                "options": ["Return -1", "Return 0", "Return None", "Return the last index"],
                "answer": "Return -1"
            },
            lambda: {
                "question": "Which of these is a benefit of Binary Search?",
                "options": ["Fast for large sorted arrays", "Works on unsorted arrays", "Needs more memory", "Checks all elements"],
                "answer": "Fast for large sorted arrays"
            },
            lambda: {
                "question": "Which pointer is updated when arr[mid] < key?",
                "options": ["low", "high", "mid", "key"],
                "answer": "low"
            },
            lambda: {
                "question": "Which pointer is updated when arr[mid] > key?",
                "options": ["low", "high", "mid", "key"],
                "answer": "high"
            },
            lambda: {
                "question": "What is the best case time complexity of Binary Search?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "answer": "O(1)"
            },
            lambda: {
                "question": "Which of the following is NOT a use case for Binary Search?",
                "options": ["Finding an element in a sorted array", "Finding the square root of a number", "Searching in an unsorted array", "Finding the first occurrence of a key"],
                "answer": "Searching in an unsorted array"
            },
            lambda: {
                "question": "What is the output if the key is not found in Binary Search?",
                "options": ["IndexError", "-1", "0", "None"],
                "answer": "-1"
            },
            lambda: {
                "question": "Which of the following is a variant of Binary Search?",
                "options": ["Finding the lower bound", "Finding the upper bound", "Finding the peak element", "All of the above"],
                "answer": "All of the above"
            },
            lambda: {
                "question": "Which data structure is best suited for Binary Search?",
                "options": ["Array", "Linked List", "Stack", "Queue"],
                "answer": "Array"
            },
            lambda: {
                "question": "What is the minimum number of elements required for Binary Search?",
                "options": ["1", "2", "0", "Any number"],
                "answer": "1"
            },
            lambda: {
                "question": "Which of the following is NOT a property of Binary Search?",
                "options": ["Works only on sorted data", "Reduces search space by half", "Linear time complexity", "Can be implemented recursively"],
                "answer": "Linear time complexity"
            },
            lambda: {
                "question": "Which of the following is true about Binary Search?",
                "options": ["It is faster than linear search for large arrays", "It is slower than linear search", "It does not require sorted data", "It cannot be implemented iteratively"],
                "answer": "It is faster than linear search for large arrays"
            },
            lambda: {
                "question": "Which of the following is NOT a step in Binary Search?",
                "options": ["Find the middle element", "Compare with key", "Divide the array", "Sort the array"],
                "answer": "Sort the array"
            },
            lambda: {
                "question": "Which of the following is the correct update for high pointer?",
                "options": ["high = mid - 1", "high = mid + 1", "high = low + 1", "high = key - 1"],
                "answer": "high = mid - 1"
            },
            lambda: {
                "question": "Which of the following is the correct update for low pointer?",
                "options": ["low = mid + 1", "low = mid - 1", "low = high + 1", "low = key + 1"],
                "answer": "low = mid + 1"
            },
            lambda: {
                "question": "Which of the following is NOT a variant of Binary Search?",
                "options": ["Ternary Search", "Lower Bound Search", "Upper Bound Search", "Peak Element Search"],
                "answer": "Ternary Search"
            },
            lambda: {
                "question": "Which of the following is true for Binary Search?",
                "options": ["It is a divide and conquer algorithm", "It is a greedy algorithm", "It is a dynamic programming algorithm", "It is a brute force algorithm"],
                "answer": "It is a divide and conquer algorithm"
            },
            lambda: {
                "question": "What is the average case time complexity of Binary Search?",
                "options": ["O(log n)", "O(n)", "O(1)", "O(n log n)"],
                "answer": "O(log n)"
            },
            lambda: {
                "question": "Which of the following is a disadvantage of Binary Search?",
                "options": ["Requires sorted data", "High time complexity", "Uses extra space", "Cannot find elements"],
                "answer": "Requires sorted data"
            },
            lambda: {
                "question": "What is the maximum number of comparisons in Binary Search for an array of size n?",
                "options": ["log2(n) + 1", "n", "n/2", "n log n"],
                "answer": "log2(n) + 1"
            },
            lambda: {
                "question": "Which of the following can Binary Search NOT do?",
                "options": ["Find the first occurrence", "Find the last occurrence", "Find the maximum element", "Search in unsorted array"],
                "answer": "Search in unsorted array"
            }
        ],
        "MTQ": [
            lambda: {
                "question": "Match the term to its meaning in Binary Search:",
                "pairs": {
                    "low": "Starting index",
                    "high": "Ending index",
                    "mid": "Middle index"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the concept to its property:",
                "pairs": {
                    "Divide and Conquer": "Reduces problem size by half",
                    "Sorted Array": "Precondition",
                    "Stack Space": "Recursive implementation"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the operation to its effect in Binary Search:",
                "pairs": {
                    "arr[mid] == key": "Element found",
                    "arr[mid] < key": "Search right half",
                    "arr[mid] > key": "Search left half"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its update condition:",
                "pairs": {
                    "low": "arr[mid] < key",
                    "high": "arr[mid] > key",
                    "mid": "low + (high - low) // 2"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the complexity to the operation:",
                "pairs": {
                    "O(log n)": "Binary Search",
                    "O(n)": "Linear Search",
                    "O(1)": "Best case Binary Search"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the scenario to the result:",
                "pairs": {
                    "Key present": "Return index",
                    "Key absent": "Return -1",
                    "Empty array": "Return -1"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the algorithm to its requirement:",
                "pairs": {
                    "Binary Search": "Sorted array",
                    "Linear Search": "Any array",
                    "Hashing": "Hash function"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its initial value:",
                "pairs": {
                    "low": "0",
                    "high": "n-1",
                    "mid": "(low + high) // 2"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the variant to its description:",
                "pairs": {
                    "First Occurrence": "Leftmost index",
                    "Last Occurrence": "Rightmost index",
                    "Peak Element": "Maximum in unimodal array"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search type to its result:",
                "pairs": {
                    "Lower Bound": "First >= key",
                    "Upper Bound": "First > key",
                    "Exact Match": "Equal to key"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the error to its cause:",
                "pairs": {
                    "IndexError": "Access out of bounds",
                    "Wrong result": "Unsorted array",
                    "StackOverflow": "Too many recursive calls"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the step to its purpose:",
                "pairs": {
                    "Find mid": "Divide array",
                    "Compare": "Check for key",
                    "Update pointers": "Narrow search"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the use case to the algorithm:",
                "pairs": {
                    "Find square root": "Binary Search",
                    "Find minimum in rotated array": "Binary Search",
                    "Find in unsorted array": "Linear Search"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the complexity to the implementation:",
                "pairs": {
                    "Iterative": "O(1) space",
                    "Recursive": "O(log n) space",
                    "Linear": "O(n) time"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its movement:",
                "pairs": {
                    "low": "Moves right",
                    "high": "Moves left",
                    "mid": "Recomputed each step"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the variant to its application:",
                "pairs": {
                    "Lower Bound": "Insertion position",
                    "Upper Bound": "Next greater element",
                    "Peak Element": "Maximum in mountain array"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the error to its prevention:",
                "pairs": {
                    "Overflow": "Use low + (high - low) // 2",
                    "Infinite loop": "Update pointers correctly",
                    "Wrong result": "Sort array first"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search to its result:",
                "pairs": {
                    "Fixed point": "arr[i] == i",
                    "Missing number": "Gap in sequence",
                    "Closest element": "Minimum difference"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its role:",
                "pairs": {
                    "low": "Start of search",
                    "high": "End of search",
                    "mid": "Current guess"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the following:",
                "pairs": {
                    "Binary Search": "O(log n)",
                    "Linear Search": "O(n)",
                    "Sorting": "O(n log n)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the following:",
                "pairs": {
                    "Divide and Conquer": "Binary Search",
                    "Brute Force": "Linear Search",
                    "Hashing": "Hash Table"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the following:",
                "pairs": {
                    "First element": "arr[0]",
                    "Last element": "arr[n-1]",
                    "Middle element": "arr[(low+high)//2]"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the following:",
                "pairs": {
                    "Best case": "O(1)",
                    "Worst case": "O(log n)",
                    "Average case": "O(log n)"
                },
                "answer": "Correct mapping"
            }
        ],
        "ECQ": [
            lambda: {
                "question": "Fill in the blank: while ____ <= high:",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: mid = (low + ____ ) // 2",
                "answer": "high"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] == key: return ____",
                "answer": "mid"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] < key: ____ = mid + 1",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] > key: ____ = mid - 1",
                "answer": "high"
            },
            lambda: {
                "question": "Fill in the blank: If key is not found, return ____",
                "answer": "-1"
            },
            lambda: {
                "question": "Fill in the blank: To avoid overflow, mid = low + (____ - low) // 2",
                "answer": "high"
            },
            lambda: {
                "question": "Fill in the blank: To find the first occurrence, move high = mid - 1 when arr[mid] ____ key",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To find the last occurrence, move low = mid + 1 when arr[mid] ____ key",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To find the lower bound, check if arr[mid] ____ key",
                "answer": ">="
            },
            lambda: {
                "question": "Fill in the blank: To find the upper bound, check if arr[mid] ____ key",
                "answer": ">"
            },
            lambda: {
                "question": "Fill in the blank: To find the peak element, compare arr[mid] with arr[mid-1] and arr[____]",
                "answer": "mid+1"
            },
            lambda: {
                "question": "Fill in the blank: To find the fixed point, check if arr[mid] ____ mid",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To find the missing number, check if arr[mid] ____ mid + 1",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To find the closest element, update result if abs(arr[mid] - key) ____ abs(arr[result] - key)",
                "answer": "<"
            },
            lambda: {
                "question": "Fill in the blank: To find the minimum in rotated array, compare arr[mid] with arr[____]",
                "answer": "high"
            },
            lambda: {
                "question": "Fill in the blank: To find the maximum in sorted array, return arr[____]",
                "answer": "high"
            },
            lambda: {
                "question": "Fill in the blank: To search in a matrix, treat it as a 1D array of size ____",
                "answer": "rows * cols"
            },
            lambda: {
                "question": "Fill in the blank: To avoid infinite loop, update low or high after each ____",
                "answer": "comparison"
            },
            lambda: {
                "question": "Fill in the blank: To find the insertion position, return ____ when low > high",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: To find the number of steps, use ____ function on n",
                "answer": "log2 or bit_length"
            },
            lambda: {
                "question": "Fill in the blank: To prevent overflow, use mid = low + (high - low) // ____",
                "answer": "2"
            },
            lambda: {
                "question": "Fill in the blank: The first index in an array is ____",
                "answer": "0"
            },
            lambda: {
                "question": "Fill in the blank: The last index in an array of size n is ____",
                "answer": "n-1"
            }
        ],
        "NQ": [
            lambda: (lambda n: {
                "question": f"What is the maximum number of comparisons in Binary Search for an array of size {n}?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For array size {n}, how many steps does worst-case Binary Search take?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of comparisons in Binary Search?",
                "answer": "1"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the best-case time complexity of Binary Search?",
                "answer": "O(1)"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the worst-case time complexity of Binary Search?",
                "answer": "O(log n)"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the average number of comparisons in Binary Search?",
                "answer": str(round(n.bit_length() / 2))
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum depth of recursion in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum depth of recursion in Binary Search?",
                "answer": "1"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of elements checked in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of elements checked in Binary Search?",
                "answer": "1"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of recursive calls in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of recursive calls in Binary Search?",
                "answer": "1"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of iterations in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of iterations in Binary Search?",
                "answer": "1"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of steps in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of steps in Binary Search?",
                "answer": "1"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of comparisons in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of comparisons in Binary Search?",
                "answer": "1"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of steps in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of steps in Binary Search?",
                "answer": "1"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of elements checked in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of elements checked in Binary Search?",
                "answer": "1"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of recursive calls in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of recursive calls in Binary Search?",
                "answer": "1"
            })(random_choice([8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of iterations in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8, 10, 12]))
        ]
    },

    "level2": {
        "TFQ": [
            lambda: {"question": "True or False: Binary Search always reduces the search space by half.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used on a linked list efficiently.", "answer": "False"},
            lambda: {"question": "True or False: Binary Search requires the array to be sorted.", "answer": "True"},
            lambda: {"question": "True or False: The time complexity of Binary Search is O(n).", "answer": "False"},
            lambda: {"question": "True or False: Binary Search can be implemented recursively.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search is faster than Linear Search for large sorted arrays.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can find an element in an unsorted array.", "answer": "False"},
            lambda: {"question": "True or False: Binary Search can be used to find the first occurrence of a number.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to count the number of occurrences of a number.", "answer": "False"},
            lambda: {"question": "True or False: Binary Search can be used on strings if they are sorted.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the minimum in a rotated sorted array.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search always returns the index of the found element.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the square root of a number.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search is not suitable for small arrays.", "answer": "False"},
            lambda: {"question": "True or False: Binary Search can be used to solve optimization problems.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the peak element in a mountain array.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the lower bound of a number.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the upper bound of a number.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the insertion position of a number.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the maximum element in a sorted array.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the minimum element in a sorted array.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the last occurrence of a number.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the first element greater than a given value.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the smallest missing number in a sorted array.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the index of a target value in a rotated sorted array.", "answer": "True"},
            lambda: {"question": "True or False: Binary Search can be used to find the fixed point in a sorted array.", "answer": "True"},
        ],
        "MCQ": [
            lambda: {
                "question": "What is the time complexity of Binary Search in the worst case?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n log n)"],
                "answer": "O(log n)"
            },
            lambda: {
                "question": "Which data structure is best suited for Binary Search?",
                "options": ["Unsorted Array", "Sorted Array", "Linked List", "Stack"],
                "answer": "Sorted Array"
            },
            lambda: {
                "question": "What is the main requirement for applying Binary Search?",
                "options": ["Array must be sorted", "Array must be unsorted", "Array must be reversed", "Array must be empty"],
                "answer": "Array must be sorted"
            },
            lambda: {
                "question": "How do you calculate the middle index in Binary Search?",
                "options": ["(low + high) // 2", "(low + high) / 2", "low + high", "high - low"],
                "answer": "(low + high) // 2"
            },
            lambda: {
                "question": "What happens if the array is not sorted when using Binary Search?",
                "options": ["It works correctly", "It may give wrong results", "It is faster", "It finds the maximum"],
                "answer": "It may give wrong results"
            },
            lambda: {
                "question": "Which of the following is NOT a use case for Binary Search?",
                "options": ["Finding an element", "Finding lower bound", "Finding upper bound", "Sorting an array"],
                "answer": "Sorting an array"
            },
            lambda: {
                "question": "What is the best case time complexity of Binary Search?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "answer": "O(1)"
            },
            lambda: {
                "question": "Which of the following is true about Binary Search?",
                "options": ["It works on any array", "It works only on sorted arrays", "It works only on even-sized arrays", "It works only on odd-sized arrays"],
                "answer": "It works only on sorted arrays"
            },
            lambda: {
                "question": "What is returned if the element is not found in Binary Search?",
                "options": ["-1", "0", "None", "IndexError"],
                "answer": "-1"
            },
            lambda: {
                "question": "Which pointer is updated when arr[mid] < key in Binary Search?",
                "options": ["low", "high", "mid", "key"],
                "answer": "low"
            },
            lambda: {
                "question": "Which pointer is updated when arr[mid] > key in Binary Search?",
                "options": ["low", "high", "mid", "key"],
                "answer": "high"
            },
            lambda: {
                "question": "What is the initial value of low in Binary Search?",
                "options": ["0", "1", "n-1", "mid"],
                "answer": "0"
            },
            lambda: {
                "question": "What is the initial value of high in Binary Search for an array of size n?",
                "options": ["n", "n-1", "0", "mid"],
                "answer": "n-1"
            },
            lambda: {
                "question": "Which of the following is a correct stopping condition for Binary Search?",
                "options": ["low > high", "low < high", "low == high", "low != high"],
                "answer": "low > high"
            },
            lambda: {
                "question": "Which of the following is NOT a variant of Binary Search?",
                "options": ["Finding first occurrence", "Finding last occurrence", "Finding maximum", "Bubble Sort"],
                "answer": "Bubble Sort"
            },
            lambda: {
                "question": "What is the output if the key is found at the first try in Binary Search?",
                "options": ["mid", "low", "high", "n"],
                "answer": "mid"
            },
            lambda: {
                "question": "Which of the following is a disadvantage of Binary Search?",
                "options": ["Requires sorted array", "Slow for large arrays", "Uses more memory", "Cannot find elements"],
                "answer": "Requires sorted array"
            },
            lambda: {
                "question": "Which of the following is a correct recursive call for Binary Search if arr[mid] < key?",
                "options": ["binarySearch(arr, mid+1, high, key)", "binarySearch(arr, low, mid-1, key)", "binarySearch(arr, low, high, key)", "binarySearch(arr, mid, high, key)"],
                "answer": "binarySearch(arr, mid+1, high, key)"
            },
            lambda: {
                "question": "Which of the following is a correct iterative update for high?",
                "options": ["high = mid - 1", "high = mid + 1", "high = low", "high = key"],
                "answer": "high = mid - 1"
            },
            lambda: {
                "question": "What is the maximum number of comparisons in Binary Search for an array of size n?",
                "options": ["log2(n) + 1", "n", "n/2", "1"],
                "answer": "log2(n) + 1"
            },
            lambda: {
                "question": "Which of the following is a correct way to find the middle element?",
                "options": ["(low + high) // 2", "(low + high) / 2", "low + high", "high - low"],
                "answer": "(low + high) // 2"
            },
            lambda: {
                "question": "Which of the following is NOT a property of Binary Search?",
                "options": ["Divide and conquer", "Works on sorted data", "Linear time", "Logarithmic time"],
                "answer": "Linear time"
            },
            lambda: {
                "question": "Which of the following is a correct base case for recursive Binary Search?",
                "options": ["low > high", "low < high", "low == high", "low != high"],
                "answer": "low > high"
            },
            lambda: {
                "question": "Which of the following is a correct way to update low?",
                "options": ["low = mid + 1", "low = mid - 1", "low = high", "low = key"],
                "answer": "low = mid + 1"
            },
            lambda: {
                "question": "Which of the following is a correct way to update high?",
                "options": ["high = mid - 1", "high = mid + 1", "high = low", "high = key"],
                "answer": "high = mid - 1"
            },
        ],
        "MTQ": [
            lambda: {
                "question": "Match the term to its description:",
                "pairs": {
                    "low": "Start index of search",
                    "high": "End index of search",
                    "mid": "Middle index"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the concept to its property:",
                "pairs": {
                    "Binary Search": "O(log n) time",
                    "Linear Search": "O(n) time",
                    "Bubble Sort": "O(n^2) time"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the operation to its effect in Binary Search:",
                "pairs": {
                    "low = mid + 1": "Search right half",
                    "high = mid - 1": "Search left half",
                    "mid = (low + high) // 2": "Find middle"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the variant to its use:",
                "pairs": {
                    "Lower Bound": "First element >= key",
                    "Upper Bound": "First element > key",
                    "Exact Match": "Element == key"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the step to its description:",
                "pairs": {
                    "Initialization": "Set low and high",
                    "Comparison": "Check arr[mid] vs key",
                    "Update": "Change low or high"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its initial value:",
                "pairs": {
                    "low": "0",
                    "high": "n-1",
                    "mid": "(low + high) // 2"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the scenario to the update:",
                "pairs": {
                    "arr[mid] < key": "low = mid + 1",
                    "arr[mid] > key": "high = mid - 1",
                    "arr[mid] == key": "return mid"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the algorithm to its requirement:",
                "pairs": {
                    "Binary Search": "Sorted array",
                    "Linear Search": "Any array",
                    "Selection Sort": "Any array"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the function to its purpose:",
                "pairs": {
                    "binarySearch": "Find element",
                    "lower_bound": "Find first >= key",
                    "upper_bound": "Find first > key"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the complexity to the algorithm:",
                "pairs": {
                    "O(log n)": "Binary Search",
                    "O(n)": "Linear Search",
                    "O(n^2)": "Bubble Sort"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the update to the result:",
                "pairs": {
                    "low = mid + 1": "Search right",
                    "high = mid - 1": "Search left",
                    "return mid": "Found"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the term to its meaning:",
                "pairs": {
                    "Divide and conquer": "Divide problem into subproblems",
                    "Base case": "Stopping condition",
                    "Recursive call": "Function calls itself"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its role:",
                "pairs": {
                    "low": "Start of search",
                    "high": "End of search",
                    "mid": "Current middle"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the variant to its result:",
                "pairs": {
                    "First occurrence": "First index of key",
                    "Last occurrence": "Last index of key",
                    "Any occurrence": "Any index of key"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the function to its input:",
                "pairs": {
                    "binarySearch(arr, low, high, key)": "Array, start, end, target",
                    "lower_bound(arr, key)": "Array, target",
                    "upper_bound(arr, key)": "Array, target"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the step to its action:",
                "pairs": {
                    "Check mid": "Compare arr[mid] and key",
                    "Update low": "low = mid + 1",
                    "Update high": "high = mid - 1"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the property to the algorithm:",
                "pairs": {
                    "Requires sorted data": "Binary Search",
                    "Works on any data": "Linear Search",
                    "Stable sort": "Merge Sort"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the result to the input:",
                "pairs": {
                    "Element found": "Return index",
                    "Element not found": "Return -1",
                    "Search continues": "Update pointers"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the update to the pointer:",
                "pairs": {
                    "low = mid + 1": "Move right",
                    "high = mid - 1": "Move left",
                    "mid = (low + high) // 2": "Find new middle"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search type to its result:",
                "pairs": {
                    "Lower bound": "First >= key",
                    "Upper bound": "First > key",
                    "Exact match": "Element == key"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the function to its output:",
                "pairs": {
                    "binarySearch": "Index or -1",
                    "lower_bound": "Index",
                    "upper_bound": "Index"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the scenario to the result:",
                "pairs": {
                    "Key found": "Return index",
                    "Key not found": "Return -1",
                    "Continue search": "Update pointers"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its update:",
                "pairs": {
                    "low": "mid + 1",
                    "high": "mid - 1",
                    "mid": "(low + high) // 2"
                },
                "answer": "Correct mapping"
            },
        ],
        "ECQ": [
            lambda: {
                "question": "Complete the code: while low <= high: mid = (low + high) // 2; if arr[mid] == key: return ____",
                "answer": "mid"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] < key: ____ = mid + 1",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] > key: ____ = mid - 1",
                "answer": "high"
            },
            lambda: {
                "question": "Complete the stopping condition: while ____ <= high:",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: mid = (____ + high) // 2",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: mid = (low + ____) // 2",
                "answer": "high"
            },
            lambda: {
                "question": "Complete the code: if arr[mid] == key: return ____",
                "answer": "mid"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] < key: ____ = mid + 1",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] > key: ____ = mid - 1",
                "answer": "high"
            },
            lambda: {
                "question": "Complete the code: if low > high: return ____",
                "answer": "-1"
            },
            lambda: {
                "question": "Fill in the blank: while ____ <= high:",
                "answer": "low"
            },
            lambda: {
                "question": "Complete the code: mid = (low + high) // ____",
                "answer": "2"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] == key: return ____",
                "answer": "mid"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] < key: ____ = mid + 1",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] > key: ____ = mid - 1",
                "answer": "high"
            },
            lambda: {
                "question": "Complete the code: if low > high: return ____",
                "answer": "-1"
            },
            lambda: {
                "question": "Fill in the blank: while ____ <= high:",
                "answer": "low"
            },
            lambda: {
                "question": "Complete the code: mid = (low + high) // ____",
                "answer": "2"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] == key: return ____",
                "answer": "mid"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] < key: ____ = mid + 1",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] > key: ____ = mid - 1",
                "answer": "high"
            },
            lambda: {
                "question": "Complete the code: if low > high: return ____",
                "answer": "-1"
            },
            lambda: {
                "question": "Fill in the blank: while ____ <= high:",
                "answer": "low"
            },
            lambda: {
                "question": "Complete the code: mid = (low + high) // ____",
                "answer": "2"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] == key: return ____",
                "answer": "mid"
            },
        ],
        "NQ": [
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of steps in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question":f"If Binary Search takes {n.bit_length()} steps for size {n}, what is the minimum number of steps?",
                "answer": "1"
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the average number of comparisons in Binary Search?",
                "answer": str(round(n.bit_length() / 2))
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the value of mid in the first step?",
                "answer": str((0 + n - 1) // 2)
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the value of high at the start?",
                "answer": str(n - 1)
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the value of low at the start?",
                "answer": "0"
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum value of mid?",
                "answer": str(n - 1)
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the minimum value of mid?",
                "answer": "0"
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of recursive calls in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of iterations in iterative Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the minimum number of iterations in Binary Search?",
                "answer": "1"
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find a missing element?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find the first element?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find the last element?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find the middle element?",
                "answer": "1"
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find an element not present?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find an element at index {n//2}?",
                "answer": "1"
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find an element at index 0?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find an element at index {n-1}?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find an element at index {n//4}?",
                "answer": str(n.bit_length() - 1)
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find an element at index {3*n//4}?",
                "answer": str(n.bit_length() - 1)
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find an element at index {n//8}?",
                "answer": str(n.bit_length() - 2)
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find an element at index {7*n//8}?",
                "answer": str(n.bit_length() - 2)
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find an element at index {n//16}?",
                "answer": str(n.bit_length() - 3)
            })(random_choice([8,10,12,15])),
            lambda: (lambda n: {
                "question": f"For array size {n}, what is the maximum number of comparisons to find an element at index {15*n//16}?",
                "answer": str(n.bit_length() - 3)
            })(random_choice([8,10,12,15])),
        ]
    },

    "level3": {
        "TFQ": [
            lambda: {
                "question": "True or False: Binary Search can be implemented both recursively and iteratively.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search always finds the target in O(1) time.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Binary Search requires the input array to be sorted.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: The space complexity of iterative Binary Search is O(1).",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Recursive Binary Search uses stack space proportional to log n.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the first occurrence of a duplicate element.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be applied to linked lists efficiently.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Binary Search is a divide and conquer algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to search in a rotated sorted array without modifications.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: The worst-case time complexity of Binary Search is O(log n).",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to count the number of occurrences of a key in a sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the smallest element greater than a given value.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the peak element in a unimodal array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the square root of a number.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to solve optimization problems.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search is not suitable for searching in a hash table.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the insertion position of a key in a sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the minimum in a rotated sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the maximum element in a sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to search in a matrix if each row and column is sorted.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the fixed point in a sorted array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the missing number in a sequence.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the element with minimum absolute difference.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the first and last positions of a key.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Binary Search can be used to find the local minimum in an array.",
                "answer": "True"
            }
        ],
        "MCQ": [
            lambda: {
                "question": "Which of the following is a necessary condition for Binary Search?",
                "options": [
                    "Array must be sorted",
                    "Array must be unsorted",
                    "Array must be of even length",
                    "Array must contain only positive numbers"
                ],
                "answer": "Array must be sorted"
            },
            lambda: {
                "question": "What is the time complexity of Binary Search in the worst case?",
                "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
                "answer": "O(log n)"
            },
            lambda: {
                "question": "How is the middle index calculated in Binary Search?",
                "options": [
                    "(low + high) // 2",
                    "(low + high) / 2",
                    "(high - low) // 2",
                    "low + high // 2"
                ],
                "answer": "(low + high) // 2"
            },
            lambda: {
                "question": "What is the space complexity of iterative Binary Search?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "answer": "O(1)"
            },
            lambda: {
                "question": "Which of the following is true about recursive Binary Search?",
                "options": [
                    "It uses extra stack space",
                    "It is always faster than iterative",
                    "It cannot be implemented",
                    "It does not require sorted array"
                ],
                "answer": "It uses extra stack space"
            },
            lambda: {
                "question": "Which pointer is updated when arr[mid] < key in Binary Search?",
                "options": ["low", "high", "mid", "key"],
                "answer": "low"
            },
            lambda: {
                "question": "Which pointer is updated when arr[mid] > key in Binary Search?",
                "options": ["low", "high", "mid", "key"],
                "answer": "high"
            },
            lambda: {
                "question": "What is the best case time complexity of Binary Search?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "answer": "O(1)"
            },
            lambda: {
                "question": "Which of the following is NOT a use case for Binary Search?",
                "options": [
                    "Finding an element in a sorted array",
                    "Finding the square root of a number",
                    "Searching in an unsorted array",
                    "Finding the first occurrence of a key"
                ],
                "answer": "Searching in an unsorted array"
            },
            lambda: {
                "question": "What happens if the array is not sorted when using Binary Search?",
                "options": [
                    "It may return incorrect results",
                    "It works as expected",
                    "It is faster",
                    "It sorts the array first"
                ],
                "answer": "It may return incorrect results"
            },
            lambda: {
                "question": "Which of the following is a variant of Binary Search?",
                "options": [
                    "Finding the lower bound",
                    "Finding the upper bound",
                    "Finding the peak element",
                    "All of the above"
                ],
                "answer": "All of the above"
            },
            lambda: {
                "question": "What is the maximum number of comparisons in Binary Search for an array of size n?",
                "options": [
                    "log2(n) + 1",
                    "n",
                    "n/2",
                    "n log n"
                ],
                "answer": "log2(n) + 1"
            },
            lambda: {
                "question": "Which of the following is true for Binary Search?",
                "options": [
                    "It is a divide and conquer algorithm",
                    "It is a greedy algorithm",
                    "It is a dynamic programming algorithm",
                    "It is a brute force algorithm"
                ],
                "answer": "It is a divide and conquer algorithm"
            },
            lambda: {
                "question": "Which data structure is best suited for Binary Search?",
                "options": [
                    "Array",
                    "Linked List",
                    "Stack",
                    "Queue"
                ],
                "answer": "Array"
            },
            lambda: {
                "question": "What is the minimum number of elements required for Binary Search?",
                "options": [
                    "1",
                    "2",
                    "0",
                    "Any number"
                ],
                "answer": "1"
            },
            lambda: {
                "question": "Which of the following is NOT a property of Binary Search?",
                "options": [
                    "Works only on sorted data",
                    "Reduces search space by half",
                    "Linear time complexity",
                    "Can be implemented recursively"
                ],
                "answer": "Linear time complexity"
            },
            lambda: {
                "question": "What is the output if the key is not found in Binary Search?",
                "options": [
                    "IndexError",
                    "-1 or not found",
                    "0",
                    "None"
                ],
                "answer": "-1 or not found"
            },
            lambda: {
                "question": "Which of the following can Binary Search NOT do?",
                "options": [
                    "Find the first occurrence",
                    "Find the last occurrence",
                    "Find the maximum element",
                    "Search in unsorted array"
                ],
                "answer": "Search in unsorted array"
            },
            lambda: {
                "question": "What is the average case time complexity of Binary Search?",
                "options": [
                    "O(log n)",
                    "O(n)",
                    "O(1)",
                    "O(n log n)"
                ],
                "answer": "O(log n)"
            },
            lambda: {
                "question": "Which of the following is a disadvantage of Binary Search?",
                "options": [
                    "Requires sorted data",
                    "High time complexity",
                    "Uses extra space",
                    "Cannot find elements"
                ],
                "answer": "Requires sorted data"
            },
            lambda: {
                "question": "Which of the following is true about Binary Search?",
                "options": [
                    "It is faster than linear search for large arrays",
                    "It is slower than linear search",
                    "It does not require sorted data",
                    "It cannot be implemented iteratively"
                ],
                "answer": "It is faster than linear search for large arrays"
            },
            lambda: {
                "question": "Which of the following is NOT a step in Binary Search?",
                "options": [
                    "Find the middle element",
                    "Compare with key",
                    "Divide the array",
                    "Sort the array"
                ],
                "answer": "Sort the array"
            },
            lambda: {
                "question": "Which of the following is the correct update for high pointer?",
                "options": [
                    "high = mid - 1",
                    "high = mid + 1",
                    "high = low + 1",
                    "high = key - 1"
                ],
                "answer": "high = mid - 1"
            },
            lambda: {
                "question": "Which of the following is the correct update for low pointer?",
                "options": [
                    "low = mid + 1",
                    "low = mid - 1",
                    "low = high + 1",
                    "low = key + 1"
                ],
                "answer": "low = mid + 1"
            },
            lambda: {
                "question": "Which of the following is NOT a variant of Binary Search?",
                "options": [
                    "Ternary Search",
                    "Lower Bound Search",
                    "Upper Bound Search",
                    "Peak Element Search"
                ],
                "answer": "Ternary Search"
            }
        ],
        "MTQ": [
            lambda: {
                "question": "Match implementation to description:",
                "pairs": {
                    "Recursive Binary Search": "Function calls itself",
                    "Iterative Binary Search": "Uses loop",
                    "Time Complexity": "O(log n)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the term to its meaning in Binary Search:",
                "pairs": {
                    "low": "Starting index",
                    "high": "Ending index",
                    "mid": "Middle index"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the concept to its property:",
                "pairs": {
                    "Divide and Conquer": "Reduces problem size by half",
                    "Sorted Array": "Precondition",
                    "Stack Space": "Recursive implementation"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the operation to its effect in Binary Search:",
                "pairs": {
                    "arr[mid] == key": "Element found",
                    "arr[mid] < key": "Search right half",
                    "arr[mid] > key": "Search left half"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the variant to its use:",
                "pairs": {
                    "Lower Bound": "First position >= key",
                    "Upper Bound": "First position > key",
                    "Peak Element": "Maximum in unimodal array"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the data structure to Binary Search suitability:",
                "pairs": {
                    "Array": "Efficient",
                    "Linked List": "Inefficient",
                    "Hash Table": "Not applicable"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its update condition:",
                "pairs": {
                    "low": "arr[mid] < key",
                    "high": "arr[mid] > key",
                    "mid": "low + (high - low) // 2"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the complexity to the operation:",
                "pairs": {
                    "O(log n)": "Binary Search",
                    "O(n)": "Linear Search",
                    "O(1)": "Best case Binary Search"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the scenario to the result:",
                "pairs": {
                    "Key present": "Return index",
                    "Key absent": "Return -1",
                    "Empty array": "Return -1"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the algorithm to its requirement:",
                "pairs": {
                    "Binary Search": "Sorted array",
                    "Linear Search": "Any array",
                    "Hashing": "Hash function"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its initial value:",
                "pairs": {
                    "low": "0",
                    "high": "n-1",
                    "mid": "(low + high) // 2"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the variant to its description:",
                "pairs": {
                    "First Occurrence": "Leftmost index",
                    "Last Occurrence": "Rightmost index",
                    "Peak Element": "Maximum in unimodal array"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search type to its result:",
                "pairs": {
                    "Lower Bound": "First >= key",
                    "Upper Bound": "First > key",
                    "Exact Match": "Equal to key"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the error to its cause:",
                "pairs": {
                    "IndexError": "Access out of bounds",
                    "Wrong result": "Unsorted array",
                    "StackOverflow": "Too many recursive calls"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the step to its purpose:",
                "pairs": {
                    "Find mid": "Divide array",
                    "Compare": "Check for key",
                    "Update pointers": "Narrow search"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the use case to the algorithm:",
                "pairs": {
                    "Find square root": "Binary Search",
                    "Find minimum in rotated array": "Binary Search",
                    "Find in unsorted array": "Linear Search"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the complexity to the implementation:",
                "pairs": {
                    "Iterative": "O(1) space",
                    "Recursive": "O(log n) space",
                    "Linear": "O(n) time"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its movement:",
                "pairs": {
                    "low": "Moves right",
                    "high": "Moves left",
                    "mid": "Recomputed each step"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the variant to its application:",
                "pairs": {
                    "Lower Bound": "Insertion position",
                    "Upper Bound": "Next greater element",
                    "Peak Element": "Maximum in mountain array"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the error to its prevention:",
                "pairs": {
                    "Overflow": "Use low + (high - low) // 2",
                    "Infinite loop": "Update pointers correctly",
                    "Wrong result": "Sort array first"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search to its result:",
                "pairs": {
                    "Fixed point": "arr[i] == i",
                    "Missing number": "Gap in sequence",
                    "Closest element": "Minimum difference"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the pointer to its role:",
                "pairs": {
                    "low": "Start of search",
                    "high": "End of search",
                    "mid": "Current guess"
                },
                "answer": "Correct mapping"
            }
        ],
        "ECQ": [
            lambda: {
                "question": "Fill in the base case for recursive Binary Search:\nif high >= low:\n    mid = (high + low) // 2\n    if arr[mid] == key:\n        return mid\n    elif arr[mid] > key:\n        return binarySearch(arr, low, mid-1, key)\n    else:\n        return binarySearch(arr, ____, high, key)",
                "answer": "mid + 1"
            },
            lambda: {
                "question": "Complete the condition: while ____ <= high:",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] < key: ____ = mid + 1",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: if arr[mid] > key: ____ = mid - 1",
                "answer": "high"
            },
            lambda: {
                "question": "Complete the return value: if arr[mid] == key: return ____",
                "answer": "mid"
            },
            lambda: {
                "question": "Fill in the blank: mid = (____ + high) // 2",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: mid = (low + ____) // 2",
                "answer": "high"
            },
            lambda: {
                "question": "Fill in the blank: To avoid overflow, mid = low + (____ - low) // 2",
                "answer": "high"
            },
            lambda: {
                "question": "Complete the loop: while low <= ____:",
                "answer": "high"
            },
            lambda: {
                "question": "Fill in the blank: If key is not found, return ____",
                "answer": "-1"
            },
            lambda: {
                "question": "Fill in the blank: To find the first occurrence, move high = mid - 1 when arr[mid] ____ key",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To find the last occurrence, move low = mid + 1 when arr[mid] ____ key",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To find the lower bound, check if arr[mid] ____ key",
                "answer": ">="
            },
            lambda: {
                "question": "Fill in the blank: To find the upper bound, check if arr[mid] ____ key",
                "answer": ">"
            },
            lambda: {
                "question": "Fill in the blank: To find the peak element, compare arr[mid] with arr[mid-1] and arr[____]",
                "answer": "mid+1"
            },
            lambda: {
                "question": "Fill in the blank: To find the fixed point, check if arr[mid] ____ mid",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To find the missing number, check if arr[mid] ____ mid + 1",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To find the closest element, update result if abs(arr[mid] - key) ____ abs(arr[result] - key)",
                "answer": "<"
            },
            lambda: {
                "question": "Fill in the blank: To find the minimum in rotated array, compare arr[mid] with arr[____]",
                "answer": "high"
            },
            lambda: {
                "question": "Fill in the blank: To find the maximum in sorted array, return arr[____]",
                "answer": "high"
            },
            lambda: {
                "question": "Fill in the blank: To search in a matrix, treat it as a 1D array of size ____",
                "answer": "rows * cols"
            },
            lambda: {
                "question": "Fill in the blank: To avoid infinite loop, update low or high after each ____",
                "answer": "comparison"
            },
            lambda: {
                "question": "Fill in the blank: To find the insertion position, return ____ when low > high",
                "answer": "low"
            },
            lambda: {
                "question": "Fill in the blank: To find the number of steps, use ____ function on n",
                "answer": "log2 or bit_length"
            },
            lambda: {
                "question": "Fill in the blank: To prevent overflow, use mid = low + (high - low) // ____",
                "answer": "2"
            }
        ],
        "NQ": [
            lambda: (lambda n: {
                "question": f"If Binary Search takes {n.bit_length()} steps for size {n}, what is the average comparisons?",
                "answer": str(round(n.bit_length() / 2))
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of comparisons in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of comparisons in Binary Search?",
                "answer": "1"
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the worst-case time complexity of Binary Search?",
                "answer": "O(log n)"
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the best-case time complexity of Binary Search?",
                "answer": "O(1)"
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, how many steps does Binary Search take in the worst case?",
                "answer": str(n.bit_length())
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the average number of comparisons in Binary Search?",
                "answer": str(round(n.bit_length() / 2))
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum depth of recursion in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum depth of recursion in Binary Search?",
                "answer": "1"
            })(random_choice(([10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of elements checked in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of elements checked in Binary Search?",
                "answer": "1"
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of recursive calls in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of recursive calls in Binary Search?",
                "answer": "1"
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of iterations in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of iterations in Binary Search?",
                "answer": "1"
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of comparisons in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of comparisons in Binary Search?",
                "answer": "1"
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of steps in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of steps in Binary Search?",
                "answer": "1"
            })(random_choice(([8,10,13,15,17]))),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of elements checked in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,13,15,17])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of elements checked in Binary Search?",
                "answer": "1"
            })(random_choice([8,10,13,15,17])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of recursive calls in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,13,15,17])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of recursive calls in Binary Search?",
                "answer": "1"
            })(random_choice([8,10,13,15,17])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of iterations in Binary Search?",
                "answer": str(n.bit_length())
            })(random_choice([8,10,13,15,17])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of iterations in Binary Search?",
                "answer": "1"
            })(random_choice([8,10,13,15,17]))
        ]
    }
}

# =========================
# MAIN GENERATOR FUNCTION
# =========================

def generate_questions(level: str, num_questions: int):
    level = level.lower()
    if level not in templates:
        raise ValueError("Invalid level. Choose from: level1, level2, level3.")

    typewise_templates = templates[level]
    all_templates = [tpl for tpl_list in typewise_templates.values() for tpl in tpl_list]
    questions = []
    seen = set()
    attempt = 0
    max_attempts = num_questions * 10

    while len(questions) < num_questions and attempt < max_attempts:
        template = random.choice(all_templates)
        q = template()
        if q['question'] not in seen:
            questions.append(q)
            seen.add(q['question'])
        attempt += 1

    #if len(questions) < num_questions:
     #   print(f"\n[!] Only {len(questions)} unique questions could be generated.")

    return questions

# =========================
# USER INPUT
# =========================

if __name__ == "__main__":
    level = input("Enter difficulty level (level1, level2, level3): ").strip()
    num = int(input("Enter number of questions to generate: "))

    try:
        output = generate_questions(level, num)
        for i, q in enumerate(output, 1):
            print(f"\nQ{i}: {q['question']}")
            if 'options' in q:
                for opt in q['options']:
                    print(f"   - {opt}")
            if 'pairs' in q:
                for k, v in q['pairs'].items():
                    print(f"   {k}  ->  {v}")
            print(f"Answer: {q['answer']}")
    except Exception as e:
        print("Error:", e)
