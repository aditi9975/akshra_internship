import random
import math

def random_n(min_val=6, max_val=12):
    return random.randint(min_val, max_val)

def random_array(size):
    return random.sample(range(1, 100), size)

def random_choice(choices):
    return random.choice(choices)

quicksort_templates = {
    
    "level1": {
        "TFQ": [
            lambda: {
                "question": "True or False: QuickSort is a divide and conquer algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: The worst-case time complexity of QuickSort is O(n log n).",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: QuickSort always requires additional arrays to perform sorting.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: QuickSort can be implemented both recursively and iteratively.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: The pivot in QuickSort is always the smallest element.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: QuickSort generally performs better than MergeSort for small arrays.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: QuickSort is a stable sorting algorithm.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: QuickSort works by repeatedly merging sorted arrays.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Choosing a bad pivot can degrade QuickSort's performance.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: QuickSort has a worst-case time complexity of O(n^2).",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: QuickSort is not suitable for linked lists.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: QuickSort requires less memory than MergeSort.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: QuickSort is always faster than Bubble Sort.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: QuickSort does not work on duplicate elements.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: The partition step in QuickSort places the pivot in its final position.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: QuickSort always picks a random pivot.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: QuickSort cannot be used in parallel algorithms.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: QuickSort may lead to stack overflow on very large arrays.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: QuickSort modifies the input array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: The average number of comparisons in QuickSort is less than O(n log n).",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: QuickSort is implemented only in Python.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: QuickSort and MergeSort both follow divide and conquer.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: The space complexity of QuickSort is O(log n) due to recursion.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: The partitioning logic in QuickSort is based on binary search.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: QuickSort can be optimized using tail call elimination.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: QuickSort is used in many library sort functions.",
                "answer": "True"
            }
        ],
        "MCQ": [
    lambda: {
        "question": "What is the average case time complexity of QuickSort?",
        "options": ["O(n)", "O(log n)", "O(n log n)", "O(n^2)"],
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "Which of these best describes QuickSort?",
        "options": ["Divide and Merge", "Divide and Conquer", "Dynamic Programming", "Greedy Algorithm"],
        "answer": "Divide and Conquer"
    },
    lambda: {
        "question": "Which is not a valid pivot selection method in QuickSort?",
        "options": ["First element", "Random element", "Median of three", "Binary search"],
        "answer": "Binary search"
    },
    lambda: {
        "question": "Which case leads to O(n^2) time complexity in QuickSort?",
        "options": ["Best case", "Average case", "Worst case", "None"],
        "answer": "Worst case"
    },
    lambda: {
        "question": "What does QuickSort primarily depend on for efficiency?",
        "options": ["Pivot selection", "Array size", "Sorting order", "Number of recursive calls"],
        "answer": "Pivot selection"
    },
    lambda: {
        "question": "QuickSort sorts an array by repeatedly dividing it into ____ parts.",
        "options": ["Two", "Three", "Four", "One"],
        "answer": "Two"
    },
    lambda: {
        "question": "Which of these is a stable sorting algorithm?",
        "options": ["QuickSort", "MergeSort", "HeapSort", "Selection Sort"],
        "answer": "MergeSort"
    },
    lambda: {
        "question": "What is the worst-case space complexity of QuickSort?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "answer": "O(log n)"
    },
    lambda: {
        "question": "Which part of QuickSort algorithm is responsible for dividing the array?",
        "options": ["Partitioning", "Merging", "Recursion", "Sorting"],
        "answer": "Partitioning"
    },
    lambda: {
        "question": "QuickSort is generally faster than MergeSort because it is ____.",
        "options": ["In-place", "Stable", "Uses extra space", "Non-recursive"],
        "answer": "In-place"
    },
    lambda: {
        "question": "What happens when the pivot is chosen as the smallest or largest element every time?",
        "options": ["Best case", "Average case", "Worst case", "Stable case"],
        "answer": "Worst case"
    },
    lambda: {
        "question": "The process of rearranging elements around the pivot is called ____.",
        "options": ["Partitioning", "Swapping", "Merging", "Sorting"],
        "answer": "Partitioning"
    },
    lambda: {
        "question": "In QuickSort, the pivot is often chosen as ____.",
        "options": ["First element", "Last element", "Random element", "Any of the above"],
        "answer": "Any of the above"
    },
    lambda: {
        "question": "What kind of algorithm is QuickSort?",
        "options": ["Divide and Conquer", "Dynamic Programming", "Greedy", "Backtracking"],
        "answer": "Divide and Conquer"
    },
    lambda: {
        "question": "The best case time complexity of QuickSort occurs when the pivot divides the array into ____ parts.",
        "options": ["Unequal", "Equal", "One part", "No division"],
        "answer": "Equal"
    },
    lambda: {
        "question": "Which data structure is used implicitly in QuickSort for recursion?",
        "options": ["Stack", "Queue", "Heap", "Tree"],
        "answer": "Stack"
    },
    lambda: {
        "question": "QuickSort does not require extra space for merging because it is ____.",
        "options": ["Stable", "In-place", "Recursive", "Iterative"],
        "answer": "In-place"
    },
    lambda: {
        "question": "Which of the following sorting algorithms is generally faster on average?",
        "options": ["QuickSort", "Bubble Sort", "Insertion Sort", "Selection Sort"],
        "answer": "QuickSort"
    },
    lambda: {
        "question": "QuickSort's worst case occurs when the pivot results in ____.",
        "options": ["Balanced partitions", "Highly unbalanced partitions", "Random partitions", "Equal partitions"],
        "answer": "Highly unbalanced partitions"
    },
    lambda: {
        "question": "Which statement is true about QuickSort's recursive calls?",
        "options": [
            "They divide the problem into smaller subarrays",
            "They merge sorted subarrays",
            "They sort using dynamic programming",
            "They use extra space for sorting"
        ],
        "answer": "They divide the problem into smaller subarrays"
    },
    lambda: {
        "question": "QuickSort's partition function usually returns the index of ____.",
        "options": ["The pivot after partition", "The smallest element", "The largest element", "The middle element"],
        "answer": "The pivot after partition"
    },
    lambda: {
        "question": "Which of these is NOT true about QuickSort?",
        "options": [
            "It is an in-place algorithm",
            "It is a stable sorting algorithm",
            "It uses divide and conquer",
            "Its average time complexity is O(n log n)"
        ],
        "answer": "It is a stable sorting algorithm"
    },
    lambda: {
        "question": "QuickSort’s best performance depends on ____.",
        "options": ["Pivot selection", "Array size", "Sorting order", "Memory usage"],
        "answer": "Pivot selection"
    },
    lambda: {
        "question": "QuickSort partitions the array into two parts based on the ____.",
        "options": ["Pivot", "Middle element", "First element", "Last element always"],
        "answer": "Pivot"
    },
    lambda: {
        "question": "Which statement best describes the recursive nature of QuickSort?",
        "options": [
            "It sorts by dividing the array and recursively sorting the parts",
            "It sorts by repeatedly merging sorted arrays",
            "It uses iteration instead of recursion",
            "It sorts by scanning the entire array multiple times"
        ],
        "answer": "It sorts by dividing the array and recursively sorting the parts"
    }
],

        "MTQ": [
    lambda: {
        "question": "Match QuickSort concepts (Note: below pairs are wrongly matched):",
        "pairs": {
            "Partitioning": "Merge step",
            "Pivot": "Always last element",
            "Best Case Time": "O(n^2)"
        },
        "answer": {
            "Partitioning": "Divide array using pivot",
            "Pivot": "Element used for partition",
            "Best Case Time": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match terms (Note: below pairs are wrongly matched):",
        "pairs": {
            "Worst Case": "O(n log n)",
            "Recursive Calls": "End immediately",
            "Pivot Location": "Fixed at middle"
        },
        "answer": {
            "Worst Case": "O(n^2)",
            "Recursive Calls": "Divide problem into subarrays",
            "Pivot Location": "Can vary"
        }
    },
    lambda: {
        "question": "Match QuickSort behavior (Note: below pairs are wrongly matched):",
        "pairs": {
            "Stable Sort": "QuickSort",
            "Space Complexity": "O(n)",
            "Sorting Principle": "Merge and conquer"
        },
        "answer": {
            "Stable Sort": "MergeSort",
            "Space Complexity": "O(log n)",
            "Sorting Principle": "Divide and conquer"
        }
    },
    lambda: {
        "question": "Match QuickSort with its characteristics (Note: below pairs are wrongly matched):",
        "pairs": {
            "Pivot Selection": "Always first",
            "In-place Sort": "Uses extra memory",
            "Time Complexity (Avg)": "O(n)"
        },
        "answer": {
            "Pivot Selection": "Can be random or median",
            "In-place Sort": "Does not use extra memory",
            "Time Complexity (Avg)": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match the complexity with QuickSort scenarios (Note: below pairs are wrongly matched):",
        "pairs": {
            "Average Case": "O(n)",
            "Best Case": "O(n^2)",
            "Worst Case": "O(n log n)"
        },
        "answer": {
            "Average Case": "O(n log n)",
            "Best Case": "O(n log n)",
            "Worst Case": "O(n^2)"
        }
    },
    lambda: {
        "question": "Match the QuickSort terms with correct definitions (Note: below pairs are wrongly matched):",
        "pairs": {
            "Recursion": "Looping",
            "Pivot": "Merged element",
            "Partitioning": "Combine arrays"
        },
        "answer": {
            "Recursion": "Function calling itself",
            "Pivot": "Element used for comparison",
            "Partitioning": "Dividing array into subarrays"
        }
    },
    lambda: {
        "question": "Match QuickSort comparisons (Note: below pairs are wrongly matched):",
        "pairs": {
            "First call": "Smallest element",
            "Last call": "Pivot chosen",
            "Middle case": "Best performance"
        },
        "answer": {
            "First call": "Selects initial pivot",
            "Last call": "Occurs after all divisions",
            "Middle case": "Average performance"
        }
    },
    lambda: {
        "question": "Match QuickSort feature with description (Note: below pairs are wrongly matched):",
        "pairs": {
            "Stack usage": "O(n)",
            "Pivot role": "Final output",
            "Divide step": "Merging arrays"
        },
        "answer": {
            "Stack usage": "O(log n) in best case",
            "Pivot role": "Divides array",
            "Divide step": "Partitioning process"
        }
    },
    lambda: {
        "question": "Match these QuickSort key points (Note: below pairs are wrongly matched):",
        "pairs": {
            "Pivot movement": "Stays fixed",
            "Sort type": "Stable",
            "Merge step": "Exists"
        },
        "answer": {
            "Pivot movement": "May change during partition",
            "Sort type": "Unstable",
            "Merge step": "Not required"
        }
    },
    lambda: {
        "question": "Match these sorting terms with QuickSort usage (Note: below pairs are wrongly matched):",
        "pairs": {
            "Base case": "Infinite loop",
            "Pivot comparison": "With first only",
            "Recursive call": "On whole array"
        },
        "answer": {
            "Base case": "Subarray with size ≤ 1",
            "Pivot comparison": "With every element",
            "Recursive call": "On left and right subarrays"
        }
    },
    lambda: {
        "question": "Match the operation with its result in QuickSort (Note: below pairs are wrongly matched):",
        "pairs": {
            "Choosing worst pivot": "Faster sort",
            "Balanced partitions": "Worst case",
            "Sorted input": "Best case"
        },
        "answer": {
            "Choosing worst pivot": "More comparisons",
            "Balanced partitions": "Best case",
            "Sorted input": "Worst case (if pivot is last element)"
        }
    },
    lambda: {
        "question": "Match time complexities with QuickSort scenarios (Note: below pairs are wrongly matched):",
        "pairs": {
            "Sorted array (last pivot)": "O(n log n)",
            "Equal partitions": "O(n^2)",
            "Median pivot": "Worst case"
        },
        "answer": {
            "Sorted array (last pivot)": "O(n^2)",
            "Equal partitions": "O(n log n)",
            "Median pivot": "Good partitioning"
        }
    },
    lambda: {
        "question": "Match QuickSort elements (Note: below pairs are wrongly matched):",
        "pairs": {
            "Middle element pivot": "Worst performance",
            "Best case input": "Already sorted",
            "Unstable sort": "MergeSort"
        },
        "answer": {
            "Middle element pivot": "Usually good partition",
            "Best case input": "Balanced partitions",
            "Unstable sort": "QuickSort"
        }
    },
    lambda: {
        "question": "Match QuickSort attributes (Note: below pairs are wrongly matched):",
        "pairs": {
            "Stack depth (worst)": "O(n log n)",
            "Space efficient": "False",
            "Pivot (role)": "Sorts subarrays"
        },
        "answer": {
            "Stack depth (worst)": "O(n)",
            "Space efficient": "True (in-place)",
            "Pivot (role)": "Divides array"
        }
    },
    lambda: {
        "question": "Match QuickSort characteristics (Note: below pairs are wrongly matched):",
        "pairs": {
            "Time complexity average": "O(n^2)",
            "Sorting principle": "Conquer and divide",
            "Pivot": "Always middle"
        },
        "answer": {
            "Time complexity average": "O(n log n)",
            "Sorting principle": "Divide and conquer",
            "Pivot": "Can be any element"
        }
    },
    lambda: {
        "question": "Match QuickSort outcome (Note: below pairs are wrongly matched):",
        "pairs": {
            "Random pivot": "Always worst case",
            "Recursive function": "Uses loops",
            "Partition result": "Merged array"
        },
        "answer": {
            "Random pivot": "Improves average performance",
            "Recursive function": "Calls itself",
            "Partition result": "Two subarrays"
        }
    },
    lambda: {
        "question": "Match pivot strategies with outcome (Note: below pairs are wrongly matched):",
        "pairs": {
            "Median of three": "Unstable result",
            "First element": "Balanced partition",
            "Random pivot": "Slowest result"
        },
        "answer": {
            "Median of three": "Improves partitioning",
            "First element": "May lead to unbalanced split",
            "Random pivot": "Average case O(n log n)"
        }
    },
    lambda: {
        "question": "Match sorting algorithms (Note: below pairs are wrongly matched):",
        "pairs": {
            "QuickSort": "Stable",
            "MergeSort": "In-place",
            "Bubble Sort": "Divide and conquer"
        },
        "answer": {
            "QuickSort": "Unstable",
            "MergeSort": "Not in-place",
            "Bubble Sort": "Simple comparison sort"
        }
    },
    lambda: {
        "question": "Match QuickSort aspects (Note: below pairs are wrongly matched):",
        "pairs": {
            "Recursive nature": "Not present",
            "Partition logic": "Merges sorted halves",
            "Best time": "O(n^2)"
        },
        "answer": {
            "Recursive nature": "Present",
            "Partition logic": "Divides around pivot",
            "Best time": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match sorting types (Note: below pairs are wrongly matched):",
        "pairs": {
            "Internal sort": "Needs external memory",
            "QuickSort": "Stable and slow",
            "HeapSort": "Recursive sort"
        },
        "answer": {
            "Internal sort": "Works in RAM",
            "QuickSort": "Unstable and fast",
            "HeapSort": "Uses heap structure"
        }
    },
    lambda: {
        "question": "Match QuickSort's limitations (Note: below pairs are wrongly matched):",
        "pairs": {
            "Worst case": "Always occurs",
            "Sorted input": "Best case",
            "Space complexity": "O(n)"
        },
        "answer": {
            "Worst case": "Depends on pivot choice",
            "Sorted input": "Worst case (for some pivot choices)",
            "Space complexity": "O(log n)"
        }
    },
    lambda: {
        "question": "Match pivot impact (Note: below pairs are wrongly matched):",
        "pairs": {
            "Random pivot": "High chance of worst case",
            "Good pivot": "Unbalanced subarrays",
            "Last element": "Always balanced"
        },
        "answer": {
            "Random pivot": "Reduces chance of worst case",
            "Good pivot": "Balanced subarrays",
            "Last element": "May cause imbalance"
        }
    }
],

        "ECQ": [
    lambda: {
        "question": "In QuickSort, the element used to divide the array is called ___.",
        "answer": "pivot"
    },
    lambda: {
        "question": "To partition the array in QuickSort, we compare each element with the ___.",
        "answer": "pivot"
    },
    lambda: {
        "question": "The recursive QuickSort function calls itself on the ___ and ___ partitions.",
        "answer": "left, right"
    },
    lambda: {
        "question": "QuickSort follows the ___ and ___ strategy.",
        "answer": "divide, conquer"
    },
    lambda: {
        "question": "In the worst case, QuickSort takes ___ time complexity.",
        "answer": "O(n^2)"
    },
    lambda: {
        "question": "The average case time complexity of QuickSort is ___.",
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "QuickSort is an ___ sorting algorithm, meaning it uses no extra space.",
        "answer": "in-place"
    },
    lambda: {
        "question": "The process of dividing an array into two subarrays around a pivot is called ___.",
        "answer": "partitioning"
    },
    lambda: {
        "question": "QuickSort is generally ___ than MergeSort in practice.",
        "answer": "faster"
    },
    lambda: {
        "question": "If the pivot divides the array into equal halves, the performance is ___.",
        "answer": "optimal"
    },
    lambda: {
        "question": "The best case time complexity of QuickSort is ___.",
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "QuickSort does not perform well when the pivot causes ___ partitions.",
        "answer": "unbalanced"
    },
    lambda: {
        "question": "The number of recursive calls in QuickSort depends on the position of the ___.",
        "answer": "pivot"
    },
    lambda: {
        "question": "QuickSort is not a ___ sorting algorithm, as it may change the order of equal elements.",
        "answer": "stable"
    },
    lambda: {
        "question": "The worst case of QuickSort usually occurs when the array is already ___.",
        "answer": "sorted"
    },
    lambda: {
        "question": "A good choice of ___ can reduce the chances of worst-case behavior in QuickSort.",
        "answer": "pivot"
    },
    lambda: {
        "question": "The pivot is used to divide the array into elements less than and greater than the ___.",
        "answer": "pivot"
    },
    lambda: {
        "question": "QuickSort reduces the original problem size by performing ___ on subarrays.",
        "answer": "recursion"
    },
    lambda: {
        "question": "QuickSort does not require ___ memory like MergeSort.",
        "answer": "extra"
    },
    lambda: {
        "question": "When using QuickSort, we typically sort the ___ first, then the ___.",
        "answer": "left, right"
    },
    lambda: {
        "question": "In QuickSort, recursion stops when the subarray has ___ or zero elements.",
        "answer": "one"
    },
    lambda: {
        "question": "QuickSort performs better on ___ data sets compared to Bubble Sort.",
        "answer": "large"
    },
    lambda: {
        "question": "The ___ of QuickSort depends on how well the pivot divides the array.",
        "answer": "performance"
    },
    lambda: {
        "question": "QuickSort is commonly used in programming languages like ___ for built-in sorting.",
        "answer": "Python"
    },
    lambda: {
        "question": "The space complexity of QuickSort in the best case is ___.",
        "answer": "O(log n)"
    }
],

        "NQ": [
    lambda: (lambda n: {
        "question": f"What is the worst-case recursion depth of QuickSort on an array of size {n}?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"If QuickSort is applied on a sorted array of size {n} with last element as pivot, what is the total comparisons?",
        "answer": str(n * (n - 1) // 2)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"If QuickSort runs in best case on an array of size {n}, how many levels of recursion occur?",
        "answer": str(int(math.log2(n)))
    })(random_n(8, 64)),

    lambda: (lambda n: {
        "question": f"How many comparisons are done in QuickSort best case (approx) for array of size {n}?",
        "answer": str(n * int(math.log2(n)))
    })(random_n(8, 16)),

    lambda: (lambda n: {
        "question": f"If an array has {n} elements and is already sorted, how many times will QuickSort call partition in worst case?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"In worst case, what is the number of swaps in QuickSort on array of size {n}?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"If pivot always divides array into two equal halves, how many levels of recursion for array of size {n}?",
        "answer": str(int(math.log2(n)))
    })(random_n(8, 64)),

    lambda: (lambda n: {
        "question": f"If an array has {n} elements and pivot always splits into 1 and (n-1) size, how many total recursive calls?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the space complexity (call stack depth) in best case for QuickSort with {n} elements?",
        "answer": "O(log n)"
    })(random_n(6, 20)),

    lambda: (lambda n: {
        "question": f"How many comparisons does QuickSort make on average for array size {n}?",
        "answer": str(n * int(math.log2(n)))
    })(random_n(8, 16)),

    lambda: (lambda n: {
        "question": f"If pivot is always smallest element in array of size {n}, how many comparisons will be made?",
        "answer": str(n * (n - 1) // 2)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"For an array of {n} elements, what is the expected number of partitions in average case?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"In a QuickSort run, how many recursive calls happen for an array of size {n} in worst case?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the maximum number of comparisons in worst case of QuickSort for {n} elements?",
        "answer": str(n * (n - 1) // 2)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the minimum number of comparisons in QuickSort (best case) for array of size {n}?",
        "answer": str(n * int(math.log2(n)))
    })(random_n(8, 16)),

    lambda: (lambda n: {
        "question": f"If QuickSort processes left and right partitions evenly, what is recursion tree height for {n} elements?",
        "answer": str(int(math.log2(n)))
    })(random_n(8, 64)),

    lambda: (lambda n: {
        "question": f"How many elements does QuickSort partition function typically compare against the pivot in array of size {n}?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"If QuickSort runs on array of size {n} in worst case, what is the number of recursive levels?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the number of comparisons done during the first partition call for array of size {n}?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the maximum height of recursion tree in QuickSort worst case for size {n}?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"How many total partitions occur for array of size {n} in worst case of QuickSort?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"If we pick pivot randomly, average-case partitions for array size {n} would be approximately?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"In QuickSort, how many total function calls happen including base cases for array of size {n}?",
        "answer": str(2 * n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"If QuickSort processes left half first and right half next, how many total calls for size {n}?",
        "answer": str(2 * n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the approximate number of comparisons in average case for array size {n}?",
        "answer": str(n * int(math.log2(n)))
    })(random_n(8, 16)),
],
    },

"level2": {
    "TFQ": [
    lambda: {"question": "True or False: QuickSort is stable by default.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort can perform better than MergeSort on average.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort is always faster than MergeSort.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort always uses the middle element as pivot.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort can be implemented recursively and iteratively.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort uses a stack implicitly in recursive implementation.", "answer": "True"},
    lambda: {"question": "True or False: Choosing a good pivot improves QuickSort performance.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort's worst case happens when pivot is always maximum or minimum.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort requires additional memory for merging.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort divides the array based on pivot.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort is a dynamic programming algorithm.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort can be optimized with tail recursion.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort sorts linked lists better than arrays.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort has better locality of reference compared to MergeSort.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort can degrade to O(n^2) if pivot is poorly chosen.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort is a comparison-based sorting algorithm.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort cannot be implemented in-place.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort always splits the array into equal halves.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort may require log(n) stack space in best case.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort can sort arrays with duplicate values.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort is not a stable algorithm unless modified.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort requires O(n log n) space complexity.", "answer": "False"},
    lambda: {"question": "True or False: The first and last elements are never used as pivots.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort needs the array to be sorted beforehand.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort performance is dependent on pivot selection.", "answer": "True"}
],


    
"MCQ": [
    lambda: {"question": "Which of the following is *not* true about QuickSort?", "options": ["It is an in-place algorithm", "It uses extra space proportional to input size", "It is faster on average than MergeSort", "It uses divide and conquer"], "answer": "It uses extra space proportional to input size"},
    lambda: {"question": "Which pivot selection method can lead to worst case in QuickSort?", "options": ["First element", "Random element", "Median of three", "None"], "answer": "First element"},
    lambda: {"question": "Which of the following is true for QuickSort in worst-case scenario?", "options": ["O(n log n) time", "O(log n) space", "O(n^2) time", "Constant space"], "answer": "O(n^2) time"},
    lambda: {"question": "Which condition results in QuickSort having best performance?", "options": ["Pivot always largest", "Pivot always smallest", "Pivot splits evenly", "Sorted array"], "answer": "Pivot splits evenly"},
    lambda: {"question": "In which scenario does QuickSort perform worst?", "options": ["Unsorted array", "Sorted array", "Equal elements", "Random input"], "answer": "Sorted array"},
    lambda: {"question": "Which of the following is QuickSort *not* based on?", "options": ["Divide and conquer", "Recursion", "Comparison", "Merging"], "answer": "Merging"},
    lambda: {"question": "Which sorting algorithm is generally faster than QuickSort on linked lists?", "options": ["MergeSort", "BubbleSort", "InsertionSort", "SelectionSort"], "answer": "MergeSort"},
    lambda: {"question": "What happens if all elements are equal in QuickSort?", "options": ["O(n^2)", "O(n log n)", "O(log n)", "O(n)"], "answer": "O(n^2)"},
    lambda: {"question": "How does QuickSort differ from MergeSort?", "options": ["QuickSort is stable", "QuickSort is slower", "QuickSort is in-place", "QuickSort uses merging"], "answer": "QuickSort is in-place"},
    lambda: {"question": "Which of the following describes an in-place sort?", "options": ["Uses recursion", "Uses O(n) memory", "Uses O(1) extra space", "Uses stack"], "answer": "Uses O(1) extra space"},
    lambda: {"question": "What is the key operation that makes QuickSort efficient?", "options": ["Merging", "Swapping", "Dividing", "Partitioning"], "answer": "Partitioning"},
    lambda: {"question": "Which of the following is not a valid pivot selection strategy?", "options": ["First element", "Middle element", "Random element", "Sorted order"], "answer": "Sorted order"},
    lambda: {"question": "Which sorting algorithm is best for nearly sorted data?", "options": ["QuickSort", "InsertionSort", "MergeSort", "SelectionSort"], "answer": "InsertionSort"},
    lambda: {"question": "Which best describes QuickSort's average time complexity?", "options": ["O(n)", "O(log n)", "O(n log n)", "O(n^2)"], "answer": "O(n log n)"},
    lambda: {"question": "Which of these is a disadvantage of QuickSort?", "options": ["Slow average case", "Not in-place", "Recursive overhead", "High memory usage"], "answer": "Recursive overhead"},
    lambda: {"question": "Which of these sorting algorithms is not divide-and-conquer?", "options": ["MergeSort", "QuickSort", "HeapSort", "None of these"], "answer": "HeapSort"},
    lambda: {"question": "If a bad pivot is always chosen, QuickSort behaves like:", "options": ["SelectionSort", "BubbleSort", "InsertionSort", "None of these"], "answer": "SelectionSort"},
    lambda: {"question": "When is QuickSort's performance similar to BubbleSort?", "options": ["Average case", "Best case", "Worst case", "All cases"], "answer": "Worst case"},
    lambda: {"question": "Which QuickSort version minimizes stack depth?", "options": ["Random pivot", "Tail recursion", "Mid pivot", "Looping"], "answer": "Tail recursion"},
    lambda: {"question": "Which sorting algorithm is generally best for small arrays?", "options": ["QuickSort", "MergeSort", "BubbleSort", "InsertionSort"], "answer": "InsertionSort"},
    lambda: {"question": "What is the average case space complexity of QuickSort?", "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"], "answer": "O(log n)"},
    lambda: {"question": "Which of these is not a valid complexity of QuickSort?", "options": ["Best: O(n log n)", "Average: O(n log n)", "Worst: O(n^2)", "Worst: O(n^3)"], "answer": "Worst: O(n^3)"},
    lambda: {"question": "Which is a valid base case for QuickSort recursion?", "options": ["size < 2", "pivot == arr[0]", "size > 1", "pivot != arr[n-1]"], "answer": "size < 2"},
    lambda: {"question": "Which of the following is *not* a characteristic of QuickSort?", "options": ["Comparison sort", "Stable sort", "Recursive", "Divide-and-conquer"], "answer": "Stable sort"},
    lambda: {"question": "Why is QuickSort faster than other O(n log n) algorithms in practice?", "options": ["Less memory", "Simple recursion", "Better cache use", "Fewer comparisons"], "answer": "Better cache use"}
],

    
"MTQ": [
    lambda: {
        "question": "Match QuickSort terms (Note: below pairs are wrongly matched):",
        "pairs": {
            "Recursive Calls": "Can be first, last, random, or median",
            "Pivot Selection": "Divide input around pivot",
            "In-place Sorting": "Divide input around pivot"
        },
        "answer": {
            "Recursive Calls": "Divide input around pivot",
            "Pivot Selection": "Can be first, last, random, or median",
            "In-place Sorting": "Does not need extra array"
        }
    },
    lambda: {
        "question": "Match QuickSort concepts (some pairs are incorrectly matched):",
        "pairs": {
            "Partitioning": "Pivot selection technique",
            "Recursion Base Case": "Splits the array based on a pivot",
            "Best Pivot": "Occurs when pivot is median"
        },
        "answer": {
            "Partitioning": "Splits the array based on a pivot",
            "Recursion Base Case": "Occurs when pivot is median",
            "Best Pivot": "Pivot selection technique"
        }
    },
    lambda: {
        "question": "Match QuickSort operations (some items are incorrectly matched):",
        "pairs": {
            "First Element Pivot": "O(n log n) worst case",
            "Stack Depth": "Always best performance",
            "Time Complexity": "O(n) in worst case"
        },
        "answer": {
            "First Element Pivot": "Always best performance",
            "Stack Depth": "O(n) in worst case",
            "Time Complexity": "O(n log n) worst case"
        }
    },
    lambda: {
        "question": "Match the strategies with their characteristics (note incorrect matches):",
        "pairs": {
            "Median Pivot": "Leads to O(n^2) worst case",
            "Random Pivot": "Ensures balanced partitions",
            "Sorted Array Input": "Improves average case"
        },
        "answer": {
            "Median Pivot": "Ensures balanced partitions",
            "Random Pivot": "Improves average case",
            "Sorted Array Input": "Leads to O(n^2) worst case"
        }
    },
    lambda: {
        "question": "Match terms with their QuickSort-related roles (some are wrongly matched):",
        "pairs": {
            "Pivot": "Divides input based on pivot",
            "Partition": "Used for merging",
            "Tail Recursion": "Reduces stack usage"
        },
        "answer": {
            "Pivot": "Used for dividing the array",
            "Partition": "Divides input based on pivot",
            "Tail Recursion": "Reduces stack usage"
        }
    },
    lambda: {
        "question": "Match descriptions with QuickSort elements:",
        "pairs": {
            "Average Time Complexity": "O(n^2)",
            "Worst Time Complexity": "O(n log n)",
            "Space Complexity": "O(1) auxiliary"
        },
        "answer": {
            "Average Time Complexity": "O(n log n)",
            "Worst Time Complexity": "O(n^2)",
            "Space Complexity": "O(1) auxiliary"
        }
    },
    lambda: {
        "question": "Match the QuickSort phase to its function (note: incorrect matching present):",
        "pairs": {
            "Recursive Call": "Splits input using merge",
            "Pivot Selection": "Sorts the full array",
            "Partitioning": "Moves elements around the pivot"
        },
        "answer": {
            "Recursive Call": "Sorts the sub-arrays",
            "Pivot Selection": "Chooses a reference value",
            "Partitioning": "Moves elements around the pivot"
        }
    },
    lambda: {
        "question": "Match QuickSort characteristics (some pairs mismatched):",
        "pairs": {
            "Divide and Conquer": "Preserves relative order",
            "Stability": "Uses merging step",
            "Efficiency": "Good cache performance"
        },
        "answer": {
            "Divide and Conquer": "Divides problem into subproblems",
            "Stability": "Not stable by default",
            "Efficiency": "Good cache performance"
        }
    },
    lambda: {
        "question": "Match QuickSort edge cases to results:",
        "pairs": {
            "Sorted Input": "Balanced partitions",
            "Duplicate Elements": "Worst case time",
            "Random Input": "Average case time"
        },
        "answer": {
            "Sorted Input": "Worst case time",
            "Duplicate Elements": "Can degrade performance",
            "Random Input": "Average case time"
        }
    }
],


    
"ECQ": [
    lambda: {"question": "Complete: The element chosen to divide the array is called ____.", "answer": "pivot"},
    lambda: {"question": "Complete: QuickSort divides the array into ____ partitions.", "answer": "two"},
    lambda: {"question": "Complete: The process of rearranging elements around the pivot is called ____.", "answer": "partitioning"},
    lambda: {"question": "Complete: QuickSort uses ____ and conquer strategy.", "answer": "divide"},
    lambda: {"question": "Complete: The worst-case time complexity of QuickSort is ____.", "answer": "O(n^2)"},
    lambda: {"question": "Complete: QuickSort is ____ in terms of memory since it sorts in place.", "answer": "in-place"},
    lambda: {"question": "Complete: Recursive calls in QuickSort reduce the problem size by sorting ____ partitions.", "answer": "left and right"},
    lambda: {"question": "Complete: The best pivot choice is one that splits the array into ____ parts.", "answer": "equal"},
    lambda: {"question": "Complete: After partitioning, the pivot is at its ____ position.", "answer": "correct"},
    lambda: {"question": "Complete: QuickSort uses ____ comparisons in the average case.", "answer": "O(n log n)"},
    lambda: {"question": "Complete: Tail recursion optimization reduces the ____ used by QuickSort.", "answer": "stack"},
    lambda: {"question": "Complete: When all elements are equal, QuickSort performs ____.", "answer": "poorly"},
    lambda: {"question": "Complete: QuickSort swaps elements to put those less than the pivot to the ____.", "answer": "left"},
    lambda: {"question": "Complete: The variable used to track smaller elements is usually called ____.", "answer": "low"},
    lambda: {"question": "Complete: If arr[i] <= pivot, increment ____ and swap elements.", "answer": "low"},
    lambda: {"question": "Complete: QuickSort’s recursive calls end when the sub-array size is less than ____.", "answer": "2"},
    lambda: {"question": "Complete: Pivot selection strategies include first, last, random, and ____.", "answer": "median"},
    lambda: {"question": "Complete: QuickSort divides the problem into subproblems that are solved ____.", "answer": "recursively"},
    lambda: {"question": "Complete: QuickSort’s average time complexity is ____.", "answer": "O(n log n)"},
    lambda: {"question": "Complete: The partitioning step puts elements smaller than the pivot to the ____ side.", "answer": "left"},
    lambda: {"question": "Complete: QuickSort is ____ stable unless modified.", "answer": "not"},
    lambda: {"question": "Complete: The partition function returns the index of the ____.", "answer": "pivot"},
    lambda: {"question": "Complete: QuickSort works by comparing array elements to the ____.", "answer": "pivot"},
    lambda: {"question": "Complete: Recursive QuickSort calls happen on the left and right ____.", "answer": "subarrays"},
    lambda: {"question": "Complete: QuickSort’s space complexity in the average case is ____.", "answer": "O(log n)"}
],



    "NQ": [
    lambda: (lambda n: {
        "question": f"If the input array size is {n}, what is the worst case number of comparisons in QuickSort?",
        "answer": str(n * (n - 1) // 2)
    })(random_n(5, 15)),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the average case number of comparisons in QuickSort (approximate)?",
        "answer": str(int(n * math.log2(n)))
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"How many recursive calls are made by QuickSort on an array of size {n} in the worst case?",
        "answer": str(n)
    })(random_n(5, 12)),

    lambda: (lambda n: {
        "question": f"If QuickSort partitions an array of size {n} into two equal halves each time, how many levels of recursion occur?",
        "answer": str(int(math.log2(n)))
    })(random_n(8, 16)),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the best-case number of comparisons in QuickSort?",
        "answer": str(int(n * math.log2(n)))
    })(random_n(7, 14)),

    lambda: (lambda n: {
        "question": f"In the worst case, QuickSort performs how many swaps for an array of size {n}?",
        "answer": str(n - 1)
    })(random_n(5, 10)),

    lambda: (lambda n: {
        "question": f"If QuickSort uses tail recursion optimization, what is the maximum depth of recursion for array size {n}?",
        "answer": str(int(math.log2(n)))
    })(random_n(6, 14)),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the average space complexity (stack space) of QuickSort?",
        "answer": "O(log n)"
    })(random_n(5, 10)),

    lambda: (lambda n: {
        "question": f"If a bad pivot is chosen every time, how many comparisons does QuickSort perform on an array of size {n}?",
        "answer": str(n * (n - 1) // 2)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"How many partitions does QuickSort perform to sort an array of size {n}?",
        "answer": str(n - 1)
    })(random_n(5, 10)),

    lambda: (lambda n: {
        "question": f"For array size {n}, how many elements are compared during the first partition?",
        "answer": str(n - 1)
    })(random_n(5, 12)),

    lambda: (lambda n: {
        "question": f"What is the approximate number of comparisons in the best case QuickSort for array size {n}?",
        "answer": str(int(n * math.log2(n)))
    })(random_n(7, 15)),

    lambda: (lambda n: {
        "question": f"If QuickSort processes left and right partitions evenly, what is recursion tree height for {n} elements?",
        "answer": str(int(math.log2(n)))
    })(random_n(8, 64)),

    lambda: (lambda n: {
        "question": f"How many elements does QuickSort partition function typically compare against the pivot in array of size {n}?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"If QuickSort runs on array of size {n} in worst case, what is the number of recursive levels?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the number of comparisons done during the first partition call for array of size {n}?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the maximum height of recursion tree in QuickSort worst case for size {n}?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"How many total partitions occur for array of size {n} in worst case of QuickSort?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"If we pick pivot randomly, average-case partitions for array size {n} would be approximately?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"In QuickSort, how many total function calls happen including base cases for array of size {n}?",
        "answer": str(2 * n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"If QuickSort processes left half first and right half next, how many total calls for size {n}?",
        "answer": str(2 * n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the approximate number of comparisons in average case for array size {n}?",
        "answer": str(int(n * math.log2(n)))
    })(random_n(8, 16)),
],
},



    "level3": {
        "TFQ": [
    lambda: {"question": "True or False: QuickSort uses recursion to sort subarrays.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort is always stable.", "answer": "False"},
    lambda: {"question": "True or False: Pivot selection can affect QuickSort’s efficiency.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort can be implemented in-place.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort’s worst-case time is O(n log n).", "answer": "False"},
    lambda: {"question": "True or False: QuickSort divides the array into two parts around the pivot.", "answer": "True"},
    lambda: {"question": "True or False: The partition function returns the pivot’s final position.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort always chooses the first element as pivot.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort’s average time complexity is O(n log n).", "answer": "True"},
    lambda: {"question": "True or False: QuickSort requires extra space equal to the size of the input array.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort is faster than Bubble Sort for large arrays.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort can sort arrays of strings.", "answer": "True"},
    lambda: {"question": "True or False: The pivot can be chosen randomly in QuickSort.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort always performs the same number of comparisons regardless of input.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort’s space complexity is O(log n) on average.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort never swaps elements during sorting.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort’s base case is when the subarray has one or zero elements.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort uses the ‘merge’ operation to combine sorted parts.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort works well even if the input array is already sorted.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort is a comparison-based sorting algorithm.", "answer": "True"},
    lambda: {"question": "True or False: The pivot always ends up in the correct sorted position after partition.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort can be used to sort linked lists efficiently.", "answer": "False"},
    lambda: {"question": "True or False: QuickSort can have worse performance if the pivot is badly chosen.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort’s recursion depth depends on input size and pivot selection.", "answer": "True"},
    lambda: {"question": "True or False: QuickSort is less efficient than MergeSort in all cases.", "answer": "False"}
],

        "MCQ": [
    lambda: {
        "question": "What is the average time complexity of QuickSort?",
        "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "Which pivot choice often leads to worst-case QuickSort performance?",
        "options": ["Random element", "Median element", "First element", "Middle element"],
        "answer": "First element"
    },
    lambda: {
        "question": "QuickSort’s partition function returns:",
        "options": ["Sorted array", "Pivot index", "Number of swaps", "Array length"],
        "answer": "Pivot index"
    },
    lambda: {
        "question": "QuickSort is an example of which algorithmic paradigm?",
        "options": ["Dynamic Programming", "Divide and Conquer", "Greedy", "Backtracking"],
        "answer": "Divide and Conquer"
    },
    lambda: {
        "question": "Which is NOT a valid pivot selection strategy?",
        "options": ["First element", "Last element", "Random element", "Maximum element"],
        "answer": "Maximum element"
    },
    lambda: {
        "question": "What is QuickSort’s worst-case time complexity?",
        "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
        "answer": "O(n²)"
    },
    lambda: {
        "question": "QuickSort’s space complexity is usually:",
        "options": ["O(n)", "O(log n)", "O(1)", "O(n log n)"],
        "answer": "O(log n)"
    },
    lambda: {
        "question": "Which step is NOT part of QuickSort?",
        "options": ["Selecting a pivot", "Partitioning array", "Merging subarrays", "Recursively sorting subarrays"],
        "answer": "Merging subarrays"
    },
    lambda: {
        "question": "QuickSort is considered:",
        "options": ["Stable", "In-place", "Both", "Neither"],
        "answer": "In-place"
    },
    lambda: {
        "question": "Best pivot choice for average performance is:",
        "options": ["First element", "Median of three", "Last element", "Random element"],
        "answer": "Median of three"
    },
    
],

        "MTQ": [
    lambda: {
        "question": "Match QuickSort terms with their correct definitions (pairs wrongly matched):",
        "pairs": {
            "Pivot": "Process to rearrange elements",
            "Partition": "Element used to split array",
            "Recursive Call": "Sort subarrays around pivot",
            "Worst Case": "Average case complexity O(n log n)",
            "In-place Sorting": "Needs extra memory"
        },
        "answer": {
            "Pivot": "Element used to split array",
            "Partition": "Process to rearrange elements",
            "Recursive Call": "Sort subarrays around pivot",
            "Worst Case": "Time complexity O(n²)",
            "In-place Sorting": "Sorts without extra memory"
        }
    },
    lambda: {
        "question": "Match pivot strategies with descriptions:",
        "pairs": {
            "First Element": "Randomly picked",
            "Last Element": "Always the first",
            "Random Element": "Middle of array",
            "Median of Three": "Median of first, middle, last"
        },
        "answer": {
            "First Element": "Always the first",
            "Last Element": "Always the last",
            "Random Element": "Randomly picked",
            "Median of Three": "Median of first, middle, last"
        }
    },
    lambda: {
        "question": "Match QuickSort complexities with their cases (pairs wrongly matched):",
        "pairs": {
            "Best Case": "O(n²)",
            "Average Case": "O(n log n)",
            "Worst Case": "O(n)",
            "Space Complexity": "O(n log n)"
        },
        "answer": {
            "Best Case": "O(n log n)",
            "Average Case": "O(n log n)",
            "Worst Case": "O(n²)",
            "Space Complexity": "O(log n)"
        }
    },
    lambda: {
        "question": "Match QuickSort parts with their roles:",
        "pairs": {
            "Partition": "Selects pivot",
            "Pivot": "Divides array into subarrays",
            "Recursive Calls": "Rearranges array",
            "Base Case": "Array with two elements"
        },
        "answer": {
            "Partition": "Rearranges array",
            "Pivot": "Selects pivot",
            "Recursive Calls": "Sort subarrays",
            "Base Case": "Array with one or zero elements"
        }
    },
    lambda: {
        "question": "Match these terms with correct statements (pairs wrongly matched):",
        "pairs": {
            "In-place QuickSort": "Requires extra array",
            "Stable Sorting": "Does not change order of equal elements",
            "Recursion Depth": "Always O(log n)",
            "Pivot Choice": "Does not affect performance"
        },
        "answer": {
            "In-place QuickSort": "Does not require extra array",
            "Stable Sorting": "Does not change order of equal elements",
            "Recursion Depth": "Depends on pivot selection",
            "Pivot Choice": "Heavily affects performance"
        }
    },
    lambda: {
        "question": "Match the pivot selection with expected performance:",
        "pairs": {
            "First Element": "Good average case",
            "Random Pivot": "Worst case guaranteed",
            "Median of Three": "Improves average case",
            "Last Element": "Always worst case"
        },
        "answer": {
            "First Element": "Can cause worst case",
            "Random Pivot": "Good average case",
            "Median of Three": "Improves average case",
            "Last Element": "Can cause worst case"
        }
    },
    lambda: {
        "question": "Match partition steps with descriptions (pairs wrongly matched):",
        "pairs": {
            "Choose Pivot": "Split array into two equal halves",
            "Compare Elements": "Move pivot to correct position",
            "Swap Elements": "Choose middle element as pivot",
            "Return Index": "Count comparisons"
        },
        "answer": {
            "Choose Pivot": "Select pivot element",
            "Compare Elements": "Check elements against pivot",
            "Swap Elements": "Swap smaller and larger elements",
            "Return Index": "Pivot’s final position"
        }
    },
    lambda: {
        "question": "Match QuickSort algorithm stages:",
        "pairs": {
            "Divide": "Recursive call",
            "Conquer": "Partition array",
            "Combine": "Merge sorted arrays",
            "Base Case": "Array with one or no elements"
        },
        "answer": {
            "Divide": "Partition array",
            "Conquer": "Recursive call",
            "Combine": "No merge needed",
            "Base Case": "Array with one or no elements"
        }
    },
    lambda: {
        "question": "Match QuickSort facts:",
        "pairs": {
            "Worst Case Input": "Random array",
            "Average Case Input": "Sorted array",
            "Best Case Input": "Pivot is median",
            "Pivot Role": "Swap elements randomly"
        },
        "answer": {
            "Worst Case Input": "Sorted or reverse sorted array",
            "Average Case Input": "Random array",
            "Best Case Input": "Pivot is median",
            "Pivot Role": "Divides array for sorting"
        }
    },
    lambda: {
        "question": "Match QuickSort advantages with reasons (pairs wrongly matched):",
        "pairs": {
            "In-place": "Requires extra memory",
            "Fast Average Time": "Pivot choice irrelevant",
            "Recursive": "Uses loops instead of calls",
            "Unstable": "May reorder equal elements"
        },
        "answer": {
            "In-place": "Does not require extra memory",
            "Fast Average Time": "Depends on pivot choice",
            "Recursive": "Uses recursive calls",
            "Unstable": "May reorder equal elements"
        }
    },
    lambda: {
        "question": "Match QuickSort terms:",
        "pairs": {
            "Tail Recursion": "Recursion at the end of function",
            "Stack Depth": "Always O(n log n)",
            "Pivot Selection": "Has no effect",
            "Partition Function": "Splits array"
        },
        "answer": {
            "Tail Recursion": "Recursion at the end of function",
            "Stack Depth": "Depends on pivot and input",
            "Pivot Selection": "Affects performance",
            "Partition Function": "Splits array"
        }
    },
    lambda: {
        "question": "Match QuickSort characteristics:",
        "pairs": {
            "Divide and Conquer": "Sorts array using merge",
            "Stable": "Does not reorder equal items",
            "Average Complexity": "O(n²)",
            "In-place": "No extra memory needed"
        },
        "answer": {
            "Divide and Conquer": "Sorts array recursively",
            "Stable": "No",
            "Average Complexity": "O(n log n)",
            "In-place": "Yes"
        }
    },
    lambda: {
        "question": "Match QuickSort recursion limits:",
        "pairs": {
            "Worst case recursion": "O(log n)",
            "Best case recursion": "O(n)",
            "Average case recursion": "O(log n)",
            "Recursive call count": "Equal for all inputs"
        },
        "answer": {
            "Worst case recursion": "O(n)",
            "Best case recursion": "O(log n)",
            "Average case recursion": "O(log n)",
            "Recursive call count": "Varies with input"
        }
    },
    lambda: {
        "question": "Match pivot placement after partition:",
        "pairs": {
            "Pivot position": "Always at start",
            "Elements smaller": "Right side of pivot",
            "Elements greater": "Left side of pivot",
            "Pivot final": "Correct sorted position"
        },
        "answer": {
            "Pivot position": "Anywhere before partition",
            "Elements smaller": "Left side of pivot",
            "Elements greater": "Right side of pivot",
            "Pivot final": "Correct sorted position"
        }
    },
    lambda: {
        "question": "Match QuickSort terms:",
        "pairs": {
            "Partitioning": "Selecting pivot",
            "Swapping": "Recursive call",
            "Pivot": "Rearranging array",
            "Recursion": "Divide and conquer"
        },
        "answer": {
            "Partitioning": "Rearranging array",
            "Swapping": "Exchange elements",
            "Pivot": "Element chosen to split",
            "Recursion": "Divide and conquer"
        }
    },
    lambda: {
        "question": "Match QuickSort performance with inputs:",
        "pairs": {
            "Sorted input": "Best case",
            "Random input": "Worst case",
            "Reverse sorted": "Average case",
            "Median pivot": "Improves performance"
        },
        "answer": {
            "Sorted input": "Worst case (if poor pivot)",
            "Random input": "Average case",
            "Reverse sorted": "Worst case (if poor pivot)",
            "Median pivot": "Improves performance"
        }
    },
    lambda: {
        "question": "Match QuickSort properties:",
        "pairs": {
            "Time Complexity": "Always O(n log n)",
            "Space Complexity": "O(n)",
            "Stability": "Stable",
            "Pivot Role": "Divide array"
        },
        "answer": {
            "Time Complexity": "Average O(n log n), Worst O(n²)",
            "Space Complexity": "O(log n)",
            "Stability": "Unstable",
            "Pivot Role": "Divide array"
        }
    },
    lambda: {
        "question": "Match QuickSort components:",
        "pairs": {
            "Recursive calls": "Perform partition",
            "Partition": "Place pivot correctly",
            "Swap": "Compare and exchange",
            "Base case": "Array of size > 1"
        },
        "answer": {
            "Recursive calls": "Call quickSort on subarrays",
            "Partition": "Place pivot correctly",
            "Swap": "Compare and exchange",
            "Base case": "Array of size ≤ 1"
        }
    },
    lambda: {
        "question": "Match QuickSort concepts:",
        "pairs": {
            "Divide": "Split array by pivot",
            "Conquer": "Recursive calls on subarrays",
            "Combine": "Merge sorted parts",
            "Base case": "Subarray of size 1 or 0"
        },
        "answer": {
            "Divide": "Split array by pivot",
            "Conquer": "Recursive calls on subarrays",
            "Combine": "No merging needed",
            "Base case": "Subarray of size 1 or 0"
        }
    },
    lambda: {
        "question": "Match QuickSort algorithm steps:",
        "pairs": {
            "Choose pivot": "Divide array",
            "Partition": "Rearrange elements",
            "Recursive calls": "Sort subarrays",
            "Merge": "Combine sorted arrays"
        },
        "answer": {
            "Choose pivot": "Select element",
            "Partition": "Rearrange elements",
            "Recursive calls": "Sort subarrays",
            "Merge": "Not required in QuickSort"
        }
    },
    lambda: {
        "question": "Match QuickSort pivot selection advantages:",
        "pairs": {
            "First element": "Simple but may cause worst case",
            "Random element": "Avoids worst case on sorted input",
            "Median of three": "Better pivot choice",
            "Last element": "Same as first element"
        },
        "answer": {
            "First element": "Simple but may cause worst case",
            "Random element": "Avoids worst case on sorted input",
            "Median of three": "Better pivot choice",
            "Last element": "May cause worst case"
        }
    },
    lambda: {
        "question": "Match QuickSort sorting properties:",
        "pairs": {
            "Stable": "Yes",
            "In-place": "Yes",
            "Recursive": "Yes",
            "Comparison based": "No"
        },
        "answer": {
            "Stable": "No",
            "In-place": "Yes",
            "Recursive": "Yes",
            "Comparison based": "Yes"
        }
    },
    lambda: {
        "question": "Match QuickSort drawbacks:",
        "pairs": {
            "Worst case time": "O(n log n)",
            "Pivot selection": "Does not affect complexity",
            "Unstable sorting": "Equal elements may reorder",
            "Extra memory": "Requires additional array"
        },
        "answer": {
            "Worst case time": "O(n²)",
            "Pivot selection": "Heavily affects complexity",
            "Unstable sorting": "Equal elements may reorder",
            "Extra memory": "Usually no extra memory needed"
        }
    }
],

        "ECQ": [
    lambda: {
        "question": "Fill in: QuickSort is a _______ and conquer algorithm.",
        "answer": "divide"
    },
    lambda: {
        "question": "Complete: The pivot divides the array into elements less than or equal to pivot and _______.",
        "answer": "greater"
    },
    lambda: {
        "question": "Fill base case: if low >= _______: return",
        "answer": "high"
    },
    lambda: {
        "question": "Complete: After partitioning, the pivot is at its _______ position.",
        "answer": "correct"
    },
    lambda: {
        "question": "Fill in: QuickSort’s average time complexity is O(_______).",
        "answer": "n log n"
    },
    lambda: {
        "question": "Fill in: QuickSort’s worst case time complexity occurs when the pivot is the _______ or _______ element repeatedly.",
        "answer": "first last"
    },
    lambda: {
        "question": "Complete: QuickSort is considered _______ sorting because it sorts without using extra arrays.",
        "answer": "in-place"
    },
    lambda: {
        "question": "Fill base case: The recursion in QuickSort stops when the subarray has _______ or fewer elements.",
        "answer": "one"
    },
    lambda: {
        "question": "Fill in: Partition function rearranges elements so that those less than pivot come _______ the pivot.",
        "answer": "before"
    },
    lambda: {
        "question": "Complete: The _______ of the pivot is its final sorted index after partitioning.",
        "answer": "position"
    },
    lambda: {
        "question": "Fill in: The median of _______ pivot selection improves QuickSort’s average performance.",
        "answer": "three"
    },
    lambda: {
        "question": "Complete: QuickSort uses _______ calls to sort the subarrays formed after partition.",
        "answer": "recursive"
    },
    lambda: {
        "question": "Fill in: In QuickSort, the average number of comparisons is proportional to n log _______.",
        "answer": "n"
    },
    
    lambda: {
        "question": "Fill in: The choice of pivot affects both time complexity and _______ complexity of QuickSort.",
        "answer": "space"
    },
    lambda: {
        "question": "Complete: QuickSort is generally faster than MergeSort because it has lower _______ overhead.",
        "answer": "memory"
    },
    lambda: {
        "question": "Fill base case: if low < _______: proceed with partition and recursive calls.",
        "answer": "high"
    },
    lambda: {
        "question": "Fill in: When the pivot divides the array into two nearly equal parts, QuickSort performs at its _______ case.",
        "answer": "best"
    },
    lambda: {
        "question": "Complete: QuickSort is called an _______ algorithm because it uses comparisons to sort elements.",
        "answer": "comparison-based"
    },
    lambda: {
        "question": "Fill in: The partition step in QuickSort is responsible for placing the pivot in its _______ sorted position.",
        "answer": "correct"
    },
    lambda: {
        "question": "Complete: The average recursion depth of QuickSort is O(_______).",
        "answer": "log n"
    },
    lambda: {
        "question": "Fill in: QuickSort’s performance deteriorates to O(n²) when the pivot is chosen _______ each time.",
        "answer": "poorly"
    },
    lambda: {
        "question": "Complete: The 'divide' step in QuickSort involves selecting a _______ element.",
        "answer": "pivot"
    },
    lambda: {
        "question": "Fill base case: QuickSort recursion ends when subarray size is less than or equal to _______.",
        "answer": "one"
    },
    lambda: {
        "question": "Complete: Using a random pivot reduces the chance of hitting the _______ case in QuickSort.",
        "answer": "worst"
    }
],

        "NQ": [
    lambda: (lambda n: {
        "question": f"What is the worst-case number of comparisons in QuickSort for array size {n}?",
        "answer": str(n * (n - 1) // 2)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the average-case number of comparisons in QuickSort for array size {n} (approximate)?",
        "answer": str(int(n * (math.log2(n))))
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the maximum recursion depth in the worst case for QuickSort with array size {n}?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"Given QuickSort average complexity O(n log n), what is the approximate time complexity for n={n}?",
        "answer": str(int(n * math.log2(n)))
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"In QuickSort, if array size is {n}, how many comparisons are done in the best case?",
        "answer": str(int(n * math.log2(n)))
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the height of the recursion tree in the best case QuickSort?",
        "answer": str(int(math.log2(n)))
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"How many partitioning steps occur in QuickSort for an array of size {n} in the best case?",
        "answer": str(int(n))
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"For QuickSort on array size {n}, what is the minimum number of swaps during partition?",
        "answer": "0"
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"If QuickSort makes {n} recursive calls, what is the approximate size of subarrays being sorted?",
        "answer": str(1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the average number of recursive calls in QuickSort?",
        "answer": str(int(2 * n * math.log2(n)))
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the total number of comparisons in worst case QuickSort for array size {n}?",
        "answer": str(n * (n - 1) // 2)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"In QuickSort, if the pivot always splits array into two equal parts, what is recursion depth for size {n}?",
        "answer": str(int(math.log2(n)))
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"How many elements are compared during one partition of an array of size {n}?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the best-case time complexity in terms of comparisons for QuickSort on size {n}?",
        "answer": str(int(n * math.log2(n)))
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the average number of swaps in QuickSort for array size {n}?",
        "answer": str(int(n * math.log2(n) / 3))  # Approximate heuristic
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the size of the largest subarray sorted after the first partition in QuickSort for size {n} if pivot is worst case?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"How many comparisons are done in QuickSort's last recursive call for array size {n}?",
        "answer": "1"
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"In QuickSort, what is the average number of comparisons for array size {n}?",
        "answer": str(int(2 * n * math.log2(n)))
    })(random_n(6, 12)),


    lambda: (lambda n: {
        "question": f"What is the number of comparisons in QuickSort if array is already sorted of size {n} and pivot is always last element?",
        "answer": str(n * (n - 1) // 2)
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"Given array size {n}, what is the space complexity due to recursion stack in worst case of QuickSort?",
        "answer": str(n)
    })(random_n(6, 12)),

    lambda: (lambda n: {
    "question": f"What is the total number of partitions performed by QuickSort for array size {n}?",
    "answer": str(n - 1)
})(random_n(6, 12)),


    lambda: (lambda n: {
        "question": f"How many elements does the pivot get compared to during one partition for size {n} array?",
        "answer": str(n - 1)
    })(random_n(6, 12)),

    lambda: (lambda n: {
    "question": f"For an array of size {n}, what is the minimum recursion depth possible in QuickSort?",
    "answer": str(int(math.log2(n)))
})(random_n(6, 12)),


    lambda: (lambda n: {
        "question": f"If QuickSort chooses the median as pivot, what is the expected recursion depth for size {n}?",
        "answer": str(int(math.log2(n)))
    })(random_n(6, 12)),

    lambda: (lambda n: {
        "question": f"What is the worst-case time complexity in terms of comparisons for QuickSort with array size {n}?",
        "answer": str(n * (n - 1) // 2)
    })(random_n(6, 12))
],

    },
}


def generate_quick_sort_questions(level: str, num_questions: int):
    level = level.lower()
    if level not in quicksort_templates:
        raise ValueError("Invalid level. Choose from: level1, level2, level3.")

    typewise_templates = quicksort_templates[level]
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

# === MAIN ENTRY ===

if __name__ == "__main__":
    level = input("Enter difficulty level (level1, level2, level3): ").strip()
    num = int(input("Enter number of questions to generate: "))

    try:
        output = generate_quick_sort_questions(level, num)
        for i, q in enumerate(output, 1):
            print(f"\nQ{i}: {q['question']}")
            if 'options' in q:
                for opt in q['options']:
                    print(f"   - {opt}")
            if 'pairs' in q:
                print("   Mismatched Pairs (in question):")
                for k, v in q['pairs'].items():
                    print(f"     {k} -> {v}")
                print("   Correct Answer Mapping:")
                for k, v in q['answer'].items():
                    print(f"     {k} -> {v}")
            else:
                print(f"Answer: {q['answer']}")
    except Exception as e:
        print("Error:", e)
    