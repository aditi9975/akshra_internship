import random

def random_n(min_val=5, max_val=15):
    return random.randint(min_val, max_val)

def random_choice(choices):
    return random.choice(choices)

templates = {
    "level1": {
        "TFQ": [
    lambda: {
        "question": "True or False: Merge Sort is a divide and conquer algorithm.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort always works in O(n log n) time complexity.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is an unstable sorting algorithm.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort requires extra space for merging.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort sorts the array in place without using additional memory.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort can be used to sort linked lists efficiently.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort divides the array into two halves at each step.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is faster than Bubble Sort for large data sets.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: The merging step in Merge Sort combines two sorted arrays into one sorted array.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort has a worst-case time complexity of O(n²).",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort can be easily implemented using recursion.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort always splits the array into more than two parts at each recursive step.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort is more memory efficient than QuickSort.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort is a comparison-based sorting algorithm.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort can handle data sets that do not fit entirely in memory.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort guarantees stable sorting results.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is generally slower than Heap Sort for small arrays.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort only works on numeric data.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort can be parallelized to improve performance.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort requires fewer comparisons than QuickSort on average.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort’s recursion depth is proportional to log(n), where n is the size of the array.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort cannot be used for external sorting (sorting on disk).",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort divides the input array until single-element arrays remain.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort was invented by John von Neumann in 1945.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort performs better than Insertion Sort for large datasets.",
        "answer": "True"
    }
],

        "MCQ": [
    lambda: {
        "question": "Which of the following is true about Merge Sort?",
        "options": [
            "It sorts in-place",
            "It is not stable",
            "It uses recursion",
            "It is faster than QuickSort always"
        ],
        "answer": "It uses recursion"
    },
    lambda: {
        "question": "What is the time complexity of Merge Sort in the worst case?",
        "options": [
            "O(n²)",
            "O(n log n)",
            "O(log n)",
            "O(n)"
        ],
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "What additional space does Merge Sort require?",
        "options": [
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n²)"
        ],
        "answer": "O(n)"
    },
    lambda: {
        "question": "Which step involves combining two sorted halves in Merge Sort?",
        "options": [
            "Partitioning",
            "Merging",
            "Splitting",
            "Swapping"
        ],
        "answer": "Merging"
    },
    lambda: {
        "question": "Merge Sort is best described as which type of algorithm?",
        "options": [
            "Divide and conquer",
            "Greedy",
            "Dynamic programming",
            "Backtracking"
        ],
        "answer": "Divide and conquer"
    },
    lambda: {
        "question": "Which of the following is NOT true about Merge Sort?",
        "options": [
            "It is stable",
            "It works well with linked lists",
            "It is an in-place algorithm",
            "It always divides the array into halves"
        ],
        "answer": "It is an in-place algorithm"
    },
    lambda: {
        "question": "Which data structure is often used implicitly in Merge Sort due to recursion?",
        "options": [
            "Stack",
            "Queue",
            "Heap",
            "Graph"
        ],
        "answer": "Stack"
    },
    lambda: {
        "question": "During merging in Merge Sort, elements are compared and placed into what?",
        "options": [
            "Original array",
            "Temporary array",
            "Hash map",
            "Linked list"
        ],
        "answer": "Temporary array"
    },
    lambda: {
        "question": "Which sorting algorithm guarantees stability?",
        "options": [
            "Quick Sort",
            "Selection Sort",
            "Merge Sort",
            "Heap Sort"
        ],
        "answer": "Merge Sort"
    },
    lambda: {
        "question": "What is the base case for the Merge Sort recursion?",
        "options": [
            "Array size is zero",
            "Array size is one",
            "Array is sorted",
            "Array size is two"
        ],
        "answer": "Array size is one"
    },
    lambda: {
        "question": "How does Merge Sort handle an array that cannot fit entirely into memory?",
        "options": [
            "It can’t handle it",
            "Uses external sorting",
            "Uses in-place sorting",
            "Uses bubble sort"
        ],
        "answer": "Uses external sorting"
    },
    lambda: {
        "question": "Which step in Merge Sort is the most time-consuming?",
        "options": [
            "Splitting the array",
            "Comparing elements during merging",
            "Choosing pivot",
            "Swapping elements"
        ],
        "answer": "Comparing elements during merging"
    },
    lambda: {
        "question": "What does Merge Sort require to combine sorted subarrays?",
        "options": [
            "Random access",
            "Linear time merging",
            "Hashing",
            "In-place swapping"
        ],
        "answer": "Linear time merging"
    },
    lambda: {
        "question": "Merge Sort’s divide step breaks the problem into how many subproblems?",
        "options": [
            "Two equal halves",
            "Three parts",
            "Single element",
            "Four equal parts"
        ],
        "answer": "Two equal halves"
    },
    lambda: {
        "question": "Merge Sort’s worst-case and best-case time complexities are:",
        "options": [
            "Different",
            "The same",
            "Best case is faster",
            "Worst case is faster"
        ],
        "answer": "The same"
    },
    lambda: {
        "question": "Merge Sort was first invented by:",
        "options": [
            "Donald Knuth",
            "John von Neumann",
            "Edsger Dijkstra",
            "Alan Turing"
        ],
        "answer": "John von Neumann"
    },
    lambda: {
        "question": "Which of these algorithms is Merge Sort commonly compared with?",
        "options": [
            "Insertion Sort",
            "Quick Sort",
            "Counting Sort",
            "Bucket Sort"
        ],
        "answer": "Quick Sort"
    },
    lambda: {
        "question": "Is Merge Sort suitable for sorting linked lists?",
        "options": [
            "Yes, because it does not require random access",
            "No, it needs arrays only",
            "Yes, but only for small lists",
            "No, it is unstable for lists"
        ],
        "answer": "Yes, because it does not require random access"
    },
    lambda: {
        "question": "Which property is true for Merge Sort?",
        "options": [
            "It is unstable",
            "It does not use recursion",
            "It uses extra space",
            "It sorts only numbers"
        ],
        "answer": "It uses extra space"
    },
    lambda: {
        "question": "Merge Sort can be implemented iteratively using:",
        "options": [
            "Queue",
            "Stack",
            "Bottom-up approach",
            "Recursion only"
        ],
        "answer": "Bottom-up approach"
    },
    lambda: {
        "question": "Merge Sort compares elements from subarrays in:",
        "options": [
            "Random order",
            "Sorted order",
            "Any order",
            "Reverse order"
        ],
        "answer": "Sorted order"
    },
    lambda: {
        "question": "Which is a disadvantage of Merge Sort compared to Quick Sort?",
        "options": [
            "More complex to implement",
            "Uses more memory",
            "Unstable sorting",
            "Slower in all cases"
        ],
        "answer": "Uses more memory"
    },
    lambda: {
        "question": "In Merge Sort, the merge step happens:",
        "options": [
            "Before dividing the array",
            "After dividing into smaller arrays",
            "Only once at the end",
            "Only at the start"
        ],
        "answer": "After dividing into smaller arrays"
    },
    lambda: {
        "question": "Merge Sort can be used to sort data on disk because:",
        "options": [
            "It is in-place",
            "It uses minimal memory",
            "It accesses data sequentially",
            "It requires random access"
        ],
        "answer": "It accesses data sequentially"
    },
    lambda: {
        "question": "Merge Sort guarantees a time complexity of O(n log n) for:",
        "options": [
            "Best case only",
            "Worst case only",
            "Average case only",
            "All cases"
        ],
        "answer": "All cases"
    }
],

        "MTQ": [
    lambda: {
        "question": "Match the Merge Sort concepts with their correct descriptions (Note: below pairs are incorrectly matched):",
        "pairs": {
            "Divide Step": "Combines sorted arrays",
            "Merge Step": "Splitting the array",
            "Time Complexity": "O(n)"
        },
        "answer": {
            "Divide Step": "Splitting the array",
            "Merge Step": "Combining sorted arrays",
            "Time Complexity": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match the Merge Sort terms with their meanings:",
        "pairs": {
            "Stable Sort": "Changes order of equal elements",
            "Space Complexity": "O(1)",
            "Recursion Base Case": "Array size greater than one"
        },
        "answer": {
            "Stable Sort": "Maintains order of equal elements",
            "Space Complexity": "O(n)",
            "Recursion Base Case": "Array size is one"
        }
    },
    lambda: {
        "question": "Match the sorting phase to its function in Merge Sort:",
        "pairs": {
            "Splitting": "Merging two sorted lists",
            "Merging": "Dividing the array into halves",
            "Sorting": "Random swapping"
        },
        "answer": {
            "Splitting": "Dividing the array into halves",
            "Merging": "Merging two sorted lists",
            "Sorting": "Combining results into sorted array"
        }
    },
    lambda: {
        "question": "Match the algorithm features to Merge Sort specifics:",
        "pairs": {
            "Algorithm Type": "Dynamic Programming",
            "Worst-case Time Complexity": "O(n²)",
            "Auxiliary Space": "O(n)"
        },
        "answer": {
            "Algorithm Type": "Divide and Conquer",
            "Worst-case Time Complexity": "O(n log n)",
            "Auxiliary Space": "O(n)"
        }
    },
    lambda: {
        "question": "Match the terms to correct Merge Sort properties:",
        "pairs": {
            "In-place Algorithm": "Yes",
            "Stable Sorting": "No",
            "Best Case Time": "O(n log n)"
        },
        "answer": {
            "In-place Algorithm": "No",
            "Stable Sorting": "Yes",
            "Best Case Time": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match the Merge Sort step to its purpose:",
        "pairs": {
            "Divide": "Merge sorted subarrays",
            "Conquer": "Split the array",
            "Combine": "Sort individual elements"
        },
        "answer": {
            "Divide": "Split the array",
            "Conquer": "Sort individual elements",
            "Combine": "Merge sorted subarrays"
        }
    },
    lambda: {
        "question": "Match the concepts with Merge Sort's performance characteristics:",
        "pairs": {
            "Average Case": "O(n)",
            "Space Usage": "O(1)",
            "Stability": "Maintains order"
        },
        "answer": {
            "Average Case": "O(n log n)",
            "Space Usage": "O(n)",
            "Stability": "Maintains order"
        }
    },
    lambda: {
        "question": "Match the step to what happens during Merge Sort:",
        "pairs": {
            "Recursion Ends": "Array of size zero",
            "Merge Process": "Sorting subarrays",
            "Divide Process": "Combining two arrays"
        },
        "answer": {
            "Recursion Ends": "Array of size one",
            "Merge Process": "Combining two arrays",
            "Divide Process": "Sorting subarrays"
        }
    },
    lambda: {
        "question": "Match the terms to Merge Sort memory usage:",
        "pairs": {
            "In-place Sorting": "True",
            "Extra Memory Needed": "O(1)",
            "Auxiliary Space": "O(n)"
        },
        "answer": {
            "In-place Sorting": "False",
            "Extra Memory Needed": "O(n)",
            "Auxiliary Space": "O(n)"
        }
    },
    lambda: {
        "question": "Match the Merge Sort concepts with examples:",
        "pairs": {
            "Divide": "Sorting two halves",
            "Merge": "Combining unsorted arrays",
            "Base Case": "Array size 2"
        },
        "answer": {
            "Divide": "Splitting the array",
            "Merge": "Combining sorted halves",
            "Base Case": "Array size 1"
        }
    },
    lambda: {
        "question": "Match the Merge Sort terminology with definitions:",
        "pairs": {
            "Stable Sort": "Changes relative order",
            "Divide Step": "Splitting array",
            "Merge Step": "Sorting subarrays separately"
        },
        "answer": {
            "Stable Sort": "Maintains relative order",
            "Divide Step": "Splitting array",
            "Merge Step": "Combining sorted arrays"
        }
    },
    lambda: {
        "question": "Match Merge Sort terms with algorithm characteristics:",
        "pairs": {
            "Time Complexity": "O(n²)",
            "Algorithm Paradigm": "Dynamic programming",
            "Space Complexity": "O(n)"
        },
        "answer": {
            "Time Complexity": "O(n log n)",
            "Algorithm Paradigm": "Divide and conquer",
            "Space Complexity": "O(n)"
        }
    },
    lambda: {
        "question": "Match the Merge Sort steps with what happens:",
        "pairs": {
            "Divide": "Combining arrays",
            "Merge": "Splitting array",
            "Recursion": "Breaking down problem"
        },
        "answer": {
            "Divide": "Breaking down problem",
            "Merge": "Combining arrays",
            "Recursion": "Breaking down problem"
        }
    },
    lambda: {
        "question": "Match Merge Sort characteristics with statements:",
        "pairs": {
            "Stable": "No",
            "Divide and Conquer": "Yes",
            "Worst Case Time": "O(n²)"
        },
        "answer": {
            "Stable": "Yes",
            "Divide and Conquer": "Yes",
            "Worst Case Time": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match the algorithm terms with Merge Sort details:",
        "pairs": {
            "Recursive": "No",
            "Stable": "Yes",
            "In-place": "Yes"
        },
        "answer": {
            "Recursive": "Yes",
            "Stable": "Yes",
            "In-place": "No"
        }
    },
    lambda: {
        "question": "Match the following with their Merge Sort properties:",
        "pairs": {
            "Memory Usage": "Constant",
            "Divide Step": "Combining",
            "Merge Step": "Merging sorted subarrays"
        },
        "answer": {
            "Memory Usage": "O(n)",
            "Divide Step": "Splitting array",
            "Merge Step": "Merging sorted subarrays"
        }
    },
    lambda: {
        "question": "Match the Merge Sort features with correct descriptions:",
        "pairs": {
            "Time Complexity": "O(n)",
            "Auxiliary Space": "O(1)",
            "Sorting Type": "In-place"
        },
        "answer": {
            "Time Complexity": "O(n log n)",
            "Auxiliary Space": "O(n)",
            "Sorting Type": "Not in-place"
        }
    },
    lambda: {
        "question": "Match the Merge Sort steps with the right function:",
        "pairs": {
            "Split": "Merge two arrays",
            "Merge": "Split array into halves",
            "Base Case": "Array size 2"
        },
        "answer": {
            "Split": "Split array into halves",
            "Merge": "Merge two arrays",
            "Base Case": "Array size 1"
        }
    },
    lambda: {
        "question": "Match the terms with their role in Merge Sort:",
        "pairs": {
            "Recursion": "Splits array",
            "Merging": "Splits array",
            "Base Case": "Array size greater than one"
        },
        "answer": {
            "Recursion": "Splits array",
            "Merging": "Combines sorted arrays",
            "Base Case": "Array size is one"
        }
    },
    lambda: {
        "question": "Match the Merge Sort properties with statements:",
        "pairs": {
            "Best Case Time": "O(n²)",
            "Worst Case Time": "O(n log n)",
            "Stable Sort": "No"
        },
        "answer": {
            "Best Case Time": "O(n log n)",
            "Worst Case Time": "O(n log n)",
            "Stable Sort": "Yes"
        }
    },
    lambda: {
        "question": "Match the terms to the correct Merge Sort phases:",
        "pairs": {
            "Divide": "Merge two arrays",
            "Merge": "Split array",
            "Base Case": "Array size zero"
        },
        "answer": {
            "Divide": "Split array",
            "Merge": "Merge two arrays",
            "Base Case": "Array size one"
        }
    },
    lambda: {
        "question": "Match the algorithm steps with their actions in Merge Sort:",
        "pairs": {
            "Divide": "Sort arrays",
            "Merge": "Combine arrays",
            "Recursive Call": "Divide array"
        },
        "answer": {
            "Divide": "Divide array",
            "Merge": "Combine arrays",
            "Recursive Call": "Divide array"
        }
    },
    lambda: {
        "question": "Match the sorting algorithm properties to Merge Sort:",
        "pairs": {
            "Stability": "No",
            "Time Complexity": "O(n log n)",
            "Space Complexity": "O(1)"
        },
        "answer": {
            "Stability": "Yes",
            "Time Complexity": "O(n log n)",
            "Space Complexity": "O(n)"
        }
    },
    lambda: {
        "question": "Match the steps with their descriptions in Merge Sort:",
        "pairs": {
            "Split": "Merge sorted arrays",
            "Merge": "Split array",
            "Base Case": "Array size zero"
        },
        "answer": {
            "Split": "Split array",
            "Merge": "Merge sorted arrays",
            "Base Case": "Array size one"
        }
    }
],

        "ECQ": [
    lambda: {
        "question": "Complete the statement: Merge Sort divides the array until each sub-array has only ____ element(s).",
        "answer": "one"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort has a time complexity of ____ in the worst case.",
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "Complete: The merging process in Merge Sort combines two ____ subarrays.",
        "answer": "sorted"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort is an example of a ____ and conquer algorithm.",
        "answer": "divide"
    },
    lambda: {
        "question": "Complete the sentence: Merge Sort requires ____ extra space to merge subarrays.",
        "answer": "linear"
    },
    lambda: {
        "question": "Fill in the blank: The base case of Merge Sort recursion occurs when the array size is ____.",
        "answer": "one"
    },
    lambda: {
        "question": "Complete the statement: Merge Sort is ____ stable, meaning it maintains the order of equal elements.",
        "answer": "stable"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort splits the array approximately ____ times for an array of size n.",
        "answer": "log n"
    },
    lambda: {
        "question": "Complete: The merge step in Merge Sort takes ____ time proportional to the combined size of the two arrays.",
        "answer": "linear"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort is ____ efficient for sorting linked lists compared to arrays.",
        "answer": "more"
    },
    lambda: {
        "question": "Complete the sentence: Merge Sort has a ____ auxiliary space complexity.",
        "answer": "O(n)"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort does not sort the array ____-place.",
        "answer": "in"
    },
    lambda: {
        "question": "Complete the statement: The first step in Merge Sort is to ____ the array into smaller parts.",
        "answer": "divide"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort combines sorted subarrays in the ____ step.",
        "answer": "merge"
    },
    lambda: {
        "question": "Complete: Merge Sort’s recursion depth is proportional to ____ of the array size.",
        "answer": "log n"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort works best when the data can be accessed ____.",
        "answer": "sequentially"
    },
    lambda: {
        "question": "Complete the sentence: Merge Sort was invented by John von ____.",
        "answer": "Neumann"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort's worst-case and average-case time complexity are both ____.",
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "Complete: Merge Sort divides the problem recursively until subarrays of size ____ are reached.",
        "answer": "one"
    },
    lambda: {
        "question": "Fill in the blank: The total number of merge operations in Merge Sort for n elements is approximately ____.",
        "answer": "n - 1"
    },
    lambda: {
        "question": "Complete the statement: Merge Sort is often preferred for sorting ____ data structures like linked lists.",
        "answer": "linked list"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort requires ____ passes through the array for sorting.",
        "answer": "multiple"
    },
    lambda: {
        "question": "Complete the sentence: The time complexity of merging two sorted arrays of sizes m and n is ____.",
        "answer": "O(m + n)"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort’s performance does not degrade significantly for ____ data.",
        "answer": "sorted"
    },
    lambda: {
        "question": "Complete the statement: Merge Sort is ____ recursive algorithm.",
        "answer": "a"
    }
],

        "NQ": [
    lambda: (lambda n: {
        "question": f"How many total levels of recursion occur in Merge Sort for an array of size {n}?",
        "answer": str(n.bit_length())
    })(random_choice([8, 16, 32, 64, 128])),
    
    lambda: (lambda n: {
        "question": f"What is the worst-case time complexity (in Big-O notation) for Merge Sort sorting an array of size {n}?",
        "answer": "O(n log n)"
    })(random_choice([10, 20, 50, 100])),

    lambda: (lambda n: {
        "question": f"How many comparisons are made during the merge step when merging two sorted arrays of size {n//2} each?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32, 64])),

    lambda: (lambda n: {
        "question": f"What is the total auxiliary space required by Merge Sort to sort an array of size {n}?",
        "answer": str(n)
    })(random_choice([10, 50, 100])),

    lambda: (lambda n: {
        "question": f"How many times is the array divided in half when performing Merge Sort on an array of size {n}?",
        "answer": str(n.bit_length() - 1)
    })(random_choice([8, 16, 32, 64])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many merge operations are performed in total in Merge Sort?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32, 64])),

    lambda: (lambda n: {
        "question": f"How many subarrays does Merge Sort create at the deepest level when sorting an array of size {n}?",
        "answer": str(n)
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"Calculate the approximate total number of comparisons made by Merge Sort when sorting an array of size {n} (assume ideal conditions).",
        "answer": str(int(n * (n.bit_length())))
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the minimum size of subarrays before merging starts in Merge Sort?",
        "answer": "1"
    })(random_choice([10, 20, 50])),

    lambda: (lambda n: {
        "question": f"How many recursive calls are made in total when performing Merge Sort on an array of size {n}?",
        "answer": str(2 * n - 1)
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"How many times does Merge Sort call the merge function for an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"What is the depth of the recursion tree in Merge Sort for an array of size {n}?",
        "answer": str(n.bit_length())
    })(random_choice([8, 16, 32, 64])),

    lambda: (lambda n: {
        "question": f"Calculate the time complexity exponent in Merge Sort for array size {n} (log base 2 of n).",
        "answer": str(n.bit_length() - 1)
    })(random_choice([8, 16, 32, 64])),

    lambda: (lambda n: {
        "question": f"For Merge Sort, what is the total number of merges required to completely sort an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"How many elements are there in each subarray at the deepest recursion level for array size {n} in Merge Sort?",
        "answer": "1"
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"What is the total number of comparisons made during the merge step for sorting an array of size {n}?",
        "answer": str(n * (n.bit_length()))
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"How many times is the merge step executed in Merge Sort for an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"Calculate the number of elements in each merged subarray at the first merge step for an array of size {n} in Merge Sort.",
        "answer": str(2)
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the total number of recursive splits in Merge Sort?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"What is the time complexity of merging two arrays of size {n//2} each in Merge Sort?",
        "answer": "O(n)"
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"How many times is an array of size {n} divided in Merge Sort before reaching subarrays of size 1?",
        "answer": str(n.bit_length() - 1)
    })(random_choice([8, 16, 32])),

    lambda: (lambda n: {
        "question": f"Calculate the number of merge operations performed at the second level of Merge Sort recursion for an array of size {n}.",
        "answer": str(n // 4)
    })(random_choice([8, 16, 32, 64])),

    lambda: (lambda n: {
        "question": f"What is the height of the recursion tree for Merge Sort sorting an array of size {n}?",
        "answer": str(n.bit_length())
    })(random_choice([8, 16, 32, 64])),

    lambda: (lambda n: {
        "question": f"How many comparisons are performed when merging two sorted subarrays of size {n // 2} in Merge Sort?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32]))
]

    },

    "level2": {
        "TFQ": [
    lambda: {
        "question": "True or False: Merge Sort is a stable sorting algorithm.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort requires O(1) auxiliary space.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort performs better than QuickSort in the worst case.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is an in-place sorting algorithm.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort divides the array into halves until subarrays of size two are reached.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort’s time complexity is unaffected by the initial order of elements.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort can be implemented iteratively as well as recursively.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort’s merging process always involves comparing elements from both subarrays.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort can sort data stored on external memory efficiently.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is slower than Bubble Sort for very small arrays.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort’s performance is significantly impacted by the choice of pivot element.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort is based on the principle of divide and conquer.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: The merge step in Merge Sort can be parallelized to improve performance.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort requires extra space proportional to the input size during merging.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort can be adapted to work on linked lists without extra space.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort’s average time complexity is O(n^2).",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort splits the array until each subarray has a single element.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is less efficient than QuickSort on average.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is the best choice when stability in sorting is required.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort can handle sorting data stored on tape drives efficiently.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort can be used as a base case for hybrid sorting algorithms.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort’s recursion depth is logarithmic relative to the input size.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort performs fewer comparisons than QuickSort in all cases.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort’s merge function combines two sorted subarrays into one sorted array.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort requires random access to data for efficient sorting.",
        "answer": "False"
    }
],

        "MCQ": [
    lambda: {
        "question": "What is the auxiliary space complexity of Merge Sort?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "answer": "O(n)"
    },
    lambda: {
        "question": "Which data structure is commonly used during the merge process of Merge Sort?",
        "options": ["Stack", "Queue", "Temporary array", "Linked list"],
        "answer": "Temporary array"
    },
    lambda: {
        "question": "Merge Sort is most suitable for which of the following scenarios?",
        "options": ["Sorting small arrays", "Sorting linked lists", "Sorting already sorted arrays", "Sorting data in-place"],
        "answer": "Sorting linked lists"
    },
    lambda: {
        "question": "What is the worst-case time complexity of Merge Sort?",
        "options": ["O(n)", "O(n^2)", "O(n log n)", "O(log n)"],
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "Which property makes Merge Sort preferred over QuickSort in some cases?",
        "options": ["In-place sorting", "Stability", "Faster average case", "Less memory usage"],
        "answer": "Stability"
    },
    lambda: {
        "question": "In Merge Sort, the array is divided into how many parts during the divide step?",
        "options": ["Two", "Three", "Four", "Multiple parts"],
        "answer": "Two"
    },
    lambda: {
        "question": "What is the best-case time complexity of Merge Sort?",
        "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "Which of the following sorting algorithms uses a similar divide-and-conquer approach as Merge Sort?",
        "options": ["Bubble Sort", "Insertion Sort", "QuickSort", "Selection Sort"],
        "answer": "QuickSort"
    },
    lambda: {
        "question": "Which of these is NOT a characteristic of Merge Sort?",
        "options": ["Stable", "Divide and conquer", "In-place", "Recursive"],
        "answer": "In-place"
    },
    lambda: {
        "question": "How does Merge Sort perform when sorting linked lists compared to arrays?",
        "options": ["Worse", "Better", "Same", "Not applicable"],
        "answer": "Better"
    },
    lambda: {
        "question": "What type of recursion does Merge Sort use?",
        "options": ["Tail recursion", "Head recursion", "Binary recursion", "Linear recursion"],
        "answer": "Binary recursion"
    },
    lambda: {
        "question": "What is the space complexity of an iterative implementation of Merge Sort?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
        "answer": "O(n)"
    },
    lambda: {
        "question": "Merge Sort’s merging step can be optimized to run in what time complexity?",
        "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
        "answer": "O(n)"
    },
    lambda: {
        "question": "Which of the following is a disadvantage of Merge Sort?",
        "options": ["Not stable", "Uses extra memory", "Slow average case", "Does not work for linked lists"],
        "answer": "Uses extra memory"
    },
    lambda: {
        "question": "How does Merge Sort handle duplicate elements?",
        "options": ["Removes duplicates", "Keeps duplicates in original order", "Places duplicates at the end", "Ignores duplicates"],
        "answer": "Keeps duplicates in original order"
    },
    lambda: {
        "question": "Which scenario best illustrates the worst-case performance for Merge Sort?",
        "options": ["Already sorted array", "Reverse sorted array", "Random array", "All above have same performance"],
        "answer": "All above have same performance"
    },
    lambda: {
        "question": "What happens during the merge step of Merge Sort?",
        "options": ["Divides array into subarrays", "Sorts two sorted subarrays into one", "Finds pivot element", "Removes duplicates"],
        "answer": "Sorts two sorted subarrays into one"
    },
    lambda: {
        "question": "What is the primary factor that affects the number of merge steps in Merge Sort?",
        "options": ["Array size", "Data values", "Sorting order", "Memory size"],
        "answer": "Array size"
    },
    lambda: {
        "question": "Which sorting algorithm is more memory efficient than Merge Sort?",
        "options": ["Heap Sort", "Bubble Sort", "Selection Sort", "Insertion Sort"],
        "answer": "Heap Sort"
    },
    lambda: {
        "question": "Which of these sorting algorithms is stable and uses extra memory similar to Merge Sort?",
        "options": ["QuickSort", "Counting Sort", "Heap Sort", "Insertion Sort"],
        "answer": "Counting Sort"
    },
    lambda: {
        "question": "What is the minimum subarray size at which Merge Sort stops dividing?",
        "options": ["1", "2", "0", "Depends on implementation"],
        "answer": "1"
    },
    lambda: {
        "question": "Can Merge Sort be efficiently implemented without recursion?",
        "options": ["Yes, using iterative approach", "No, recursion is mandatory", "Only with complex data structures", "Only in functional languages"],
        "answer": "Yes, using iterative approach"
    },
    lambda: {
        "question": "Which of the following best describes Merge Sort’s approach to sorting?",
        "options": ["Sorting by swapping adjacent elements", "Sorting by dividing and merging", "Sorting by selecting the minimum element", "Sorting by comparing with pivot"],
        "answer": "Sorting by dividing and merging"
    },
    lambda: {
        "question": "Merge Sort is often preferred for sorting which type of data due to its stable nature?",
        "options": ["Unstable data", "Data with duplicate keys", "Random data with unique keys", "Data with small size"],
        "answer": "Data with duplicate keys"
    },
    lambda: {
        "question": "Which of the following is true for the number of comparisons in Merge Sort?",
        "options": ["Always n", "Approximately n log n", "Approximately n^2", "Always constant"],
        "answer": "Approximately n log n"
    }
],

        "MTQ": [
    lambda: {
        "question": "Match Merge Sort terms (some are incorrectly matched):",
        "pairs": {
            "Stability": "Unstable",
            "Divide and Conquer": "Used by QuickSort only",
            "Base Case": "Array size > 1"
        },
        "answer": {
            "Stability": "Stable",
            "Divide and Conquer": "Used by Merge Sort",
            "Base Case": "Array size == 1"
        }
    },
    lambda: {
        "question": "Match the step in Merge Sort to its description:",
        "pairs": {
            "Divide": "Combining sorted halves",
            "Conquer": "Splitting the array",
            "Merge": "Sorting individual elements"
        },
        "answer": {
            "Divide": "Splitting the array",
            "Conquer": "Sorting individual elements",
            "Merge": "Combining sorted halves"
        }
    },
    lambda: {
        "question": "Match the time complexity terms with their correct meaning:",
        "pairs": {
            "O(n log n)": "Worst case of Bubble Sort",
            "O(n^2)": "Worst case of Merge Sort",
            "O(n)": "Best case of Merge Sort"
        },
        "answer": {
            "O(n log n)": "Worst case of Merge Sort",
            "O(n^2)": "Worst case of Bubble Sort",
            "O(n)": "Best case of Merge Sort"
        }
    },
    lambda: {
        "question": "Match Merge Sort properties with True or False:",
        "pairs": {
            "Stable": "False",
            "In-place": "True",
            "Divide and Conquer": "True"
        },
        "answer": {
            "Stable": "True",
            "In-place": "False",
            "Divide and Conquer": "True"
        }
    },
    lambda: {
        "question": "Match the auxiliary space usages with sorting algorithms:",
        "pairs": {
            "Merge Sort": "O(1)",
            "QuickSort": "O(n)",
            "Heap Sort": "O(log n)"
        },
        "answer": {
            "Merge Sort": "O(n)",
            "QuickSort": "O(log n)",
            "Heap Sort": "O(1)"
        }
    },
    lambda: {
        "question": "Match the terms to their correct explanations in Merge Sort:",
        "pairs": {
            "Merge Step": "Divide array into halves",
            "Base Condition": "Array size equals 0",
            "Recursive Calls": "Combine sorted arrays"
        },
        "answer": {
            "Merge Step": "Combine sorted arrays",
            "Base Condition": "Array size equals 1",
            "Recursive Calls": "Divide array into halves"
        }
    },
    lambda: {
        "question": "Match the sorting concepts with their definitions:",
        "pairs": {
            "Stability": "Order changes for equal elements",
            "In-place": "Extra memory used",
            "Divide and Conquer": "Breaking problem into subproblems"
        },
        "answer": {
            "Stability": "Order preserved for equal elements",
            "In-place": "Minimal extra memory used",
            "Divide and Conquer": "Breaking problem into subproblems"
        }
    },
    lambda: {
        "question": "Match the Merge Sort steps to their order:",
        "pairs": {
            "First": "Merge arrays",
            "Second": "Divide arrays",
            "Third": "Sort single elements"
        },
        "answer": {
            "First": "Divide arrays",
            "Second": "Sort single elements",
            "Third": "Merge arrays"
        }
    },
    lambda: {
        "question": "Match the scenarios with Merge Sort performance:",
        "pairs": {
            "Sorted array": "Best case O(n log n)",
            "Reverse sorted": "Worst case O(n log n)",
            "Nearly sorted": "Best case O(n)"
        },
        "answer": {
            "Sorted array": "Best case O(n log n)",
            "Reverse sorted": "Worst case O(n log n)",
            "Nearly sorted": "Best case O(n log n)"
        }
    },
    lambda: {
        "question": "Match the following array sizes with number of recursion levels in Merge Sort:",
        "pairs": {
            "Array size 8": "3 levels",
            "Array size 16": "5 levels",
            "Array size 32": "4 levels"
        },
        "answer": {
            "Array size 8": "3 levels",
            "Array size 16": "4 levels",
            "Array size 32": "5 levels"
        }
    },
    lambda: {
        "question": "Match the Merge Sort terms with memory usage:",
        "pairs": {
            "Temporary array": "In-place sorting",
            "Auxiliary space": "Extra memory for merging",
            "Stack space": "Memory for recursion"
        },
        "answer": {
            "Temporary array": "Extra memory for merging",
            "Auxiliary space": "Memory for recursion",
            "Stack space": "In-place sorting"
        }
    },
    lambda: {
        "question": "Match Merge Sort algorithm phases to their characteristics:",
        "pairs": {
            "Divide": "Recursively split arrays",
            "Merge": "Combine sorted subarrays",
            "Sort": "Use bubble sort on small arrays"
        },
        "answer": {
            "Divide": "Recursively split arrays",
            "Merge": "Combine sorted subarrays",
            "Sort": "N/A"
        }
    },
    lambda: {
        "question": "Match the sorting algorithms with their stability:",
        "pairs": {
            "Merge Sort": "Unstable",
            "QuickSort": "Stable",
            "Bubble Sort": "Stable"
        },
        "answer": {
            "Merge Sort": "Stable",
            "QuickSort": "Unstable",
            "Bubble Sort": "Stable"
        }
    },
    lambda: {
        "question": "Match the Merge Sort components with their definitions:",
        "pairs": {
            "Recursion": "Breaking down problems",
            "Iteration": "Repeated looping",
            "Merge function": "Combining two sorted arrays"
        },
        "answer": {
            "Recursion": "Breaking down problems",
            "Iteration": "Repeated looping",
            "Merge function": "Combining two sorted arrays"
        }
    },
    lambda: {
        "question": "Match the sorting concepts with correct properties:",
        "pairs": {
            "In-place sorting": "No extra memory",
            "Stable sorting": "Preserves order",
            "Divide and conquer": "Solves smaller problems"
        },
        "answer": {
            "In-place sorting": "No extra memory",
            "Stable sorting": "Preserves order",
            "Divide and conquer": "Solves smaller problems"
        }
    },
    lambda: {
        "question": "Match the sorting algorithms with their typical use cases:",
        "pairs": {
            "Merge Sort": "Sorting linked lists",
            "QuickSort": "Sorting arrays in-place",
            "Insertion Sort": "Nearly sorted arrays"
        },
        "answer": {
            "Merge Sort": "Sorting linked lists",
            "QuickSort": "Sorting arrays in-place",
            "Insertion Sort": "Nearly sorted arrays"
        }
    },
    lambda: {
        "question": "Match the following concepts with Merge Sort characteristics:",
        "pairs": {
            "Divide step": "Splits the array",
            "Conquer step": "Sorting subarrays",
            "Combine step": "Merging sorted arrays"
        },
        "answer": {
            "Divide step": "Splits the array",
            "Conquer step": "Sorting subarrays",
            "Combine step": "Merging sorted arrays"
        }
    },
    lambda: {
        "question": "Match the following terms with Merge Sort's space complexity types:",
        "pairs": {
            "Auxiliary space": "Memory outside input",
            "In-place": "Sort without extra memory",
            "Stack space": "Memory for recursive calls"
        },
        "answer": {
            "Auxiliary space": "Memory outside input",
            "In-place": "Sort without extra memory",
            "Stack space": "Memory for recursive calls"
        }
    },
    lambda: {
        "question": "Match the algorithm steps to descriptions:",
        "pairs": {
            "Divide": "Break array into halves",
            "Recursive call": "Sort smaller arrays",
            "Merge": "Combine sorted arrays"
        },
        "answer": {
            "Divide": "Break array into halves",
            "Recursive call": "Sort smaller arrays",
            "Merge": "Combine sorted arrays"
        }
    },
    lambda: {
        "question": "Match the Merge Sort advantages with their explanations:",
        "pairs": {
            "Stable": "Preserves input order of equal keys",
            "Consistent runtime": "Always O(n log n)",
            "In-place": "Doesn't need extra memory"
        },
        "answer": {
            "Stable": "Preserves input order of equal keys",
            "Consistent runtime": "Always O(n log n)",
            "In-place": "False"
        }
    },
    lambda: {
        "question": "Match the following Merge Sort terms with their role:",
        "pairs": {
            "Temporary array": "Used for sorting in-place",
            "Recursive division": "Splitting arrays into halves",
            "Base case": "When array size is 0"
        },
        "answer": {
            "Temporary array": "Used for merging sorted arrays",
            "Recursive division": "Splitting arrays into halves",
            "Base case": "When array size is 1"
        }
    },
    lambda: {
        "question": "Match the Merge Sort concepts with their correctness:",
        "pairs": {
            "Stable sorting": "Keeps order of equal elements",
            "Worst-case time": "O(n^2)",
            "Space complexity": "O(n)"
        },
        "answer": {
            "Stable sorting": "Keeps order of equal elements",
            "Worst-case time": "O(n log n)",
            "Space complexity": "O(n)"
        }
    },
    lambda: {
        "question": "Match Merge Sort steps to their input/output:",
        "pairs": {
            "Divide": "Takes array, outputs halves",
            "Merge": "Takes sorted halves, outputs sorted array",
            "Base case": "Single element array"
        },
        "answer": {
            "Divide": "Takes array, outputs halves",
            "Merge": "Takes sorted halves, outputs sorted array",
            "Base case": "Single element array"
        }
    },
    lambda: {
        "question": "Match Merge Sort phases with their computational costs:",
        "pairs": {
            "Divide": "O(1)",
            "Merge": "O(n)",
            "Recursive call overhead": "O(log n)"
        },
        "answer": {
            "Divide": "O(1)",
            "Merge": "O(n)",
            "Recursive call overhead": "O(log n)"
        }
    }
],

        "ECQ": [
    lambda: {
        "question": "Fill in the blank: To merge two sorted arrays, we compare the ____ elements.",
        "answer": "first"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort requires ____ extra space for merging arrays.",
        "answer": "O(n)"
    },
    lambda: {
        "question": "Fill in the blank: The base case in Merge Sort occurs when the array size is ____.",
        "answer": "one"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort is a ____ sorting algorithm because it breaks problems into smaller subproblems.",
        "answer": "divide and conquer"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort is considered ____ because it preserves the order of equal elements.",
        "answer": "stable"
    },
    lambda: {
        "question": "Fill in the blank: The time complexity of merging two sorted arrays of size n is ____.",
        "answer": "O(n)"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort recursively splits the array into two halves until the sub-array size is ____.",
        "answer": "one"
    },
    lambda: {
        "question": "Fill in the blank: The recursive depth of Merge Sort for an array of size n is approximately ____.",
        "answer": "log n"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort is not considered an ____ sorting algorithm because it requires additional memory.",
        "answer": "in-place"
    },
    lambda: {
        "question": "Fill in the blank: The final sorted array in Merge Sort is obtained after the ____ step.",
        "answer": "merge"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort guarantees a worst-case time complexity of ____.",
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort is efficient for sorting linked lists because it does not require ____ access.",
        "answer": "random"
    },
    lambda: {
        "question": "Fill in the blank: During merging, if the elements are equal, Merge Sort places the element from the ____ sub-array first to maintain stability.",
        "answer": "left"
    },
    lambda: {
        "question": "Fill in the blank: The merge operation combines two sorted arrays into a ____ sorted array.",
        "answer": "single"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort splits the array into ____ halves during the divide step.",
        "answer": "two"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort requires extra space proportional to the size of the ____ being sorted.",
        "answer": "array"
    },
    lambda: {
        "question": "Fill in the blank: The merging process in Merge Sort involves repeatedly choosing the ____ smallest element from the sub-arrays.",
        "answer": "next"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort is preferred over QuickSort in cases where ____ time complexity is critical.",
        "answer": "worst-case"
    },
    lambda: {
        "question": "Fill in the blank: The merge function in Merge Sort runs in linear time proportional to the ____ of the two arrays being merged.",
        "answer": "total size"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort is a ____ algorithm since it uses recursion to break down the problem.",
        "answer": "recursive"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort handles large data sets well because its time complexity grows in the order of ____ times n.",
        "answer": "log n"
    },
    lambda: {
        "question": "Fill in the blank: The performance of Merge Sort does not depend on the initial order of the ____.",
        "answer": "input"
    },
    lambda: {
        "question": "Fill in the blank: When merging, if one sub-array is exhausted, the remaining elements of the other sub-array are ____ to the result.",
        "answer": "appended"
    },
    lambda: {
        "question": "Fill in the blank: Merge Sort can be implemented using ____ or bottom-up approaches.",
        "answer": "top-down"
    },
    lambda: {
        "question": "Fill in the blank: The extra memory used by Merge Sort is primarily due to the ____ needed during merging.",
        "answer": "temporary arrays"
    }
],

        "NQ": [
    lambda: (lambda n: {
        "question": f"If Merge Sort processes an array of size {n}, how many merge operations occur in total (approximately)?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"Calculate the auxiliary space used by Merge Sort for an array of size {n}.",
        "answer": str(n)
    })(random_choice([10, 20, 40])),
    
    lambda: (lambda n: {
        "question": f"How many comparisons are performed in the worst case when merging two sorted arrays of size {n//2} each in Merge Sort?",
        "answer": str(n - 1)
    })(random_choice([10, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the maximum recursion depth reached by Merge Sort?",
        "answer": str(n.bit_length())
    })(random_choice([8, 16, 64])),
    
    lambda: (lambda n: {
        "question": f"How many total splits occur during Merge Sort on an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"Find the worst-case time complexity of Merge Sort expressed as O(f(n)) where n = {n}. What is f(n)?",
        "answer": f"{n} log {n}"
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"How many sub-arrays are created after the first split of an array of size {n} in Merge Sort?",
        "answer": "2"
    })(random_choice([10, 20, 40])),
    
    lambda: (lambda n: {
        "question": f"For Merge Sort on an array of size {n}, how many times is the merge function called?",
        "answer": str(n - 1)
    })(random_choice([10, 16, 64])),
    
    lambda: (lambda n: {
        "question": f"How many elements will be in the smallest sub-array after recursively splitting an array of size {n}?",
        "answer": "1"
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"What is the approximate total number of comparisons performed during Merge Sort on an array of size {n}?",
        "answer": str(int(n * (n.bit_length() - 1)))
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"How many levels of recursive calls does Merge Sort make for an array of size {n}?",
        "answer": str(n.bit_length())
    })(random_choice([16, 32, 64])),
    
    lambda: (lambda n: {
        "question": f"What is the auxiliary space complexity of Merge Sort for an array of size {n}?",
        "answer": str(n)
    })(random_choice([16, 32, 64])),
    
    lambda: (lambda n: {
        "question": f"During merging in Merge Sort, how many elements at maximum need to be held temporarily for an array of size {n}?",
        "answer": str(n)
    })(random_choice([10, 20, 40])),
    
    lambda: (lambda n: {
        "question": f"How many times is the array divided in Merge Sort before reaching the base case for an array of size {n}?",
        "answer": str(n.bit_length() - 1)
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"How many comparisons are performed when merging two sorted sub-arrays of size {n//4} in Merge Sort?",
        "answer": str((n // 4) * 2 - 1)
    })(random_choice([16, 32, 64])),
    
    lambda: (lambda n: {
        "question": f"For an array of size {n}, what is the minimum number of merge steps needed to get the fully sorted array?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"How many recursive calls does Merge Sort make for an array of size {n}?",
        "answer": str(2 * n - 1)
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"If Merge Sort splits an array of size {n} into halves, how many times must it split to reach arrays of size 1?",
        "answer": str(n.bit_length() - 1)
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"What is the height of the recursion tree for Merge Sort on an array of size {n}?",
        "answer": str(n.bit_length())
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"For Merge Sort, how many extra copies of the original array size {n} might be made during execution?",
        "answer": "1"
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"How many total merge operations occur when sorting an array of size {n} using Merge Sort?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"How many times is the merge operation executed per level in Merge Sort for an array size {n}?",
        "answer": str(n // 2)
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"How many comparisons does Merge Sort make when merging two sorted sub-arrays of size {n//2} each?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"What is the worst-case number of comparisons in Merge Sort for array size {n}?",
        "answer": str(int(n * (n.bit_length() - 1)))
    })(random_choice([8, 16, 32])),
    
    lambda: (lambda n: {
        "question": f"For an array of size {n}, how many merge calls are made excluding the base cases?",
        "answer": str(n - 1)
    })(random_choice([8, 16, 32]))
]

    },

    "level3": {
        "TFQ": [
    lambda: {
        "question": "True or False: Merge Sort uses a divide and conquer strategy by recursively splitting the array until single elements remain.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort requires additional memory space proportional to the input array size during merging.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort has a worst-case time complexity of O(n^2).",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort performs well on linked lists due to its sequential access pattern.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort does not guarantee stability of the sorted output.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort's recursion tree height is proportional to log n, where n is the array size.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort can be implemented without recursion using iterative methods.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort always divides the array into three parts for sorting.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort is more suitable for sorting large datasets than bubble sort.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is an in-place sorting algorithm.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: The merging step in Merge Sort is the only phase that requires linear time.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort can be efficiently parallelized because of its divide and conquer nature.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is rarely used in practical applications due to its high space complexity.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort is stable, meaning equal elements retain their relative order after sorting.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort's time complexity depends on the initial order of the elements.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort can handle large datasets efficiently on external memory devices like disks.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort requires fewer swaps compared to QuickSort.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: The base case in Merge Sort occurs when the array to be sorted has only one element.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is a comparison-based sorting algorithm.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort divides the array until subarrays of size zero are reached.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort can sort a linked list in O(n log n) time without using extra space.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort can perform poorly on already sorted arrays compared to random arrays.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: Merge Sort's space complexity can be optimized to O(1) with a careful implementation.",
        "answer": "False"
    },
    lambda: {
        "question": "True or False: The merge step of Merge Sort combines two sorted arrays into a single sorted array.",
        "answer": "True"
    },
    lambda: {
        "question": "True or False: Merge Sort is slower than Heap Sort in all cases.",
        "answer": "False"
    }
],

        "MCQ": [
    lambda: {
        "question": "What is the worst-case time complexity of Merge Sort?",
        "options": [
            "O(n)",
            "O(n log n)",
            "O(n^2)",
            "O(log n)"
        ],
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "Which of the following best describes the memory usage of Merge Sort?",
        "options": [
            "In-place sorting with O(1) extra space",
            "Uses O(n) extra space for merging",
            "No extra space needed",
            "Uses O(log n) extra space"
        ],
        "answer": "Uses O(n) extra space for merging"
    },
    lambda: {
        "question": "Merge Sort splits the array into how many parts during each recursive call?",
        "options": [
            "Two equal halves",
            "Three equal parts",
            "One part",
            "Variable parts depending on input"
        ],
        "answer": "Two equal halves"
    },
    lambda: {
        "question": "Which property of Merge Sort makes it suitable for sorting linked lists?",
        "options": [
            "Low time complexity",
            "Stability",
            "Sequential access pattern",
            "In-place operation"
        ],
        "answer": "Sequential access pattern"
    },
    lambda: {
        "question": "In the merging process, how does Merge Sort decide which element to place next in the result array?",
        "options": [
            "Select the larger element from the two subarrays",
            "Select the smaller element from the two subarrays",
            "Randomly select elements",
            "Select from the left subarray only"
        ],
        "answer": "Select the smaller element from the two subarrays"
    },
    lambda: {
        "question": "What is the height of the recursion tree in Merge Sort for an array of size n?",
        "options": [
            "O(n)",
            "O(log n)",
            "O(n log n)",
            "O(1)"
        ],
        "answer": "O(log n)"
    },
    lambda: {
        "question": "Why is Merge Sort considered a stable sorting algorithm?",
        "options": [
            "It uses extra space for sorting",
            "Equal elements maintain their relative order",
            "It sorts elements in place",
            "It uses a pivot"
        ],
        "answer": "Equal elements maintain their relative order"
    },
    lambda: {
        "question": "What is the base case for the Merge Sort recursive function?",
        "options": [
            "When array size is zero",
            "When array size is one",
            "When array is sorted",
            "When array size is two"
        ],
        "answer": "When array size is one"
    },
    lambda: {
        "question": "Which of these sorting algorithms generally uses less extra memory than Merge Sort?",
        "options": [
            "QuickSort",
            "HeapSort",
            "BubbleSort",
            "SelectionSort"
        ],
        "answer": "QuickSort"
    },
    lambda: {
        "question": "How does Merge Sort perform on already sorted arrays compared to random arrays?",
        "options": [
            "Faster on sorted arrays",
            "Slower on sorted arrays",
            "Same time complexity in all cases",
            "Fails on sorted arrays"
        ],
        "answer": "Same time complexity in all cases"
    },
    lambda: {
        "question": "What is the main drawback of Merge Sort compared to QuickSort?",
        "options": [
            "Unstable sorting",
            "Higher time complexity",
            "Higher space complexity",
            "Does not work on linked lists"
        ],
        "answer": "Higher space complexity"
    },
    lambda: {
        "question": "Which scenario best describes when Merge Sort is the preferred sorting algorithm?",
        "options": [
            "When in-place sorting is required",
            "When stability is required",
            "When memory is highly constrained",
            "When the input size is very small"
        ],
        "answer": "When stability is required"
    },
    lambda: {
        "question": "How many merge operations are required to fully sort an array of n elements?",
        "options": [
            "n",
            "n-1",
            "log n",
            "2n"
        ],
        "answer": "n-1"
    },
    lambda: {
        "question": "How many subarrays does Merge Sort create after the first split?",
        "options": [
            "1",
            "2",
            "n",
            "log n"
        ],
        "answer": "2"
    },
    lambda: {
        "question": "Which of these sorting algorithms has the same average-case time complexity as Merge Sort?",
        "options": [
            "Bubble Sort",
            "Insertion Sort",
            "QuickSort",
            "Selection Sort"
        ],
        "answer": "QuickSort"
    },
    lambda: {
        "question": "During merging, if both subarrays have the same element, which element does Merge Sort pick first?",
        "options": [
            "From the left subarray",
            "From the right subarray",
            "Randomly from either",
            "It depends on the implementation"
        ],
        "answer": "From the left subarray"
    },
    lambda: {
        "question": "Which of these is NOT a step in the Merge Sort algorithm?",
        "options": [
            "Divide the array",
            "Conquer by recursively sorting",
            "Swap adjacent elements repeatedly",
            "Merge sorted subarrays"
        ],
        "answer": "Swap adjacent elements repeatedly"
    },
    lambda: {
        "question": "What is the time complexity of merging two sorted arrays of size n/2 each?",
        "options": [
            "O(n log n)",
            "O(n^2)",
            "O(n)",
            "O(log n)"
        ],
        "answer": "O(n)"
    },
    lambda: {
        "question": "Merge Sort is particularly efficient on which of the following data structures?",
        "options": [
            "Arrays only",
            "Linked lists only",
            "Both arrays and linked lists",
            "Neither arrays nor linked lists"
        ],
        "answer": "Both arrays and linked lists"
    },
    lambda: {
        "question": "Which characteristic of Merge Sort makes it useful in external sorting (sorting large data sets stored on disk)?",
        "options": [
            "In-place sorting",
            "Stable sorting and sequential access",
            "Random access only",
            "Low auxiliary space"
        ],
        "answer": "Stable sorting and sequential access"
    },
    lambda: {
        "question": "Which step in Merge Sort is responsible for the majority of the work done by the algorithm?",
        "options": [
            "Splitting arrays",
            "Recursion overhead",
            "Merging sorted arrays",
            "Selecting pivots"
        ],
        "answer": "Merging sorted arrays"
    },
    lambda: {
        "question": "How many recursive calls does Merge Sort make for an array of size n?",
        "options": [
            "n",
            "2n - 1",
            "log n",
            "n log n"
        ],
        "answer": "2n - 1"
    },
    lambda: {
        "question": "Which of the following is true about the auxiliary space complexity of Merge Sort?",
        "options": [
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n log n)"
        ],
        "answer": "O(n)"
    },
    lambda: {
        "question": "What is the primary advantage of Merge Sort over QuickSort in worst-case scenarios?",
        "options": [
            "Lower average time complexity",
            "Better worst-case time complexity",
            "Lower space complexity",
            "More cache-friendly"
        ],
        "answer": "Better worst-case time complexity"
    }
],

        "MTQ": [
    lambda: {
        "question": "Match Merge Sort terms with their correct properties (pairs below are incorrect):",
        "pairs": {
            "Best Case": "O(n^2)",
            "Uses": "Stack",
            "Primary Operation": "Swapping"
        },
        "answer": {
            "Best Case": "O(n log n)",
            "Uses": "Recursion",
            "Primary Operation": "Merging"
        }
    },
    lambda: {
        "question": "Match the property of Merge Sort (pairs below are incorrect):",
        "pairs": {
            "Space Complexity": "O(1)",
            "Recursion Depth": "O(n^2)",
            "Algorithm Type": "Greedy"
        },
        "answer": {
            "Space Complexity": "O(n)",
            "Recursion Depth": "O(log n)",
            "Algorithm Type": "Divide and Conquer"
        }
    },
    lambda: {
        "question": "Match the phase of Merge Sort with its characteristic (pairs below are incorrect):",
        "pairs": {
            "Divide Phase": "Combines arrays",
            "Merge Phase": "Splits the array",
            "Base Case": "When array size is 2"
        },
        "answer": {
            "Divide Phase": "Splits the array",
            "Merge Phase": "Combines arrays",
            "Base Case": "When array size is 1"
        }
    },
    lambda: {
        "question": "Match Merge Sort with appropriate features (pairs below are incorrect):",
        "pairs": {
            "Stable": "No",
            "In-place": "Yes",
            "Comparison-based": "No"
        },
        "answer": {
            "Stable": "Yes",
            "In-place": "No",
            "Comparison-based": "Yes"
        }
    },
    lambda: {
        "question": "Match Merge Sort use-cases with reasons (pairs below are incorrect):",
        "pairs": {
            "Linked List": "Bad due to random access",
            "External Sorting": "Not suitable",
            "Multithreading": "Not possible"
        },
        "answer": {
            "Linked List": "Good due to sequential access",
            "External Sorting": "Preferred due to stability",
            "Multithreading": "Easier as subarrays are independent"
        }
    },
    lambda: {
        "question": "Match components of Merge Sort with their purposes (pairs below are incorrect):",
        "pairs": {
            "Merge Function": "Divides array",
            "Recursive Function": "Combines sorted parts",
            "Base Case": "Array length is 10"
        },
        "answer": {
            "Merge Function": "Combines sorted parts",
            "Recursive Function": "Divides array recursively",
            "Base Case": "Array length is 1"
        }
    },
    lambda: {
        "question": "Match Merge Sort terms with their examples (pairs below are incorrect):",
        "pairs": {
            "Divide and Conquer": "Quick access",
            "Stability": "Changes order of equal elements",
            "Auxiliary Space": "O(1)"
        },
        "answer": {
            "Divide and Conquer": "Splitting and merging",
            "Stability": "Maintains relative order",
            "Auxiliary Space": "O(n)"
        }
    },
    lambda: {
        "question": "Match sorting algorithms with Merge Sort features (pairs below are incorrect):",
        "pairs": {
            "Merge Sort": "Unstable and in-place",
            "Quick Sort": "Stable and uses O(n) space",
            "Bubble Sort": "Divide and Conquer"
        },
        "answer": {
            "Merge Sort": "Stable and uses O(n) space",
            "Quick Sort": "Unstable and in-place",
            "Bubble Sort": "Repeated swapping"
        }
    },
    lambda: {
        "question": "Match the sorting scenario with the correct algorithm (pairs below are incorrect):",
        "pairs": {
            "Stable and recursive": "Heap Sort",
            "Unstable and in-place": "Merge Sort",
            "Small input size": "Merge Sort"
        },
        "answer": {
            "Stable and recursive": "Merge Sort",
            "Unstable and in-place": "Quick Sort",
            "Small input size": "Insertion Sort"
        }
    },
    lambda: {
        "question": "Match sorting algorithm with its worst-case time complexity (pairs below are incorrect):",
        "pairs": {
            "Merge Sort": "O(n^2)",
            "Quick Sort": "O(n log n)",
            "Bubble Sort": "O(n)"
        },
        "answer": {
            "Merge Sort": "O(n log n)",
            "Quick Sort": "O(n^2)",
            "Bubble Sort": "O(n^2)"
        }
    },
    lambda: {
        "question": "Match Merge Sort operations with their time complexities (pairs below are incorrect):",
        "pairs": {
            "Splitting array": "O(n^2)",
            "Merging subarrays": "O(log n)",
            "Total sorting": "O(n)"
        },
        "answer": {
            "Splitting array": "O(log n)",
            "Merging subarrays": "O(n)",
            "Total sorting": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match the Merge Sort property with its correct impact (pairs below are incorrect):",
        "pairs": {
            "Stability": "Useful for numeric data only",
            "Extra space": "Saves memory",
            "Time complexity": "Depends on input order"
        },
        "answer": {
            "Stability": "Useful for objects with multiple keys",
            "Extra space": "Uses more memory",
            "Time complexity": "Independent of input order"
        }
    },
    lambda: {
        "question": "Match the algorithm step with its description (pairs below are incorrect):",
        "pairs": {
            "Split": "Join the arrays",
            "Base Case": "Array size is 2",
            "Merge": "Break into halves"
        },
        "answer": {
            "Split": "Break into halves",
            "Base Case": "Array size is 1",
            "Merge": "Join the arrays"
        }
    },
    lambda: {
        "question": "Match Merge Sort stage with array transformation (pairs below are incorrect):",
        "pairs": {
            "Initial": "Sorted array",
            "Middle": "Fully merged array",
            "Final": "Unsorted divided array"
        },
        "answer": {
            "Initial": "Unsorted array",
            "Middle": "Partially sorted subarrays",
            "Final": "Sorted array"
        }
    },
    lambda: {
        "question": "Match input type with Merge Sort behavior (pairs below are incorrect):",
        "pairs": {
            "Sorted Input": "Time complexity reduces",
            "Reverse Input": "Sorts in linear time",
            "Random Input": "Fails to sort"
        },
        "answer": {
            "Sorted Input": "Still O(n log n)",
            "Reverse Input": "Still O(n log n)",
            "Random Input": "Sorted in O(n log n)"
        }
    },
    lambda: {
        "question": "Match Merge Sort property with true/false (pairs below are incorrect):",
        "pairs": {
            "Stable": "False",
            "Divide and Conquer": "False",
            "Uses recursion": "False"
        },
        "answer": {
            "Stable": "True",
            "Divide and Conquer": "True",
            "Uses recursion": "True"
        }
    },
    lambda: {
        "question": "Match algorithm feature with its benefit in Merge Sort (pairs below are incorrect):",
        "pairs": {
            "Parallel Execution": "Hard to achieve",
            "Memory Usage": "Very low",
            "Sorting Order": "Not preserved"
        },
        "answer": {
            "Parallel Execution": "Easy due to independent calls",
            "Memory Usage": "High due to extra array",
            "Sorting Order": "Preserved (stable)"
        }
    },
    lambda: {
        "question": "Match array size to merge sort recursion depth (pairs below are incorrect):",
        "pairs": {
            "Size 16": "Depth 4",
            "Size 8": "Depth 2",
            "Size 32": "Depth 3"
        },
        "answer": {
            "Size 16": "Depth 4",
            "Size 8": "Depth 3",
            "Size 32": "Depth 5"
        }
    },
    lambda: {
        "question": "Match Merge Sort applications with their suitability (pairs below are incorrect):",
        "pairs": {
            "Sorting large files": "Not useful",
            "Linked list sorting": "Very slow",
            "Stable sorting": "Impossible"
        },
        "answer": {
            "Sorting large files": "Very useful",
            "Linked list sorting": "Very efficient",
            "Stable sorting": "Perfect choice"
        }
    },
    lambda: {
        "question": "Match recursion concept in Merge Sort (pairs below are incorrect):",
        "pairs": {
            "Recursive call": "Merging phase",
            "Recursive return": "Divide phase",
            "Base condition": "Array length > 1"
        },
        "answer": {
            "Recursive call": "Divide phase",
            "Recursive return": "Merging phase",
            "Base condition": "Array length <= 1"
        }
    },
    lambda: {
        "question": "Match performance trait of Merge Sort (pairs below are incorrect):",
        "pairs": {
            "Best case": "O(n)",
            "Worst case": "O(n^2)",
            "Average case": "O(log n)"
        },
        "answer": {
            "Best case": "O(n log n)",
            "Worst case": "O(n log n)",
            "Average case": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match the Merge Sort drawback with its explanation (pairs below are incorrect):",
        "pairs": {
            "Slow on small arrays": "Due to pivot selection",
            "High memory usage": "Due to frequent swaps",
            "Hard to implement": "Because of loops"
        },
        "answer": {
            "Slow on small arrays": "Due to recursion overhead",
            "High memory usage": "Due to extra arrays in merge",
            "Hard to implement": "Because of recursive logic"
        }
    }
],

        "ECQ": [
    lambda: {
        "question": "In Merge Sort, the base case of recursion is when the length of array is ____.",
        "answer": "1"
    },
    lambda: {
        "question": "Merge Sort follows the ____ and conquer paradigm.",
        "answer": "divide"
    },
    lambda: {
        "question": "In the merging step, if L[i] <= R[j], then L[i] is placed in the array and ____ is incremented.",
        "answer": "i"
    },
    lambda: {
        "question": "After merging both subarrays, any remaining elements from L or R are added using ____.",
        "answer": "extend"
    },
    lambda: {
        "question": "The overall time complexity of Merge Sort is O(____).",
        "answer": "n log n"
    },
    lambda: {
        "question": "Merge Sort is considered a ____ algorithm because it preserves the relative order of equal elements.",
        "answer": "stable"
    },
    lambda: {
        "question": "Merge Sort is implemented using ____ functions to divide the array.",
        "answer": "recursive"
    },
    lambda: {
        "question": "Merge Sort requires extra ____ for temporary arrays during merging.",
        "answer": "space"
    },
    lambda: {
        "question": "The merge operation compares elements of ____ sorted subarrays.",
        "answer": "two"
    },
    lambda: {
        "question": "To split an array in Merge Sort, we use mid = len(arr) // ____.",
        "answer": "2"
    },
    lambda: {
        "question": "The process of combining sorted arrays is known as the ____ step.",
        "answer": "merge"
    },
    lambda: {
        "question": "If the input array is already sorted, Merge Sort still runs in O(____) time.",
        "answer": "n log n"
    },
    lambda: {
        "question": "During merging, elements are compared using a(n) ____ operation.",
        "answer": "comparison"
    },
    lambda: {
        "question": "Merge Sort is ____ efficient than Quick Sort for small datasets.",
        "answer": "less"
    },
    lambda: {
        "question": "To implement Merge Sort, the input array is recursively split until each subarray contains only ____ element.",
        "answer": "one"
    },
    lambda: {
        "question": "The recursion tree of Merge Sort has a height of log____.",
        "answer": "n"
    },
    lambda: {
        "question": "The number of merge operations required for sorting 16 elements is ____.",
        "answer": "15"
    },
    lambda: {
        "question": "Merge Sort is not considered in-place because it uses additional ____.",
        "answer": "memory"
    },
    lambda: {
        "question": "Merge Sort has a worst-case time complexity of O(n ____ n).",
        "answer": "log"
    },
    lambda: {
        "question": "Merge Sort can be efficiently applied to ____ data structures like linked lists.",
        "answer": "linear"
    },
    lambda: {
        "question": "Merge Sort splits the array, sorts the parts, and then ____ them.",
        "answer": "merges"
    },
    lambda: {
        "question": "In Merge Sort, merging two sorted arrays of total size n takes ____ time.",
        "answer": "O(n)"
    },
    lambda: {
        "question": "The extra space required by Merge Sort for an array of size n is O(____).",
        "answer": "n"
    },
    lambda: {
        "question": "Unlike Quick Sort, Merge Sort always divides the array into two ____ halves.",
        "answer": "equal"
    },
    lambda: {
        "question": "Merge Sort’s performance is not affected by the initial ____ of elements.",
        "answer": "order"
    }
],

        "NQ": [
    lambda: (lambda n: {
        "question": f"For Merge Sort on an array of size {n}, how many recursive calls are made in total?",
        "answer": str(2 * n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"How many comparisons are required to merge two sorted arrays of size {n//2} each?",
        "answer": str(n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"What is the maximum recursion depth of Merge Sort for an array of size {n}?",
        "answer": str(n.bit_length())
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"Total number of split operations Merge Sort performs on array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"How many merge steps are performed during Merge Sort on an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"How many comparisons are done during the second last level of merging in Merge Sort for array of size {n}?",
        "answer": str(n // 2 - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"How many levels of merge operations occur in Merge Sort for array of size {n}?",
        "answer": str(n.bit_length())
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"What is the number of merge calls made for an array of size {n} using Merge Sort (excluding base cases)?",
        "answer": str(n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"What is the total number of elements compared throughout Merge Sort on array of size {n} (approx)?",
        "answer": str(int(n * (n.bit_length() - 1)))
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"Auxiliary space used by Merge Sort on an array of size {n} is ____ units.",
        "answer": str(n)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"Minimum number of comparisons to merge two sorted arrays of size {n//2} each?",
        "answer": str(n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"Total recursive calls at all levels for array of size {n}?",
        "answer": str(2 * n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"In Merge Sort, how many merge operations are required to sort an array of size {n}?",
        "answer": str(n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"What is the number of array accesses needed to perform all merges in Merge Sort of size {n} (approximately)?",
        "answer": str(2 * n * (n.bit_length() - 1))
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"For Merge Sort on array of size {n}, how many total divisions occur before base cases?",
        "answer": str(n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"How many sorted subarrays exist just before the final merge step in Merge Sort of size {n}?",
        "answer": str(2)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"At recursion level 0, Merge Sort performs how many merges on array of size {n}?",
        "answer": str(n // 2)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"In total, how many sorted arrays are generated during the full Merge Sort process for size {n}?",
        "answer": str(2 * n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"During Merge Sort, what is the total number of intermediate arrays created for size {n}?",
        "answer": str(n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"Merge Sort splits an array of size {n} into how many arrays at depth 1?",
        "answer": str(2)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"Merge Sort of array size {n} performs how many comparisons in the best case?",
        "answer": str(int(n * (n.bit_length() - 1)))
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"If Merge Sort is applied to an array of {n} elements, how many total merge function invocations occur?",
        "answer": str(n - 1)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"What is the average number of comparisons in Merge Sort for an array of size {n}?",
        "answer": str(int(n * (n.bit_length() - 1)))
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"How many sub-arrays of size 1 are formed in Merge Sort for an array of size {n}?",
        "answer": str(n)
    })(random_choice([16, 32, 64])),

    lambda: (lambda n: {
        "question": f"How many elements are merged in the final merge operation for array size {n}?",
        "answer": str(n)
    })(random_choice([16, 32, 64]))
]

    }
}

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

    return questions

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
                print("   Given (possibly incorrect) pairs:")
                for k, v in q['pairs'].items():
                    print(f"     {k} -> {v}")
                if isinstance(q['answer'], dict):
                    print("   Correct matching should be:")
                    for k, v in q['answer'].items():
                        print(f"     {k} -> {v}")
            else:
                print(f"Answer: {q['answer']}")
    except Exception as e:
        print("Error:", e)
