import random
import json

QUESTION_TYPES = ["TFQ", "MCQ", "MTQ", "ECQ", "EXPQ"]
LEVELS = {
    "1": "Foundational",
    "2": "Intermediate",
    "3": "Advanced"
}

def generate_array1():
    import random
    size = random.randint(4, 7)
    return [random.randint(1, 20) for _ in range(size)]

# ------------------------------------------
# Template banks for Level 1 – Foundational
# ------------------------------------------
level_1 = {
    "TFQ": [
        lambda: {"question": "Bubble Sort compares and swaps adjacent elements. (True/False)", "answer": "True"},
        lambda: {"question": f"Bubble Sort sorts this array in one pass: {generate_array1()} (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort always takes the same number of passes regardless of input. (True/False)", "answer": "False"},
        lambda: {"question": "In Bubble Sort, a sorted region grows from the end. (True/False)", "answer": "True"},
        lambda: {"question": "The best-case time complexity of Bubble Sort is O(n). (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort always makes at least one swap in every pass. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort can sort a list in descending order by simply reversing the comparison operator. (True/False)", "answer": "True"},
        lambda: {"question": "The term \"Bubble\" in Bubble Sort refers to the smallest element bubbling to the top. (True/False)", "answer": "False"},
        lambda: {"question": "In Bubble Sort, comparisons are made only between adjacent elements. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort works only with integer values. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort modifies the original array in-place. (True/False)", "answer": "True"},
        lambda: {"question": "The worst-case time complexity of Bubble Sort is O(n). (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort can terminate early if no swaps occur in a pass. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is more efficient than Merge Sort in large datasets. (True/False)", "answer": "False"},
        lambda: {"question": "In Bubble Sort, the number of passes is always equal to the number of elements. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort is a stable sorting algorithm. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort does not require any additional memory. (True/False)", "answer": "True"},
        lambda: {"question": "In Bubble Sort, the last element is always compared twice in a pass. (True/False)", "answer": "False"},
        lambda: {"question": "The inner loop in Bubble Sort decreases in size each pass. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort uses divide and conquer technique. (True/False)", "answer": "False"},
        lambda: {"question": "If the array is already sorted, Bubble Sort still performs all passes. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort swaps elements that are not in correct order. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is not suitable for real-time applications. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort has a time complexity of O(n^2) in average case. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is the fastest sorting algorithm. (True/False)", "answer": "False"}
    ],

    "MCQ": [
        lambda: {
            "question": "What does Bubble Sort primarily use for sorting?",
            "options": ["Divide and Conquer", "Recursion", "Adjacent comparisons", "Heaps"],
            "answer": "Adjacent comparisons"
        },
        lambda: {
            "question": "Which of the following is true about Bubble Sort?",
            "options": ["It is not stable", "It is space inefficient", "It always uses recursion", "It is a stable sort"],
            "answer": "It is a stable sort"
        },
        lambda: {
            "question": "In Bubble Sort, where does the largest element end up after the first pass?",
            "options": ["Start", "Middle", "End", "Unchanged"],
            "answer": "End"
        },
        lambda: {
            "question": "What type of algorithm is Bubble Sort?",
            "options": ["Divide-and-Conquer", "Greedy", "Backtracking", "Comparison-based"],
            "answer": "Comparison-based"
        },
        lambda: {
            "question": "Bubble Sort is classified as which type of sorting algorithm?",
            "options": ["Selection Sort", "Exchange Sort", "Insertion Sort", "Quick Sort"],
            "answer": "Exchange Sort"
        },
        lambda: {
            "question": "What is the best case time complexity of Bubble Sort?",
            "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
            "answer": "O(n)"
        },
        lambda: {
            "question": "How does Bubble Sort detect that the list is already sorted?",
            "options": ["By checking for no swaps in a pass", "By counting comparisons", "Using recursion", "Using a secondary array"],
            "answer": "By checking for no swaps in a pass"
        },
        lambda: {
            "question": "Which part of Bubble Sort shrinks after each pass?",
            "options": ["Sorted region", "Unsorted region", "Number of elements", "Number of comparisons"],
            "answer": "Unsorted region"
        },
        lambda: {
            "question": "Which of these is an advantage of Bubble Sort?",
            "options": ["Simple to implement", "Efficient for large data", "Uses extra memory", "Fastest algorithm"],
            "answer": "Simple to implement"
        },
        lambda: {
            "question": "What happens in Bubble Sort when two adjacent elements are in correct order?",
            "options": ["They are swapped", "No action is taken", "They are removed", "Algorithm terminates"],
            "answer": "No action is taken"
        },
        lambda: {
            "question": "What is the space complexity of Bubble Sort?",
            "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
            "answer": "O(1)"
        },
        lambda: {
            "question": "What does Bubble Sort rely on to rearrange elements?",
            "options": ["Swapping adjacent elements", "Dividing array", "Using pivot", "Creating sublists"],
            "answer": "Swapping adjacent elements"
        },
        lambda: {
            "question": "How many passes are needed in the worst case for Bubble Sort on an array of size n?",
            "options": ["n", "n-1", "n/2", "log n"],
            "answer": "n-1"
        },
        lambda: {
            "question": "What is the primary characteristic of a stable sorting algorithm like Bubble Sort?",
            "options": ["Maintains relative order of equal elements", "Sorts faster", "Uses less memory", "Works only on integers"],
            "answer": "Maintains relative order of equal elements"
        },
        lambda: {
            "question": "Which element does Bubble Sort 'bubble' to its correct position in each pass?",
            "options": ["Largest unsorted element", "Smallest unsorted element", "Middle element", "Random element"],
            "answer": "Largest unsorted element"
        },
        lambda: {
            "question": "What happens if all elements in the array are equal?",
            "options": ["No swaps occur", "Multiple swaps occur", "Algorithm crashes", "Algorithm restarts"],
            "answer": "No swaps occur"
        },
        lambda: {
            "question": "Can Bubble Sort be used for sorting strings?",
            "options": ["Yes, by comparing ASCII values", "No", "Only with integers", "Only with floats"],
            "answer": "Yes, by comparing ASCII values"
        },
        lambda: {
            "question": "What happens to the inner loop size after each pass in Bubble Sort?",
            "options": ["Decreases", "Increases", "Stays the same", "Becomes zero"],
            "answer": "Decreases"
        },
        lambda: {
            "question": "Which sorting algorithm is generally faster than Bubble Sort?",
            "options": ["Merge Sort", "Selection Sort", "Bubble Sort itself", "Insertion Sort"],
            "answer": "Merge Sort"
        },
        lambda: {
            "question": "What does 'in-place' sorting mean in Bubble Sort?",
            "options": ["Sorting without extra space", "Sorting using extra memory", "Sorting in multiple arrays", "Sorting with recursion"],
            "answer": "Sorting without extra space"
        },
        lambda: {
            "question": "Which case of Bubble Sort is when the array is already sorted?",
            "options": ["Best case", "Worst case", "Average case", "Random case"],
            "answer": "Best case"
        },
        lambda: {
            "question": "Which loop in Bubble Sort is responsible for comparing adjacent elements?",
            "options": ["Inner loop", "Outer loop", "Both loops", "Neither loop"],
            "answer": "Inner loop"
        },
        lambda: {
            "question": "What kind of data structure is Bubble Sort mainly applied to?",
            "options": ["Arrays", "Trees", "Graphs", "Linked Lists"],
            "answer": "Arrays"
        },
        lambda: {
            "question": "How does Bubble Sort behave with nearly sorted arrays?",
            "options": ["Runs faster", "Runs slower", "Runs the same", "Fails to sort"],
            "answer": "Runs faster"
        },
        lambda: {
            "question": "Is Bubble Sort adaptive (can it detect sorted arrays to stop early)?",
            "options": ["Yes", "No", "Sometimes", "Depends on implementation"],
            "answer": "Yes"
        }
    ],

    "MTQ": [
        lambda: {
            "question": "Match the terms with Bubble Sort concepts:\n1. Pass\n2. Swap\n3. Sorted Region\n4. Unsorted Region",
            "pairs": {
                "1": "One complete iteration over the array",
                "2": "Exchange two adjacent elements",
                "3": "Section confirmed in order",
                "4": "Part yet to be sorted"
            },
            "answer": "1->One complete iteration over the array, 2->Exchange two adjacent elements, 3->Section confirmed in order, 4->Part yet to be sorted"
        },
        lambda: {
            "question": "Match Bubble Sort terms:\n1. Stability\n2. Optimization\n3. Worst case\n4. Space usage",
            "pairs": {
                "1": "Preserves original order",
                "2": "Stop early if no swaps",
                "3": "Reversed array",
                "4": "In-place algorithm"
            },
            "answer": "1->Preserves original order, 2->Stop early if no swaps, 3->Reversed array, 4->In-place algorithm"
        },
        lambda: {
            "question": "Match the sorting concepts:\n1. Stable sort\n2. In-place\n3. Pass\n4. Swap",
            "pairs": {
                "1": "Maintains order of equal elements",
                "2": "Does not require extra memory",
                "3": "Complete iteration through array",
                "4": "Exchange of adjacent elements"
            },
            "answer": "1->Maintains order of equal elements, 2->Does not require extra memory, 3->Complete iteration through array, 4->Exchange of adjacent elements"
        },
        lambda: {
            "question": "Match the following:\n1. Inner loop\n2. Outer loop\n3. Early termination\n4. Time complexity",
            "pairs": {
                "1": "Compares adjacent elements",
                "2": "Controls passes",
                "3": "Stops if no swaps",
                "4": "O(n^2) average case"
            },
            "answer": "1->Compares adjacent elements, 2->Controls passes, 3->Stops if no swaps, 4->O(n^2) average case"
        },
        lambda: {
            "question": "Match terms:\n1. Best case\n2. Worst case\n3. Average case\n4. Space complexity",
            "pairs": {
                "1": "Array already sorted",
                "2": "Array reversed",
                "3": "Random order",
                "4": "O(1)"
            },
            "answer": "1->Array already sorted, 2->Array reversed, 3->Random order, 4->O(1)"
        },
        lambda: {
            "question": "Match the steps of Bubble Sort:\n1. Compare\n2. Swap\n3. Pass\n4. Sorted region",
            "pairs": {
                "1": "Check adjacent elements",
                "2": "Exchange if needed",
                "3": "Complete iteration",
                "4": "Portion sorted"
            },
            "answer": "1->Check adjacent elements, 2->Exchange if needed, 3->Complete iteration, 4->Portion sorted"
        },
        lambda: {
            "question": "Match these terms:\n1. Adaptive\n2. Stable\n3. In-place\n4. Iteration",
            "pairs": {
                "1": "Stops early if sorted",
                "2": "Maintains relative order",
                "3": "Uses no extra space",
                "4": "Repeats over array"
            },
            "answer": "1->Stops early if sorted, 2->Maintains relative order, 3->Uses no extra space, 4->Repeats over array"
        },
        lambda: {
            "question": "Match Bubble Sort characteristics:\n1. Time complexity\n2. Space complexity\n3. Stability\n4. Optimization",
            "pairs": {
                "1": "O(n^2) average case",
                "2": "O(1)",
                "3": "Stable",
                "4": "Early termination"
            },
            "answer": "1->O(n^2) average case, 2->O(1), 3->Stable, 4->Early termination"
        },
        lambda: {
            "question": "Match the following array conditions:\n1. Sorted\n2. Reverse sorted\n3. Random\n4. Nearly sorted",
            "pairs": {
                "1": "Best case",
                "2": "Worst case",
                "3": "Average case",
                "4": "Runs faster"
            },
            "answer": "1->Best case, 2->Worst case, 3->Average case, 4->Runs faster"
        },
        lambda: {
            "question": "Match terms:\n1. Outer loop\n2. Inner loop\n3. Swap\n4. Pass",
            "pairs": {
                "1": "Controls passes",
                "2": "Compares adjacent",
                "3": "Exchange elements",
                "4": "One iteration"
            },
            "answer": "1->Controls passes, 2->Compares adjacent, 3->Exchange elements, 4->One iteration"
        },
       
        lambda: {
            "question": "Match the Bubble Sort terms:\n1. Early stop\n2. Pass count\n3. Element comparison\n4. Sorting stability",
            "pairs": {
                "1": "Optimization to stop if sorted",
                "2": "Number of passes in worst case",
                "3": "Compare adjacent elements",
                "4": "Preserves equal element order"
            },
            "answer": "1->Optimization to stop if sorted, 2->Number of passes in worst case, 3->Compare adjacent elements, 4->Preserves equal element order"
        },
        lambda: {
            "question": "Match the algorithm features:\n1. Adaptive\n2. Stable\n3. In-place\n4. Iterative",
            "pairs": {
                "1": "Can stop early",
                "2": "Preserves order",
                "3": "Sorts without extra memory",
                "4": "Uses loops"
            },
            "answer": "1->Can stop early, 2->Preserves order, 3->Sorts without extra memory, 4->Uses loops"
        },
        lambda: {
            "question": "Match the Bubble Sort terminology:\n1. Swap\n2. Sorted section\n3. Pass\n4. Inner loop",
            "pairs": {
                "1": "Exchange adjacent elements",
                "2": "Confirmed sorted part",
                "3": "Complete iteration",
                "4": "Compare adjacent elements"
            },
            "answer": "1->Exchange adjacent elements, 2->Confirmed sorted part, 3->Complete iteration, 4->Compare adjacent elements"
        },
        lambda: {
            "question": "Match the complexity terms:\n1. Best case\n2. Average case\n3. Worst case\n4. Space complexity",
            "pairs": {
                "1": "O(n)",
                "2": "O(n^2)",
                "3": "O(n^2)",
                "4": "O(1)"
            },
            "answer": "1->O(n), 2->O(n^2), 3->O(n^2), 4->O(1)"
        },
        lambda: {
            "question": "Match the sorting outcomes:\n1. Sorted array\n2. Unsorted array\n3. Nearly sorted array\n4. Reverse sorted array",
            "pairs": {
                "1": "Best case",
                "2": "Average case",
                "3": "Runs faster",
                "4": "Worst case"
            },
            "answer": "1->Best case, 2->Average case, 3->Runs faster, 4->Worst case"
        },
        lambda: {
            "question": "Match the Bubble Sort components:\n1. Outer loop\n2. Inner loop\n3. Swap\n4. Optimization",
            "pairs": {
                "1": "Controls passes",
                "2": "Compares elements",
                "3": "Exchange adjacent",
                "4": "Early termination"
            },
            "answer": "1->Controls passes, 2->Compares elements, 3->Exchange adjacent, 4->Early termination"
        },
        lambda: {
            "question": "Match the following:\n1. Stable sort\n2. Adaptive\n3. In-place\n4. Complexity",
            "pairs": {
                "1": "Preserves equal elements order",
                "2": "Stops early if sorted",
                "3": "Uses constant space",
                "4": "O(n^2)"
            },
            "answer": "1->Preserves equal elements order, 2->Stops early if sorted, 3->Uses constant space, 4->O(n^2)"
        },
        lambda: {
            "question": "Match the sorting phases:\n1. Compare\n2. Swap\n3. Pass\n4. Sorted region",
            "pairs": {
                "1": "Check adjacent elements",
                "2": "Exchange if needed",
                "3": "Complete iteration",
                "4": "Confirmed sorted part"
            },
            "answer": "1->Check adjacent elements, 2->Exchange if needed, 3->Complete iteration, 4->Confirmed sorted part"
        },
        lambda: {
            "question": "Match these terms:\n1. Inner loop\n2. Outer loop\n3. Early stop\n4. Time complexity",
            "pairs": {
                "1": "Compares adjacent",
                "2": "Controls passes",
                "3": "Stops if no swaps",
                "4": "O(n^2) average case"
            },
            "answer": "1->Compares adjacent, 2->Controls passes, 3->Stops if no swaps, 4->O(n^2) average case"
        }
    ],

    "ECQ": [
        lambda: {"question": "Explain why Bubble Sort is called a 'stable' sorting algorithm.", "answer": "Because it maintains the relative order of equal elements."},
        lambda: {"question": "Describe the worst-case time complexity of Bubble Sort.", "answer": "The worst-case time complexity is O(n^2) when the array is reverse sorted."},
        lambda: {"question": "How does Bubble Sort optimize to stop early?", "answer": "If no swaps occur during a pass, it stops early as the array is sorted."},
        lambda: {"question": "What is the space complexity of Bubble Sort and why?", "answer": "O(1) because it sorts the array in-place without extra memory."},
        lambda: {"question": "Why is Bubble Sort inefficient for large datasets?", "answer": "Because it repeatedly compares and swaps adjacent elements, leading to O(n^2) time complexity."},
        lambda: {"question": "Explain how Bubble Sort progresses after each pass.", "answer": "After each pass, the largest unsorted element bubbles to its correct position at the end."},
        lambda: {"question": "What type of algorithm is Bubble Sort and what is its primary method?", "answer": "It is a comparison-based exchange sort that swaps adjacent elements."},
        lambda: {"question": "Why does the inner loop reduce in size after each pass?", "answer": "Because the largest elements settle at the end and no longer need comparison."},
        lambda: {"question": "Explain the significance of the 'swap' operation in Bubble Sort.", "answer": "Swapping moves elements towards their sorted position by exchanging adjacent out-of-order elements."},
        lambda: {"question": "How does Bubble Sort maintain the order of equal elements?", "answer": "It doesn't swap elements that are equal, preserving their original order."},
        lambda: {"question": "Describe the best-case input for Bubble Sort.", "answer": "An already sorted array where no swaps occur."},
        lambda: {"question": "What role does the outer loop play in Bubble Sort?", "answer": "It controls the number of passes needed to fully sort the array."},
        lambda: {"question": "How can Bubble Sort be modified to sort in descending order?", "answer": "By reversing the comparison operator during adjacent comparisons."},
        lambda: {"question": "Why is Bubble Sort considered simple to implement?", "answer": "Because it uses simple loops and swapping adjacent elements without complex data structures."},
        lambda: {"question": "Explain the trade-off between Bubble Sort’s simplicity and efficiency.", "answer": "While easy to implement, it is inefficient for large data due to high time complexity."},
        lambda: {"question": "What happens if Bubble Sort is applied on an empty array?", "answer": "It simply does nothing as there are no elements to sort."},
        lambda: {"question": "Why is Bubble Sort rarely used in practical applications?", "answer": "Due to its poor performance compared to more efficient algorithms like QuickSort or MergeSort."},
        lambda: {"question": "Explain what 'in-place' sorting means in Bubble Sort.", "answer": "Sorting done by modifying the original array without using extra space."},
        lambda: {"question": "How does Bubble Sort behave on a nearly sorted array?", "answer": "It performs better because fewer swaps and passes are needed."},
        lambda: {"question": "What is the significance of the 'pass' in Bubble Sort?", "answer": "A pass is one complete iteration of comparisons and possible swaps over the array."},
        lambda: {"question": "Explain the difference between Bubble Sort and Selection Sort.", "answer": "Bubble Sort swaps adjacent elements, Selection Sort finds min/max and swaps with fixed position."},
        lambda: {"question": "What happens when two adjacent elements are equal in Bubble Sort?", "answer": "No swap occurs, preserving their order."},
        lambda: {"question": "Why can Bubble Sort be considered adaptive?", "answer": "Because it can terminate early if the array is already sorted."},
        lambda: {"question": "Explain how Bubble Sort is related to Exchange Sorts.", "answer": "Bubble Sort is a type of exchange sort because it swaps elements to sort the array."},
        lambda: {"question": "Describe how Bubble Sort can be visualized.", "answer": "As the largest unsorted element 'bubbles' up to the end after each pass."}
    ],

    "EXPQ": [
        lambda: {"question": "Complete the expression: Bubble Sort repeatedly compares and ______ adjacent elements.", "answer": "swaps"},
        lambda: {"question": "Fill in the blank: The time complexity of Bubble Sort in the best case is ______.", "answer": "O(n)"},
        lambda: {"question": "Complete the sentence: Bubble Sort is considered a ______ sorting algorithm because it swaps elements in-place.", "answer": "stable"},
        lambda: {"question": "Fill the blank: After each pass in Bubble Sort, the ______ element is placed at its correct position.", "answer": "largest"},
        lambda: {"question": "Complete the statement: Bubble Sort terminates early if during a pass, no ______ are made.", "answer": "swaps"},
        lambda: {"question": "Fill in: Bubble Sort’s inner loop compares elements at indices i and i+______.", "answer": "1"},
        lambda: {"question": "Complete: The outer loop in Bubble Sort runs for a maximum of ______ passes.", "answer": "n-1"},
        lambda: {"question": "Fill in: Bubble Sort’s space complexity is ______ because it sorts the array without extra storage.", "answer": "O(1)"},
        lambda: {"question": "Complete: Bubble Sort is inefficient for large arrays due to its ______ time complexity.", "answer": "quadratic"},
        lambda: {"question": "Fill the blank: Bubble Sort sorts elements by repeatedly ______ the larger elements to the end.", "answer": "bubbling"},
        lambda: {"question": "Complete: The process of swapping two adjacent elements in Bubble Sort is called a ______.", "answer": "swap"},
        lambda: {"question": "Fill in: Bubble Sort can be optimized by adding a flag to detect if any ______ happened.", "answer": "swaps"},
        lambda: {"question": "Complete: Bubble Sort works by comparing adjacent elements and swapping them if they are in the wrong ______.", "answer": "order"},
        lambda: {"question": "Fill the blank: The best case for Bubble Sort occurs when the array is already ______.", "answer": "sorted"},
        lambda: {"question": "Complete: Bubble Sort is a ______ sorting algorithm that compares pairs of elements.", "answer": "comparison-based"},
        lambda: {"question": "Fill in: Bubble Sort is also called an exchange sort because it exchanges ______ elements.", "answer": "adjacent"},
        lambda: {"question": "Complete: After each pass, Bubble Sort reduces the number of elements it needs to ______.", "answer": "check"},
        lambda: {"question": "Fill the blank: Bubble Sort’s time complexity is worst when the array is ______ sorted.", "answer": "reverse"},
        lambda: {"question": "Complete: The number of passes Bubble Sort takes in the worst case is ______.", "answer": "n-1"},
        lambda: {"question": "Fill in: Bubble Sort’s algorithm is ______ because it only uses loops, not recursion.", "answer": "iterative"},
        lambda: {"question": "Complete: Bubble Sort’s swapping operation moves the ______ elements toward the end.", "answer": "largest"},
        lambda: {"question": "Fill the blank: Bubble Sort is rarely used in practice because it is not ______.", "answer": "efficient"},
        lambda: {"question": "Complete: Bubble Sort’s inner loop compares elements up to the ______ sorted region.", "answer": "unsorted"},
        lambda: {"question": "Fill in: Bubble Sort is suitable for small datasets because of its ______ implementation.", "answer": "simple"},
        lambda: {"question": "Complete: Bubble Sort checks adjacent pairs and swaps if the left is ______ than the right.", "answer": "greater"}
    ]
}



