import random
import json

QUESTION_TYPES = ["TFQ", "MCQ", "MTQ", "ECQ", "EXPQ"]
LEVELS = {
    "1": "Foundational",
    "2": "Intermediate",
    "3": "Advanced"
}

def generate_array():
    return [random.randint(1, 99) for _ in range(random.randint(4, 8))]

# ------------------------------------------
# Template banks for Level 1 – Foundational
# ------------------------------------------
level_1 = {
    "TFQ": [
        lambda: {"question": "Bubble Sort compares and swaps adjacent elements. (True/False)", "answer": "True"},
        lambda: {"question": f"Bubble Sort sorts this array in one pass: {generate_array()} (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort always takes the same number of passes regardless of input. (True/False)", "answer": "False"},
        lambda: {"question": "In Bubble Sort, a sorted region grows from the end. (True/False)", "answer": "True"},
        lambda: {"question": "The best-case time complexity of Bubble Sort is O(n). (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort always makes at least one swap in every pass.", "answer": "False"},
            lambda: {"question": "Bubble Sort can sort a list in descending order by simply reversing the comparison operator.", "answer": "True"},
            lambda: {"question": "The term \"Bubble\" in Bubble Sort refers to the smallest element bubbling to the top.", "answer": "False"},
            lambda: {"question": "In Bubble Sort, comparisons are made only between adjacent elements.", "answer": "True"},
            lambda: {"question": "Bubble Sort works only with integer values.", "answer": "False"},
            lambda: {"question": "Bubble Sort modifies the original array in-place.", "answer": "True"},
            lambda: {"question": "The worst-case time complexity of Bubble Sort is O(n).", "answer": "False"},
            lambda: {"question": "Bubble Sort can terminate early if no swaps occur in a pass.", "answer": "True"},
            lambda: {"question": "Bubble Sort is more efficient than Merge Sort in large datasets.", "answer": "False"},
            lambda: {"question": "In Bubble Sort, the number of passes is always equal to the number of elements.", "answer": "False"},
        
    ],
    "MCQ": [
        lambda: {
            "question": "What does Bubble Sort primarily use for sorting?",
            "options": ["Divide and Conquer", "Recursion", "Adjacent comparisons", "Heaps"],
            "answer": "Adjacent comparisons"
        },
        lambda: {
            "question": f"In the array {generate_array()} how many passes are needed in worst case?",
            "options": ["n", "n-1", "n/2", "n+1"],
            "answer": "n-1"
        },
        lambda: {
            "question": "Which of the following is true about Bubble Sort?",
            "options": ["It is not stable", "It is space inefficient", "It always uses recursion", "It is a stable sort"],
            "answer": "It is a stable sort"
        },
        lambda: {
            "question": "In Bubble Sort, where does the largest element end up after first pass?",
            "options": ["Start", "Middle", "End", "Unchanged"],
            "answer": "End"
        },
        lambda: {
            "question": "What type of algorithm is Bubble Sort?",
            "options": ["Divide-and-Conquer", "Greedy", "Backtracking", "Comparison-based"],
            "answer": "Comparison-based"
        },
        lambda: {
        "question": "Which element does Bubble Sort compare first in an array?",
        "options": ["First and second", "Last two", "Middle two", "Random pair"],
        "answer": "First and second"
    },
    lambda: {
        "question": "Bubble Sort is classified as which type of sorting algorithm?",
        "options": ["Selection Sort", "Exchange Sort", "Insertion Sort", "Quick Sort"],
        "answer": "Exchange Sort"
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
        }
    ],
    "ECQ": [
        lambda: {
            "question": "Explain how Bubble Sort ensures the largest element reaches the end in each pass.", "answer": "By comparing adjacent elements and swapping, the largest bubbles to the end."},
        lambda: {"question": "Why is Bubble Sort called a “comparison-based” sorting algorithm?", "answer": "Because it compares adjacent elements and swaps them based on their values."},
            lambda: {"question": "Describe a situation where Bubble Sort stops early before completing all passes.", "answer": "If a full pass completes with no swaps, the array is already sorted, and the algorithm terminates early."},
            lambda: {"question": "Why is Bubble Sort considered inefficient for large datasets?", "answer": "Because its time complexity is O(n²), leading to poor performance with larger arrays."},
            lambda: {"question": "Explain what happens during the first pass of Bubble Sort on an unsorted array.", "answer": "The largest element 'bubbles' to the last position by swapping with larger adjacent elements."},
            lambda: {"question": "What is meant by 'in-place' sorting in the context of Bubble Sort?", "answer": "The algorithm doesn't require extra memory; it sorts the data within the original array."},
            lambda: {"question": "What happens if all elements in the array are equal in Bubble Sort?", "answer": "No swaps will be made in any pass, and the algorithm will terminate early."},
            lambda: {"question": "Why is Bubble Sort classified as a stable sort?", "answer": "It maintains the relative order of equal elements after sorting."},
            lambda: {"question": "Can Bubble Sort work on strings or characters? Explain.", "answer": "Yes, it can compare characters based on their ASCII or Unicode values."},
            lambda: {"question": "What role does the inner loop play in Bubble Sort?", "answer": "It performs the adjacent comparisons and swaps within a pass."},
            lambda: {"question": "Why is Bubble Sort easy to understand and implement?", "answer": "Its logic is straightforward, involving only simple comparisons and swaps."},
    ],
    "EXPQ": [
        lambda: {
            "question": "Complete the expression for total comparisons in Bubble Sort for n elements: n(n-1)/__",
            "answer": "2"
        },
        lambda: {
        "question": "Complete the expression for total passes in Bubble Sort for n elements: n-__",
        "answer": "1"
    },
    lambda: {
        "question": "Fill in the blank: Bubble Sort compares __ elements in adjacent pairs.",
        "answer": "two"
    }
    ]
}

