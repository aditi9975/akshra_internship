import random
import json

QUESTION_TYPES = ["TFQ", "MCQ", "MTQ", "ECQ", "EXPQ"]
LEVELS = {
    "1": "Foundational",
    "2": "Intermediate",
    "3": "Advanced"
}

def generate_array_heap(size=None, low=1, high=50):
    if size is None:
        size = random.randint(5, 10)
    return [random.randint(low, high) for _ in range(size)]

# Level 1 (Foundational) Questions
level_1_heap = {
    "TFQ": [
        lambda: {"question": "Heap Sort builds a binary heap from the input array. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort always sorts in descending order. (True/False)", "answer": "False"},
        lambda: {"question": "A max-heap is used to implement Heap Sort for ascending order. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort has an average time complexity of O(n log n). (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort requires extra memory proportional to the array size. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort is an unstable sorting algorithm. (True/False)", "answer": "True"},
        lambda: {"question": "In a max-heap, the largest element is always at the root. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort is an example of a comparison-based sorting algorithm. (True/False)", "answer": "True"},
        lambda: {"question": "The heap property must be maintained after extracting the root during Heap Sort. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort sorts the array in-place. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort is slower than Bubble Sort in all cases. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort always uses recursion. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort converts the input array into a min-heap for ascending sort. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort is efficient for sorting large datasets. (True/False)", "answer": "True"},
        lambda: {"question": "The process of maintaining heap property after changes is called 'heapify'. (True/False)", "answer": "True"},
    ],
    "MCQ": [
        lambda: {
            "question": "What data structure is primarily used in Heap Sort?",
            "options": ["Linked List", "Binary Heap", "Queue", "Stack"],
            "answer": "Binary Heap"
        },
        lambda: {
            "question": f"In the array {generate_array_heap()}, which node represents the root of the max-heap?",
            "options": ["Index 0", "Index 1", "Last index", "Middle index"],
            "answer": "Index 0"
        },
        lambda: {
            "question": "What is the time complexity of building a heap from an unordered array?",
            "options": ["O(n)", "O(n log n)", "O(log n)", "O(n^2)"],
            "answer": "O(n)"
        },
        lambda: {
            "question": "Which of the following best describes 'heapify'?",
            "options": ["Sorting the array", "Maintaining heap property", "Swapping root and last node", "Deleting nodes"],
            "answer": "Maintaining heap property"
        },
        lambda: {
            "question": "Heap Sort's space complexity is:",
            "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
            "answer": "O(1)"
        },
        lambda: {
            "question": "After extracting the root in Heap Sort, what is the next step?",
            "options": ["Rebuild the heap from scratch", "Heapify the reduced heap", "Sort the extracted elements", "Reverse the array"],
            "answer": "Heapify the reduced heap"
        }
    ],
    "MTQ": [
        lambda: {
            "question": "Match the Heap Sort terms with their meanings:\n1. Heapify\n2. Max-Heap\n3. Root\n4. Extraction",
            "pairs": {
                "1": "Process to maintain heap property",
                "2": "Heap where parent is larger than children",
                "3": "Top node of the heap",
                "4": "Removing root and reducing heap size"
            },
            "answer": "1->Process to maintain heap property, 2->Heap where parent is larger than children, 3->Top node of the heap, 4->Removing root and reducing heap size"
        }
    ],
    "ECQ": [
        lambda: {"question": "Explain why Heap Sort is considered an in-place sorting algorithm.", "answer": "Because it sorts the array by rearranging elements within the original array without extra space."},
        lambda: {"question": "Describe the purpose of 'heapify' in Heap Sort.", "answer": "Heapify restores the heap property after extracting the root or during heap building."},
        lambda: {"question": "Why is Heap Sort faster than Bubble Sort on large datasets?", "answer": "Because Heap Sort has O(n log n) time complexity versus Bubble Sort's O(n²)."},
        lambda: {"question": "Explain the difference between a max-heap and a min-heap.", "answer": "Max-heap's parent nodes are greater or equal to children; min-heap's parents are smaller or equal."},
        lambda: {"question": "What is the significance of the root node in Heap Sort?", "answer": "It holds the maximum value in a max-heap and is extracted for sorting."},
        lambda: {"question": "How does Heap Sort extract sorted elements from the heap?", "answer": "It swaps the root with the last element, reduces heap size, and heapifies."},
        lambda: {"question": "Why is the time complexity to build a heap O(n) and not O(n log n)?", "answer": "Because heapify runs faster on lower levels and the total work sums to O(n)."},
        lambda: {"question": "How can Heap Sort be modified to sort in descending order?", "answer": "By building a min-heap instead of a max-heap."},
        lambda: {"question": "What role does the binary tree structure play in Heap Sort?", "answer": "It allows efficient parent-child comparisons and heap property maintenance."},
        lambda: {"question": "Why is Heap Sort not considered a stable sort?", "answer": "Because equal elements may be reordered during heapify and swaps."},
    ],
    "EXPQ": [
        lambda: {
            "question": "Complete the expression: Heap Sort has a time complexity of O(__ log __).",
            "answer": "n, n"
        },
        lambda: {
            "question": "Fill in the blank: Heap Sort builds the __ heap from the array before sorting.",
            "answer": "max"
        },
        lambda: {
            "question": "Complete: The operation that maintains the heap property after extraction is called __.",
            "answer": "heapify"
        }
    ]
}

