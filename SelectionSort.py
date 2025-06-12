import random

# =========================
# HELPERS
# =========================

def random_n(min_val=5, max_val=20):
    return random.randint(min_val, max_val)

def random_choice(choices):
    return random.choice(choices)

# =========================
# TEMPLATES FOR SELECTION SORT
# =========================

selection_sort_templates = {
    "level1": {
        "TFQ": [
    lambda: {"question": "True or False: Selection Sort is a comparison-based sorting algorithm.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort always selects the maximum element to place at the beginning.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort finds the minimum element and puts it in the correct position.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort has a time complexity of O(n log n).", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort can be used to sort an array in ascending or descending order.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort works by swapping elements after each comparison.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort does not require extra memory beyond the input array.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is faster than Merge Sort on large datasets.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort has a worst-case time complexity of O(n^2).", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort always makes exactly n-1 swaps for an array of size n.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is useful for sorting small arrays.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is an adaptive sorting algorithm.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort is a stable sorting algorithm by default.", "answer": "False"},
    lambda: {"question": "True or False: In Selection Sort, the outer loop runs n-1 times for an array of size n.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort's performance is affected by the initial order of elements.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort is an in-place sorting algorithm.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort compares each element with all other elements in the array.", "answer": "False"},
    lambda: {"question": "True or False: The number of comparisons in Selection Sort depends on input size.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort can sort both integers and strings.", "answer": "True"},
    lambda: {"question": "True or False: The best-case time complexity of Selection Sort is O(n).", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort works well with linked lists.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort is easy to implement and understand.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort uses divide and conquer strategy.", "answer": "False"},
    lambda: {"question": "True or False: After each outer loop iteration, one element is placed in its correct position.", "answer": "True"},
    lambda: {"question": "True or False: In Selection Sort, the largest unsorted element is moved to the end.", "answer": "False"},
],

        "MCQ": [
    lambda: {
        "question": "What is the time complexity of Selection Sort in the worst case?",
        "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "answer": "O(n^2)"
    },
    lambda: {
        "question": "What is the space complexity of Selection Sort?",
        "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
        "answer": "O(1)"
    },
    lambda: {
        "question": "Which of the following sorting algorithms is similar in logic to Selection Sort?",
        "options": ["Insertion Sort", "Bubble Sort", "Heap Sort", "None of these"],
        "answer": "Heap Sort"
    },
    lambda: {
        "question": "How many swaps are made by Selection Sort in the best case?",
        "options": ["0", "1", "n-1", "Depends on data"],
        "answer": "n-1"
    },
    lambda: {
        "question": "In Selection Sort, what is done after finding the minimum element?",
        "options": ["It is ignored", "It is moved to the end", "It is swapped with the first unsorted element", "It is deleted"],
        "answer": "It is swapped with the first unsorted element"
    },
    lambda: {
        "question": "What is the best case time complexity of Selection Sort?",
        "options": ["O(n)", "O(log n)", "O(n^2)", "O(n log n)"],
        "answer": "O(n^2)"
    },
    lambda: {
        "question": "Which of the following is true about Selection Sort?",
        "options": [
            "It is stable",
            "It is adaptive",
            "It is in-place",
            "It uses recursion"
        ],
        "answer": "It is in-place"
    },
    lambda: {
        "question": "Which type of datasets is Selection Sort suitable for?",
        "options": ["Large datasets", "Sorted datasets", "Real-time systems", "Small datasets"],
        "answer": "Small datasets"
    },
    lambda: {
        "question": "Which operation is most frequent in Selection Sort?",
        "options": ["Swap", "Comparison", "Insertion", "Deletion"],
        "answer": "Comparison"
    },
    lambda: {
        "question": "Selection Sort always performs a fixed number of which operations?",
        "options": ["Comparisons", "Swaps", "Shifts", "Recursive calls"],
        "answer": "Swaps"
    },
    lambda: {
        "question": "Which of the following makes Selection Sort different from Bubble Sort?",
        "options": [
            "Selection Sort is stable",
            "Bubble Sort makes fewer comparisons",
            "Selection Sort finds the minimum in each pass",
            "Bubble Sort is faster in worst case"
        ],
        "answer": "Selection Sort finds the minimum in each pass"
    },
    lambda: {
        "question": "What is the first step in each pass of Selection Sort?",
        "options": [
            "Swap first two elements",
            "Find maximum element",
            "Find minimum element",
            "Reverse the array"
        ],
        "answer": "Find minimum element"
    },
    lambda: {
        "question": "Which sorting algorithm has a similar number of comparisons to Selection Sort?",
        "options": ["Merge Sort", "Insertion Sort", "Quick Sort", "Bubble Sort"],
        "answer": "Bubble Sort"
    },
    lambda: {
        "question": "Which sorting algorithm does NOT guarantee stability unless modified?",
        "options": ["Bubble Sort", "Merge Sort", "Selection Sort", "Insertion Sort"],
        "answer": "Selection Sort"
    },
    lambda: {
        "question": "Which of the following sorting algorithms does NOT use divide-and-conquer?",
        "options": ["Merge Sort", "Quick Sort", "Selection Sort", "None of these"],
        "answer": "Selection Sort"
    },
    lambda: {
        "question": "How many total passes does Selection Sort make on an array of size n?",
        "options": ["n", "n+1", "n-1", "log n"],
        "answer": "n-1"
    },
    lambda: {
        "question": "In Selection Sort, which elements are compared in the inner loop?",
        "options": ["Sorted only", "Unsorted only", "All elements", "None"],
        "answer": "Unsorted only"
    },
    lambda: {
        "question": "How many times does the outer loop run in Selection Sort?",
        "options": ["n", "n-1", "log n", "n+1"],
        "answer": "n-1"
    },
    lambda: {
        "question": "Which of the following does Selection Sort NOT do?",
        "options": ["Use extra memory", "Sort in-place", "Work on arrays", "Use nested loops"],
        "answer": "Use extra memory"
    },
    lambda: {
        "question": "Which property of Selection Sort makes it unsuitable for large data?",
        "options": ["High space complexity", "Recursive nature", "O(n^2) time complexity", "Uses stacks"],
        "answer": "O(n^2) time complexity"
    },
    lambda: {
        "question": "Selection Sort is known to be which type of algorithm?",
        "options": ["Stable and adaptive", "Unstable and recursive", "Iterative and in-place", "Randomized"],
        "answer": "Iterative and in-place"
    },
    lambda: {
        "question": "Which of the following is the core idea of Selection Sort?",
        "options": ["Divide and conquer", "Repeated minimum selection", "Recursive partitioning", "Insertion into sorted list"],
        "answer": "Repeated minimum selection"
    },
    lambda: {
        "question": "In Selection Sort, how many comparisons are made for an array of size n?",
        "options": ["n", "n^2", "n(n-1)/2", "log n"],
        "answer": "n(n-1)/2"
    },
    lambda: {
        "question": "What does Selection Sort primarily optimize for?",
        "options": ["Speed", "Memory usage", "Number of swaps", "Recursion depth"],
        "answer": "Number of swaps"
    },
    lambda: {
        "question": "What is the average time complexity of Selection Sort?",
        "options": ["O(n)", "O(n log n)", "O(n^2)", "O(1)"],
        "answer": "O(n^2)"
    }
],

        "MTQ": [
    lambda: {
        "question": "Match the Selection Sort concepts with their correct descriptions (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Time Complexity": "O(1)",
            "Space Complexity": "O(n)",
            "Best Use Case": "Large datasets"
        },
        "answer": {
            "Time Complexity": "O(n^2)",
            "Space Complexity": "O(1)",
            "Best Use Case": "Small datasets"
        }
    },
    lambda: {
        "question": "Match the Sorting Types with the correct property (Note: some matches are incorrect):",
        "pairs": {
            "Selection Sort": "Stable",
            "Bubble Sort": "Unstable",
            "Merge Sort": "O(n^2)"
        },
        "answer": {
            "Selection Sort": "Unstable",
            "Bubble Sort": "Stable",
            "Merge Sort": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match the loop types with their actual function in Selection Sort (Note: the matches may be wrong):",
        "pairs": {
            "Outer Loop": "Finds minimum element",
            "Inner Loop": "Fixes correct position",
            "Swap": "Repeats search"
        },
        "answer": {
            "Outer Loop": "Fixes correct position",
            "Inner Loop": "Finds minimum element",
            "Swap": "Places smallest at current index"
        }
    },
    lambda: {
        "question": "Match the behavior of Selection Sort on different inputs (Note: some are incorrect):",
        "pairs": {
            "Sorted array": "Takes O(n) time",
            "Reverse sorted": "Takes O(n)",
            "All same elements": "No comparisons needed"
        },
        "answer": {
            "Sorted array": "Takes O(n^2) time",
            "Reverse sorted": "Takes O(n^2)",
            "All same elements": "Makes comparisons"
        }
    },
    lambda: {
        "question": "Match the step with what it performs in Selection Sort (note: incorrect mappings given):",
        "pairs": {
            "Start pass": "Place largest element",
            "Find minimum": "Delete it",
            "Swap": "Move max to beginning"
        },
        "answer": {
            "Start pass": "Select starting index of unsorted part",
            "Find minimum": "Compare and find smallest",
            "Swap": "Exchange with current index"
        }
    },
    lambda: {
        "question": "Match terms with their accurate explanation (Incorrect matches present):",
        "pairs": {
            "In-place": "Requires extra space",
            "Stable": "Selection Sort is always stable",
            "Unstable": "Does not allow duplicate values"
        },
        "answer": {
            "In-place": "Does not require extra space",
            "Stable": "Maintains relative order of duplicates",
            "Unstable": "May rearrange equal elements"
        }
    },
    lambda: {
        "question": "Match the sorting algorithms with their correct time complexities (incorrect values shown):",
        "pairs": {
            "Selection Sort": "O(log n)",
            "Merge Sort": "O(n)",
            "Quick Sort": "O(n^2) in average case"
        },
        "answer": {
            "Selection Sort": "O(n^2)",
            "Merge Sort": "O(n log n)",
            "Quick Sort": "O(n log n) in average case"
        }
    },
    lambda: {
        "question": "Match Selection Sort facts (Note: wrong matches below):",
        "pairs": {
            "Type of algorithm": "Divide and Conquer",
            "Sorting method": "Recursive",
            "Comparison method": "Binary Search"
        },
        "answer": {
            "Type of algorithm": "Iterative",
            "Sorting method": "Iterative",
            "Comparison method": "Linear Scan"
        }
    },
    lambda: {
        "question": "Match Selection Sort steps (Note: incorrect mappings):",
        "pairs": {
            "Fix position": "Remove element",
            "Compare elements": "Swap them immediately",
            "Select smallest": "Place it at the end"
        },
        "answer": {
            "Fix position": "Current index of outer loop",
            "Compare elements": "Find smallest in unsorted",
            "Select smallest": "Move it to correct position"
        }
    },
    lambda: {
        "question": "Match operations with their description (some mismatches exist):",
        "pairs": {
            "Comparison": "Swap values",
            "Iteration": "Find maximum",
            "Swap": "Loop through sorted part"
        },
        "answer": {
            "Comparison": "Check which is smaller",
            "Iteration": "Loop through unsorted part",
            "Swap": "Exchange elements"
        }
    },
    lambda: {
        "question": "Match array status with behavior of Selection Sort (note: incorrect mapping):",
        "pairs": {
            "Already sorted": "Performs zero operations",
            "Partially sorted": "Adapts and skips work",
            "Random": "Very fast"
        },
        "answer": {
            "Already sorted": "Still O(n^2) time",
            "Partially sorted": "No adaptivity",
            "Random": "Performs fixed comparisons"
        }
    },
    lambda: {
        "question": "Match performance characteristics (wrong pairs shown):",
        "pairs": {
            "Best Case": "O(n)",
            "Worst Case": "O(n log n)",
            "Average Case": "O(n)"
        },
        "answer": {
            "Best Case": "O(n^2)",
            "Worst Case": "O(n^2)",
            "Average Case": "O(n^2)"
        }
    },
    lambda: {
        "question": "Match memory usage with sorting methods (incorrectly matched):",
        "pairs": {
            "Selection Sort": "O(n)",
            "Merge Sort": "O(1)",
            "Quick Sort": "O(n)"
        },
        "answer": {
            "Selection Sort": "O(1)",
            "Merge Sort": "O(n)",
            "Quick Sort": "O(log n)"
        }
    },
    lambda: {
        "question": "Match concept to fact (some are wrong):",
        "pairs": {
            "Number of swaps": "Varies by input",
            "Number of passes": "Depends on sorting order",
            "Total comparisons": "Always n"
        },
        "answer": {
            "Number of swaps": "Exactly (n-1)",
            "Number of passes": "Exactly (n-1)",
            "Total comparisons": "n(n-1)/2"
        }
    },
    lambda: {
        "question": "Match sorting with stability (incorrect):",
        "pairs": {
            "Selection Sort": "Stable",
            "Bubble Sort": "Unstable",
            "Insertion Sort": "Unstable"
        },
        "answer": {
            "Selection Sort": "Unstable",
            "Bubble Sort": "Stable",
            "Insertion Sort": "Stable"
        }
    },
    lambda: {
        "question": "Match role in sorting process (incorrectly matched):",
        "pairs": {
            "min_index": "Stores max value index",
            "j loop": "Starts from 0",
            "i loop": "Always inner loop"
        },
        "answer": {
            "min_index": "Stores index of smallest element",
            "j loop": "Finds minimum",
            "i loop": "Fixes position"
        }
    },
    lambda: {
        "question": "Match advantages with correct algorithm (wrong matches):",
        "pairs": {
            "Low swaps": "Bubble Sort",
            "Stability": "Selection Sort",
            "In-place and simple": "Merge Sort"
        },
        "answer": {
            "Low swaps": "Selection Sort",
            "Stability": "Bubble Sort",
            "In-place and simple": "Selection Sort"
        }
    },
    lambda: {
        "question": "Match term to Selection Sort description (incorrect):",
        "pairs": {
            "Adaptive": "Adjusts to sorted input",
            "Recursive": "Uses function calls",
            "Iterative": "Runs with log n steps"
        },
        "answer": {
            "Adaptive": "No - always O(n^2)",
            "Recursive": "No - Selection Sort is iterative",
            "Iterative": "Yes - uses loops"
        }
    },
    lambda: {
        "question": "Match complexity to situation (some mismatches shown):",
        "pairs": {
            "O(n^2)": "Best case for Selection Sort",
            "O(n log n)": "Worst case for Selection Sort",
            "O(1)": "Number of passes"
        },
        "answer": {
            "O(n^2)": "Time complexity for all cases",
            "O(n log n)": "Merge Sort complexity",
            "O(1)": "Space complexity of Selection Sort"
        }
    },
    lambda: {
        "question": "Match concept with count (incorrect mappings below):",
        "pairs": {
            "Outer loop": "Runs n times",
            "Swaps": "Varies by input",
            "Comparisons": "Fixed at n"
        },
        "answer": {
            "Outer loop": "Runs n-1 times",
            "Swaps": "Exactly n-1",
            "Comparisons": "n(n-1)/2"
        }
    },
    lambda: {
        "question": "Match scenario with expected result (some matches wrong):",
        "pairs": {
            "All equal elements": "No comparisons",
            "Sorted input": "No iterations",
            "Random input": "O(log n) time"
        },
        "answer": {
            "All equal elements": "O(n^2) comparisons",
            "Sorted input": "Still runs all passes",
            "Random input": "O(n^2) time"
        }
    },
    lambda: {
        "question": "Match code step with what it performs (incorrect matches given):",
        "pairs": {
            "if arr[j] < arr[min_index]": "Swapping step",
            "arr[i], arr[min_index] = ...": "Comparison step",
            "min_index = j": "Skip logic"
        },
        "answer": {
            "if arr[j] < arr[min_index]": "Finds minimum element",
            "arr[i], arr[min_index] = ...": "Swapping step",
            "min_index = j": "Update index of minimum"
        }
    },
    lambda: {
        "question": "Match time complexity terms (wrong matches shown):",
        "pairs": {
            "Best Case": "O(n)",
            "Worst Case": "O(n log n)",
            "Average Case": "O(n)"
        },
        "answer": {
            "Best Case": "O(n^2)",
            "Worst Case": "O(n^2)",
            "Average Case": "O(n^2)"
        }
    },
    lambda: {
        "question": "Match sorting technique with type (incorrect mappings):",
        "pairs": {
            "Selection Sort": "Divide and Conquer",
            "Quick Sort": "In-place but slow",
            "Merge Sort": "In-place and fast"
        },
        "answer": {
            "Selection Sort": "Iterative, not Divide and Conquer",
            "Quick Sort": "In-place and fast",
            "Merge Sort": "Not in-place but fast"
        }
    }
],

        "ECQ": [
    lambda: {
        "question": "Fill in the blank: In Selection Sort, we find the _____ element from the unsorted part.",
        "answer": "minimum"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort has a time complexity of _____ in all cases.",
        "answer": "O(n^2)"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort is _____, meaning it doesn’t use extra space.",
        "answer": "in-place"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort is generally _____ than Merge Sort for large inputs.",
        "answer": "slower"
    },
    lambda: {
        "question": "Fill in the blank: In each pass of Selection Sort, one element is placed at its _____ position.",
        "answer": "correct"
    },
    lambda: {
        "question": "Fill in the blank: The number of comparisons in Selection Sort is _____ of the input order.",
        "answer": "independent"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort is _____ stable sorting algorithm.",
        "answer": "not"
    },
    lambda: {
        "question": "Fill in the blank: The outer loop in Selection Sort runs _____ times for n elements.",
        "answer": "n-1"
    },
    lambda: {
        "question": "Fill in the blank: The total number of swaps in Selection Sort is at most _____.",
        "answer": "n-1"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort repeatedly selects the _____ element from the unsorted part.",
        "answer": "smallest"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort is best suited for _____ sized datasets.",
        "answer": "small"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort maintains _____ space complexity.",
        "answer": "O(1)"
    },
    lambda: {
        "question": "Fill in the blank: In Selection Sort, the inner loop is used to find the _____ element.",
        "answer": "minimum"
    },
    lambda: {
        "question": "Fill in the blank: The worst-case time complexity of Selection Sort is _____.",
        "answer": "O(n^2)"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort compares each element with the rest of the _____.",
        "answer": "array"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort is an _____ algorithm because it modifies the original array.",
        "answer": "in-place"
    },
    lambda: {
        "question": "Fill in the blank: In Selection Sort, we usually use a temporary variable to _____ elements.",
        "answer": "swap"
    },
    lambda: {
        "question": "Fill in the blank: The number of passes in Selection Sort for an array of size n is _____.",
        "answer": "n-1"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort algorithm is easy to _____ and implement.",
        "answer": "understand"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort always takes _____ number of comparisons.",
        "answer": "same"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort selects the minimum and puts it at the _____ of the unsorted part.",
        "answer": "beginning"
    },
    lambda: {
        "question": "Fill in the blank: The Selection Sort algorithm is based on the _____ and conquer paradigm.",
        "answer": "selection"  # Trick question (it's not divide-and-conquer)
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort does not adapt to _____ input arrays.",
        "answer": "sorted"
    },
    lambda: {
        "question": "Fill in the blank: In Selection Sort, after each pass, the size of the unsorted part _____.",
        "answer": "decreases"
    },
    lambda: {
        "question": "Fill in the blank: If all elements are equal, Selection Sort will still perform _____ comparisons.",
        "answer": "n(n-1)/2"
    }
],

        "NQ": [
    lambda: (lambda n: {
        "question": f"How many comparisons does Selection Sort make on an array of size {n}?",
        "answer": str(n * (n - 1) // 2)
    })(random_choice([5, 10, 15])),

    lambda: (lambda n: {
        "question": f"For array of size {n}, how many swaps are performed in Selection Sort?",
        "answer": str(n - 1)
    })(random_choice([6, 12, 18])),

    lambda: (lambda n: {
        "question": f"What is the time complexity (in Big-O) of Selection Sort for array of size {n}?",
        "answer": "O(n^2)"
    })(random_choice([7, 13, 20])),

    lambda: {
        "question": "If Selection Sort makes 45 comparisons, what is the size of the array?",
        "answer": "10"
    },

    lambda: {
        "question": "If Selection Sort performs 9 swaps, what is the array size?",
        "answer": "10"
    },

    lambda: {
        "question": "Calculate total comparisons for Selection Sort on array of size 8.",
        "answer": "28"
    },

    lambda: {
        "question": "Calculate the number of swaps in Selection Sort for array of 15 elements.",
        "answer": "14"
    },

    lambda: {
        "question": "What is the space complexity of Selection Sort?",
        "answer": "O(1)"
    },

    lambda: {
        "question": "Selection Sort makes 3 comparisons in the first pass of array of size 4. How many total comparisons?",
        "answer": "6"
    },

    lambda: {
        "question": "Find total number of passes for array of size 11 using Selection Sort.",
        "answer": "10"
    },

    lambda: {
        "question": "Total comparisons in Selection Sort for array of size 12?",
        "answer": "66"
    },

    lambda: {
        "question": "Find the number of swaps made by Selection Sort for array of size 1.",
        "answer": "0"
    },

    lambda: {
        "question": "If Selection Sort makes 78 comparisons, how many elements were sorted?",
        "answer": "13"
    },

    lambda: {
        "question": "Selection Sort performs how many comparisons for array of size 9?",
        "answer": "36"
    },

    lambda: {
        "question": "How many swaps in Selection Sort for array of size 3?",
        "answer": "2"
    },

    lambda: {
        "question": "Calculate comparisons made for array size 7 using Selection Sort.",
        "answer": "21"
    },

    lambda: {
        "question": "If Selection Sort does 1 swap, what is the minimum array size?",
        "answer": "2"
    },

    lambda: {
        "question": "How many times the outer loop runs in Selection Sort for array of size 5?",
        "answer": "4"
    },

    lambda: {
        "question": "How many inner loop comparisons are made in the last pass of Selection Sort?",
        "answer": "1"
    },

    lambda: {
        "question": "Selection Sort sorts 6 elements. How many comparisons in the second pass?",
        "answer": "4"
    },

    lambda: {
        "question": "If there are 15 elements, what is the total number of passes?",
        "answer": "14"
    },

    lambda: {
        "question": "For array size 4, how many total passes and swaps in Selection Sort?",
        "answer": "3"
    },

    lambda: {
        "question": "Selection Sort makes 10 comparisons and 4 swaps. What is the array size?",
        "answer": "5"
    },

    lambda: {
        "question": "What is the value of comparisons made in first 2 passes of Selection Sort for size 6?",
        "answer": "9"
    },

    lambda: {
        "question": "Selection Sort performs 1+2+3+...+n comparisons. What is the formula?",
        "answer": "n(n-1)/2"
    }
]

    },

    "level2": {
        "TFQ": [
    lambda: {"question": "True or False: Selection Sort always performs the same number of comparisons regardless of the input array.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is stable by default.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort requires extra space proportional to the input size.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort can be optimized to perform fewer swaps on nearly sorted arrays.", "answer": "False"},
    lambda: {"question": "True or False: The best-case time complexity of Selection Sort is O(n^2).", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is a recursive sorting algorithm.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort performs fewer swaps than Bubble Sort in all cases.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort can be used efficiently for large datasets.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort repeatedly selects the maximum element in the unsorted part of the array.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort does not take advantage of partially sorted data.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is an in-place sorting algorithm.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort’s performance depends on the initial order of elements.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort has a space complexity of O(1).", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is more efficient than QuickSort on average.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort only swaps elements when necessary.", "answer": "True"},
    lambda: {"question": "True or False: The number of swaps in Selection Sort is always less than or equal to the number of comparisons.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is commonly used in practical applications for large data sorting.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort can be considered a stable sorting algorithm if implemented carefully.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort’s outer loop runs exactly n-1 times for an array of size n.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort requires O(n) extra memory for sorting.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort is a non-adaptive sorting algorithm.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort always makes n-1 swaps for an array of size n.", "answer": "True"},
    lambda: {"question": "True or False: The inner loop of Selection Sort finds the minimum element in the unsorted portion.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort’s worst-case and best-case time complexities differ significantly.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort works by repeatedly swapping the first element with the minimum element found.", "answer": "False"}
],

        "MCQ": [
    lambda: {
        "question": "Which of the following best describes Selection Sort's space complexity?",
        "options": ["O(n)", "O(log n)", "O(1)", "O(n^2)"],
        "answer": "O(1)"
    },
    lambda: {
        "question": "Selection Sort is classified as which type of algorithm?",
        "options": ["Divide and Conquer", "Comparison-based", "Dynamic Programming", "Greedy"],
        "answer": "Comparison-based"
    },
    lambda: {
        "question": "How many swaps does Selection Sort perform in the best case?",
        "options": ["0", "n", "n-1", "n*(n-1)/2"],
        "answer": "n-1"
    },
    lambda: {
        "question": "Which property does Selection Sort NOT have?",
        "options": ["In-place", "Stable", "Deterministic", "Simple to implement"],
        "answer": "Stable"
    },
    lambda: {
        "question": "Selection Sort is most efficient when used on:",
        "options": ["Large datasets", "Linked lists", "Small datasets", "Datasets with many duplicates"],
        "answer": "Small datasets"
    },
    lambda: {
        "question": "Which loop in Selection Sort is responsible for finding the minimum element?",
        "options": ["Outer loop", "Inner loop", "Both loops", "No loops"],
        "answer": "Inner loop"
    },
    lambda: {
        "question": "What does Selection Sort do after finding the minimum element in each iteration?",
        "options": ["Swaps it with the first unsorted element", "Deletes it", "Moves it to the end", "Ignores it"],
        "answer": "Swaps it with the first unsorted element"
    },
    lambda: {
        "question": "Which of the following is a disadvantage of Selection Sort?",
        "options": [
            "Requires extra memory",
            "Performs many swaps",
            "Time complexity is always O(n^2)",
            "Complex to understand"
        ],
        "answer": "Time complexity is always O(n^2)"
    },
    lambda: {
        "question": "Which of these statements about Selection Sort is true?",
        "options": [
            "It performs fewer comparisons than Bubble Sort",
            "It is adaptive to input order",
            "It always scans the entire unsorted list to find the next element",
            "It is a recursive algorithm"
        ],
        "answer": "It always scans the entire unsorted list to find the next element"
    },
    lambda: {
        "question": "What is the best-case time complexity of Selection Sort?",
        "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "answer": "O(n^2)"
    },
    lambda: {
        "question": "Which characteristic is NOT true for Selection Sort?",
        "options": [
            "In-place sorting",
            "Stable sorting",
            "Deterministic time complexity",
            "Simple implementation"
        ],
        "answer": "Stable sorting"
    },
    lambda: {
        "question": "Which of the following sorting algorithms does Selection Sort most closely resemble?",
        "options": ["Insertion Sort", "Bubble Sort", "Merge Sort", "Quick Sort"],
        "answer": "Bubble Sort"
    },
    lambda: {
        "question": "What happens in each iteration of Selection Sort?",
        "options": [
            "The largest element is moved to the end",
            "The minimum element is found and swapped with the first unsorted element",
            "The array is divided into two halves",
            "Elements are inserted into a sorted sublist"
        ],
        "answer": "The minimum element is found and swapped with the first unsorted element"
    },
    lambda: {
        "question": "Which is NOT a typical use case of Selection Sort?",
        "options": [
            "Sorting small datasets",
            "Educational purposes",
            "Sorting large datasets",
            "Simple embedded systems"
        ],
        "answer": "Sorting large datasets"
    },
    lambda: {
        "question": "What is the space complexity of Selection Sort?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
        "answer": "O(1)"
    },
    lambda: {
        "question": "Which feature best describes Selection Sort?",
        "options": [
            "It is adaptive",
            "It has quadratic time complexity",
            "It is recursive",
            "It uses extra memory"
        ],
        "answer": "It has quadratic time complexity"
    },
    lambda: {
        "question": "Selection Sort performs swaps based on:",
        "options": [
            "The number of elements already sorted",
            "The position of the maximum element",
            "Finding the minimum element each iteration",
            "The position of duplicates"
        ],
        "answer": "Finding the minimum element each iteration"
    },
    lambda: {
        "question": "What does 'in-place' mean in the context of Selection Sort?",
        "options": [
            "It sorts the array without using extra memory",
            "It uses recursion",
            "It sorts linked lists efficiently",
            "It requires additional arrays"
        ],
        "answer": "It sorts the array without using extra memory"
    },
    lambda: {
        "question": "Which of the following is true about Selection Sort's number of swaps?",
        "options": [
            "Equal to the number of comparisons",
            "Always zero",
            "At most n-1 swaps",
            "Equal to n * (n-1) / 2"
        ],
        "answer": "At most n-1 swaps"
    },
    lambda: {
        "question": "Selection Sort is NOT efficient for:",
        "options": [
            "Small arrays",
            "Nearly sorted arrays",
            "Large arrays",
            "Arrays with few elements"
        ],
        "answer": "Large arrays"
    },
    lambda: {
        "question": "Which sorting method does Selection Sort use?",
        "options": [
            "Swapping minimum elements to front",
            "Merging sorted arrays",
            "Recursively partitioning array",
            "Inserting elements into a sorted list"
        ],
        "answer": "Swapping minimum elements to front"
    },
    lambda: {
        "question": "In Selection Sort, which element is swapped in each iteration?",
        "options": [
            "The first unsorted element with the minimum element",
            "The last unsorted element with the maximum element",
            "Any random element",
            "The middle element"
        ],
        "answer": "The first unsorted element with the minimum element"
    },
    lambda: {
        "question": "Which of the following is true about Selection Sort's comparison count?",
        "options": [
            "It always does n*(n-1)/2 comparisons",
            "It performs fewer comparisons on sorted data",
            "It uses divide and conquer to reduce comparisons",
            "It uses a heap data structure"
        ],
        "answer": "It always does n*(n-1)/2 comparisons"
    },
    lambda: {
        "question": "Selection Sort is best described as:",
        "options": [
            "A stable, adaptive sorting algorithm",
            "A simple, in-place, comparison-based algorithm",
            "A recursive, divide and conquer algorithm",
            "An efficient algorithm for large datasets"
        ],
        "answer": "A simple, in-place, comparison-based algorithm"
    },
    lambda: {
        "question": "Which of the following does Selection Sort minimize?",
        "options": [
            "Number of swaps",
            "Number of comparisons",
            "Time complexity",
            "Memory usage"
        ],
        "answer": "Number of swaps"
    }
],

        "MTQ": [
    lambda: {
        "question": "Match Selection Sort terms with their correct definitions (Note: below pairs are mismatched):",
        "pairs": {
            "Selection": "Swapping elements randomly",
            "Stability": "Preserves original order always",
            "Time Complexity": "O(n)"
        },
        "answer": {
            "Selection": "Choosing minimum element each iteration",
            "Stability": "Does NOT preserve original order",
            "Time Complexity": "O(n^2)"
        }
    },
    lambda: {
        "question": "Match the Selection Sort phases with their descriptions (Note: below pairs are mismatched):",
        "pairs": {
            "Finding minimum": "Outer loop control",
            "Swapping": "Searching the list",
            "Iteration": "Swapping elements"
        },
        "answer": {
            "Finding minimum": "Inner loop searching",
            "Swapping": "Exchange minimum with unsorted start",
            "Iteration": "Outer loop progresses"
        }
    },
    lambda: {
        "question": "Match the Selection Sort attributes with correct characteristics (Note: below pairs are mismatched):",
        "pairs": {
            "Space complexity": "O(n)",
            "Best case time": "O(n)",
            "Number of swaps": "Same as comparisons"
        },
        "answer": {
            "Space complexity": "O(1)",
            "Best case time": "O(n^2)",
            "Number of swaps": "At most n-1"
        }
    },
    lambda: {
        "question": "Match Selection Sort terms with accurate explanations (Note: below pairs are mismatched):",
        "pairs": {
            "In-place": "Uses extra memory",
            "Stable": "Maintains element order",
            "Adaptive": "Handles sorted input faster"
        },
        "answer": {
            "In-place": "Does NOT use extra memory",
            "Stable": "Is NOT stable",
            "Adaptive": "Is NOT adaptive"
        }
    },
    lambda: {
        "question": "Match the loop types in Selection Sort with their roles (Note: below pairs are mismatched):",
        "pairs": {
            "Outer loop": "Finds minimum element",
            "Inner loop": "Swaps elements",
            "Swap step": "Controls iteration"
        },
        "answer": {
            "Outer loop": "Controls position to fix next minimum",
            "Inner loop": "Finds minimum element",
            "Swap step": "Swaps minimum with current position"
        }
    },
    lambda: {
        "question": "Match Selection Sort steps with correct actions (Note: below pairs are mismatched):",
        "pairs": {
            "Find minimum": "Swap elements",
            "Swap minimum": "Advance pointer",
            "Increment index": "Select next minimum"
        },
        "answer": {
            "Find minimum": "Scan unsorted part",
            "Swap minimum": "Exchange with first unsorted",
            "Increment index": "Move to next element"
        }
    },
    lambda: {
        "question": "Match Selection Sort terms with true meanings (Note: below pairs are mismatched):",
        "pairs": {
            "Time complexity": "O(n)",
            "Swaps": "Equal to comparisons",
            "Stability": "Yes"
        },
        "answer": {
            "Time complexity": "O(n^2)",
            "Swaps": "At most n-1",
            "Stability": "No"
        }
    },
    lambda: {
        "question": "Match Selection Sort's attributes with correct facts (Note: below pairs are mismatched):",
        "pairs": {
            "Best case": "O(n)",
            "Worst case": "O(n log n)",
            "Extra space": "O(n)"
        },
        "answer": {
            "Best case": "O(n^2)",
            "Worst case": "O(n^2)",
            "Extra space": "O(1)"
        }
    },
    lambda: {
        "question": "Match Selection Sort's process stages with their true descriptions (Note: below pairs are mismatched):",
        "pairs": {
            "Selection": "Divide and conquer",
            "Swapping": "Recursive step",
            "Scanning": "Find max element"
        },
        "answer": {
            "Selection": "Find minimum element",
            "Swapping": "Exchange elements",
            "Scanning": "Find minimum element"
        }
    },
    lambda: {
        "question": "Match Selection Sort terms to their correct statements (Note: below pairs are mismatched):",
        "pairs": {
            "Algorithm type": "Stable",
            "Number of comparisons": "O(n)",
            "Memory usage": "High"
        },
        "answer": {
            "Algorithm type": "Not stable",
            "Number of comparisons": "O(n^2)",
            "Memory usage": "Low (in-place)"
        }
    },
    lambda: {
        "question": "Match the following Selection Sort terms with explanations (Note: below pairs are mismatched):",
        "pairs": {
            "Swap operation": "Find minimum element",
            "Iteration": "Advance the array pointer",
            "Inner loop": "Fix element position"
        },
        "answer": {
            "Swap operation": "Exchange elements",
            "Iteration": "Loop over elements",
            "Inner loop": "Find minimum element"
        }
    },
    lambda: {
        "question": "Match Selection Sort concepts with accurate explanations (Note: below pairs are mismatched):",
        "pairs": {
            "Stable sorting": "Preserves order",
            "Adaptive algorithm": "Faster on sorted data",
            "In-place": "Requires extra array"
        },
        "answer": {
            "Stable sorting": "Not stable",
            "Adaptive algorithm": "Not adaptive",
            "In-place": "Uses no extra array"
        }
    },
    lambda: {
        "question": "Match Selection Sort properties with true characteristics (Note: below pairs are mismatched):",
        "pairs": {
            "Number of swaps": "Equal to comparisons",
            "Best case time": "O(n)",
            "Worst case time": "O(n log n)"
        },
        "answer": {
            "Number of swaps": "At most n-1",
            "Best case time": "O(n^2)",
            "Worst case time": "O(n^2)"
        }
    },
    lambda: {
        "question": "Match Selection Sort terms with correct explanations (Note: below pairs are mismatched):",
        "pairs": {
            "Outer loop": "Swaps elements",
            "Inner loop": "Controls iteration",
            "Swap step": "Finds minimum"
        },
        "answer": {
            "Outer loop": "Controls current position",
            "Inner loop": "Finds minimum element",
            "Swap step": "Swaps elements"
        }
    },
    lambda: {
        "question": "Match Selection Sort components with their functions (Note: below pairs are mismatched):",
        "pairs": {
            "Finding min": "Swapping elements",
            "Swapping": "Moving pointer",
            "Increment pointer": "Searching minimum"
        },
        "answer": {
            "Finding min": "Searching minimum",
            "Swapping": "Swapping elements",
            "Increment pointer": "Moving pointer"
        }
    },
    lambda: {
        "question": "Match the roles of loops and steps in Selection Sort (Note: below pairs are mismatched):",
        "pairs": {
            "Outer loop": "Find minimum",
            "Inner loop": "Swap elements",
            "Swap": "Move to next index"
        },
        "answer": {
            "Outer loop": "Move to next index",
            "Inner loop": "Find minimum",
            "Swap": "Swap elements"
        }
    },
    lambda: {
        "question": "Match Selection Sort phases with their true meanings (Note: below pairs are mismatched):",
        "pairs": {
            "Selection": "Swapping elements randomly",
            "Swapping": "Finding next minimum",
            "Progression": "Fixes position"
        },
        "answer": {
            "Selection": "Finding next minimum",
            "Swapping": "Swapping elements",
            "Progression": "Fixes position"
        }
    },
    lambda: {
        "question": "Match Selection Sort steps with their actual descriptions (Note: below pairs are mismatched):",
        "pairs": {
            "Find minimum": "Move pointer",
            "Swap elements": "Search minimum",
            "Increment index": "Swap elements"
        },
        "answer": {
            "Find minimum": "Search minimum",
            "Swap elements": "Swap elements",
            "Increment index": "Move pointer"
        }
    },
    lambda: {
        "question": "Match Selection Sort concepts with correct meanings (Note: below pairs are mismatched):",
        "pairs": {
            "Stable": "Does not change order",
            "In-place": "Uses extra space",
            "Complexity": "Linear"
        },
        "answer": {
            "Stable": "Not stable",
            "In-place": "No extra space",
            "Complexity": "Quadratic"
        }
    },
    lambda: {
        "question": "Match Selection Sort terms with their true definitions (Note: below pairs are mismatched):",
        "pairs": {
            "Swap count": "Same as comparisons",
            "Time complexity": "Linear",
            "Best case": "Linear"
        },
        "answer": {
            "Swap count": "At most n-1",
            "Time complexity": "Quadratic",
            "Best case": "Quadratic"
        }
    },
    lambda: {
        "question": "Match the Selection Sort steps with their actual roles (Note: below pairs are mismatched):",
        "pairs": {
            "Scan for minimum": "Swap elements",
            "Swap elements": "Move pointer",
            "Move pointer": "Find minimum"
        },
        "answer": {
            "Scan for minimum": "Find minimum",
            "Swap elements": "Swap elements",
            "Move pointer": "Move pointer"
        }
    },
    lambda: {
        "question": "Match Selection Sort concepts with their true descriptions (Note: below pairs are mismatched):",
        "pairs": {
            "Algorithm type": "Stable",
            "Memory usage": "High",
            "Best case time": "Linear"
        },
        "answer": {
            "Algorithm type": "Not stable",
            "Memory usage": "Low",
            "Best case time": "Quadratic"
        }
    },
    lambda: {
        "question": "Match Selection Sort properties with correct facts (Note: below pairs are mismatched):",
        "pairs": {
            "Adaptive": "Yes",
            "Stable": "Yes",
            "Space complexity": "O(n)"
        },
        "answer": {
            "Adaptive": "No",
            "Stable": "No",
            "Space complexity": "O(1)"
        }
    },
    lambda: {
        "question": "Match the phases of Selection Sort with their actual purposes (Note: below pairs are mismatched):",
        "pairs": {
            "Find minimum": "Fix position",
            "Swap": "Find minimum",
            "Advance index": "Swap elements"
        },
        "answer": {
            "Find minimum": "Find minimum",
            "Swap": "Swap elements",
            "Advance index": "Fix position"
        }
    }
],

        "ECQ": [
    lambda: {
        "question": "Fill in the blank: The variable used to store the index of the minimum element is _____.",
        "answer": "min_index"
    },
    lambda: {
        "question": "Fill in the blank: The outer loop of Selection Sort runs from index 0 to ____ - 1.",
        "answer": "len(arr)"
    },
    lambda: {
        "question": "Complete the statement: Selection Sort swaps the minimum element with the element at index _____.",
        "answer": "i"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort is called an _____ sorting algorithm because it does not adapt to input data.",
        "answer": "non-adaptive"
    },
    lambda: {
        "question": "Fill in the blank: The inner loop in Selection Sort starts scanning from index _____.",
        "answer": "i + 1"
    },
    lambda: {
        "question": "Complete the code: for i in range(len(arr)): min_index = i; for j in range(i + 1, _____):",
        "answer": "len(arr)"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort requires ____ extra space, making it an in-place algorithm.",
        "answer": "constant"
    },
    lambda: {
        "question": "Complete the code: if arr[j] < arr[min_index]: min_index = _____",
        "answer": "j"
    },
    lambda: {
        "question": "Fill in the blank: The maximum number of swaps performed by Selection Sort is _____.",
        "answer": "len(arr) - 1"
    },
    lambda: {
        "question": "Fill in the blank: The time complexity of Selection Sort in the worst case is _____.",
        "answer": "O(n^2)"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort is _____ stable, meaning it may change the relative order of equal elements.",
        "answer": "not"
    },
    lambda: {
        "question": "Complete the code: Swap arr[i] and arr[min_index] using a temporary variable _____",
        "answer": "temp"
    },
    lambda: {
        "question": "Fill in the blank: In Selection Sort, the outer loop controls the position where the _____ element is placed.",
        "answer": "minimum"
    },
    lambda: {
        "question": "Fill in the blank: The inner loop scans the _____ portion of the array to find the minimum element.",
        "answer": "unsorted"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort performs _____ comparisons on an array of size n.",
        "answer": "n * (n - 1) / 2"
    },
    lambda: {
        "question": "Complete the code: To swap two elements, you can write arr[i], arr[min_index] = arr[min_index], _____.",
        "answer": "arr[i]"
    },
    lambda: {
        "question": "Fill in the blank: The number of iterations of the inner loop decreases by _____ after each outer loop iteration.",
        "answer": "1"
    },
    lambda: {
        "question": "Complete the code: for j in range(i + 1, len(arr)): if arr[j] < arr[min_index]: _____ = j",
        "answer": "min_index"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort does not perform well on _____ datasets due to its quadratic time complexity.",
        "answer": "large"
    },
    lambda: {
        "question": "Fill in the blank: Selection Sort is easy to implement but inefficient for _____ inputs.",
        "answer": "large"
    },
    lambda: {
        "question": "Complete the code: Initialize min_index with the value _____ in each iteration of the outer loop.",
        "answer": "i"
    },
    lambda: {
        "question": "Fill in the blank: The final sorted portion of the array grows from the _____ to the right.",
        "answer": "left"
    },
    lambda: {
        "question": "Fill in the blank: After each pass, the minimum element is placed at its correct _____ in the array.",
        "answer": "position"
    },
    lambda: {
        "question": "Fill in the blank: The swap operation exchanges the minimum element with the element at index _____.",
        "answer": "i"
    },
    lambda: {
        "question": "Complete the code: Selection Sort is not _____ because it always scans the entire unsorted array segment.",
        "answer": "adaptive"
    }
],

        "NQ": [
    lambda: (lambda n: {
        "question": f"In Selection Sort, how many swaps are made in total for an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([7, 12, 20])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many total comparisons does Selection Sort perform?",
        "answer": str(n * (n - 1) // 2)
    })(random_choice([8, 10, 15])),

    lambda: (lambda n: {
        "question": f"How many iterations does the outer loop run in Selection Sort for an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([9, 14, 18])),

    lambda: (lambda n: {
        "question": f"What is the total number of iterations in the inner loop over the whole run of Selection Sort on an array of size {n}?",
        "answer": str(n * (n - 1) // 2)
    })(random_choice([6, 11, 16])),

    lambda: (lambda n: {
        "question": f"How many comparisons are made in the first pass of Selection Sort for an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([5, 7, 10])),

    lambda: (lambda n: {
        "question": f"In Selection Sort, how many comparisons are made in the second pass on an array of size {n}?",
        "answer": str(n - 2)
    })(random_choice([6, 8, 12])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many total swaps will Selection Sort perform if the array is already sorted?",
        "answer": str(n - 1)
    })(random_choice([8, 15, 22])),

    lambda: (lambda n: {
        "question": f"How many swaps are done in Selection Sort for an array of size {n} in the worst case?",
        "answer": str(n - 1)
    })(random_choice([7, 14, 21])),

    lambda: (lambda n: {
        "question": f"Calculate the total number of elements Selection Sort compares in the entire process for an array of size {n}.",
        "answer": str(n * (n - 1) // 2)
    })(random_choice([10, 12, 20])),

    lambda: (lambda n: {
        "question": f"What is the number of comparisons in Selection Sort's third pass on an array of size {n}?",
        "answer": str(n - 3)
    })(random_choice([7, 9, 13])),

    lambda: (lambda n: {
        "question": f"Find the total number of passes in Selection Sort for an array of size {n}.",
        "answer": str(n - 1)
    })(random_choice([6, 11, 17])),

    lambda: (lambda n: {
        "question": f"How many comparisons does Selection Sort perform on the last pass for an array of size {n}?",
        "answer": "1"
    })(random_choice([5, 8, 12])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many total swaps will Selection Sort perform if all elements are distinct?",
        "answer": str(n - 1)
    })(random_choice([9, 16, 23])),

    lambda: (lambda n: {
        "question": f"How many comparisons does Selection Sort make during the first two passes combined for an array of size {n}?",
        "answer": str((n - 1) + (n - 2))
    })(random_choice([7, 13, 19])),

    lambda: (lambda n: {
        "question": f"In Selection Sort, total comparisons after first {k} passes for array size {n} is?",
        "answer": str(sum([n - i - 1 for i in range(k)]))
    })(random_choice([5, 6, 7])),  # 'k' is chosen as 5,6,7 here

    lambda: (lambda n: {
        "question": f"Calculate the number of swaps if Selection Sort is run on an array of size {n} with repeated elements.",
        "answer": str(n - 1)
    })(random_choice([7, 10, 15])),

    lambda: (lambda n: {
        "question": f"For an array size {n}, what is the difference between number of comparisons and swaps in Selection Sort?",
        "answer": str(n * (n - 1) // 2 - (n - 1))
    })(random_choice([8, 12, 20])),

    lambda: (lambda n: {
        "question": f"How many comparisons does Selection Sort perform on an array of size {n} in the average case?",
        "answer": str(n * (n - 1) // 2)
    })(random_choice([9, 15, 18])),

    lambda: (lambda n: {
        "question": f"What is the minimum number of swaps Selection Sort can perform on an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([6, 11, 13])),

    lambda: (lambda n: {
        "question": f"In Selection Sort, how many elements remain unsorted after {1} passes for an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([5, 7, 9])),  # p = 5,7,9 as example number of passes

    lambda: (lambda n: {
        "question": f"During Selection Sort on an array of size {n}, how many total iterations does the inner loop perform?",
        "answer": str(n * (n - 1) // 2)
    })(random_choice([10, 14, 17])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many comparisons does Selection Sort skip due to the sorted portion growing?",
        "answer": str(sum([i for i in range(n - 1)]))
    })(random_choice([8, 12, 15])),

    lambda: (lambda n: {
        "question": f"What is the total number of times the minimum element is updated in Selection Sort on an array of size {n}?",
        "answer": str(n * (n - 1) // 2)
    })(random_choice([6, 10, 13])),

    lambda: (lambda n: {
        "question": f"In Selection Sort, after how many passes will the entire array of size {n} be sorted?",
        "answer": str(n - 1)
    })(random_choice([7, 12, 19]))
]

    },

    "level3": {
        "TFQ": [
    lambda: {"question": "True or False: Selection Sort can be modified to be stable without increasing its time complexity.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort performs the same number of comparisons regardless of the initial order of elements.", "answer": "True"},
    lambda: {"question": "True or False: The number of swaps in Selection Sort depends on the initial order of the array.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort has a better best-case time complexity than its worst-case.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort is an in-place sorting algorithm.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is more efficient than QuickSort on average.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort uses divide and conquer strategy.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort requires additional memory proportional to the input size.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort is useful for sorting linked lists efficiently.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort always selects the minimum element during each iteration.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort can be used for sorting large datasets efficiently.", "answer": "False"},
    lambda: {"question": "True or False: The performance of Selection Sort does not improve even if the array is partially sorted.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort makes at most n-1 swaps for an array of size n.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort can be adapted to sort in descending order by selecting the maximum element in each pass.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is considered a stable sorting algorithm in its basic form.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort is more suitable than Bubble Sort when minimizing the number of swaps is important.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort’s time complexity is independent of the distribution of input values.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort can be parallelized easily to improve performance.", "answer": "False"},
    lambda: {"question": "True or False: The worst-case and average-case time complexity of Selection Sort are both O(n^2).", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort modifies the input array during its execution.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is preferable over insertion sort for nearly sorted data.", "answer": "False"},
    lambda: {"question": "True or False: The inner loop in Selection Sort always runs fewer times with each outer loop iteration.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort can be considered inefficient for real-time systems requiring fast response.", "answer": "True"},
    lambda: {"question": "True or False: Selection Sort is a recursive sorting algorithm.", "answer": "False"},
    lambda: {"question": "True or False: Selection Sort does not require any extra space besides a few variables.", "answer": "True"}
],

        "MCQ": [
    lambda: {
        "question": "Which of the following statements about Selection Sort is TRUE?",
        "options": [
            "It is a stable sorting algorithm by default",
            "It has a worst-case time complexity of O(n log n)",
            "It performs a fixed number of swaps regardless of input",
            "It requires additional memory proportional to input size"
        ],
        "answer": "It performs a fixed number of swaps regardless of input"
    },
    lambda: {
        "question": "What is the main factor that makes Selection Sort inefficient compared to QuickSort?",
        "options": [
            "High number of swaps",
            "High number of comparisons",
            "High space complexity",
            "Uses recursion extensively"
        ],
        "answer": "High number of comparisons"
    },
    lambda: {
        "question": "How many swaps does Selection Sort perform in the best, average, and worst cases?",
        "options": [
            "O(n^2) swaps",
            "O(n log n) swaps",
            "Exactly n - 1 swaps",
            "Depends on input order"
        ],
        "answer": "Exactly n - 1 swaps"
    },
    lambda: {
        "question": "Which property of Selection Sort can be a disadvantage when sorting large datasets?",
        "options": [
            "Stable sorting",
            "In-place sorting",
            "Consistent O(n²) comparisons",
            "Adaptive behavior"
        ],
        "answer": "Consistent O(n²) comparisons"
    },
    lambda: {
        "question": "In Selection Sort, what does the outer loop index represent?",
        "options": [
            "The current minimum element index",
            "The boundary between sorted and unsorted parts",
            "The element to be swapped",
            "The maximum element found so far"
        ],
        "answer": "The boundary between sorted and unsorted parts"
    },
    lambda: {
        "question": "Why is Selection Sort considered inefficient for nearly sorted arrays?",
        "options": [
            "Because it performs unnecessary swaps",
            "Because it always performs the same number of comparisons",
            "Because it uses extra memory",
            "Because it uses recursion"
        ],
        "answer": "Because it always performs the same number of comparisons"
    },
    lambda: {
        "question": "Which of the following is NOT true about Selection Sort?",
        "options": [
            "It is an in-place algorithm",
            "It always makes n-1 swaps",
            "It is stable by default",
            "Its time complexity is O(n²)"
        ],
        "answer": "It is stable by default"
    },
    lambda: {
        "question": "What is the space complexity of Selection Sort?",
        "options": [
            "O(1)",
            "O(n)",
            "O(log n)",
            "O(n²)"
        ],
        "answer": "O(1)"
    },
    lambda: {
        "question": "How can Selection Sort be modified to make it stable?",
        "options": [
            "Use an auxiliary array",
            "Only swap when necessary",
            "Insert the minimum element and shift others",
            "It cannot be made stable"
        ],
        "answer": "Insert the minimum element and shift others"
    },
    lambda: {
        "question": "Which sorting algorithm is generally more efficient than Selection Sort on large datasets?",
        "options": [
            "Bubble Sort",
            "Insertion Sort",
            "QuickSort",
            "Counting Sort"
        ],
        "answer": "QuickSort"
    },
    lambda: {
        "question": "What does Selection Sort do in each iteration of the inner loop?",
        "options": [
            "Selects the minimum element in the unsorted part",
            "Swaps two elements",
            "Partitions the array",
            "Recursively sorts subarrays"
        ],
        "answer": "Selects the minimum element in the unsorted part"
    },
    lambda: {
        "question": "Why does Selection Sort always make exactly n-1 swaps?",
        "options": [
            "Because it swaps once per outer loop iteration",
            "Because it swaps after every comparison",
            "Because it uses recursive swapping",
            "Because it swaps randomly"
        ],
        "answer": "Because it swaps once per outer loop iteration"
    },
    lambda: {
        "question": "Which of these is a typical use case for Selection Sort?",
        "options": [
            "Sorting large datasets quickly",
            "Sorting small datasets with limited memory",
            "Sorting data with many duplicates",
            "Sorting data already mostly sorted"
        ],
        "answer": "Sorting small datasets with limited memory"
    },
    lambda: {
        "question": "Which statement about the inner loop in Selection Sort is TRUE?",
        "options": [
            "It runs a decreasing number of times each outer loop iteration",
            "It runs the same number of times in every iteration",
            "It runs only once per iteration",
            "It swaps elements each time"
        ],
        "answer": "It runs a decreasing number of times each outer loop iteration"
    },
    lambda: {
        "question": "In Selection Sort, what happens if the minimum element is already in the correct position?",
        "options": [
            "No swap is performed",
            "Swap with itself",
            "Algorithm restarts",
            "Array is reversed"
        ],
        "answer": "No swap is performed"
    },
    lambda: {
        "question": "Which of the following best describes Selection Sort's approach?",
        "options": [
            "Divide and conquer",
            "Incremental insertion",
            "Repeated selection and swapping",
            "Recursive partitioning"
        ],
        "answer": "Repeated selection and swapping"
    },
    lambda: {
        "question": "What is a disadvantage of Selection Sort related to the number of comparisons?",
        "options": [
            "It performs fewer comparisons than Bubble Sort",
            "It performs O(n log n) comparisons",
            "It performs O(n²) comparisons regardless of input",
            "It performs no comparisons on sorted arrays"
        ],
        "answer": "It performs O(n²) comparisons regardless of input"
    },
    lambda: {
        "question": "Which part of Selection Sort is responsible for finding the minimum element?",
        "options": [
            "Outer loop",
            "Inner loop",
            "Swap operation",
            "Base case"
        ],
        "answer": "Inner loop"
    },
    lambda: {
        "question": "In Selection Sort, the 'swap' step is:",
        "options": [
            "Performed after every comparison",
            "Performed only when the minimum is different from current position",
            "Performed at the start of the algorithm",
            "Not necessary for the algorithm to work"
        ],
        "answer": "Performed only when the minimum is different from current position"
    },
    lambda: {
        "question": "Which of the following sorting algorithms generally outperforms Selection Sort in practice?",
        "options": [
            "Bubble Sort",
            "Insertion Sort",
            "Merge Sort",
            "Gnome Sort"
        ],
        "answer": "Merge Sort"
    },
    lambda: {
        "question": "Selection Sort's performance is primarily limited by:",
        "options": [
            "Number of swaps",
            "Number of comparisons",
            "Memory usage",
            "Recursive depth"
        ],
        "answer": "Number of comparisons"
    },
    lambda: {
        "question": "Which sorting algorithm does NOT share the same time complexity as Selection Sort?",
        "options": [
            "Insertion Sort",
            "Bubble Sort",
            "Merge Sort",
            "Selection Sort"
        ],
        "answer": "Merge Sort"
    },
    lambda: {
        "question": "What is the typical behavior of Selection Sort on nearly sorted data?",
        "options": [
            "Runs faster than average",
            "Runs slower than average",
            "Runs the same as always",
            "Does not work correctly"
        ],
        "answer": "Runs the same as always"
    },
    lambda: {
        "question": "Which feature differentiates Selection Sort from Insertion Sort?",
        "options": [
            "Number of swaps performed",
            "Number of comparisons performed",
            "Whether it is in-place",
            "Whether it is stable"
        ],
        "answer": "Number of swaps performed"
    },
    lambda: {
        "question": "Which is a limitation of Selection Sort in terms of adaptability?",
        "options": [
            "It adapts well to sorted data",
            "It performs fewer comparisons on sorted data",
            "It always performs the same comparisons regardless of input",
            "It is efficient for large data"
        ],
        "answer": "It always performs the same comparisons regardless of input"
    }
],

        "MTQ": [
    lambda: {
        "question": "Match the sorting algorithm terms with their correct definitions (Note: below pairs are incorrectly matched):",
        "pairs": {
            "In-place Sorting": "Requires extra space proportional to input",
            "Stable Sorting": "May reorder equal elements",
            "Selection Sort": "Stable by default"
        },
        "answer": {
            "In-place Sorting": "Sorts without requiring extra space",
            "Stable Sorting": "Maintains relative order of equal elements",
            "Selection Sort": "Unstable"
        }
    },
    lambda: {
        "question": "Match the following Selection Sort operations with their descriptions (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Outer Loop": "Finds minimum element in the unsorted array",
            "Inner Loop": "Swaps minimum element to correct position",
            "Swap": "Runs from first to last element"
        },
        "answer": {
            "Outer Loop": "Runs from first to last element",
            "Inner Loop": "Finds minimum element in the unsorted array",
            "Swap": "Swaps minimum element to correct position"
        }
    },
    lambda: {
        "question": "Match these sorting complexities with their correct meanings (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Time Complexity": "O(n log n) for Selection Sort",
            "Space Complexity": "O(n) for Selection Sort",
            "Best Case Complexity": "O(n) for Selection Sort"
        },
        "answer": {
            "Time Complexity": "O(n^2) for Selection Sort",
            "Space Complexity": "O(1) for Selection Sort",
            "Best Case Complexity": "O(n^2) for Selection Sort"
        }
    },
    lambda: {
        "question": "Match these sorting algorithm characteristics with their accurate descriptions (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Bubble Sort": "Always faster than Selection Sort",
            "Insertion Sort": "Unstable sort",
            "Selection Sort": "Adaptive to sorted data"
        },
        "answer": {
            "Bubble Sort": "Can be slower or faster depending on input",
            "Insertion Sort": "Stable sort",
            "Selection Sort": "Not adaptive to input order"
        }
    },
    lambda: {
        "question": "Match the sorting terms with their definitions (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Adaptive Sort": "Always performs the same comparisons",
            "Stable Sort": "Changes order of equal elements",
            "Selection Sort": "Adaptive"
        },
        "answer": {
            "Adaptive Sort": "Changes behavior based on input order",
            "Stable Sort": "Maintains relative order of equal elements",
            "Selection Sort": "Not adaptive"
        }
    },
    lambda: {
        "question": "Match the sorting algorithm with their typical use cases (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Selection Sort": "Efficient for large datasets",
            "QuickSort": "Uses O(n^2) time in average case",
            "Merge Sort": "In-place sorting algorithm"
        },
        "answer": {
            "Selection Sort": "Used for small datasets or teaching",
            "QuickSort": "Average time O(n log n)",
            "Merge Sort": "Requires additional memory"
        }
    },
    lambda: {
        "question": "Match the following sorting algorithm properties (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Selection Sort": "Stable and in-place",
            "QuickSort": "Unstable and requires extra space",
            "Insertion Sort": "Unstable"
        },
        "answer": {
            "Selection Sort": "Unstable and in-place",
            "QuickSort": "Unstable and in-place",
            "Insertion Sort": "Stable and in-place"
        }
    },
    lambda: {
        "question": "Match the algorithm components with their purposes (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Find Minimum": "Outer loop's job",
            "Swap": "Inner loop's job",
            "Outer Loop": "Swaps elements"
        },
        "answer": {
            "Find Minimum": "Inner loop's job",
            "Swap": "Swaps elements",
            "Outer Loop": "Controls the boundary of sorted/unsorted array"
        }
    },
    lambda: {
        "question": "Match the sorting complexity classes with their algorithms (Note: below pairs are incorrectly matched):",
        "pairs": {
            "O(n log n)": "Selection Sort",
            "O(n^2)": "Merge Sort",
            "O(n)": "Bubble Sort in worst case"
        },
        "answer": {
            "O(n log n)": "Merge Sort",
            "O(n^2)": "Selection Sort",
            "O(n)": "Bubble Sort best case (already sorted)"
        }
    },
    lambda: {
        "question": "Match the sorting concepts with their details (Note: below pairs are incorrectly matched):",
        "pairs": {
            "In-place Sorting": "Uses extra memory for sorting",
            "Stable Sorting": "Can reorder equal elements",
            "Selection Sort": "Stable"
        },
        "answer": {
            "In-place Sorting": "Does not use extra memory",
            "Stable Sorting": "Maintains order of equal elements",
            "Selection Sort": "Unstable"
        }
    },
    lambda: {
        "question": "Match the Selection Sort steps to their roles (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Initialize min_index": "After swapping elements",
            "Compare elements": "At start of outer loop",
            "Swap elements": "During inner loop"
        },
        "answer": {
            "Initialize min_index": "At start of outer loop",
            "Compare elements": "During inner loop",
            "Swap elements": "After inner loop finishes"
        }
    },
    lambda: {
        "question": "Match the sorting algorithm with its characteristic (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Selection Sort": "Adaptive and stable",
            "Heap Sort": "Uses extra memory",
            "Bubble Sort": "Always O(n log n)"
        },
        "answer": {
            "Selection Sort": "Not adaptive and unstable",
            "Heap Sort": "In-place sorting algorithm",
            "Bubble Sort": "O(n^2) average and worst case"
        }
    },
    lambda: {
        "question": "Match the sorting term with its meaning (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Stable Sort": "Randomizes equal elements",
            "In-place Sort": "Uses extra memory",
            "Selection Sort": "Stable"
        },
        "answer": {
            "Stable Sort": "Maintains order of equal elements",
            "In-place Sort": "Sorts without extra memory",
            "Selection Sort": "Unstable"
        }
    },
    lambda: {
        "question": "Match the Selection Sort loop with its task (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Outer Loop": "Finds minimum element",
            "Inner Loop": "Controls sorted-unsorted boundary",
            "Swap": "Finds minimum element"
        },
        "answer": {
            "Outer Loop": "Controls sorted-unsorted boundary",
            "Inner Loop": "Finds minimum element",
            "Swap": "Swaps minimum element with current index"
        }
    },
    lambda: {
        "question": "Match the sorting algorithms to their time complexities (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Selection Sort": "O(n log n)",
            "Insertion Sort": "O(n^2)",
            "Merge Sort": "O(n^2)"
        },
        "answer": {
            "Selection Sort": "O(n^2)",
            "Insertion Sort": "O(n^2)",
            "Merge Sort": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match the sorting algorithm with its best use case (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Selection Sort": "Sorting large datasets quickly",
            "Insertion Sort": "Unsorted data with many unique elements",
            "Bubble Sort": "Nearly sorted arrays"
        },
        "answer": {
            "Selection Sort": "Small datasets or teaching purposes",
            "Insertion Sort": "Nearly sorted or small datasets",
            "Bubble Sort": "Nearly sorted arrays"
        }
    },
    lambda: {
        "question": "Match the sorting algorithm characteristic with the correct algorithm (Note: below pairs are incorrectly matched):",
        "pairs": {
            "In-place": "Merge Sort",
            "Stable": "Selection Sort",
            "Adaptive": "QuickSort"
        },
        "answer": {
            "In-place": "Selection Sort",
            "Stable": "Insertion Sort",
            "Adaptive": "Insertion Sort"
        }
    },
    lambda: {
        "question": "Match the sorting algorithm to its space complexity (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Selection Sort": "O(n)",
            "Merge Sort": "O(1)",
            "QuickSort": "O(n)"
        },
        "answer": {
            "Selection Sort": "O(1)",
            "Merge Sort": "O(n)",
            "QuickSort": "O(log n) average"
        }
    },
    lambda: {
        "question": "Match the selection sort phase with its function (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Selection Phase": "Swaps elements",
            "Comparison Phase": "Moves boundary between sorted/unsorted",
            "Swap Phase": "Finds minimum"
        },
        "answer": {
            "Selection Phase": "Finds minimum",
            "Comparison Phase": "Compares elements",
            "Swap Phase": "Swaps elements"
        }
    },
    lambda: {
        "question": "Match the terms related to sorting with their correct explanations (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Stable": "May change order of equal elements",
            "In-place": "Requires extra memory",
            "Selection Sort": "Stable"
        },
        "answer": {
            "Stable": "Maintains order of equal elements",
            "In-place": "Does not require extra memory",
            "Selection Sort": "Unstable"
        }
    },
    lambda: {
        "question": "Match these sorting concepts with their definitions (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Adaptive Algorithm": "Always performs same steps",
            "Stable Algorithm": "May reorder duplicates",
            "Selection Sort": "Adaptive"
        },
        "answer": {
            "Adaptive Algorithm": "Changes behavior based on input",
            "Stable Algorithm": "Maintains order of duplicates",
            "Selection Sort": "Not adaptive"
        }
    },
    lambda: {
        "question": "Match the sorting algorithm component with its role (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Inner Loop": "Swaps elements",
            "Outer Loop": "Finds minimum element",
            "Swap": "Controls sorted-unsorted boundary"
        },
        "answer": {
            "Inner Loop": "Finds minimum element",
            "Outer Loop": "Controls sorted-unsorted boundary",
            "Swap": "Swaps elements"
        }
    },
    lambda: {
        "question": "Match the sorting terms with correct statements (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Selection Sort": "Stable and adaptive",
            "QuickSort": "In-place and stable",
            "Merge Sort": "Unstable and not in-place"
        },
        "answer": {
            "Selection Sort": "Unstable and not adaptive",
            "QuickSort": "In-place and unstable",
            "Merge Sort": "Stable and not in-place"
        }
    },
    lambda: {
        "question": "Match the sorting property with the sorting algorithm (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Stable Sort": "QuickSort",
            "Unstable Sort": "Insertion Sort",
            "Selection Sort": "Stable"
        },
        "answer": {
            "Stable Sort": "Insertion Sort",
            "Unstable Sort": "QuickSort",
            "Selection Sort": "Unstable"
        }
    },
    lambda: {
        "question": "Match the sorting algorithm with its average time complexity (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Selection Sort": "O(n log n)",
            "Heap Sort": "O(n^2)",
            "Bubble Sort": "O(n)"
        },
        "answer": {
            "Selection Sort": "O(n^2)",
            "Heap Sort": "O(n log n)",
            "Bubble Sort": "O(n^2)"
        }
    }
],

        "ECQ": [
    lambda: {
        "question": "Complete the code to initialize the minimum index in Selection Sort:\nmin_index = ____",
        "answer": "i"
    },
    lambda: {
        "question": "Complete the inner loop condition in Selection Sort:\nfor j in range(i + 1, ____):",
        "answer": "len(arr)"
    },
    lambda: {
        "question": "Fill in the comparison to update min_index:\nif arr[j] ____ arr[min_index]:",
        "answer": "<"
    },
    lambda: {
        "question": "Complete the code to swap elements in Selection Sort:\narr[i], arr[min_index] = ____, ____",
        "answer": "arr[min_index], arr[i]"
    },
    lambda: {
        "question": "Fill in the missing keyword for the outer loop:\nfor i in ____(len(arr)-1):",
        "answer": "range"
    },
    lambda: {
        "question": "Complete the loop to traverse unsorted part in Selection Sort:\nfor j in range(i+1, ____):",
        "answer": "len(arr)"
    },
    lambda: {
        "question": "Fill in the condition to check if swapping is needed:\nif ____ != i:",
        "answer": "min_index"
    },
    lambda: {
        "question": "Complete the statement to start the inner loop:\nfor j in ____(i+1, len(arr)):",
        "answer": "range"
    },
    lambda: {
        "question": "Complete the initialization of min_index before inner loop:\nmin_index = ____",
        "answer": "i"
    },
    lambda: {
        "question": "Complete the code to find minimum element index:\nif arr[j] < ____:",
        "answer": "arr[min_index]"
    },
    lambda: {
        "question": "Fill in the missing code to swap elements safely:\nif min_index != i:\n    ____[i], ____[min_index] = ____[min_index], ____[i]",
        "answer": "arr, arr, arr, arr"
    },
    lambda: {
        "question": "Complete the outer loop for Selection Sort:\nfor i in ____(len(arr)-1):",
        "answer": "range"
    },
    lambda: {
        "question": "Fill in the blank to traverse entire array:\nfor i in range(____):",
        "answer": "len(arr)-1"
    },
    lambda: {
        "question": "Complete the code to assign new min_index:\nmin_index = ____",
        "answer": "j"
    },
    lambda: {
        "question": "Fill the blank to iterate over unsorted subarray:\nfor j in range(____, len(arr)):",
        "answer": "i+1"
    },
    lambda: {
        "question": "Complete the swap statement:\narr[i], arr[min_index] = ____, ____",
        "answer": "arr[min_index], arr[i]"
    },
    lambda: {
        "question": "Fill in to check if min_index differs from current index:\nif ____ != i:",
        "answer": "min_index"
    },
    lambda: {
        "question": "Complete the statement to find minimum element:\nif ____ < arr[min_index]:",
        "answer": "arr[j]"
    },
    lambda: {
        "question": "Fill the range in inner loop for Selection Sort:\nfor j in range(i + 1, ____):",
        "answer": "len(arr)"
    },
    lambda: {
        "question": "Complete the initialization line in Selection Sort:\nmin_index = ____",
        "answer": "i"
    },
    lambda: {
        "question": "Complete the condition for swapping elements:\nif min_index ____ i:",
        "answer": "!="
    },
    lambda: {
        "question": "Fill in the swap code:\narr[____], arr[____] = arr[____], arr[____]",
        "answer": "i, min_index, min_index, i"
    },
    lambda: {
        "question": "Complete the inner loop to find minimum element:\nfor j in ____(i+1, len(arr)):",
        "answer": "range"
    },
    lambda: {
        "question": "Fill the blank to update min_index when smaller element found:\nmin_index = ____",
        "answer": "j"
    },
    lambda: {
        "question": "Complete the swap condition check:\nif ____ != i:",
        "answer": "min_index"
    }
],

        "NQ": [
    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many total swaps does Selection Sort perform in the worst case?",
        "answer": str(n - 1)
    })(random_choice([20, 25, 30])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many total comparisons does Selection Sort perform?",
        "answer": str(n * (n - 1) // 2)
    })(random_choice([15, 18, 22])),

    lambda: (lambda n: {
        "question": f"In Selection Sort on an array of size {n}, how many times is the inner loop executed in total?",
        "answer": str((n * (n - 1)) // 2)
    })(random_choice([10, 12, 16])),

    lambda: (lambda n: {
        "question": f"For array size {n}, what is the total number of iterations of the outer loop in Selection Sort?",
        "answer": str(n - 1)
    })(random_choice([25, 30, 40])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many element swaps will Selection Sort perform if the array is already sorted?",
        "answer": "0"
    })(random_choice([12, 14, 18])),

    lambda: (lambda n: {
        "question": f"For array size {n}, what is the total number of minimum index updates in Selection Sort?",
        "answer": str((n * (n - 1)) // 2)
    })(random_choice([14, 17, 19])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many times does Selection Sort compare elements during the first pass of the outer loop?",
        "answer": str(n - 1)
    })(random_choice([16, 20, 24])),

    lambda: (lambda n: {
        "question": f"For array size {n}, what is the total number of comparisons during the last pass (outer loop iteration) of Selection Sort?",
        "answer": "1"
    })(random_choice([8, 10, 12])),

    lambda: (lambda n: {
        "question": f"In Selection Sort, how many total swaps are performed for an array of size {n} with all elements equal?",
        "answer": "0"
    })(random_choice([10, 15, 20])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many comparisons happen in the second pass of Selection Sort's inner loop?",
        "answer": str(n - 2)
    })(random_choice([12, 15, 18])),

    lambda: (lambda n: {
        "question": f"For an array size {n}, what is the minimum number of swaps Selection Sort will perform on any array?",
        "answer": "0"
    })(random_choice([20, 25, 30])),

    lambda: (lambda n: {
        "question": f"How many total passes does Selection Sort make for an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([22, 26, 30])),

    lambda: (lambda n: {
        "question": f"For array size {n}, what is the sum of comparisons made during all passes of Selection Sort?",
        "answer": str(n * (n - 1) // 2)
    })(random_choice([18, 22, 25])),

    lambda: (lambda n: {
        "question": f"For an array size {n}, how many comparisons are made in the third pass of Selection Sort?",
        "answer": str(n - 3)
    })(random_choice([10, 13, 15])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many swaps occur if the array is sorted in reverse order using Selection Sort?",
        "answer": str(n - 1)
    })(random_choice([10, 14, 18])),

    lambda: (lambda n: {
        "question": f"For array size {n}, what is the total number of index checks in Selection Sort's inner loop?",
        "answer": str((n * (n - 1)) // 2)
    })(random_choice([15, 20, 25])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the total number of element assignments during swaps in Selection Sort?",
        "answer": str(2 * (n - 1))
    })(random_choice([10, 12, 16])),

    lambda: (lambda n: {
        "question": f"In Selection Sort, how many iterations does the inner loop have on the fourth pass for an array of size {n}?",
        "answer": str(n - 4)
    })(random_choice([15, 20, 25])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the total number of element comparisons when the array is already sorted in Selection Sort?",
        "answer": str(n * (n - 1) // 2)
    })(random_choice([12, 15, 18])),

    lambda: (lambda n: {
        "question": f"For array size {n}, how many total operations (comparisons + swaps) does Selection Sort perform in the worst case?",
        "answer": str((n * (n - 1) // 2) + (n - 1))
    })(random_choice([10, 15, 20])),

    lambda: (lambda n: {
        "question": f"For array size {n}, how many comparisons occur on the fifth pass in Selection Sort?",
        "answer": str(n - 5)
    })(random_choice([15, 18, 20])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many times is the minimum element updated during the entire Selection Sort process?",
        "answer": str((n * (n - 1)) // 2)
    })(random_choice([18, 20, 22])),

    lambda: (lambda n: {
        "question": f"For array size {n}, how many comparisons occur in the penultimate pass of Selection Sort?",
        "answer": "2"
    })(random_choice([10, 12, 15])),

    lambda: (lambda n: {
        "question": f"For array size {n}, how many comparisons occur in the first pass of Selection Sort?",
        "answer": str(n - 1)
    })(random_choice([20, 25, 30])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the maximum number of swaps performed by Selection Sort?",
        "answer": str(n - 1)
    })(random_choice([15, 20, 25]))
]

    }
}

# =========================
# MAIN GENERATOR FUNCTION
# =========================

def generate_selection_sort_questions(level: str, num_questions: int):
    level = level.lower()
    if level not in selection_sort_templates:
        raise ValueError("Invalid level. Choose from: level1, level2, level3.")

    typewise_templates = selection_sort_templates[level]
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

    return questions

# =========================
# USER INPUT
# =========================

if __name__ == "__main__":
    level = input("Enter difficulty level (level1, level2, level3): ").strip()
    num = int(input("Enter number of questions to generate: "))

    try:
        output = generate_selection_sort_questions(level, num)
        for i, q in enumerate(output, 1):
            print(f"\nQ{i}: {q['question']}")
            if 'options' in q:
                for opt in q['options']:
                    print(f"   - {opt}")
            if 'pairs' in q:
                print("   Given Pairs:")
                for k, v in q['pairs'].items():
                    print(f"     {k}  ->  {v}")
                print("   Correct Answer:")
                for k, v in q['answer'].items():
                    print(f"     {k}  ->  {v}")
            else:
                print(f"Answer: {q['answer']}")
    except Exception as e:
        print("Error:", e)