# ------------------------------------------
# Template banks for Level 2 – Intermediate
# ------------------------------------------
level_2 = {
    "TFQ": [
        lambda: {"question": "Average-case time complexity of Bubble Sort is O(n^2). (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort always uses additional memory. (True/False)", "answer": "False"},
        lambda: {"question": "Optimized Bubble Sort stops early if no swaps happen in a pass. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is unstable. (True/False)", "answer": "False"},
        lambda: {"question": "Bubble Sort’s space complexity is O(1). (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort has the same average and worst-case time complexity.", "answer": "True"},
            lambda: {"question": "Bubble Sort requires additional memory proportional to the input size.", "answer": "False"},
            lambda: {"question": "Bubble Sort always performs exactly n-1 passes.", "answer": "False"},
            lambda: {"question": "In the best-case scenario, Bubble Sort can perform in O(n) time.", "answer": "True"},
            lambda: {"question": "A single misplaced element at the start can delay sorting in Bubble Sort.", "answer": "True"},
            lambda: {"question": "Bubble Sort uses recursion internally.", "answer": "False"},
            lambda: {"question": "Bubble Sort can be optimized by ignoring the last sorted elements in each pass.", "answer": "True"},
            lambda: {"question": "Bubble Sort is an example of a divide-and-conquer algorithm.", "answer": "False"},
            lambda: {"question": "Bubble Sort is always the best choice for sorting small lists.", "answer": "False"},
            lambda: {"question": "Bubble Sort does not maintain the input order of equal elements.", "answer": "False"},
    ],
    "MCQ": [
        lambda: (lambda n=random.randint(5, 9): {
    "question": f"How many comparisons are done for array of length {n}?",
    "options": [str((n*(n-1))//2), str(n*n), str(n-1), str(n+1)],
    "answer": str((n*(n-1))//2)
})()
,
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
            "question": f"For array {generate_array()} how many total swaps in worst case?",
            "options": ["n-1", "n(n-1)/2", "log n", "n^2"],
            "answer": "n(n-1)/2"
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
        "question": "Which element does Bubble Sort compare first in an array?",
        "options": ["First and second", "Last two", "Middle two", "Random pair"],
        "answer": "First and second"
    },
    lambda: {
        "question": "Bubble Sort is classified as which type of sorting algorithm?",
        "options": ["Selection Sort", "Exchange Sort", "Insertion Sort", "Quick Sort"],
        "answer": "Exchange Sort"
    }   
    ],
    "ECQ": [
        lambda: {"question": "Describe how optimization using a swap flag enhances Bubble Sort.","answer": "It stops sorting if no swaps occur, reducing unnecessary passes."},
         lambda: {"question": "Explain how Bubble Sort can be optimized to detect already sorted arrays.", "answer": "By checking if any swaps were made during a pass; if none were made, sorting is complete."},
            lambda: {"question": "How does the time complexity of Bubble Sort compare to Insertion Sort in most cases?", "answer": "Bubble Sort is generally slower; Insertion Sort tends to be faster for nearly sorted arrays."},
            lambda: {"question": "Explain the role of the 'flag' variable in optimized Bubble Sort implementations.", "answer": "It tracks whether any swaps were made in a pass to determine early termination."},
            lambda: {"question": "Why is Bubble Sort considered inefficient despite being stable and simple?", "answer": "Due to its O(n²) time complexity, it becomes very slow for large datasets."},
            lambda: {"question": "In what scenario might Bubble Sort actually outperform more complex algorithms?", "answer": "On very small datasets or nearly sorted arrays due to its simplicity."},
            lambda: {"question": "How does Bubble Sort behave on a reverse-sorted array?", "answer": "It performs the maximum number of comparisons and swaps, leading to worst-case performance."},
            lambda: {"question": "Why does the number of comparisons reduce in each pass of Bubble Sort?", "answer": "Because the largest elements get sorted to the end, they don’t need to be compared again."},
            lambda: {"question": "How can you track the number of swaps performed in Bubble Sort?", "answer": "By using a counter that increments each time a swap is made."},
            lambda: {"question": "Explain how Bubble Sort compares elements in terms of array indices.", "answer": "It compares each element with the next one (i and i+1) in the loop."},
            lambda: {"question": "Describe a variation of Bubble Sort that improves performance.", "answer": "Optimized Bubble Sort terminates early and avoids redundant comparisons by reducing the iteration range."},
    ],
    "EXPQ": [
        lambda: {
            "question": "Fill in the blank: Best-case time complexity of Bubble Sort is O(__)",
            "answer": "n"
        },
         lambda: {
        "question": "Fill in the blank: The worst-case number of swaps in Bubble Sort is n(__)/2",
        "answer": "n-1"
    },
    lambda: {
        "question": "Complete the sentence: The optimization flag in Bubble Sort helps to detect __.",
        "answer": "no swaps"
    }
        
    ]
}

# ------------------------------------------
# Template banks for Level 3 – Advanced
# ------------------------------------------
level_3 = {
    "TFQ": [
        lambda: {"question": "Bubble Sort is usually not used in real-world applications. (True/False)", "answer": "True"},
        lambda: {"question": "Recursive Bubble Sort is possible. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort is faster than Quick Sort. (True/False)", "answer": "False"},
        lambda: {"question": "Worst-case for Bubble Sort is on a reversed array. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort adapts well to nearly sorted data. (True/False)", "answer": "True"},
        lambda: {"question": "Bubble Sort has quadratic time complexity due to nested loops.", "answer": "True"},
            lambda: {"question": "The adaptive property of Bubble Sort makes it faster than Quick Sort for large arrays.", "answer": "False"},
            lambda: {"question": "Bubble Sort can be implemented recursively.", "answer": "True"},
            lambda: {"question": "Bubble Sort is not suitable for linked list data structures.", "answer": "False"},
            lambda: {"question": "In Bubble Sort, the time complexity can be improved to linear for sorted data.", "answer": "True"},
            lambda: {"question": "Bubble Sort’s worst-case performance is when the array is already sorted.", "answer": "False"},
            lambda: {"question": "The number of total comparisons in Bubble Sort is independent of array contents.", "answer": "True"},
            lambda: {"question": "Bubble Sort cannot be parallelized.", "answer": "False"},
            lambda: {"question": "In Bubble Sort, after each full pass, the smallest unsorted element moves to the end.", "answer": "False"},
            lambda: {"question": "Bubble Sort guarantees sorting after (n-1) passes regardless of input.", "answer": "True"},
    ],
    "MCQ": [
        lambda: {
            "question": "What’s the swap count in worst-case for n=6?",
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
            "question": "What’s a practical use case for Bubble Sort?",
            "options": ["Teaching algorithm basics", "Sorting big data", "Optimizing DB queries", "AI modeling"],
            "answer": "Teaching algorithm basics"
        },
          lambda: {
        "question": "Which condition ends the recursion in recursive Bubble Sort?",
        "options": ["No swaps", "Array size 0 or 1", "Max element reached", "Array is sorted"],
        "answer": "Array size 0 or 1"
    },
    lambda: {
        "question": "Why is Bubble Sort considered inefficient for large datasets?",
        "options": ["High time complexity", "High memory use", "Unstable sort", "Complex implementation"],
        "answer": "High time complexity"
    }
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
        }
    ],
    "ECQ": [
        lambda: {  "question": "Describe how recursive Bubble Sort works.",  "answer": "Sorts the first n-1 elements recursively after bubbling max to end."},
        lambda: {"question": "How does recursive Bubble Sort work compared to the iterative version?", "answer": "It reduces the problem size with each recursive call, mimicking the outer loop of the iterative version."},
            lambda: {"question": "Why might Bubble Sort be preferred in embedded systems with memory constraints?", "answer": "It requires no extra memory allocation, making it suitable for environments with strict memory usage."},
            lambda: {"question": "Compare Bubble Sort’s space complexity with that of Merge Sort.", "answer": "Bubble Sort is O(1) in space, while Merge Sort requires O(n) extra space."},
            lambda: {"question": "Discuss the cache performance of Bubble Sort.", "answer": "Poor cache performance due to repeated scanning and adjacent swaps which do not exploit spatial locality."},
            lambda: {"question": "How would you modify Bubble Sort to sort in descending order?", "answer": "Reverse the comparison logic (e.g., if arr[i] < arr[i+1], then swap)."},
            lambda: {"question": "What is the impact of input distribution on Bubble Sort performance?", "answer": "Nearly sorted arrays result in early termination and improved performance."},
            lambda: {"question": "Why is Bubble Sort not preferred in modern libraries and frameworks?", "answer": "Due to its inefficiency and better alternatives like Timsort, Merge Sort, and Quick Sort."},
            lambda: {"question": "Explain how Bubble Sort could be visualized in a GUI tool.", "answer": "By animating bar heights and showing swaps during each pass to depict bubbling effect."},
            lambda: {"question": "How can you measure the total number of operations performed by Bubble Sort?", "answer": "By counting total comparisons and swaps in a single run."},
            lambda: {"question": "Compare and contrast Bubble Sort with Selection Sort in terms of swap behavior.", "answer": "Bubble Sort swaps more frequently, while Selection Sort minimizes swaps but still has O(n²) comparisons."},
    ],
    "EXPQ": [
        lambda: {
            "question": "Complete the recursive base case: if n <= __ then return.",
            "answer": "1"
        },
         lambda: {
        "question": "Complete the expression: Recursive Bubble Sort calls itself with n minus __ elements.",
        "answer": "1"
    },
    lambda: {
        "question": "Fill in the blank: Bubble Sort has a space complexity of O(__).",
        "answer": "1"
    }
    ]
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