# Level 2 (Intermediate) Questions
level_2_heap = {
    "TFQ": [
        lambda: {"question": "The 'heapify' process has a worst-case complexity of O(log n). (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort's average and worst-case time complexity are both O(n log n). (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort is a stable sorting algorithm. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort always requires additional memory proportional to input size. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort works by repeatedly removing the root of the heap. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort performs better than Quick Sort in the average case. (True/False)", "answer": "False"},
        lambda: {"question": "The height of a binary heap with n nodes is O(log n). (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort can be implemented without recursion. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort can be adapted to work with a min-heap for descending order. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort is not suitable for real-time systems due to its worst-case behavior. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort extracts the smallest element in a max-heap during sorting. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort involves swapping the root with the last heap element in each iteration. (True/False)", "answer": "True"},
        lambda: {"question": "The heap structure used in Heap Sort is a complete binary tree. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort has a best-case time complexity of O(n). (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort is comparison-based but not in-place. (True/False)", "answer": "False"},
    ],
    "MCQ": [
        lambda: {
            "question": "Given a heap array: [9, 5, 6, 2, 3], what is the index of the parent of element at index 3?",
            "options": ["1", "0", "2", "3"],
            "answer": "1"
        },
        lambda: {
            "question": "During Heap Sort, which element is swapped with the root in each iteration?",
            "options": ["Last element of heap", "First element", "Middle element", "Smallest element"],
            "answer": "Last element of heap"
        },
        lambda: {
            "question": "Which of the following is NOT a step in Heap Sort?",
            "options": ["Build max-heap", "Extract max", "Heapify root", "Merge sorted subarrays"],
            "answer": "Merge sorted subarrays"
        },
        lambda: {
            "question": "Heap Sort is efficient because it:",
            "options": ["Uses extra arrays", "Avoids recursion", "Maintains a heap structure", "Uses linked lists"],
            "answer": "Maintains a heap structure"
        },
        lambda: {
            "question": "What is the worst-case time complexity of heapify operation?",
            "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
            "answer": "O(log n)"
        }
    ],
    "MTQ": [
        lambda: {
            "question": "Match the terms to their Heap Sort descriptions:\n1. Build Heap\n2. Extract Root\n3. Heapify\n4. Swap",
            "pairs": {
                "1": "Construct initial heap from array",
                "2": "Remove the root element",
                "3": "Restore heap property after changes",
                "4": "Exchange two elements in array"
            },
            "answer": "1->Construct initial heap from array, 2->Remove the root element, 3->Restore heap property after changes, 4->Exchange two elements in array"
        }
    ],
    "ECQ": [
        lambda: {"question": "Explain why Heap Sort is not stable.", "answer": "Because during heapify, equal elements may be swapped changing their original order."},
        lambda: {"question": "Describe the heap property in a max-heap.", "answer": "Each parent node is greater than or equal to its children."},
        lambda: {"question": "How does Heap Sort maintain the heap structure after extracting the root?", "answer": "By calling heapify on the root after swapping with the last element."},
        lambda: {"question": "What is the significance of the complete binary tree property in Heap Sort?", "answer": "It allows the heap to be efficiently stored in an array."},
        lambda: {"question": "How is the height of a heap related to the number of elements?", "answer": "The height is approximately log base 2 of the number of elements."},
        lambda: {"question": "Explain how Heap Sort handles duplicate values.", "answer": "Duplicates are treated like any elements; stability is not guaranteed."},
        lambda: {"question": "What happens if heapify is not called after swapping the root?", "answer": "Heap property will be violated and sorting will be incorrect."},
        lambda: {"question": "Why is heapify considered a recursive or iterative operation?", "answer": "Because it may need to be applied down multiple levels to restore heap."},
        lambda: {"question": "Describe how Heap Sort differs from Quick Sort in terms of worst-case time complexity.", "answer": "Heap Sort is O(n log n) always; Quick Sort can degrade to O(n^2)."},
        lambda: {"question": "What is the impact of using a min-heap instead of a max-heap in Heap Sort?", "answer": "Sorting order changes from ascending to descending."},
    ],
    "EXPQ": [
        lambda: {
            "question": "Fill in the blanks: In a heap array, the children of node at index i are at indices __ and __.",
            "answer": "2*i + 1, 2*i + 2"
        },
        lambda: {
            "question": "Complete the statement: After swapping root and last element, Heap Sort calls __ to restore heap property.",
            "answer": "heapify"
        },
        lambda: {
            "question": "Fill in: The parent of a node at index i is at index __.",
            "answer": "(i-1)//2"
        }
    ]
}