# ------------------------------------------
# Template banks for Level 2 – Intermediate
# ------------------------------------------


def generate_array2(min_len=5, max_len=9, min_val=1, max_val=50):
    length = random.randint(min_len, max_len)
    return [random.randint(min_val, max_val) for _ in range(length)]

level_2 = {
    "TFQ": [
        lambda: {"question": "Average-case time complexity of Bubble Sort is O(n^2). (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort always uses additional memory. (True/False)", "answer": "False"},
        lambda: {"question": "Optimized Bubble Sort stops early if no swaps happen in a pass. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is unstable. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort's space complexity is O(1). (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort has the same average and worst-case time complexity. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort requires additional memory proportional to the input size. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort always performs exactly n-1 passes. (True/False)", "answer": "False"},
        lambda: {"question": "In the best-case scenario, Bubble Sort can perform in O(n) time. (True/False)", "answer": "True"},
        lambda: {"question": "A single misplaced element at the start can delay sorting in Bubble Sort. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort uses recursion internally. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort can be optimized by ignoring the last sorted elements in each pass. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is an example of a divide-and-conquer algorithm. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort is always the best choice for sorting small lists. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort does not maintain the input order of equal elements. (True/False)", "answer": "False"},
        lambda: {"question": "Each pass in Bubble Sort pushes the largest unsorted element to the end. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort compares adjacent elements during sorting. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort can handle negative numbers without modifications. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort can detect sorted arrays and stop early if optimized. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort always requires n passes to sort any list. (True/False)", "answer": "False"},
        lambda: {"question": "In-place sorting means Bubble Sort does not require extra space. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is slower than Quick Sort for large arrays. (True/False)", "answer": "True"},
        lambda: {"question": "The time complexity of Bubble Sort is independent of the input order. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort swaps elements only if they are in the wrong order. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort can be implemented both iteratively and recursively. (True/False)", "answer": "True"},
    ],

    "MCQ": [
        lambda: (lambda n=random.randint(5, 9): {
    "question": f"Calculate the total number of comparisons in Bubble Sort for an array of {n} elements:",
    "answer": str((n*(n-1))//2),
    "options": [str((n*(n-1))//2), str(n*n), str(n-1), str(n+1)],
    "explanation": f"Bubble Sort compares adjacent elements. For {n} elements, total comparisons = {n}×({n}-1)/2 = {(n*(n-1))//2}"
      })(),
        lambda: {
            "question": "What is the space complexity of Bubble Sort?",
            "options": ["O(n)", "O(n log n)", "O(1)", "O(n^2)"],
            "answer": "O(1)"
        },
        lambda: {
            "question": "Which feature improves Bubble Sort performance?",
            "options": ["Flag for no swaps", "Recursion", "Divide and Conquer", "Linked list"],
            "answer": "Flag for no swaps"
        },
        lambda: {
            "question": "For an array [4, 3, 2, 1], how many total swaps are done in worst case Bubble Sort?",
            "options": ["3", "6", "10", "15"],
            "answer": "6"
        },
        lambda: {
            "question": "Which best describes a stable sorting algorithm?",
            "options": ["Preserves equal elements' order", "Fastest always", "Recursive", "Uses stacks"],
            "answer": "Preserves equal elements' order"
        },
        lambda: {
            "question": "In an optimized Bubble Sort, what happens when no swaps occur in a pass?",
            "options": ["Sorting stops", "Sorting restarts", "Swaps double", "Array reverses"],
            "answer": "Sorting stops"
        },
        lambda: {
            "question": "What is the worst-case time complexity of Bubble Sort?",
            "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
            "answer": "O(n^2)"
        },
        lambda: {
            "question": "Which of the following is NOT a characteristic of Bubble Sort?",
            "options": ["Stable", "In-place", "Divide and conquer", "Iterative"],
            "answer": "Divide and conquer"
        },
        lambda: {
            "question": "How does Bubble Sort handle equal elements?",
            "options": ["Maintains order", "Changes order randomly", "Sorts descending", "Ignores them"],
            "answer": "Maintains order"
        },
        lambda: {
            "question": "Which scenario gives Bubble Sort its best-case time complexity?",
            "options": ["Already sorted array", "Reverse sorted array", "Random array", "Array with duplicates"],
            "answer": "Already sorted array"
        },
        lambda: {
            "question": "How many passes does Bubble Sort perform in the worst case for array of length n?",
            "options": ["n-1", "n", "log n", "n^2"],
            "answer": "n-1"
        },
        lambda: {
            "question": "Which of the following is the key optimization in Bubble Sort?",
            "options": ["Early termination when no swaps", "Using extra memory", "Divide and conquer", "Recursive calls"],
            "answer": "Early termination when no swaps"
        },
        lambda: {
            "question": "What does Bubble Sort compare during sorting?",
            "options": ["Adjacent elements", "First and last elements", "Middle elements", "Random elements"],
            "answer": "Adjacent elements"
        },
        lambda: {
            "question": "Which of these sorting algorithms is usually faster than Bubble Sort?",
            "options": ["Quick Sort", "Selection Sort", "Bubble Sort", "Insertion Sort"],
            "answer": "Quick Sort"
        },
        lambda: {
            "question": "In Bubble Sort, after the first pass, what can be said about the largest element?",
            "options": ["It is at the end", "It is at the beginning", "It is in the middle", "Position unknown"],
            "answer": "It is at the end"
        },
        lambda: {
            "question": "What kind of algorithm is Bubble Sort considered?",
            "options": ["Comparison-based", "Non-comparison", "Divide and conquer", "Hashing"],
            "answer": "Comparison-based"
        },
        lambda: {
            "question": "Which of these is a downside of Bubble Sort?",
            "options": ["Slow for large inputs", "Requires extra space", "Unstable", "Complex implementation"],
            "answer": "Slow for large inputs"
        },
        lambda: {
            "question": "What is the typical use case of Bubble Sort?",
            "options": ["Educational purposes", "High performance sorting", "Database indexing", "Real-time systems"],
            "answer": "Educational purposes"
        },
        lambda: {
            "question": "What is the main reason Bubble Sort is rarely used in practice?",
            "options": ["Inefficiency on large datasets", "Requires recursion", "Complex code", "High memory usage"],
            "answer": "Inefficiency on large datasets"
        },
        lambda: {
            "question": "Which data structure is Bubble Sort best applied to?",
            "options": ["Arrays", "Trees", "Graphs", "Hash tables"],
            "answer": "Arrays"
        },
        lambda: {
            "question": "What happens to the unsorted portion of the array after each pass in Bubble Sort?",
            "options": ["It shrinks", "It grows", "It stays the same", "It doubles"],
            "answer": "It shrinks"
        },
        lambda: {
            "question": "Which operation primarily determines Bubble Sort's efficiency?",
            "options": ["Swapping elements", "Copying elements", "Deleting elements", "Inserting elements"],
            "answer": "Swapping elements"
        },
        lambda: {
            "question": "Which variable is commonly used to detect if the array is sorted in Bubble Sort?",
            "options": ["Swap flag", "Counter", "Index", "Sum"],
            "answer": "Swap flag"
        },
        lambda: {
            "question": "How does optimized Bubble Sort improve time complexity on nearly sorted arrays?",
            "options": ["Stops early when sorted", "Uses recursion", "Sorts twice", "Uses extra space"],
            "answer": "Stops early when sorted"
        },
        lambda: {
            "question": "Bubble Sort is best classified as which type of algorithm?",
            "options": ["Simple", "Complex", "Recursive", "Non-deterministic"],
            "answer": "Simple"
        }
    ],

    "MTQ": [
        lambda: {
            "question": "Match optimized Bubble Sort terms:\n1. Optimization\n2. Worst case\n3. Stability\n4. Space usage",
            "pairs": {
                "1": "Stop early if no swaps",
                "2": "Reversed array",
                "3": "Preserves original order",
                "4": "In-place algorithm"
            },
            "answer": "1->Stop early if no swaps, 2->Reversed array, 3->Preserves original order, 4->In-place algorithm"
        },
        lambda: {
            "question": "Match the terms related to Bubble Sort:\n1. Best case\n2. Time complexity\n3. Pass\n4. Comparison",
            "pairs": {
                "1": "O(n)",
                "2": "O(n^2)",
                "3": "Single traversal over array",
                "4": "Between adjacent elements"
            },
            "answer": "1->O(n), 2->O(n^2), 3->Single traversal over array, 4->Between adjacent elements"
        },
        lambda: {
            "question": "Match the concepts:\n1. Stable sort\n2. Swap flag\n3. Space complexity\n4. Array size",
            "pairs": {
                "1": "Maintains order of duplicates",
                "2": "Detects if swaps occurred",
                "3": "O(1)",
                "4": "Determines number of passes"
            },
            "answer": "1->Maintains order of duplicates, 2->Detects if swaps occurred, 3->O(1), 4->Determines number of passes"
        },
        lambda: {
            "question": "Match the Bubble Sort characteristics:\n1. In-place\n2. Iterative\n3. Optimized\n4. Worst case input",
            "pairs": {
                "1": "Uses constant extra space",
                "2": "Loops through the array multiple times",
                "3": "Stops if no swaps in a pass",
                "4": "Reverse sorted array"
            },
            "answer": "1->Uses constant extra space, 2->Loops through the array multiple times, 3->Stops if no swaps in a pass, 4->Reverse sorted array"
        },
        lambda: {
            "question": "Match the definitions:\n1. Swap\n2. Pass\n3. Best case\n4. Comparison",
            "pairs": {
                "1": "Exchange of two elements",
                "2": "One full iteration through array",
                "3": "Already sorted array",
                "4": "Checking two adjacent elements"
            },
            "answer": "1->Exchange of two elements, 2->One full iteration through array, 3->Already sorted array, 4->Checking two adjacent elements"
        },
        lambda: {
            "question": "Match the Bubble Sort optimization steps:\n1. Swap flag\n2. Reduce passes\n3. Skip sorted\n4. Early exit",
            "pairs": {
                "1": "Tracks if any swaps happen",
                "2": "Decrease range after each pass",
                "3": "Ignore last sorted elements",
                "4": "Stop when no swaps detected"
            },
            "answer": "1->Tracks if any swaps happen, 2->Decrease range after each pass, 3->Ignore last sorted elements, 4->Stop when no swaps detected"
        },
        lambda: {
            "question": "Match the properties:\n1. Stability\n2. Time complexity\n3. Space\n4. Algorithm type",
            "pairs": {
                "1": "Maintains input order for duplicates",
                "2": "O(n^2)",
                "3": "O(1)",
                "4": "Comparison-based"
            },
            "answer": "1->Maintains input order for duplicates, 2->O(n^2), 3->O(1), 4->Comparison-based"
        },
        lambda: {
            "question": "Match Bubble Sort terms:\n1. Pass\n2. Swap\n3. Adjacent\n4. Sorted portion",
            "pairs": {
                "1": "Iteration over array",
                "2": "Exchange two elements",
                "3": "Next to each other",
                "4": "Elements at the end after pass"
            },
            "answer": "1->Iteration over array, 2->Exchange two elements, 3->Next to each other, 4->Elements at the end after pass"
        },
        lambda: {
            "question": "Match the Bubble Sort descriptions:\n1. Best case\n2. Worst case\n3. Average case\n4. Optimization",
            "pairs": {
                "1": "Array already sorted",
                "2": "Array reverse sorted",
                "3": "Random order array",
                "4": "Stop early if no swaps"
            },
            "answer": "1->Array already sorted, 2->Array reverse sorted, 3->Random order array, 4->Stop early if no swaps"
        },
        lambda: {
            "question": "Match the Bubble Sort results:\n1. Number of swaps\n2. Number of comparisons\n3. Space usage\n4. Pass count",
            "pairs": {
                "1": "Can be up to n(n-1)/2",
                "2": "Can be up to n(n-1)/2",
                "3": "O(1)",
                "4": "Up to n-1"
            },
            "answer": "1->Can be up to n(n-1)/2, 2->Can be up to n(n-1)/2, 3->O(1), 4->Up to n-1"
        },
        lambda: {
            "question": "Match Bubble Sort features:\n1. Stability\n2. Extra space\n3. Recursive\n4. Optimization",
            "pairs": {
                "1": "Yes",
                "2": "No extra space",
                "3": "Usually iterative",
                "4": "Stop early on sorted array"
            },
            "answer": "1->Yes, 2->No extra space, 3->Usually iterative, 4->Stop early on sorted array"
        },
        lambda: {
            "question": "Match the terms:\n1. Adjacent elements\n2. Swap flag\n3. Sorted portion\n4. Pass",
            "pairs": {
                "1": "Elements next to each other",
                "2": "Indicates if swaps happened",
                "3": "Elements at the end sorted",
                "4": "One full iteration"
            },
            "answer": "1->Elements next to each other, 2->Indicates if swaps happened, 3->Elements at the end sorted, 4->One full iteration"
        },
        lambda: {
            "question": "Match the following Bubble Sort statements:\n1. Time complexity\n2. Space complexity\n3. Stability\n4. Optimization",
            "pairs": {
                "1": "O(n^2)",
                "2": "O(1)",
                "3": "Stable",
                "4": "Stop early when no swaps"
            },
            "answer": "1->O(n^2), 2->O(1), 3->Stable, 4->Stop early when no swaps"
        },
        lambda: {
            "question": "Match the concepts:\n1. Pass\n2. Swap\n3. Best case\n4. Worst case",
            "pairs": {
                "1": "Complete iteration over array",
                "2": "Exchange of two elements",
                "3": "Already sorted array",
                "4": "Reverse sorted array"
            },
            "answer": "1->Complete iteration over array, 2->Exchange of two elements, 3->Already sorted array, 4->Reverse sorted array"
        },
        lambda: {
            "question": "Match these Bubble Sort terms:\n1. Iterative\n2. In-place\n3. Stable\n4. Flag",
            "pairs": {
                "1": "Uses loops",
                "2": "No extra array needed",
                "3": "Preserves equal element order",
                "4": "Detects no swaps"
            },
            "answer": "1->Uses loops, 2->No extra array needed, 3->Preserves equal element order, 4->Detects no swaps"
        },
        lambda: {
            "question": "Match the definitions:\n1. Comparison\n2. Swap\n3. Pass\n4. Optimization",
            "pairs": {
                "1": "Check two adjacent elements",
                "2": "Exchange elements",
                "3": "One traversal of array",
                "4": "Stop if no swaps"
            },
            "answer": "1->Check two adjacent elements, 2->Exchange elements, 3->One traversal of array, 4->Stop if no swaps"
        },
        lambda: {
            "question": "Match these terms:\n1. Complexity\n2. Stability\n3. Memory\n4. Algorithm",
            "pairs": {
                "1": "O(n^2)",
                "2": "Stable",
                "3": "O(1) extra space",
                "4": "Comparison-based"
            },
            "answer": "1->O(n^2), 2->Stable, 3->O(1) extra space, 4->Comparison-based"
        },
        lambda: {
            "question": "Match the features:\n1. Early exit\n2. Pass\n3. Swap\n4. Comparison",
            "pairs": {
                "1": "Stops sorting when no swaps",
                "2": "Complete traversal",
                "3": "Exchanging elements",
                "4": "Checking adjacent elements"
            },
            "answer": "1->Stops sorting when no swaps, 2->Complete traversal, 3->Exchanging elements, 4->Checking adjacent elements"
        },
        lambda: {
            "question": "Match these concepts:\n1. Stability\n2. Space\n3. Time\n4. Optimization",
            "pairs": {
                "1": "Preserves order of equal elements",
                "2": "O(1)",
                "3": "O(n^2)",
                "4": "Stop early on no swaps"
            },
            "answer": "1->Preserves order of equal elements, 2->O(1), 3->O(n^2), 4->Stop early on no swaps"
        },
        lambda: {
            "question": "Match Bubble Sort characteristics:\n1. Pass\n2. Swap\n3. Optimization\n4. Time complexity",
            "pairs": {
                "1": "Iteration through array",
                "2": "Exchange adjacent elements",
                "3": "Stop if no swaps",
                "4": "O(n^2)"
            },
            "answer": "1->Iteration through array, 2->Exchange adjacent elements, 3->Stop if no swaps, 4->O(n^2)"
        }
    ],

    "ECQ": [
        lambda: {"question": "Explain how the swap flag optimization works in Bubble Sort.", "answer": "The swap flag tracks if any swaps occur during a pass. If no swaps happen, the array is sorted, and Bubble Sort stops early to save time."},
        lambda: {"question": "Describe the best-case time complexity scenario for Bubble Sort.", "answer": "The best case is when the array is already sorted; optimized Bubble Sort detects no swaps on the first pass and finishes in O(n) time."},
        lambda: {"question": "What is meant by Bubble Sort being a stable sorting algorithm?", "answer": "Bubble Sort maintains the relative order of equal elements, meaning duplicates remain in their original sequence after sorting."},
        lambda: {"question": "Explain why Bubble Sort is considered an in-place sorting algorithm.", "answer": "Because it requires only a constant amount of extra space and rearranges elements within the original array without needing additional arrays."},
        lambda: {"question": "How does Bubble Sort's performance change with nearly sorted data?", "answer": "Performance improves significantly because fewer swaps occur, and with the swap flag optimization, it can finish early."},
        lambda: {"question": "Explain the role of adjacent element comparisons in Bubble Sort.", "answer": "Bubble Sort compares pairs of adjacent elements and swaps them if they are out of order, pushing the largest unsorted element to the right."},
        lambda: {"question": "Describe the difference between worst-case and average-case time complexity for Bubble Sort.", "answer": "Both worst and average cases have O(n^2) time complexity due to nested loops comparing and swapping elements."},
        lambda: {"question": "What makes Bubble Sort inefficient for large datasets?", "answer": "It performs many unnecessary comparisons and swaps, especially in the worst case, leading to O(n^2) time complexity."},
        lambda: {"question": "Explain why Bubble Sort is still useful despite its inefficiency.", "answer": "Its simplicity makes it a good teaching tool for understanding sorting concepts and algorithm design."},
        lambda: {"question": "How does Bubble Sort ensure the largest element reaches its correct position after each pass?", "answer": "By repeatedly swapping adjacent elements if the left one is greater, the largest element 'bubbles' to the end."},
        lambda: {"question": "Describe what happens during a single pass of Bubble Sort.", "answer": "The algorithm iterates through the array, compares adjacent elements, and swaps them if they are out of order, pushing the largest unsorted element to the end."},
        lambda: {"question": "Explain the significance of the number of passes in Bubble Sort.", "answer": "Maximum number of passes is n-1 because after that the array is guaranteed to be sorted."},
        lambda: {"question": "What does the space complexity of O(1) imply in Bubble Sort?", "answer": "It implies Bubble Sort uses a fixed amount of extra memory regardless of input size."},
        lambda: {"question": "Explain why Bubble Sort is not suitable for real-time applications.", "answer": "Because it is too slow (O(n^2)) for large inputs and cannot guarantee timely results."},
        lambda: {"question": "How can Bubble Sort be modified to improve performance?", "answer": "By adding a swap flag to detect if no swaps occurred and stopping early."},
        lambda: {"question": "Describe how Bubble Sort handles duplicate elements.", "answer": "Duplicates are kept in their original relative order, maintaining stability."},
        lambda: {"question": "What is the significance of comparing adjacent elements instead of distant elements?", "answer": "Comparing adjacent elements allows gradual sorting by pushing larger elements towards the end step-by-step."},
        lambda: {"question": "How does the number of swaps relate to the array's initial order?", "answer": "More disordered arrays require more swaps; already sorted arrays require zero swaps."},
        lambda: {"question": "Explain why Bubble Sort is classified as a comparison-based sorting algorithm.", "answer": "Because it sorts by comparing pairs of elements to decide if a swap is needed."},
        lambda: {"question": "What is the impact of Bubble Sort on nearly sorted versus randomly ordered arrays?", "answer": "Nearly sorted arrays benefit from fewer swaps and early termination; random arrays do not."},
        lambda: {"question": "How is the number of passes reduced after each iteration in Bubble Sort?", "answer": "Because the largest element settles at the end, subsequent passes ignore the sorted end portion."},
        lambda: {"question": "Why is Bubble Sort often used for educational purposes?", "answer": "It clearly demonstrates fundamental sorting mechanics and algorithm optimization concepts."},
        lambda: {"question": "Explain the worst-case input for Bubble Sort and why it is so inefficient.", "answer": "A reverse-sorted array causes maximum swaps and comparisons, leading to O(n^2) operations."},
        lambda: {"question": "Describe how Bubble Sort compares with Selection Sort.", "answer": "Bubble Sort repeatedly swaps adjacent elements, Selection Sort finds minimum elements; Bubble Sort is stable while Selection Sort usually isn't."},
        lambda: {"question": "Explain how the algorithm knows when the array is sorted.", "answer": "By checking if a pass completes with no swaps, indicating sorting is done."}
    ],

    "EXPQ": [
    lambda: {
        "question": f"Complete the expression for number of comparisons in Bubble Sort for array {generate_array2()}:\nTotal comparisons = (n * (n-1)) / __",
        "answer": "2"
    },
    lambda: {
        "question": f"Fill in the blank:\nBubble Sort has best-case time complexity of O(__) when the array is already sorted: {generate_array2()}",
        "answer": "n"
    },
    lambda: {
        "question": f"Complete the sentence:\nBubble Sort is a __ sorting algorithm that compares adjacent elements and swaps if needed for array {generate_array2()}.",
        "answer": "comparison-based"
    },
    lambda: {
        "question": f"Fill in the blank:\nBubble Sort is an __ algorithm, meaning it sorts the array within the same memory space: {generate_array2()}",
        "answer": "in-place"
    },
    lambda: (lambda arr=generate_array2(): {
        "question": f"Complete the expression:\nThe maximum number of passes in Bubble Sort for array length {len(arr)} is __.",
        "answer": str(len(arr) - 1)
    })(),
    lambda: {
        "question": f"Fill in the blank:\nIf no swaps occur during a pass over array {generate_array2()}, Bubble Sort __ early.",
        "answer": "stops"
    },
    lambda: {
        "question": f"Complete the statement:\nBubble Sort is considered __ stable because it preserves the relative order of equal elements in {generate_array2()}.",
        "answer": "stable"
    },
    lambda: {
        "question": f"Fill in the blank:\nThe swap flag variable in Bubble Sort indicates if any __ occurred during a pass for array {generate_array2()}.",
        "answer": "swaps"
    },
    lambda: (lambda arr=generate_array2(): {
        "question": f"Complete the formula:\nTime complexity of Bubble Sort in the worst case for array length {len(arr)} is O(__).",
        "answer": "n^2"
    })(),
    lambda: {
        "question": f"Fill in the blank:\nBubble Sort compares only __ elements during sorting, i.e., elements next to each other in array {generate_array2()}.",
        "answer": "adjacent"
    },
    lambda: (lambda arr=generate_array2(): {
        "question": f"Complete the sentence:\nBubble Sort performs __ passes in the worst case for array {arr}.",
        "answer": str(len(arr)-1)
    })(),
    lambda: {
        "question": f"Fill in the blank:\nBubble Sort's space complexity is O(__) since it uses a fixed amount of extra memory for array {generate_array2()}.",
        "answer": "1"
    },
    lambda: {
        "question": f"Complete the statement:\nIn Bubble Sort, the largest unsorted element is moved to the __ of the array {generate_array2()} after each pass.",
        "answer": "end"
    },
    lambda: {
        "question": f"Fill in the blank:\nAn optimized Bubble Sort checks if any __ occurred during a pass over {generate_array2()}.",
        "answer": "swaps"
    },
    lambda: (lambda arr=generate_array2(): {
        "question": f"Complete the expression:\nNumber of comparisons for an array of length {len(arr)} in Bubble Sort is n * (n-1) / __.",
        "answer": "2"
    })(),
    lambda: {
        "question": f"Fill in the blank:\nBubble Sort can detect a sorted array and __ early when no swaps happen for array {generate_array2()}.",
        "answer": "stop"
    },
    lambda: {
        "question": f"Complete the sentence:\nBubble Sort compares elements and __ them if they are in the wrong order for array {generate_array2()}.",
        "answer": "swaps"
    },
    lambda: {
        "question": f"Fill in the blank:\nBubble Sort has time complexity O(n^2) in the average and __ cases for array {generate_array2()}.",
        "answer": "worst"
    },
    lambda: {
        "question": f"Complete the statement:\nBubble Sort is often used to teach basic __ and algorithm optimization concepts with array {generate_array2()}.",
        "answer": "sorting"
    },
    lambda: {
        "question": f"Fill in the blank:\nThe swap flag variable is set to __ when a swap occurs in Bubble Sort for array {generate_array2()}.",
        "answer": "True"
    },
    lambda: (lambda arr=generate_array2(): {
        "question": f"Complete the expression:\nIn Bubble Sort, the number of passes needed is at most __ minus one for array {arr}.",
        "answer": str(len(arr) - 1)
    })(),
    lambda: {
        "question": f"Fill in the blank:\nBubble Sort compares pairs of __ elements to push the largest to the end for array {generate_array2()}.",
        "answer": "adjacent"
    },
    lambda: {
        "question": f"Complete the statement:\nBubble Sort's simplicity and ease of implementation make it ideal for __ purposes with array {generate_array2()}.",
        "answer": "educational"
    },
    lambda: (lambda arr=generate_array2(): {
        "question": f"Fill in the blank:\nThe optimized Bubble Sort can finish in O(n) time for an already __ array like {arr}.",
        "answer": "sorted"
    })(),
    lambda: {
        "question": f"Complete the expression:\nBubble Sort uses O(1) extra space, making it an __ sorting algorithm for array {generate_array2()}.",
        "answer": "in-place"
    },
]
}

# ------------------------------------------
# Template banks for Level 3 – Advanced
# ------------------------------------------
def generate_random_array(size=6, low=10, high=99):
    return [random.randint(low, high) for _ in range(size)]

def bubble_sort_passes(arr):
    return len(arr) - 1

def bubble_sort_swaps(arr):
    # For simplicity, just return n*(n-1)/2
    n = len(arr)
    return n*(n-1)//2

level_3 = {
    "TFQ": [
        lambda: {"question": "Bubble Sort is usually not used in real-world applications. (True/False)", "answer": "True"},
        lambda: {"question": "Recursive Bubble Sort is possible. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is faster than Quick Sort. (True/False)", "answer": "False"},
        lambda: {"question": "Worst-case for Bubble Sort is on a reversed array. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort adapts well to nearly sorted data. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort has quadratic time complexity due to nested loops. (True/False)", "answer": "True"},
        lambda: {"question": "The adaptive property of Bubble Sort makes it faster than Quick Sort for large arrays. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort can be implemented recursively. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is not suitable for linked list data structures. (True/False)", "answer": "False"},
        lambda: {"question": "In Bubble Sort, the time complexity can be improved to linear for sorted data. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort's worst-case performance is when the array is already sorted. (True/False)", "answer": "False"},
        lambda: {"question": "The number of total comparisons in Bubble Sort is independent of array contents. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort cannot be parallelized. (True/False)", "answer": "False"},
        lambda: {"question": "In Bubble Sort, after each full pass, the smallest unsorted element moves to the end. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort guarantees sorting after (n-1) passes regardless of input. (True/False)", "answer": "True"},
        lambda: {"question": "The best-case time complexity of Bubble Sort is O(n). (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is a stable sorting algorithm. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort requires extra memory for swapping. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort compares adjacent elements in each pass. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort can be optimized using a flag to check swaps. (True/False)", "answer": "True"},
        lambda: {"question": "The average-case complexity of Bubble Sort is O(n log n). (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort can sort linked lists efficiently. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort’s outer loop runs n times for an array of size n. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is an in-place sorting algorithm. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort swaps elements even if they are equal. (True/False)", "answer": "False"},
    ],

    "MCQ": [
        lambda: {
            "question": "What's the swap count in worst-case for n=6?",
            "options": ["15", "30", "6", "12"],
            "answer": "15"
        },
        lambda: {
            "question": "Which algorithm is more efficient than Bubble Sort?",
            "options": ["Merge Sort", "Bubble Sort", "Sleep Sort", "Gnome Sort"],
            "answer": "Merge Sort"
        },
        lambda: {
            "question": "Recursive Bubble Sort base condition is?",
            "options": ["Array size is 0 or 1", "No swaps", "Max element reached", "End pointer reached"],
            "answer": "Array size is 0 or 1"
        },
        lambda: {
            "question": "Which scenario gives worst-case time?",
            "options": ["Already sorted", "Partially sorted", "Reverse sorted", "All equal"],
            "answer": "Reverse sorted"
        },
        lambda: {
            "question": "What's a practical use case for Bubble Sort?",
            "options": ["Teaching algorithm basics", "Sorting big data", "Optimizing DB queries", "AI modeling"],
            "answer": "Teaching algorithm basics"
        },
        lambda: {
            "question": "Why is Bubble Sort considered inefficient for large datasets?",
            "options": ["High time complexity", "High memory use", "Unstable sort", "Complex implementation"],
            "answer": "High time complexity"
        },
        lambda: {
            "question": "How many total passes does Bubble Sort make in the worst case for an array of size n?",
            "options": ["n-1", "n", "log n", "n^2"],
            "answer": "n-1"
        },
        lambda: {
            "question": "Which sorting algorithm has better average-case performance than Bubble Sort?",
            "options": ["Selection Sort", "Insertion Sort", "Quick Sort", "None of the above"],
            "answer": "Quick Sort"
        },
        lambda: {
            "question": "What is the time complexity of Bubble Sort in best case?",
            "options": ["O(n)", "O(n^2)", "O(log n)", "O(n log n)"],
            "answer": "O(n)"
        },
        lambda: {
            "question": "Which technique improves Bubble Sort's efficiency?",
            "options": ["Using a swap flag", "Using recursion only", "Skipping elements randomly", "Sorting backwards"],
            "answer": "Using a swap flag"
        },
        lambda: {
            "question": "Which of the following is NOT true about Bubble Sort?",
            "options": ["It is stable", "It is in-place", "It is recursive only", "It compares adjacent elements"],
            "answer": "It is recursive only"
        },
        lambda: {
            "question": "In Bubble Sort, which element is guaranteed to be placed correctly after first pass?",
            "options": ["Largest", "Smallest", "Median", "Random"],
            "answer": "Largest"
        },
        lambda: {
            "question": "What is the space complexity of Bubble Sort?",
            "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
            "answer": "O(1)"
        },
        lambda: {
            "question": "Which of these is NOT a step in Bubble Sort?",
            "options": ["Swapping adjacent elements", "Comparing adjacent elements", "Merging sorted subarrays", "Repeating passes"],
            "answer": "Merging sorted subarrays"
        },
        lambda: {
            "question": "Which of the following is an adaptive sorting algorithm?",
            "options": ["Bubble Sort", "Heap Sort", "Merge Sort", "Quick Sort"],
            "answer": "Bubble Sort"
        },
        lambda: {
            "question": "Bubble Sort can be stopped early if?",
            "options": ["No swaps occur in a pass", "All elements are distinct", "Array size is even", "Pass count reaches n"],
            "answer": "No swaps occur in a pass"
        },
        lambda: {
            "question": "Bubble Sort is best used for?",
            "options": ["Small or nearly sorted arrays", "Huge datasets", "Random access memory", "Hash tables"],
            "answer": "Small or nearly sorted arrays"
        },
        lambda: {
            "question": "Which sorting algorithm is stable?",
            "options": ["Bubble Sort", "Heap Sort", "Quick Sort", "Selection Sort"],
            "answer": "Bubble Sort"
        },
        lambda: {
            "question": "In recursive Bubble Sort, what decreases after each recursive call?",
            "options": ["Size of array to sort", "Swap count", "Number of passes", "Number of comparisons"],
            "answer": "Size of array to sort"
        },
        lambda: {
            "question": "Which property of Bubble Sort allows it to stop early?",
            "options": ["Adaptive", "Stable", "Divide and Conquer", "In-place"],
            "answer": "Adaptive"
        },
        lambda: {
            "question": "Which of the following sorting algorithms is NOT comparison-based?",
            "options": ["Bubble Sort", "Counting Sort", "Quick Sort", "Merge Sort"],
            "answer": "Counting Sort"
        },
        lambda: {
            "question": "What type of sorting algorithm is Bubble Sort?",
            "options": ["Comparison", "Non-comparison", "Bucket", "Radix"],
            "answer": "Comparison"
        },
        lambda: {
            "question": "How does Bubble Sort handle equal elements?",
            "options": ["Maintains their relative order", "Swaps them arbitrarily", "Removes duplicates", "Ignores them"],
            "answer": "Maintains their relative order"
        },
        lambda: {
            "question": "Bubble Sort's performance is largely affected by?",
            "options": ["Initial order of elements", "Size of elements", "Memory size", "CPU speed"],
            "answer": "Initial order of elements"
        },
        lambda: {
            "question": "What is the main disadvantage of Bubble Sort?",
            "options": ["Inefficiency on large datasets", "High memory use", "Complex code", "Unstable sorting"],
            "answer": "Inefficiency on large datasets"
        },
          lambda: (lambda arr=generate_random_array():
            {
                "question": f"Given the array {arr}, what is the maximum number of swaps Bubble Sort will perform to sort it?",
                "answer": f"{bubble_sort_swaps(arr)}"
            })(),
    ],

    "MTQ": [
        lambda: {
            "question": "Match real-world and theoretical aspects:\n1. Inefficiency\n2. Best use\n3. Recursion\n4. Worst Case",
            "pairs": {
                "1": "Large input size",
                "2": "Educational tool",
                "3": "Function calls itself",
                "4": "Reversed array"
            },
            "answer": "1->Large input size, 2->Educational tool, 3->Function calls itself, 4->Reversed array"
        },
        lambda: {
            "question": "Match the terms to their definitions:\n1. Stability\n2. Adaptive\n3. In-place\n4. Complexity",
            "pairs": {
                "1": "Maintains relative order",
                "2": "Optimizes based on input",
                "3": "Uses constant extra space",
                "4": "Measures performance"
            },
            "answer": "1->Maintains relative order, 2->Optimizes based on input, 3->Uses constant extra space, 4->Measures performance"
        },
        lambda: {
            "question": "Match each term to the Bubble Sort characteristic:\n1. Pass\n2. Swap\n3. Comparison\n4. Flag",
            "pairs": {
                "1": "One complete scan through array",
                "2": "Exchange two adjacent elements",
                "3": "Check order of two elements",
                "4": "Indicator for early stopping"
            },
            "answer": "1->One complete scan through array, 2->Exchange two adjacent elements, 3->Check order of two elements, 4->Indicator for early stopping"
        },
        lambda: {
            "question": "Match the terms to Bubble Sort's time complexities:\n1. Best case\n2. Worst case\n3. Average case\n4. Space",
            "pairs": {
                "1": "O(n)",
                "2": "O(n^2)",
                "3": "O(n^2)",
                "4": "O(1)"
            },
            "answer": "1->O(n), 2->O(n^2), 3->O(n^2), 4->O(1)"
        },
        lambda: {
            "question": "Match sorting terms with examples:\n1. Stable sort\n2. Unstable sort\n3. In-place sort\n4. Out-of-place sort",
            "pairs": {
                "1": "Bubble Sort",
                "2": "Quick Sort",
                "3": "Bubble Sort",
                "4": "Merge Sort"
            },
            "answer": "1->Bubble Sort, 2->Quick Sort, 3->Bubble Sort, 4->Merge Sort"
        },
        lambda: {
            "question": "Match the following about Bubble Sort passes:\n1. Pass 1\n2. Pass 2\n3. Pass n-1\n4. Total passes",
            "pairs": {
                "1": "Largest element at end",
                "2": "Second largest element at end",
                "3": "Second smallest element at start",
                "4": "n-1"
            },
            "answer": "1->Largest element at end, 2->Second largest element at end, 3->Second smallest element at start, 4->n-1"
        },
        lambda: {
            "question": "Match the terms:\n1. Time complexity\n2. Space complexity\n3. Stability\n4. Adaptive",
            "pairs": {
                "1": "O(n^2)",
                "2": "O(1)",
                "3": "Yes",
                "4": "Yes"
            },
            "answer": "1->O(n^2), 2->O(1), 3->Yes, 4->Yes"
        },
        lambda: {
            "question": "Match the following optimization techniques:\n1. Early stopping\n2. Recursive approach\n3. Swap flag\n4. Loop unrolling",
            "pairs": {
                "1": "Stop when no swaps",
                "2": "Function calls itself",
                "3": "Tracks swaps in pass",
                "4": "Not typical in Bubble Sort"
            },
            "answer": "1->Stop when no swaps, 2->Function calls itself, 3->Tracks swaps in pass, 4->Not typical in Bubble Sort"
        },
        lambda: {
            "question": "Match algorithm with key feature:\n1. Bubble Sort\n2. Merge Sort\n3. Quick Sort\n4. Heap Sort",
            "pairs": {
                "1": "Stable and simple",
                "2": "Divide and conquer",
                "3": "Partitioning",
                "4": "Heap data structure"
            },
            "answer": "1->Stable and simple, 2->Divide and conquer, 3->Partitioning, 4->Heap data structure"
        },
        lambda: {
            "question": "Match sorting concepts:\n1. Comparison sort\n2. Non-comparison sort\n3. In-place sort\n4. Stable sort",
            "pairs": {
                "1": "Bubble Sort",
                "2": "Counting Sort",
                "3": "Bubble Sort",
                "4": "Bubble Sort"
            },
            "answer": "1->Bubble Sort, 2->Counting Sort, 3->Bubble Sort, 4->Bubble Sort"
        },
        # Add 5 more MTQ templates similarly...
    ],

    "ECQ": [
        lambda: {"question": "Describe how recursive Bubble Sort works.", "answer": "Sorts the first n-1 elements recursively after bubbling max to end."},
        lambda: {"question": "How does recursive Bubble Sort work compared to the iterative version?", "answer": "It reduces the problem size with each recursive call, mimicking the outer loop of the iterative version."},
        lambda: {"question": "Why might Bubble Sort be preferred in embedded systems with memory constraints?", "answer": "It requires no extra memory allocation, making it suitable for environments with strict memory usage."},
        lambda: {"question": "Compare Bubble Sort's space complexity with that of Merge Sort.", "answer": "Bubble Sort is O(1) in space, while Merge Sort requires O(n) extra space."},
        lambda: {"question": "Discuss the cache performance of Bubble Sort.", "answer": "Poor cache performance due to repeated scanning and adjacent swaps which do not exploit spatial locality."},
        lambda: {"question": "How would you modify Bubble Sort to sort in descending order?", "answer": "Reverse the comparison logic (e.g., if arr[i] < arr[i+1], then swap)."},
        lambda: {"question": "What is the impact of input distribution on Bubble Sort performance?", "answer": "Nearly sorted arrays result in early termination and improved performance."},
        lambda: {"question": "Why is Bubble Sort not preferred in modern libraries and frameworks?", "answer": "Due to its inefficiency and better alternatives like Timsort, Merge Sort, and Quick Sort."},
        lambda: {"question": "Explain how Bubble Sort could be visualized in a GUI tool.", "answer": "By animating bar heights and showing swaps during each pass to depict bubbling effect."},
        lambda: {"question": "How can you measure the total number of operations performed by Bubble Sort?", "answer": "By counting total comparisons and swaps in a single run."},
        lambda: {"question": "Compare and contrast Bubble Sort with Selection Sort in terms of swap behavior.", "answer": "Bubble Sort swaps more frequently, while Selection Sort minimizes swaps but still has O(n²) comparisons."},
        lambda: {"question": "Explain the adaptive property of Bubble Sort.", "answer": "It can stop early if no swaps are detected, improving performance on nearly sorted data."},
        lambda: {"question": "Describe the role of the swap flag in Bubble Sort optimization.", "answer": "It helps detect if the array is sorted before completing all passes, allowing early termination."},
        lambda: {"question": "Explain why Bubble Sort is called 'Bubble' Sort.", "answer": "Because larger elements 'bubble up' to the end of the list with each pass."},
        lambda: {"question": "Describe how Bubble Sort differs from Insertion Sort.", "answer": "Bubble Sort swaps adjacent elements repeatedly, while Insertion Sort builds a sorted section by inserting elements."},
        lambda: {"question": "How does Bubble Sort behave with duplicate elements?", "answer": "It maintains their relative order, so it is stable."},
        lambda: {"question": "What is the effect of reversing the comparison operator in Bubble Sort?", "answer": "It sorts the array in descending order."},
        lambda: {"question": "Explain why Bubble Sort is inefficient for large arrays.", "answer": "Because it repeatedly compares and swaps adjacent elements, resulting in O(n²) complexity."},
        lambda: {"question": "Describe a scenario where Bubble Sort performs optimally.", "answer": "When the array is already sorted or nearly sorted, allowing early termination."},
        lambda: {"question": "How does the number of swaps relate to the disorder of the array?", "answer": "More disorder results in more swaps, with worst case on reversed arrays."},
        lambda: {"question": "Explain how Bubble Sort can be implemented using pointers in C.", "answer": "By using pointer arithmetic to access and swap adjacent elements."},
        lambda: {"question": "How would you test a Bubble Sort implementation for correctness?", "answer": "By checking sorted output on varied inputs including empty, sorted, reversed, and duplicate arrays."},
        lambda: {"question": "Why is Bubble Sort considered a stable sort?", "answer": "Because it never swaps equal elements out of their relative order."},
        lambda: {"question": "Explain the significance of the inner and outer loops in Bubble Sort.", "answer": "The inner loop compares and swaps adjacent elements; the outer loop ensures multiple passes."},
        lambda: {"question": "Discuss the limitations of Bubble Sort in parallel processing.", "answer": "Dependencies between adjacent swaps limit parallelism opportunities."},
    ],

    "EXPQ": [
        lambda: {"question": "Complete the expression: The worst-case time complexity of Bubble Sort is __.", "answer": "O(n^2)"},
        lambda: {"question": "Fill in the blank: Bubble Sort performs __ comparisons in the worst case.", "answer": "n*(n-1)/2"},
        lambda: {"question": "Complete: Bubble Sort is a __ sorting algorithm that compares adjacent elements.", "answer": "comparison-based"},
        lambda: {"question": "Fill: Bubble Sort's best-case time complexity is __ when the array is already sorted.", "answer": "O(n)"},
        lambda: {"question": "Complete: The optimization to stop Bubble Sort early uses a __ flag.", "answer": "swap"},
        lambda: {"question": "Fill in the blank: Bubble Sort is __, meaning it requires only constant extra space.", "answer": "in-place"},
        lambda: {"question": "Complete the statement: Bubble Sort is considered __ because it maintains the relative order of equal elements.", "answer": "stable"},
        lambda: {"question": "Fill: Bubble Sort sorts the array by repeatedly swapping __ elements.", "answer": "adjacent"},
        lambda: {"question": "Complete the expression: Recursive Bubble Sort reduces the problem size by sorting the first __ elements.", "answer": "n-1"},
        lambda: {"question": "Fill: The worst-case input for Bubble Sort is a __ array.", "answer": "reversed"},
        lambda: {"question": "Complete the sentence: Bubble Sort's average-case time complexity is __.", "answer": "O(n^2)"},
        lambda: {"question": "Fill in the blank: The number of passes Bubble Sort makes is at most __.", "answer": "n-1"},
        lambda: {"question": "Complete: After each pass, Bubble Sort places the __ element at its correct position.", "answer": "largest unsorted"},
        lambda: {"question": "Fill: The total number of swaps in Bubble Sort depends on the __ of the array.", "answer": "initial order"},
        lambda: {"question": "Complete: The inner loop of Bubble Sort compares elements __ positions apart.", "answer": "one"},
        lambda: {"question": "Fill in the blank: Bubble Sort can be improved by using a __ to detect if the array is sorted.", "answer": "flag"},
        lambda: {"question": "Complete: Bubble Sort's space complexity is __.", "answer": "O(1)"},
        lambda: {"question": "Fill: The simplest Bubble Sort implementation uses __ nested loops.", "answer": "two"},
        lambda: {"question": "Complete: Bubble Sort is often used as an __ example in algorithm teaching.", "answer": "introductory"},
        lambda: {"question": "Fill: The swap operation in Bubble Sort exchanges the __ of two adjacent elements.", "answer": "values"},
        lambda: {"question": "Complete: The stability of Bubble Sort means it preserves the __ order of equal elements.", "answer": "relative"},
        lambda: {"question": "Fill: Bubble Sort repeatedly compares and swaps __ elements.", "answer": "adjacent"},
        lambda: {"question": "Complete: An adaptive Bubble Sort stops early when __ swaps are detected in a pass.", "answer": "no"},
        lambda: {"question": "Fill in the blank: Bubble Sort is __ efficient for large datasets.", "answer": "not"},
        lambda: {"question": "Complete: The best-case time complexity of Bubble Sort occurs when the array is __.", "answer": "already sorted"},
        lambda: (lambda arr=generate_random_array():
            {
                "question": f"Given the array {arr}, fill in the blank: The total number of passes Bubble Sort will make to sort this array is __.",
                "answer": f"{bubble_sort_passes(arr)}"
            })(),
    ],
}

# ------------------------------------------
# Utility function to generate questions
# ------------------------------------------
question_bank = {"1": level_1, "2": level_2, "3": level_3}

def generate_questions(level: str, num: int):
    if level not in question_bank:
        print("Invalid level")
        return []

    selected_templates = question_bank[level]
    all_questions = []

    # Generate all possible unique questions once
    for qtype in QUESTION_TYPES:
        if qtype not in selected_templates:
            continue
        for template in selected_templates[qtype]:
            q = template()
            all_questions.append(q)

    # Remove duplicates by question text
    seen = set()
    unique_questions = []
    for q in all_questions:
        if q["question"] not in seen:
            unique_questions.append(q)
            seen.add(q["question"])

    # If requested number is less than or equal to unique questions → no repeats
    if num <= len(unique_questions):
        random.shuffle(unique_questions)
        return unique_questions[:num]

    # If requested number > available unique questions → allow repeats
    repeated_questions = []
    while len(repeated_questions) < num:
        random.shuffle(unique_questions)
        repeated_questions.extend(unique_questions)

    return repeated_questions[:num]

# ------------------------------------------
# Main
# ------------------------------------------
if __name__ == "__main__":
    level = input("Choose Level (1: Level1, 2: Level2, 3: Level3): ").strip()
    num_qs = int(input("Enter total number of questions to generate: "))
    questions = generate_questions(level, num_qs)

    for idx, q in enumerate(questions, start=1):
        print(f"Q{idx}. {q['question']}")
        if "options" in q:
            for i, opt in enumerate(q["options"], start=1):
                print(f"   {i}. {opt}")
        if "pairs" in q:
            print("Match the following:")
            for key, val in q["pairs"].items():
                print(f"  {key}: {val}")
        print(f"Answer: {q['answer']}\n")