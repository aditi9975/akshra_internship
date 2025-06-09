import random

def random_n(min_val=5, max_val=15):
    return random.randint(min_val, max_val)

def random_choice(choices):
    return random.choice(choices)

templates = {
    "level1": {
        "TFQ": [
            lambda: {
                "question": "True or False: Insertion Sort compares each element with the elements before it.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort always needs a temporary array to work.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used to sort strings alphabetically.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is only used for numbers.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is a stable sorting algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is faster than Bubble Sort for small arrays.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort works by dividing the array into sorted and unsorted parts.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort can sort an array in descending order.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort always takes the same time regardless of input order.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not suitable for linked lists.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is an in-place algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used to sort a deck of cards.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is a recursive algorithm by default.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is efficient for sorting a small number of elements.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort always starts sorting from the last element.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used as part of more complex sorting algorithms.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not adaptive to input data.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is easy to implement.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is always faster than Selection Sort.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used for both ascending and descending orders.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not a comparison-based algorithm.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is a good choice for sorting nearly sorted arrays.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used to sort characters in a word.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort always requires O(n^2) time.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not suitable for real-time applications.",
                "answer": "False"
            }
        ],
        "MCQ": [
            lambda: {
                "question": "Which of the following best describes Insertion Sort?",
                "options": [
                    "Sorts by repeatedly inserting elements into a sorted part",
                    "Divides array into halves and sorts recursively",
                    "Swaps adjacent elements until sorted",
                    "Uses a heap to sort elements"
                ],
                "answer": "Sorts by repeatedly inserting elements into a sorted part"
            },
            lambda: {
                "question": "What is the worst-case time complexity of Insertion Sort?",
                "options": ["O(n^2)", "O(n log n)", "O(n)", "O(log n)"],
                "answer": "O(n^2)"
            },
            lambda: {
                "question": "Which of these is a stable sorting algorithm?",
                "options": ["Insertion Sort", "Selection Sort", "Heap Sort", "Quick Sort"],
                "answer": "Insertion Sort"
            },
            lambda: {
                "question": "Which scenario is best for Insertion Sort?",
                "options": [
                    "Array is already sorted",
                    "Array is in reverse order",
                    "Array is random",
                    "Array is very large"
                ],
                "answer": "Array is already sorted"
            },
            lambda: {
                "question": "Which of the following is NOT true about Insertion Sort?",
                "options": [
                    "It is in-place",
                    "It is stable",
                    "It is recursive by default",
                    "It works well for small arrays"
                ],
                "answer": "It is recursive by default"
            },
            lambda: {
                "question": "How does Insertion Sort handle duplicate values?",
                "options": [
                    "Keeps their original order",
                    "Removes duplicates",
                    "Sorts them randomly",
                    "Moves them to the end"
                ],
                "answer": "Keeps their original order"
            },
            lambda: {
                "question": "Which of the following is the first step in Insertion Sort?",
                "options": [
                    "Assume first element is sorted",
                    "Find the minimum element",
                    "Divide array into two halves",
                    "Build a heap"
                ],
                "answer": "Assume first element is sorted"
            },
            lambda: {
                "question": "Which sorting algorithm is most similar to Insertion Sort?",
                "options": [
                    "Bubble Sort",
                    "Merge Sort",
                    "Heap Sort",
                    "Counting Sort"
                ],
                "answer": "Bubble Sort"
            },
            lambda: {
                "question": "What does Insertion Sort do when the array is already sorted?",
                "options": [
                    "Makes minimal comparisons",
                    "Reverses the array",
                    "Performs maximum swaps",
                    "Does not work"
                ],
                "answer": "Makes minimal comparisons"
            },
            lambda: {
                "question": "Which data structure is best suited for Insertion Sort?",
                "options": [
                    "Array",
                    "Stack",
                    "Queue",
                    "Tree"
                ],
                "answer": "Array"
            },
            lambda: {
                "question": "What is the space complexity of Insertion Sort?",
                "options": [
                    "O(1)",
                    "O(n)",
                    "O(log n)",
                    "O(n^2)"
                ],
                "answer": "O(1)"
            },
            lambda: {
                "question": "Which of the following is true about Insertion Sort?",
                "options": [
                    "It sorts in place",
                    "It needs extra memory",
                    "It is always faster than Merge Sort",
                    "It is unstable"
                ],
                "answer": "It sorts in place"
            },
            lambda: {
                "question": "Which of these is NOT a property of Insertion Sort?",
                "options": [
                    "Stable",
                    "In-place",
                    "Adaptive",
                    "Divide and conquer"
                ],
                "answer": "Divide and conquer"
            },
            lambda: {
                "question": "Which loop is used in the main part of Insertion Sort?",
                "options": [
                    "For loop",
                    "While loop",
                    "Do-while loop",
                    "Both for and while"
                ],
                "answer": "Both for and while"
            },
            lambda: {
                "question": "What happens if all elements are equal in Insertion Sort?",
                "options": [
                    "No swaps needed",
                    "Maximum swaps needed",
                    "Algorithm fails",
                    "Elements are reversed"
                ],
                "answer": "No swaps needed"
            },
            lambda: {
                "question": "Which of the following is the best case for Insertion Sort?",
                "options": [
                    "Array is already sorted",
                    "Array is in reverse order",
                    "Array has all unique elements",
                    "Array is empty"
                ],
                "answer": "Array is already sorted"
            },
            lambda: {
                "question": "Which sorting algorithm is NOT stable?",
                "options": [
                    "Selection Sort",
                    "Insertion Sort",
                    "Bubble Sort",
                    "None of the above"
                ],
                "answer": "Selection Sort"
            },
            lambda: {
                "question": "What is the main operation in Insertion Sort?",
                "options": [
                    "Shifting elements",
                    "Swapping elements",
                    "Dividing array",
                    "Merging arrays"
                ],
                "answer": "Shifting elements"
            },
            lambda: {
                "question": "Which of the following is true for Insertion Sort?",
                "options": [
                    "It is simple to implement",
                    "It is always the fastest",
                    "It needs extra space",
                    "It is unstable"
                ],
                "answer": "It is simple to implement"
            },
            lambda: {
                "question": "Which of the following is NOT a use case for Insertion Sort?",
                "options": [
                    "Sorting small arrays",
                    "Sorting nearly sorted arrays",
                    "Sorting large datasets",
                    "Sorting a hand of cards"
                ],
                "answer": "Sorting large datasets"
            },
            lambda: {
                "question": "Which of the following is the correct order of steps in Insertion Sort?",
                "options": [
                    "Pick, compare, shift, insert",
                    "Pick, swap, merge, insert",
                    "Divide, conquer, merge, insert",
                    "Pick, heapify, insert, sort"
                ],
                "answer": "Pick, compare, shift, insert"
            },
            lambda: {
                "question": "Which of the following is NOT a characteristic of Insertion Sort?",
                "options": [
                    "Stable",
                    "Adaptive",
                    "Recursive by default",
                    "In-place"
                ],
                "answer": "Recursive by default"
            },
            lambda: {
                "question": "Which of the following is the average case time complexity of Insertion Sort?",
                "options": [
                    "O(n^2)",
                    "O(n)",
                    "O(log n)",
                    "O(n log n)"
                ],
                "answer": "O(n^2)"
            },
            lambda: {
                "question": "Which of the following is the main advantage of Insertion Sort?",
                "options": [
                    "Simple and efficient for small data",
                    "Works well for large data",
                    "Needs extra memory",
                    "Always faster than Quick Sort"
                ],
                "answer": "Simple and efficient for small data"
            }
        ],
        "MTQ": [
            lambda: {
                "question": "Match the Insertion Sort term to its meaning:",
                "pairs": {
                    "Stable": "Keeps order of equal elements",
                    "In-place": "No extra memory needed",
                    "Adaptive": "Faster for nearly sorted data"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the step to its description in Insertion Sort:",
                "pairs": {
                    "Pick key": "Select next element",
                    "Compare": "Check with sorted part",
                    "Shift": "Move elements to right"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the scenario to the number of comparisons in Insertion Sort:",
                "pairs": {
                    "Best Case": "n-1",
                    "Worst Case": "n(n-1)/2",
                    "Average Case": "About n^2/4"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the property to the sorting algorithm:",
                "pairs": {
                    "Stable": "Insertion Sort",
                    "Not Stable": "Selection Sort",
                    "Divide and Conquer": "Merge Sort"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the loop to its role in Insertion Sort:",
                "pairs": {
                    "Outer loop": "Selects key element",
                    "Inner loop": "Shifts elements",
                    "End": "Inserts key"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the array state to the number of shifts in Insertion Sort:",
                "pairs": {
                    "Already sorted": "0 shifts",
                    "Reverse order": "Maximum shifts",
                    "Random order": "Varies"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its time complexity (worst case):",
                "pairs": {
                    "Insertion Sort": "O(n^2)",
                    "Merge Sort": "O(n log n)",
                    "Bubble Sort": "O(n^2)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its space complexity:",
                "pairs": {
                    "Insertion Sort": "O(1)",
                    "Merge Sort": "O(n)",
                    "Heap Sort": "O(1)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the term to its meaning:",
                "pairs": {
                    "Key": "Element to insert",
                    "Shift": "Move element right",
                    "Insert": "Place key in position"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its adaptiveness:",
                "pairs": {
                    "Insertion Sort": "Adaptive",
                    "Selection Sort": "Not adaptive",
                    "Bubble Sort": "Adaptive"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its stability:",
                "pairs": {
                    "Insertion Sort": "Stable",
                    "Heap Sort": "Not stable",
                    "Bubble Sort": "Stable"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its best use case:",
                "pairs": {
                    "Insertion Sort": "Small or nearly sorted arrays",
                    "Merge Sort": "Large datasets",
                    "Selection Sort": "Small unsorted arrays"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its main operation:",
                "pairs": {
                    "Insertion Sort": "Shifting",
                    "Bubble Sort": "Swapping",
                    "Merge Sort": "Merging"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its implementation style:",
                "pairs": {
                    "Insertion Sort": "Iterative",
                    "Merge Sort": "Recursive",
                    "Heap Sort": "Iterative"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its average case time complexity:",
                "pairs": {
                    "Insertion Sort": "O(n^2)",
                    "Merge Sort": "O(n log n)",
                    "Bubble Sort": "O(n^2)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its extra space requirement:",
                "pairs": {
                    "Insertion Sort": "No extra space",
                    "Merge Sort": "Extra space needed",
                    "Selection Sort": "No extra space"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its sorting order capability:",
                "pairs": {
                    "Insertion Sort": "Ascending or descending",
                    "Counting Sort": "Only ascending",
                    "Bubble Sort": "Ascending or descending"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its main disadvantage:",
                "pairs": {
                    "Insertion Sort": "Slow for large arrays",
                    "Merge Sort": "Needs extra space",
                    "Selection Sort": "Not adaptive"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its best case time complexity:",
                "pairs": {
                    "Insertion Sort": "O(n)",
                    "Bubble Sort": "O(n)",
                    "Selection Sort": "O(n^2)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its use in hybrid algorithms:",
                "pairs": {
                    "Insertion Sort": "Used in TimSort",
                    "Merge Sort": "Used in TimSort",
                    "Heap Sort": "Not used in TimSort"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its comparison type:",
                "pairs": {
                    "Insertion Sort": "Comparison-based",
                    "Counting Sort": "Non-comparison-based",
                    "Bubble Sort": "Comparison-based"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its typical application:",
                "pairs": {
                    "Insertion Sort": "Small datasets",
                    "Merge Sort": "Large datasets",
                    "Selection Sort": "Simple implementations"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its stability property:",
                "pairs": {
                    "Insertion Sort": "Stable",
                    "Heap Sort": "Not stable",
                    "Selection Sort": "Not stable"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its adaptiveness property:",
                "pairs": {
                    "Insertion Sort": "Adaptive",
                    "Selection Sort": "Not adaptive",
                    "Bubble Sort": "Adaptive"
                },
                "answer": "Correct mapping"
            }
        ],
        "ECQ": [
            lambda: {
                "question": "Complete the statement: In Insertion Sort, the key is compared with elements to its ____.",
                "answer": "left"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is best suited for ____ arrays.",
                "answer": "small"
            },
            lambda: {
                "question": "Complete the code: for i in range(1, len(arr)): key = arr[i]; j = i - ____",
                "answer": "1"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is a ____ sorting algorithm.",
                "answer": "stable"
            },
            lambda: {
                "question": "Complete the code: while j >= 0 and arr[j] > key: arr[j + 1] = ____",
                "answer": "arr[j]"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is an ____ algorithm (in-place/out-of-place).",
                "answer": "in-place"
            },
            lambda: {
                "question": "Complete the code: arr[j + 1] = ____",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for nearly sorted arrays.",
                "answer": "efficient"
            },
            lambda: {
                "question": "Complete the code: The outer loop in Insertion Sort runs from 1 to ____.",
                "answer": "len(arr) - 1"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for large datasets.",
                "answer": "slow"
            },
            lambda: {
                "question": "Complete the code: The inner loop in Insertion Sort shifts elements to the ____.",
                "answer": "right"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for sorting a hand of cards.",
                "answer": "ideal"
            },
            lambda: {
                "question": "Complete the code: Insertion Sort can sort in ____ order.",
                "answer": "ascending"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ to implement.",
                "answer": "easy"
            },
            lambda: {
                "question": "Complete the code: Insertion Sort is a ____-based algorithm.",
                "answer": "comparison"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for arrays that are already sorted.",
                "answer": "fast"
            },
            lambda: {
                "question": "Complete the code: Insertion Sort can be used for ____ data types.",
                "answer": "multiple"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for sorting small arrays.",
                "answer": "good"
            },
            lambda: {
                "question": "Complete the code: Insertion Sort is ____ for sorting linked lists.",
                "answer": "suitable"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for sorting large arrays.",
                "answer": "inefficient"
            },
            lambda: {
                "question": "Complete the code: Insertion Sort is ____ for sorting nearly sorted arrays.",
                "answer": "adaptive"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for sorting arrays with few elements.",
                "answer": "efficient"
            },
            lambda: {
                "question": "Complete the code: Insertion Sort is ____ for sorting arrays with many elements.",
                "answer": "slow"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for sorting arrays with duplicate elements.",
                "answer": "stable"
            },
            lambda: {
                "question": "Complete the code: Insertion Sort is ____ for sorting arrays with unique elements.",
                "answer": "simple"
            }
        ],
        "NQ": [
            lambda: (lambda n: {
                "question": f"In the best case, how many comparisons does Insertion Sort make for an array of size {n}?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many comparisons does Insertion Sort make for an array of size {n}?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If an array of {n} elements is already sorted, how many shifts does Insertion Sort perform?",
                "answer": "0"
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If an array of {n} elements is in reverse order, how many shifts does Insertion Sort perform?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the average case, about how many comparisons does Insertion Sort make for {n} elements?",
                "answer": str((n * n) // 4)
            })(random_choice([6, 8, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of {n} elements, what is the minimum number of swaps Insertion Sort can make?",
                "answer": "0"
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of {n} elements in reverse order, what is the maximum number of swaps Insertion Sort can make?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If Insertion Sort is used on an array of {n} elements, what is the maximum number of times the inner loop runs?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the best case, how many times does the inner loop run for {n} elements?",
                "answer": "0"
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If an array of {n} elements is already sorted, how many assignments does Insertion Sort perform?",
                "answer": str(n)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many assignments does Insertion Sort perform for {n} elements?",
                "answer": str((n * (n + 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of {n} elements, what is the maximum number of comparisons in Insertion Sort?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of {n} elements, what is the minimum number of comparisons in Insertion Sort?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the best case, how many total operations (comparisons + shifts) does Insertion Sort perform for {n} elements?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many total operations (comparisons + shifts) does Insertion Sort perform for {n} elements?",
                "answer": str(n * (n - 1))
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If Insertion Sort is used on an array of {n} elements, what is the minimum number of key moves?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If Insertion Sort is used on an array of {n} elements, what is the maximum number of key moves?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the best case, how many times does the key get inserted without shifting in Insertion Sort for {n} elements?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many times does the key get shifted in Insertion Sort for {n} elements?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of {n} elements, what is the minimum number of element moves in Insertion Sort?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of {n} elements, what is the maximum number of element moves in Insertion Sort?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the best case, how many swaps does Insertion Sort make for {n} elements?",
                "answer": "0"
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many swaps does Insertion Sort make for {n} elements?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of {n} elements, what is the minimum number of shifts in Insertion Sort?",
                "answer": "0"
            })(random_choice([5, 6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of {n} elements, what is the maximum number of shifts in Insertion Sort?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9, 10]))
        ]
    },

    "level2": {
        "TFQ": [
            lambda: {
                "question": "True or False: Insertion Sort is a comparison-based sorting algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used to sort linked lists efficiently.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort always requires O(n^2) time, regardless of input.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not stable.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort sorts the array by repeatedly swapping adjacent elements.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is adaptive to nearly sorted data.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be implemented recursively.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is more efficient than Selection Sort for small arrays.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort requires extra space proportional to the input size.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is an in-place algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not suitable for sorting strings.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used for online sorting (sorting as data arrives).",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is faster than Merge Sort for large datasets.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is a stable sorting algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not adaptive.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can sort an array in descending order with minor changes.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is inefficient for large unsorted arrays.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort compares each element with all previous elements.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not a comparison-based algorithm.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used to sort both numbers and strings.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is always faster than Bubble Sort.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is a divide and conquer algorithm.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is suitable for real-time applications with small data.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used for sorting partially sorted arrays efficiently.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used to sort arrays in both ascending and descending order.",
                "answer": "True"
            }
        ],
        "MCQ": [
            lambda: {
                "question": "Which of the following best describes Insertion Sort?",
                "options": [
                    "It inserts each element into its correct position in a sorted subarray.",
                    "It divides the array into halves and sorts them recursively.",
                    "It swaps adjacent elements if they are in the wrong order.",
                    "It selects the minimum element and places it at the beginning."
                ],
                "answer": "It inserts each element into its correct position in a sorted subarray."
            },
            lambda: {
                "question": "What is the average-case time complexity of Insertion Sort?",
                "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
                "answer": "O(n^2)"
            },
            lambda: {
                "question": "Which input will make Insertion Sort perform the least number of comparisons?",
                "options": [
                    "[1, 2, 3, 4, 5]",
                    "[5, 4, 3, 2, 1]",
                    "[2, 1, 3, 5, 4]",
                    "[3, 2, 1, 4, 5]"
                ],
                "answer": "[1, 2, 3, 4, 5]"
            },
            lambda: {
                "question": "Which of the following is NOT a property of Insertion Sort?",
                "options": [
                    "Stable",
                    "In-place",
                    "Divide and conquer",
                    "Adaptive"
                ],
                "answer": "Divide and conquer"
            },
            lambda: {
                "question": "Which sorting algorithm is most similar to Insertion Sort?",
                "options": [
                    "Bubble Sort",
                    "Selection Sort",
                    "Merge Sort",
                    "Quick Sort"
                ],
                "answer": "Bubble Sort"
            },
            lambda: {
                "question": "What happens in the inner loop of Insertion Sort?",
                "options": [
                    "Elements are shifted to make space for the key.",
                    "Elements are swapped randomly.",
                    "The array is divided into two halves.",
                    "No operation is performed."
                ],
                "answer": "Elements are shifted to make space for the key."
            },
            lambda: {
                "question": "Which of the following is true about Insertion Sort?",
                "options": [
                    "It is efficient for small datasets.",
                    "It always requires extra space.",
                    "It is unstable.",
                    "It is recursive by default."
                ],
                "answer": "It is efficient for small datasets."
            },
            lambda: {
                "question": "Which of the following arrays will result in worst-case time complexity for Insertion Sort?",
                "options": [
                    "[1, 2, 3, 4, 5]",
                    "[2, 3, 1, 4, 5]",
                    "[5, 4, 3, 2, 1]",
                    "[3, 1, 2, 4, 5]"
                ],
                "answer": "[5, 4, 3, 2, 1]"
            },
            lambda: {
                "question": "What is the main advantage of Insertion Sort over Selection Sort?",
                "options": [
                    "It is stable.",
                    "It is faster for nearly sorted data.",
                    "It uses less memory.",
                    "It is recursive."
                ],
                "answer": "It is faster for nearly sorted data."
            },
            lambda: {
                "question": "Which of the following is NOT a step in Insertion Sort?",
                "options": [
                    "Pick the next element.",
                    "Compare with elements in the sorted part.",
                    "Shift elements to the right.",
                    "Divide the array into two halves."
                ],
                "answer": "Divide the array into two halves."
            },
            lambda: {
                "question": "Which of the following statements is true?",
                "options": [
                    "Insertion Sort is always faster than Merge Sort.",
                    "Insertion Sort is adaptive.",
                    "Insertion Sort is not stable.",
                    "Insertion Sort requires O(n^2) space."
                ],
                "answer": "Insertion Sort is adaptive."
            },
            lambda: {
                "question": "What is the worst-case time complexity of Insertion Sort?",
                "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
                "answer": "O(n^2)"
            },
            lambda: {
                "question": "Which of the following is a stable sorting algorithm?",
                "options": [
                    "Insertion Sort",
                    "Selection Sort",
                    "Heap Sort",
                    "Quick Sort"
                ],
                "answer": "Insertion Sort"
            },
            lambda: {
                "question": "Which of the following is NOT true about Insertion Sort?",
                "options": [
                    "It is stable.",
                    "It is in-place.",
                    "It is not adaptive.",
                    "It is simple to implement."
                ],
                "answer": "It is not adaptive."
            },
            lambda: {
                "question": "Which of the following is the best case for Insertion Sort?",
                "options": [
                    "Array is already sorted.",
                    "Array is sorted in reverse order.",
                    "Array is randomly ordered.",
                    "Array contains all equal elements."
                ],
                "answer": "Array is already sorted."
            },
            lambda: {
                "question": "What is the minimum number of comparisons Insertion Sort can make?",
                "options": [
                    "n-1",
                    "n",
                    "n^2",
                    "0"
                ],
                "answer": "n-1"
            },
            lambda: {
                "question": "Which of the following is NOT a use case for Insertion Sort?",
                "options": [
                    "Sorting small arrays",
                    "Sorting nearly sorted arrays",
                    "Sorting large random arrays",
                    "Online sorting"
                ],
                "answer": "Sorting large random arrays"
            },
            lambda: {
                "question": "Which of the following is true about the space complexity of Insertion Sort?",
                "options": [
                    "O(1)",
                    "O(n)",
                    "O(n^2)",
                    "O(log n)"
                ],
                "answer": "O(1)"
            },
            lambda: {
                "question": "Which of the following is NOT an advantage of Insertion Sort?",
                "options": [
                    "Simple implementation",
                    "Efficient for small data",
                    "Efficient for large data",
                    "Stable"
                ],
                "answer": "Efficient for large data"
            },
            lambda: {
                "question": "Which of the following statements is false?",
                "options": [
                    "Insertion Sort is stable.",
                    "Insertion Sort is in-place.",
                    "Insertion Sort is adaptive.",
                    "Insertion Sort is always O(n log n)."
                ],
                "answer": "Insertion Sort is always O(n log n)."
            },
            lambda: {
                "question": "Which of the following is the correct order of steps in Insertion Sort?",
                "options": [
                    "Pick, Compare, Shift, Insert",
                    "Divide, Merge, Sort",
                    "Swap, Compare, Insert",
                    "Pick, Swap, Insert"
                ],
                "answer": "Pick, Compare, Shift, Insert"
            },
            lambda: {
                "question": "Which of the following is NOT a characteristic of Insertion Sort?",
                "options": [
                    "Stable",
                    "In-place",
                    "Divide and conquer",
                    "Adaptive"
                ],
                "answer": "Divide and conquer"
            },
            lambda: {
                "question": "Which of the following is the main operation in Insertion Sort?",
                "options": [
                    "Shifting elements",
                    "Swapping elements",
                    "Dividing array",
                    "Merging arrays"
                ],
                "answer": "Shifting elements"
            },
            lambda: {
                "question": "Which of the following is true about Insertion Sort?",
                "options": [
                    "It is efficient for small or nearly sorted arrays.",
                    "It is always faster than Merge Sort.",
                    "It is not stable.",
                    "It requires O(n^2) space."
                ],
                "answer": "It is efficient for small or nearly sorted arrays."
            },
            lambda: {
                "question": "Which of the following is NOT true about Insertion Sort?",
                "options": [
                    "It is stable.",
                    "It is in-place.",
                    "It is not adaptive.",
                    "It is simple to implement."
                ],
                "answer": "It is not adaptive."
            }
        ],
        "MTQ": [
            lambda: {
                "question": "Match the Insertion Sort terms to their meanings:",
                "pairs": {
                    "Stable": "Does not change order of equal elements",
                    "Adaptive": "Efficient for nearly sorted data",
                    "In-place": "Uses constant extra space"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the step to its description in Insertion Sort:",
                "pairs": {
                    "Pick key": "Select next element to insert",
                    "Compare": "Check with sorted part",
                    "Shift": "Move elements to make space"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the complexity to the scenario:",
                "pairs": {
                    "Best Case": "O(n)",
                    "Worst Case": "O(n^2)",
                    "Average Case": "O(n^2)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the property to the algorithm:",
                "pairs": {
                    "Stable": "Insertion Sort",
                    "Not Stable": "Selection Sort",
                    "Divide and Conquer": "Merge Sort"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the array state to the number of shifts in Insertion Sort:",
                "pairs": {
                    "Already Sorted": "Minimum shifts",
                    "Reverse Sorted": "Maximum shifts",
                    "Random": "Average shifts"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its best use case:",
                "pairs": {
                    "Insertion Sort": "Small or nearly sorted arrays",
                    "Merge Sort": "Large datasets",
                    "Heap Sort": "Priority queues"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the loop to its function in Insertion Sort:",
                "pairs": {
                    "Outer Loop": "Selects key element",
                    "Inner Loop": "Shifts elements"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the scenario to the time complexity for Insertion Sort:",
                "pairs": {
                    "Sorted Input": "O(n)",
                    "Reverse Input": "O(n^2)",
                    "Random Input": "O(n^2)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its stability:",
                "pairs": {
                    "Insertion Sort": "Stable",
                    "Heap Sort": "Not Stable",
                    "Bubble Sort": "Stable"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its adaptiveness:",
                "pairs": {
                    "Insertion Sort": "Adaptive",
                    "Selection Sort": "Not Adaptive",
                    "Merge Sort": "Not Adaptive"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the property to the correct statement:",
                "pairs": {
                    "In-place": "Uses no extra space",
                    "Stable": "Keeps equal elements in order",
                    "Adaptive": "Faster for nearly sorted arrays"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its main operation:",
                "pairs": {
                    "Insertion Sort": "Shifting elements",
                    "Bubble Sort": "Swapping adjacent elements",
                    "Merge Sort": "Merging subarrays"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its time complexity in the best case:",
                "pairs": {
                    "Insertion Sort": "O(n)",
                    "Selection Sort": "O(n^2)",
                    "Bubble Sort": "O(n)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its space complexity:",
                "pairs": {
                    "Insertion Sort": "O(1)",
                    "Merge Sort": "O(n)",
                    "Quick Sort": "O(log n)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its typical use case:",
                "pairs": {
                    "Insertion Sort": "Online sorting",
                    "Heap Sort": "Priority queue",
                    "Merge Sort": "External sorting"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its recursive nature:",
                "pairs": {
                    "Insertion Sort": "Can be recursive",
                    "Merge Sort": "Recursive",
                    "Selection Sort": "Usually iterative"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its efficiency for small arrays:",
                "pairs": {
                    "Insertion Sort": "Efficient",
                    "Merge Sort": "Less efficient",
                    "Heap Sort": "Less efficient"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its stability:",
                "pairs": {
                    "Insertion Sort": "Stable",
                    "Quick Sort": "Not Stable",
                    "Bubble Sort": "Stable"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its adaptiveness:",
                "pairs": {
                    "Insertion Sort": "Adaptive",
                    "Heap Sort": "Not Adaptive",
                    "Selection Sort": "Not Adaptive"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its main disadvantage:",
                "pairs": {
                    "Insertion Sort": "Slow for large arrays",
                    "Merge Sort": "Uses extra space",
                    "Heap Sort": "Not stable"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its best case scenario:",
                "pairs": {
                    "Insertion Sort": "Already sorted array",
                    "Selection Sort": "Any array",
                    "Bubble Sort": "Already sorted array"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its worst case scenario:",
                "pairs": {
                    "Insertion Sort": "Reverse sorted array",
                    "Merge Sort": "All cases same",
                    "Heap Sort": "All cases same"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its main operation:",
                "pairs": {
                    "Insertion Sort": "Shifting",
                    "Selection Sort": "Selecting minimum",
                    "Bubble Sort": "Swapping"
                },
                "answer": "Correct mapping"
            }
        ],
        "ECQ": [
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the key is inserted at position ____.",
                "answer": "j + 1"
            },
            lambda: {
                "question": "Complete the code: for i in range(1, len(arr)): key = arr[____]",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: while j >= 0 and arr[j] > key: arr[j + 1] = ____",
                "answer": "arr[j]"
            },
            lambda: {
                "question": "Complete the code: arr[j + 1] = ____",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the outer loop runs from ____ to len(arr)-1.",
                "answer": "1"
            },
            lambda: {
                "question": "Complete the code: while j >= 0 and arr[j] > key: j = ____",
                "answer": "j - 1"
            },
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the inner loop shifts elements ____.",
                "answer": "to the right"
            },
            lambda: {
                "question": "Complete the code: arr[____] = key",
                "answer": "j + 1"
            },
            lambda: {
                "question": "Fill in the blank: The key is compared with elements in the ____ part of the array.",
                "answer": "sorted"
            },
            lambda: {
                "question": "Complete the code: for i in range(1, ____):",
                "answer": "len(arr)"
            },
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the initial sorted part contains ____ element(s).",
                "answer": "one"
            },
            lambda: {
                "question": "Complete the code: key = arr[i]; j = ____",
                "answer": "i - 1"
            },
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, shifting stops when ____.",
                "answer": "arr[j] <= key or j < 0"
            },
            lambda: {
                "question": "Complete the code: while j >= 0 and arr[j] > key: arr[j + 1] = arr[j]; ____",
                "answer": "j -= 1"
            },
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the key is inserted after all ____ elements.",
                "answer": "greater"
            },
            lambda: {
                "question": "Complete the code: arr[j + 1] = ____",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the sorted part grows by ____ element each iteration.",
                "answer": "one"
            },
            lambda: {
                "question": "Complete the code: for i in range(1, len(arr)): ____",
                "answer": "key = arr[i]"
            },
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the key is compared with elements to its ____.",
                "answer": "left"
            },
            lambda: {
                "question": "Complete the code: while j >= 0 and arr[j] > key: ____",
                "answer": "arr[j + 1] = arr[j]"
            },
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the unsorted part becomes ____ after each iteration.",
                "answer": "smaller"
            },
            lambda: {
                "question": "Complete the code: key = arr[i]; j = i - 1; while ____:",
                "answer": "j >= 0 and arr[j] > key"
            },
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the key is placed at ____ position.",
                "answer": "correct"
            },
            lambda: {
                "question": "Complete the code: arr[j + 1] = ____",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the process continues until the array is ____.",
                "answer": "sorted"
            }
        ],
        "NQ": [
            lambda: (lambda n: {
                "question": f"In the best case, how many comparisons does Insertion Sort make for an array of size {n}?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many comparisons does Insertion Sort make for an array of size {n}?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If an array of size {n} is already sorted, how many shifts does Insertion Sort perform?",
                "answer": "0"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If an array of size {n} is reverse sorted, how many shifts does Insertion Sort perform?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In the average case, how many comparisons does Insertion Sort make for {n} elements?",
                "answer": str((n * (n - 1)) // 4)
            })(random_choice([6, 8, 10, 12, 14])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of shifts in Insertion Sort?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of comparisons in Insertion Sort?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In the best case, how many times does the inner loop run for an array of size {n}?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many times does the inner loop run for an array of size {n}?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If an array of size {n} is nearly sorted, will Insertion Sort perform closer to best or worst case?",
                "answer": "Best case"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the time complexity of Insertion Sort in the worst case?",
                "answer": "O(n^2)"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the time complexity of Insertion Sort in the best case?",
                "answer": "O(n)"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If you insert {n} elements one by one into a sorted array, how many comparisons in total?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of swaps in Insertion Sort?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In the best case, how many swaps does Insertion Sort make for an array of size {n}?",
                "answer": "0"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of shifts in Insertion Sort?",
                "answer": "0"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many total element movements (shifts) does Insertion Sort make for {n} elements?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, how many passes does Insertion Sort make?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the first {n-1} elements are sorted and the last is smallest, how many comparisons?",
                "answer": str(n - 1)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of times the key is shifted?",
                "answer": str(n - 1)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In the best case, how many assignments does Insertion Sort make for {n} elements?",
                "answer": str(2 * (n - 1))
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many assignments does Insertion Sort make for {n} elements?",
                "answer": str((n * (n + 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of element movements?",
                "answer": "0"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of element movements?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In the average case, how many shifts does Insertion Sort make for {n} elements?",
                "answer": str((n * (n - 1)) // 4)
            })(random_choice([6, 8, 10, 12, 14]))
        ]
    },

    "level3": {
        "TFQ": [
            lambda: {
                "question": "True or False: Insertion Sort is a comparison-based sorting algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort always requires additional memory proportional to the input size.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used to sort linked lists efficiently.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not adaptive to input data.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is stable and does not change the order of equal elements.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is faster than Merge Sort for large datasets.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be implemented recursively.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort has a quadratic time complexity in the average case.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not suitable for online sorting.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is an in-place algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort can sort a list as it receives new elements.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is always faster than Bubble Sort.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is efficient for sorting small arrays.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not a stable sorting algorithm.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used for sorting strings alphabetically.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort requires the input to be sorted before starting.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used as a subroutine in more complex algorithms.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not adaptive to nearly sorted data.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is a divide and conquer algorithm.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used for real-time sorting applications.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is not suitable for sorting linked lists.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort can sort arrays in descending order with minor changes.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort is always slower than Selection Sort.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Insertion Sort is a non-recursive algorithm by default.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Insertion Sort can be used to sort both numbers and characters.",
                "answer": "True"
            }
        ],
        "MCQ": [
            lambda: {
                "question": "Which property makes Insertion Sort suitable for nearly sorted data?",
                "options": [
                    "Stability",
                    "Adaptiveness",
                    "Divide and conquer",
                    "Recursion"
                ],
                "answer": "Adaptiveness"
            },
            lambda: {
                "question": "What is the average-case time complexity of Insertion Sort?",
                "options": ["O(n)", "O(n^2)", "O(log n)", "O(n log n)"],
                "answer": "O(n^2)"
            },
            lambda: {
                "question": "Which of the following is NOT true about Insertion Sort?",
                "options": [
                    "It is stable",
                    "It is in-place",
                    "It is adaptive",
                    "It requires O(n) extra space"
                ],
                "answer": "It requires O(n) extra space"
            },
            lambda: {
                "question": "Which scenario gives the best performance for Insertion Sort?",
                "options": [
                    "Array is already sorted",
                    "Array is reverse sorted",
                    "Array is random",
                    "Array has all identical elements"
                ],
                "answer": "Array is already sorted"
            },
            lambda: {
                "question": "Which sorting algorithm is most similar to Insertion Sort in terms of implementation?",
                "options": [
                    "Selection Sort",
                    "Bubble Sort",
                    "Merge Sort",
                    "Heap Sort"
                ],
                "answer": "Bubble Sort"
            },
            lambda: {
                "question": "What is the worst-case time complexity of Insertion Sort?",
                "options": ["O(n)", "O(n^2)", "O(log n)", "O(n log n)"],
                "answer": "O(n^2)"
            },
            lambda: {
                "question": "Which of the following is a stable sorting algorithm?",
                "options": [
                    "Heap Sort",
                    "Quick Sort",
                    "Insertion Sort",
                    "Selection Sort"
                ],
                "answer": "Insertion Sort"
            },
            lambda: {
                "question": "What is the main disadvantage of Insertion Sort?",
                "options": [
                    "Requires extra space",
                    "Slow for large datasets",
                    "Not stable",
                    "Not in-place"
                ],
                "answer": "Slow for large datasets"
            },
            lambda: {
                "question": "Which data structure can benefit most from Insertion Sort?",
                "options": [
                    "Array",
                    "Linked List",
                    "Stack",
                    "Queue"
                ],
                "answer": "Linked List"
            },
            lambda: {
                "question": "Which of the following is true about Insertion Sort?",
                "options": [
                    "It is recursive by default",
                    "It is not adaptive",
                    "It is stable",
                    "It requires O(n) extra space"
                ],
                "answer": "It is stable"
            },
            lambda: {
                "question": "Which step is repeated in the inner loop of Insertion Sort?",
                "options": [
                    "Swapping elements",
                    "Shifting elements",
                    "Dividing array",
                    "Merging arrays"
                ],
                "answer": "Shifting elements"
            },
            lambda: {
                "question": "Which of the following is NOT a characteristic of Insertion Sort?",
                "options": [
                    "Stable",
                    "In-place",
                    "Divide and conquer",
                    "Adaptive"
                ],
                "answer": "Divide and conquer"
            },
            lambda: {
                "question": "Which sorting algorithm is best for small datasets?",
                "options": [
                    "Merge Sort",
                    "Heap Sort",
                    "Insertion Sort",
                    "Quick Sort"
                ],
                "answer": "Insertion Sort"
            },
            lambda: {
                "question": "What happens if all elements in the array are equal?",
                "options": [
                    "Best case performance",
                    "Worst case performance",
                    "Average case performance",
                    "Unpredictable"
                ],
                "answer": "Best case performance"
            },
            lambda: {
                "question": "Which of the following is NOT required for Insertion Sort?",
                "options": [
                    "Comparison operator",
                    "Extra array",
                    "Looping",
                    "Shifting"
                ],
                "answer": "Extra array"
            },
            lambda: {
                "question": "Which of the following is the correct order of steps in Insertion Sort?",
                "options": [
                    "Pick, Compare, Shift, Insert",
                    "Compare, Pick, Shift, Insert",
                    "Shift, Pick, Compare, Insert",
                    "Insert, Pick, Compare, Shift"
                ],
                "answer": "Pick, Compare, Shift, Insert"
            },
            lambda: {
                "question": "Which of the following is NOT a use case for Insertion Sort?",
                "options": [
                    "Sorting small arrays",
                    "Sorting nearly sorted arrays",
                    "Sorting large datasets",
                    "Online sorting"
                ],
                "answer": "Sorting large datasets"
            },
            lambda: {
                "question": "Which of the following is true about the stability of Insertion Sort?",
                "options": [
                    "It changes the order of equal elements",
                    "It preserves the order of equal elements",
                    "It is unstable for all cases",
                    "It is only stable for sorted arrays"
                ],
                "answer": "It preserves the order of equal elements"
            },
            lambda: {
                "question": "Which of the following is the correct space complexity of Insertion Sort?",
                "options": [
                    "O(1)",
                    "O(n)",
                    "O(log n)",
                    "O(n^2)"
                ],
                "answer": "O(1)"
            },
            lambda: {
                "question": "Which of the following is NOT a benefit of Insertion Sort?",
                "options": [
                    "Simple implementation",
                    "Efficient for small data",
                    "Efficient for large data",
                    "Stable sorting"
                ],
                "answer": "Efficient for large data"
            },
            lambda: {
                "question": "Which of the following is the best case input for Insertion Sort?",
                "options": [
                    "Sorted array",
                    "Reverse sorted array",
                    "Random array",
                    "Array with duplicates"
                ],
                "answer": "Sorted array"
            },
            lambda: {
                "question": "Which of the following is the correct way to make Insertion Sort sort in descending order?",
                "options": [
                    "Change comparison to <",
                    "Change comparison to >",
                    "Reverse the array before sorting",
                    "Use a stack"
                ],
                "answer": "Change comparison to <"
            },
            lambda: {
                "question": "Which of the following is NOT a limitation of Insertion Sort?",
                "options": [
                    "Inefficient for large datasets",
                    "Not stable",
                    "Quadratic time complexity",
                    "Not suitable for external sorting"
                ],
                "answer": "Not stable"
            },
            lambda: {
                "question": "Which of the following is the correct way to insert an element in Insertion Sort?",
                "options": [
                    "At the beginning",
                    "At the correct position",
                    "At the end",
                    "Randomly"
                ],
                "answer": "At the correct position"
            },
            lambda: {
                "question": "Which of the following is NOT a feature of Insertion Sort?",
                "options": [
                    "Online sorting",
                    "Stable sorting",
                    "Divide and conquer",
                    "In-place sorting"
                ],
                "answer": "Divide and conquer"
            }
        ],
        "MTQ": [
            lambda: {
                "question": "Match the Insertion Sort term to its meaning:",
                "pairs": {
                    "Stable": "Preserves order of equal elements",
                    "Adaptive": "Efficient for nearly sorted data",
                    "In-place": "No extra memory required"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the step to its description in Insertion Sort:",
                "pairs": {
                    "Pick key": "Selects next element to insert",
                    "Compare": "Checks with sorted part",
                    "Shift": "Moves elements to make space"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the scenario to the time complexity for Insertion Sort:",
                "pairs": {
                    "Best Case": "O(n)",
                    "Average Case": "O(n^2)",
                    "Worst Case": "O(n^2)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its property:",
                "pairs": {
                    "Insertion Sort": "Stable and adaptive",
                    "Selection Sort": "Not stable",
                    "Heap Sort": "Not adaptive"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the input type to Insertion Sort performance:",
                "pairs": {
                    "Sorted": "Best case",
                    "Reverse sorted": "Worst case",
                    "Random": "Average case"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the loop to its function in Insertion Sort:",
                "pairs": {
                    "Outer loop": "Selects key element",
                    "Inner loop": "Shifts elements",
                    "Assignment": "Places key in position"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the property to its definition:",
                "pairs": {
                    "Online": "Can sort as data arrives",
                    "Stable": "Order of duplicates preserved",
                    "In-place": "No extra array needed"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its best use case:",
                "pairs": {
                    "Insertion Sort": "Small or nearly sorted arrays",
                    "Merge Sort": "Large datasets",
                    "Heap Sort": "Priority queues"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the complexity to the scenario for Insertion Sort:",
                "pairs": {
                    "O(n)": "Already sorted",
                    "O(n^2)": "Reverse sorted",
                    "O(n^2)": "Random order"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its stability:",
                "pairs": {
                    "Insertion Sort": "Stable",
                    "Quick Sort": "Not stable",
                    "Bubble Sort": "Stable"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the term to its meaning in Insertion Sort:",
                "pairs": {
                    "Key": "Element to insert",
                    "Shift": "Move elements right",
                    "Insert": "Place key in position"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the property to the algorithm:",
                "pairs": {
                    "Adaptive": "Insertion Sort",
                    "Divide and conquer": "Merge Sort",
                    "Heap property": "Heap Sort"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its space complexity:",
                "pairs": {
                    "Insertion Sort": "O(1)",
                    "Merge Sort": "O(n)",
                    "Quick Sort": "O(log n)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its typical use:",
                "pairs": {
                    "Insertion Sort": "Online sorting",
                    "Heap Sort": "Priority queue",
                    "Bubble Sort": "Educational purposes"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the input to the number of shifts in Insertion Sort:",
                "pairs": {
                    "Sorted": "0",
                    "Reverse sorted": "Maximum",
                    "Random": "Varies"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its adaptiveness:",
                "pairs": {
                    "Insertion Sort": "Adaptive",
                    "Selection Sort": "Not adaptive",
                    "Merge Sort": "Not adaptive"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its best case time complexity:",
                "pairs": {
                    "Insertion Sort": "O(n)",
                    "Bubble Sort": "O(n)",
                    "Selection Sort": "O(n^2)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its worst case time complexity:",
                "pairs": {
                    "Insertion Sort": "O(n^2)",
                    "Merge Sort": "O(n log n)",
                    "Heap Sort": "O(n log n)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its stability:",
                "pairs": {
                    "Insertion Sort": "Stable",
                    "Heap Sort": "Not stable",
                    "Selection Sort": "Not stable"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its in-place property:",
                "pairs": {
                    "Insertion Sort": "In-place",
                    "Merge Sort": "Not in-place",
                    "Quick Sort": "In-place"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its online property:",
                "pairs": {
                    "Insertion Sort": "Online",
                    "Merge Sort": "Offline",
                    "Heap Sort": "Offline"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its typical application:",
                "pairs": {
                    "Insertion Sort": "Small datasets",
                    "Merge Sort": "Large datasets",
                    "Heap Sort": "Priority queues"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its main disadvantage:",
                "pairs": {
                    "Insertion Sort": "Slow for large data",
                    "Merge Sort": "Uses extra space",
                    "Heap Sort": "Not stable"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the sorting algorithm to its best case scenario:",
                "pairs": {
                    "Insertion Sort": "Sorted input",
                    "Bubble Sort": "Sorted input",
                    "Selection Sort": "Any input"
                },
                "answer": "Correct mapping"
            }
        ],
        "ECQ": [
            lambda: {
                "question": "Fill in the blank: In Insertion Sort, the key is inserted at index ____.",
                "answer": "j + 1"
            },
            lambda: {
                "question": "Complete the statement: The outer loop in Insertion Sort runs from ____ to len(arr)-1.",
                "answer": "1"
            },
            lambda: {
                "question": "Fill in the blank: The inner loop in Insertion Sort compares key with ____.",
                "answer": "arr[j]"
            },
            lambda: {
                "question": "Complete the code: while j >= 0 and arr[j] > key: arr[j + 1] = ____.",
                "answer": "arr[j]"
            },
            lambda: {
                "question": "Fill in the blank: After shifting, the key is placed at ____.",
                "answer": "arr[j + 1]"
            },
            lambda: {
                "question": "Complete the code: for i in range(1, len(arr)): key = arr[i]; j = ____.",
                "answer": "i - 1"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for small or nearly sorted arrays.",
                "answer": "efficient"
            },
            lambda: {
                "question": "Complete the code: arr[j + 1] = ____ # Place the key",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ and stable.",
                "answer": "in-place"
            },
            lambda: {
                "question": "Complete the code: while j >= 0 and arr[j] > key: ____; j -= 1",
                "answer": "arr[j + 1] = arr[j]"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is best suited for ____ datasets.",
                "answer": "small"
            },
            lambda: {
                "question": "Complete the code: for i in range(1, len(arr)): ____",
                "answer": "key = arr[i]"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for online sorting.",
                "answer": "suitable"
            },
            lambda: {
                "question": "Complete the code: if arr[j] > key: arr[j + 1] = ____",
                "answer": "arr[j]"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for nearly sorted data.",
                "answer": "adaptive"
            },
            lambda: {
                "question": "Complete the code: j = i - 1; while j >= 0 and arr[j] > key: ____",
                "answer": "arr[j + 1] = arr[j]"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for sorting linked lists.",
                "answer": "efficient"
            },
            lambda: {
                "question": "Complete the code: arr[j + 1] = ____ # Insert key",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for large datasets.",
                "answer": "inefficient"
            },
            lambda: {
                "question": "Complete the code: for i in range(1, len(arr)): ____ = arr[i]",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for sorting arrays with few elements.",
                "answer": "fast"
            },
            lambda: {
                "question": "Complete the code: while j >= 0 and arr[j] > key: arr[j + 1] = arr[j]; ____",
                "answer": "j -= 1"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for sorting data as it arrives.",
                "answer": "useful"
            },
            lambda: {
                "question": "Complete the code: arr[j + 1] = ____ # Place key in correct position",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: Insertion Sort is ____ for sorting small lists.",
                "answer": "ideal"
            }
        ],
        "NQ": [
            lambda: (lambda n: {
                "question": f"In the best case, how many comparisons does Insertion Sort make for an array of size {n}?",
                "answer": str(n - 1)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many comparisons does Insertion Sort make for {n} elements?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([7, 8, 9, 10, 12])),
            lambda: (lambda n: {
                "question": f"How many shifts are required in Insertion Sort for a reverse sorted array of size {n}?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the best case, how many shifts does Insertion Sort perform for an array of size {n}?",
                "answer": "0"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of element moves in Insertion Sort?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([7, 8, 9, 10, 12])),
            lambda: (lambda n: {
                "question": f"How many comparisons are made in Insertion Sort if the array is already sorted and has {n} elements?",
                "answer": str(n - 1)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many times does the inner loop execute for an array of size {n}?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([7, 8, 9, 10, 12])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the minimum number of shifts in Insertion Sort?",
                "answer": "0"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"How many passes does Insertion Sort make through an array of size {n}?",
                "answer": str(n - 1)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the best case, how many assignments does Insertion Sort perform for {n} elements?",
                "answer": str(n)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many assignments does Insertion Sort perform for {n} elements?",
                "answer": str((n * (n + 1)) // 2)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"How many times is the key variable assigned in Insertion Sort for an array of size {n}?",
                "answer": str(n - 1)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the maximum number of swaps in Insertion Sort?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the best case, how many times does the inner loop run in Insertion Sort for {n} elements?",
                "answer": str(n - 1)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"How many elements are compared in the first pass of Insertion Sort for an array of size {n}?",
                "answer": "1"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the second pass of Insertion Sort for an array of size {n}, how many comparisons are made?",
                "answer": "2"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the third pass of Insertion Sort for an array of size {n}, how many comparisons are made?",
                "answer": "3"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many total comparisons are made in Insertion Sort for {n} elements?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([7, 8, 9, 10, 12])),
            lambda: (lambda n: {
                "question": f"In the best case, how many total shifts are made in Insertion Sort for {n} elements?",
                "answer": "0"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the number of times the outer loop runs in Insertion Sort?",
                "answer": str(n - 1)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many times is the key compared in Insertion Sort for {n} elements?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([7, 8, 9, 10, 12])),
            lambda: (lambda n: {
                "question": f"In the best case, how many times is the key compared in Insertion Sort for {n} elements?",
                "answer": str(n - 1)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"For an array of size {n}, what is the number of times the inner loop is skipped in the best case?",
                "answer": str(n - 1)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"In the worst case, how many total element moves are made in Insertion Sort for {n} elements?",
                "answer": str((n * (n - 1)) // 2)
            })(random_choice([7, 8, 9, 10, 12]))
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
                for k, v in q['pairs'].items():
                    print(f"   {k}  ->  {v}")
            print(f"Answer: {q['answer']}")
    except Exception as e:
        print("Error:", e)