# Level 3 (Advanced) Questions
level_3_heap = {
    "TFQ": [
        lambda: {"question": "Heap Sort requires the entire array to be loaded in memory before sorting. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort can be parallelized efficiently for large datasets. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort is an in-place algorithm but not stable. (True/False)", "answer": "True"},
        lambda: {"question": "The height of a heap with n nodes is floor(log₂ n). (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort cannot be implemented using a min-heap. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort has guaranteed O(n log n) time complexity in all cases. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort is typically faster than Merge Sort in practice. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort rearranges elements in place without auxiliary arrays. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort uses recursion for heapify by definition. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort can be adapted to sort linked lists efficiently. (True/False)", "answer": "False"},
    ],
    "MCQ": [
        lambda: {
            "question": "What is the height of a binary heap with 31 nodes?",
            "options": ["4", "5", "6", "7"],
            "answer": "5"
        },
        lambda: {
            "question": f"Given the array {generate_array_heap(7)}, what is the index of the left child of the element at index 2?",
            "options": ["4", "5", "6", "3"],
            "answer": "5"
        },
        lambda: {
            "question": "During Heap Sort, when is the heap property restored?",
            "options": [
                "Before building the heap",
                "After extracting the root",
                "At the end of sorting",
                "When array is sorted"
            ],
            "answer": "After extracting the root"
        },
        lambda: {
            "question": "Which of the following is NOT true about Heap Sort?",
            "options": [
                "It uses a binary heap",
                "It is stable",
                "It has O(n log n) time complexity",
                "It sorts in-place"
            ],
            "answer": "It is stable"
        },
        lambda: {
            "question": "In Heap Sort, what is the parent index of the element at index 6?",
            "options": ["2", "3", "1", "0"],
            "answer": "2"
        }
    ],
    "MTQ": [
        lambda: {
            "question": "Match the Heap Sort terms with their descriptions:\n1. Complete Binary Tree\n2. Heapify\n3. Extract Max\n4. Swap",
            "pairs": {
                "1": "A binary tree where all levels are fully filled except possibly the last",
                "2": "Process to maintain heap property after modification",
                "3": "Removing the root element (maximum in max-heap)",
                "4": "Interchange positions of two elements"
            },
            "answer": "1->A binary tree where all levels are fully filled except possibly the last, 2->Process to maintain heap property after modification, 3->Removing the root element (maximum in max-heap), 4->Interchange positions of two elements"
        }
    ],
    "ECQ": [
        lambda: {"question": "Explain the difference between the build-heap and heapify procedures in Heap Sort.", "answer": "Build-heap creates the initial heap from the array, calling heapify on nodes; heapify restores heap property at a node after extraction or swap."},
        lambda: {"question": "Why does Heap Sort have better worst-case time complexity than Quick Sort?", "answer": "Heap Sort is O(n log n) always; Quick Sort degrades to O(n²) in worst cases."},
        lambda: {"question": "Describe how indices for parent and children are calculated in a heap array representation.", "answer": "Parent at i has children at 2i+1 (left) and 2i+2 (right). Parent index is floor((i-1)/2)."},
        lambda: {"question": "What is the significance of using a complete binary tree in Heap Sort?", "answer": "Ensures efficient array representation and balanced height for O(log n) operations."},
        lambda: {"question": "How can Heap Sort be adapted for sorting objects with keys?", "answer": "By defining a comparison on keys during heapify and swaps."},
        lambda: {"question": "Explain why Heap Sort is not stable with an example.", "answer": "Equal elements may change relative order during swaps; e.g., two equal values at different positions may swap."},
        lambda: {"question": "What happens when the last element is extracted during Heap Sort?", "answer": "Heap size reduces, and heapify restores the heap."},
        lambda: {"question": "How does Heap Sort handle memory compared to Merge Sort?", "answer": "Heap Sort sorts in-place using no additional arrays; Merge Sort requires extra space."},
        lambda: {"question": "Explain the iterative version of heapify.", "answer": "Iteratively swaps a node with largest child until heap property is restored."},
        lambda: {"question": "How does Heap Sort’s performance change with nearly sorted data?", "answer": "It has consistent O(n log n) time regardless of input order."},
    ],
    "EXPQ": [
        lambda: {
            "question": "Complete: The children of node at index i are at indices __ and __ in the heap array.",
            "answer": "2*i + 1, 2*i + 2"
        },
        lambda: {
            "question": "Fill in: The parent of node at index i is at index __.",
            "answer": "(i-1)//2"
        },
        lambda: {
            "question": "Complete the statement: Heap Sort calls __ to maintain heap after extracting max.",
            "answer": "heapify"
        },
        lambda: {
            "question": "Fill in the blank: Heap Sort builds a __ binary tree.",
            "answer": "complete"
        },
        lambda: {
            "question": "Complete: Heap Sort’s worst-case complexity is __.",
            "answer": "O(n log n)"
        }
    ]
}

heap_question_bank = {
    "1": level_1_heap,
    "2": level_2_heap,
    "3": level_3_heap,
}

# Function to generate and print questions by level and type without repeats and with formatting

def generate_questions_heap(level: str, num: int):
    if level not in heap_question_bank:
        print("Invalid level")
        return []

    selected_templates = heap_question_bank[level]
    all_questions = []

    # Generate all unique questions from templates
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

    # If requested number <= unique questions, shuffle and return subset
    if num <= len(unique_questions):
        random.shuffle(unique_questions)
        return unique_questions[:num]

    # If more requested than available, repeat questions after shuffling
    repeated_questions = []
    while len(repeated_questions) < num:
        random.shuffle(unique_questions)
        repeated_questions.extend(unique_questions)

    return repeated_questions[:num]

# Main driver
if __name__ == "__main__":
    level = input("Choose Level (1: Foundational, 2: Intermediate, 3: Advanced): ").strip()
    num_qs = int(input("Enter total number of questions to generate: "))
    questions = generate_questions_heap(level, num_qs)

    for idx, q in enumerate(questions, start=1):
        print(f"Q{idx}. {q['question']}")
        if "options" in q:
            for i, opt in enumerate(q["options"], start=1):
                print(f"   {chr(64+i)}. {opt}")
        if "pairs" in q:
            print("Match the following:")
            for key, val in q["pairs"].items():
                print(f"  {key} -> {val}")
        print(f"Answer: {q['answer']}\n")