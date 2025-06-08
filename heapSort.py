import random
import json

QUESTION_TYPES = ["TFQ", "MCQ", "MTQ", "ECQ", "EXPQ"]
LEVELS = {
    "1": "Foundational",
    "2": "Intermediate",
    "3": "Advanced"
}

import random

def generate_array_heap1(size=None, low=1, high=50):
    if size is None:
        size = random.randint(5, 10)
    return [random.randint(low, high) for _ in range(size)]

level_1 = {
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
        lambda: {"question": "Heap Sort works better on linked lists than arrays. (True/False)", "answer": "False"},
        lambda: {"question": "Min-heap is used to sort elements in ascending order using Heap Sort. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort can be used for priority queue implementations. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort maintains the original order of equal elements. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort performs better than Merge Sort in most practical cases. (True/False)", "answer": "False"},
        lambda: {"question": "In Heap Sort, each node's value must be greater than both of its children in a max-heap. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort's worst-case time complexity is O(n log n). (True/False)", "answer": "True"},
        lambda: {"question": "The number of comparisons in Heap Sort depends on the structure of the heap. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort is often used in embedded systems because of its stability. (True/False)", "answer": "False"},
        lambda: {"question": "Building a heap takes more time than sorting in Heap Sort. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort never requires swapping of elements. (True/False)", "answer": "False"}
    ],

    "MCQ": [
        # 25 unique MCQ questions
        lambda: {
            "question": "Which of the following is true about a max-heap?",
            "options": ["Parent node is smaller", "Root is the smallest", "Parent is greater or equal to children", "All values are equal"],
            "answer": "Parent is greater or equal to children"
        },
        lambda: {
            "question": "What is the height of a binary heap with n elements?",
            "options": ["log n", "n", "n log n", "sqrt(n)"],
            "answer": "log n"
        },
        lambda: {
            "question": "What is the best case time complexity of Heap Sort?",
            "options": ["O(n)", "O(log n)", "O(n log n)", "O(n^2)"],
            "answer": "O(n log n)"
        },
        lambda: {
            "question": "Which of these is not an application of heaps?",
            "options": ["Priority queues", "Graph traversal", "Sorting", "Median finding"],
            "answer": "Graph traversal"
        },
        lambda: {
            "question": "What happens when you insert a new element into a heap?",
            "options": ["Rebuild heap from scratch", "Heapify upwards", "Heapify downwards", "Sort all elements"],
            "answer": "Heapify upwards"
        },
        lambda: {
            "question": "Which of the following represents the parent index of i in a heap?",
            "options": ["(i+1)//2", "(i-1)//2", "2*i", "2*i+1"],
            "answer": "(i-1)//2"
        },
        lambda: {
            "question": "Which heap is used for ascending order Heap Sort?",
            "options": ["Max Heap", "Min Heap", "Binary Tree", "AVL Tree"],
            "answer": "Max Heap"
        },
        lambda: {
            "question": "In Heap Sort, what is the first major step?",
            "options": ["Swapping elements", "Heapify", "Build Heap", "Sort"],
            "answer": "Build Heap"
        },
        lambda: {
            "question": "Which of these operations is not required in Heap Sort?",
            "options": ["Heapify", "Swap", "Insert", "Extract max"],
            "answer": "Insert"
        },
        lambda: {
            "question": "How many children can a node have in a binary heap?",
            "options": ["1", "2", "3", "4"],
            "answer": "2"
        },
        lambda: {
            "question": "What is the typical array representation of the root node in a heap?",
            "options": ["Index 0", "Index 1", "Last index", "Middle index"],
            "answer": "Index 0"
        },
        lambda: {
            "question": "Which of the following is a property of a max-heap?",
            "options": ["Parent is always smaller than children", "Children are always greater than parent", "Parent is greater than or equal to children", "Nodes have equal values"],
            "answer": "Parent is greater than or equal to children"
        },
        lambda: {
            "question": "In Heap Sort, after building the heap, what is the next step?",
            "options": ["Sorting the heap", "Extract max repeatedly", "Rebuilding heap", "Deleting nodes"],
            "answer": "Extract max repeatedly"
        },
        lambda: {
            "question": "Which algorithmic technique does Heap Sort use?",
            "options": ["Divide and conquer", "Dynamic programming", "Greedy", "Backtracking"],
            "answer": "Divide and conquer"
        },
        lambda: {
            "question": "What is the time complexity of inserting an element into a heap of size n?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
            "answer": "O(log n)"
        },
        lambda: {
            "question": "Heap Sort is best suited for which of the following?",
            "options": ["Small datasets", "Datasets that fit in memory", "Large datasets", "Linked lists"],
            "answer": "Large datasets"
        },
        lambda: {
            "question": "The heap data structure is a __.",
            "options": ["Complete binary tree", "Full binary tree", "Perfect binary tree", "Balanced binary tree"],
            "answer": "Complete binary tree"
        },
        lambda: {
            "question": "In an array-based heap, the left child of node i is at index __.",
            "options": ["2*i + 1", "2*i", "i//2", "i-1"],
            "answer": "2*i + 1"
        },
        lambda: {
            "question": "Which step in Heap Sort restores the heap property after removal of the root?",
            "options": ["Heapify", "Insertion", "Deletion", "Traversal"],
            "answer": "Heapify"
        },
        lambda: {
            "question": "Heap Sort can be classified as a __ sort.",
            "options": ["Stable", "Unstable", "Adaptive", "Non-comparison"],
            "answer": "Unstable"
        },
        lambda: {
            "question": "What type of heap does Heap Sort use to sort in ascending order?",
            "options": ["Min heap", "Max heap", "Fibonacci heap", "Binomial heap"],
            "answer": "Max heap"
        },
        lambda: {
            "question": "The process of swapping the root with the last element and reducing heap size is called __.",
            "options": ["Extraction", "Insertion", "Heapify", "Sorting"],
            "answer": "Extraction"
        },
        lambda: {
            "question": "In Heap Sort, the array is sorted by __.",
            "options": ["Repeated extraction of root", "Sorting heap nodes", "Inserting elements", "Building a linked list"],
            "answer": "Repeated extraction of root"
        },
        lambda: {
            "question": "Which of the following is true about the space complexity of Heap Sort?",
            "options": ["O(1) extra space", "O(n) extra space", "O(log n) extra space", "O(n log n) extra space"],
            "answer": "O(1) extra space"
        }
    ],

    "MTQ": [
        # 25 unique Match The Following question templates
        lambda: {
            "question": "Match these Heap Sort terms with their meanings:\n1. Heapify\n2. Max-Heap\n3. Root\n4. Extraction\n5. Build Heap",
            "pairs": {
                "1": "Process to maintain heap property",
                "2": "Heap where parent is larger than children",
                "3": "Top node of the heap",
                "4": "Removing root and reducing heap size",
                "5": "Converting array into a heap"
            },
            "answer": "1->Process to maintain heap property, 2->Heap where parent is larger than children, 3->Top node of the heap, 4->Removing root and reducing heap size, 5->Converting array into a heap"
        },
        lambda: {
            "question": "Match these Heap Sort steps with their descriptions:\n1. Heapify\n2. Extract Max\n3. Swap\n4. Build Heap\n5. Sort",
            "pairs": {
                "1": "Restore heap property",
                "2": "Remove root element",
                "3": "Exchange two elements",
                "4": "Create heap from array",
                "5": "Order elements"
            },
            "answer": "1->Restore heap property, 2->Remove root element, 3->Exchange two elements, 4->Create heap from array, 5->Order elements"
        },
        lambda: {
            "question": "Match terms:\n1. Parent\n2. Child\n3. Leaf\n4. Root\n5. Node",
            "pairs": {
                "1": "Node with children",
                "2": "Node connected below parent",
                "3": "Node without children",
                "4": "Top node in heap",
                "5": "Element in tree"
            },
            "answer": "1->Node with children, 2->Node connected below parent, 3->Node without children, 4->Top node in heap, 5->Element in tree"
        },
        lambda: {
            "question": "Match the heap types:\n1. Max-Heap\n2. Min-Heap\n3. Binary Heap\n4. Fibonacci Heap\n5. Binomial Heap",
            "pairs": {
                "1": "Heap with largest element at root",
                "2": "Heap with smallest element at root",
                "3": "Complete binary tree",
                "4": "Heap with fast decrease key",
                "5": "Heap supporting merge operations"
            },
            "answer": "1->Heap with largest element at root, 2->Heap with smallest element at root, 3->Complete binary tree, 4->Heap with fast decrease key, 5->Heap supporting merge operations"
        },
        lambda: {
            "question": "Match the Heap Sort algorithm phases:\n1. Build Heap\n2. Sort\n3. Extract Max\n4. Heapify\n5. Initialize",
            "pairs": {
                "1": "Convert array into heap",
                "2": "Order elements after heap construction",
                "3": "Remove root repeatedly",
                "4": "Fix heap property",
                "5": "Start process"
            },
            "answer": "1->Convert array into heap, 2->Order elements after heap construction, 3->Remove root repeatedly, 4->Fix heap property, 5->Start process"
        },
        lambda: {
            "question": "Match these Heap Sort terms with explanations:\n1. Extraction\n2. Insertion\n3. Heapify Up\n4. Heapify Down\n5. Root",
            "pairs": {
                "1": "Remove max element",
                "2": "Add new element",
                "3": "Restore heap from bottom",
                "4": "Restore heap from top",
                "5": "Top of heap"
            },
            "answer": "1->Remove max element, 2->Add new element, 3->Restore heap from bottom, 4->Restore heap from top, 5->Top of heap"
        },
        lambda: {
            "question": "Match these terms:\n1. Complete Binary Tree\n2. Heap Property\n3. Max Element\n4. Leaf\n5. Parent",
            "pairs": {
                "1": "Every level fully filled except last",
                "2": "Parent ≥ children",
                "3": "Root in max-heap",
                "4": "Node without children",
                "5": "Node with children"
            },
            "answer": "1->Every level fully filled except last, 2->Parent ≥ children, 3->Root in max-heap, 4->Node without children, 5->Node with children"
        },
        lambda: {
            "question": "Match the operations:\n1. Build Heap\n2. Heapify\n3. Extract Max\n4. Swap\n5. Insert",
            "pairs": {
                "1": "Create heap",
                "2": "Fix heap property",
                "3": "Remove root",
                "4": "Exchange elements",
                "5": "Add element"
            },
            "answer": "1->Create heap, 2->Fix heap property, 3->Remove root, 4->Exchange elements, 5->Add element"
        },
        lambda: {
            "question": "Match the Heap Sort steps:\n1. Initialize array\n2. Build heap\n3. Extract max\n4. Heapify\n5. Sorted array",
            "pairs": {
                "1": "Prepare input",
                "2": "Heap construction",
                "3": "Remove root repeatedly",
                "4": "Restore heap after extraction",
                "5": "Final output"
            },
            "answer": "1->Prepare input, 2->Heap construction, 3->Remove root repeatedly, 4->Restore heap after extraction, 5->Final output"
        },
        lambda: {
            "question": "Match the terms:\n1. Max-Heap\n2. Min-Heap\n3. Binary Tree\n4. Heapify\n5. Root",
            "pairs": {
                "1": "Largest element at root",
                "2": "Smallest element at root",
                "3": "Tree with at most two children",
                "4": "Maintain heap property",
                "5": "Top node"
            },
            "answer": "1->Largest element at root, 2->Smallest element at root, 3->Tree with at most two children, 4->Maintain heap property, 5->Top node"
        },
        lambda: {
            "question": "Match the array indices:\n1. Parent of i\n2. Left child of i\n3. Right child of i\n4. Root index\n5. Last index",
            "pairs": {
                "1": "(i-1)//2",
                "2": "2*i + 1",
                "3": "2*i + 2",
                "4": "0",
                "5": "n-1"
            },
            "answer": "1->(i-1)//2, 2->2*i + 1, 3->2*i + 2, 4->0, 5->n-1"
        },
        lambda: {
            "question": "Match these Heap Sort concepts:\n1. Time Complexity\n2. Space Complexity\n3. Stability\n4. In-place\n5. Heap Type",
            "pairs": {
                "1": "O(n log n)",
                "2": "O(1)",
                "3": "Unstable",
                "4": "Yes",
                "5": "Max-Heap"
            },
            "answer": "1->O(n log n), 2->O(1), 3->Unstable, 4->Yes, 5->Max-Heap"
        },
        lambda: {
            "question": "Match these sorting concepts:\n1. Bubble Sort\n2. Merge Sort\n3. Heap Sort\n4. Quick Sort\n5. Insertion Sort",
            "pairs": {
                "1": "O(n^2), Stable",
                "2": "O(n log n), Stable",
                "3": "O(n log n), Unstable",
                "4": "O(n log n), Unstable",
                "5": "O(n^2), Stable"
            },
            "answer": "1->O(n^2), Stable, 2->O(n log n), Stable, 3->O(n log n), Unstable, 4->O(n log n), Unstable", 
},
 lambda: {
            "question": "Match these sorting terms:\n1. Stable\n2. In-place\n3. Time Complexity\n4. Space Complexity\n5. Unstable",
            "pairs": {
                "1": "Maintains relative order of equal elements",
                "2": "Uses constant extra space",
                "3": "Measure of runtime performance",
                "4": "Measure of extra memory usage",
                "5": "Does not maintain relative order"
            },
            "answer": "1->Maintains relative order of equal elements, 2->Uses constant extra space, 3->Measure of runtime performance, 4->Measure of extra memory usage, 5->Does not maintain relative order"
        },
        lambda: {
            "question": "Match Heap Sort terms with array indices:\n1. Parent\n2. Left Child\n3. Right Child\n4. Root Index\n5. Last Index",
            "pairs": {
                "1": "(i-1)//2",
                "2": "2*i + 1",
                "3": "2*i + 2",
                "4": "0",
                "5": "n - 1"
            },
            "answer": "1->(i-1)//2, 2->2*i + 1, 3->2*i + 2, 4->0, 5->n - 1"
        },
        lambda: {
            "question": "Match Heap Sort algorithm steps:\n1. Build Heap\n2. Heapify\n3. Extract Max\n4. Swap\n5. Sorted Output",
            "pairs": {
                "1": "Create max heap from array",
                "2": "Maintain heap property",
                "3": "Remove root element",
                "4": "Exchange root with last element",
                "5": "Result after repeated extraction"
            },
            "answer": "1->Create max heap from array, 2->Maintain heap property, 3->Remove root element, 4->Exchange root with last element, 5->Result after repeated extraction"
        },
        lambda: {
            "question": "Match these Heap Sort properties:\n1. Stability\n2. Space Complexity\n3. Time Complexity\n4. Heap Type\n5. Sorting Method",
            "pairs": {
                "1": "Unstable",
                "2": "O(1)",
                "3": "O(n log n)",
                "4": "Max-Heap",
                "5": "Comparison-based"
            },
            "answer": "1->Unstable, 2->O(1), 3->O(n log n), 4->Max-Heap, 5->Comparison-based"
        },
        lambda: {
            "question": "Match Heap Sort terms with their descriptions:\n1. Heapify Up\n2. Heapify Down\n3. Extraction\n4. Insertion\n5. Root",
            "pairs": {
                "1": "Restore heap from inserted node upwards",
                "2": "Restore heap from root downwards",
                "3": "Remove max element",
                "4": "Add new element",
                "5": "Top element of heap"
            },
            "answer": "1->Restore heap from inserted node upwards, 2->Restore heap from root downwards, 3->Remove max element, 4->Add new element, 5->Top element of heap"
        },
        lambda: {
            "question": "Match Heap Sort steps with their purpose:\n1. Build Heap\n2. Sort Heap\n3. Extract Max\n4. Heapify\n5. Initialize Array",
            "pairs": {
                "1": "Convert array to heap structure",
                "2": "Arrange sorted elements",
                "3": "Remove largest element repeatedly",
                "4": "Restore heap after extraction",
                "5": "Prepare input data"
            },
            "answer": "1->Convert array to heap structure, 2->Arrange sorted elements, 3->Remove largest element repeatedly, 4->Restore heap after extraction, 5->Prepare input data"
        },
        lambda: {
            "question": "Match these binary heap terms:\n1. Leaf\n2. Parent\n3. Node\n4. Root\n5. Complete Binary Tree",
            "pairs": {
                "1": "Node without children",
                "2": "Node with children",
                "3": "Element in heap",
                "4": "Top of heap",
                "5": "All levels filled except last"
            },
            "answer": "1->Node without children, 2->Node with children, 3->Element in heap, 4->Top of heap, 5->All levels filled except last"
        }
],
"ECQ": [
    lambda: {
        "question": "Explain what a binary heap is and why it is important in Heap Sort.",
        "answer": "A binary heap is a complete binary tree that satisfies the heap property, where each parent node is greater than or equal to its children (max-heap) or less than or equal (min-heap). It is important in Heap Sort because it allows efficient extraction of the maximum (or minimum) element to sort the array."
    },
    lambda: {
        "question": "Describe the process of 'heapify' in Heap Sort.",
        "answer": "Heapify is the process of maintaining the heap property by rearranging nodes in the binary heap after insertion or removal, ensuring each parent node satisfies the heap condition relative to its children."
    },
    lambda: {
        "question": "Why does Heap Sort have O(n log n) time complexity?",
        "answer": "Heap Sort has O(n log n) time complexity because building the heap takes O(n) time and each of the n extraction operations requires O(log n) time to restore the heap property."
    },
    lambda: {
        "question": "Explain why Heap Sort is considered an in-place algorithm.",
        "answer": "Heap Sort is in-place because it sorts the array without requiring additional significant memory beyond the input array itself, by repeatedly swapping elements within the same array."
    },
    lambda: {
        "question": "What is the difference between a max-heap and a min-heap?",
        "answer": "A max-heap is a heap where each parent node is greater than or equal to its children, ensuring the largest element is at the root. A min-heap is the opposite, with each parent node less than or equal to its children, so the smallest element is at the root."
    },
    lambda: {
        "question": "Explain why Heap Sort is not a stable sorting algorithm.",
        "answer": "Heap Sort is not stable because it swaps elements that are not necessarily adjacent, which can change the relative order of equal elements."
    },
    lambda: {
        "question": "Describe how the array representation of a heap works.",
        "answer": "In an array representation of a heap, the root is at index 0, and for any node at index i, its left child is at 2*i + 1 and its right child at 2*i + 2."
    },
    lambda: {
        "question": "Why do we use a max-heap for sorting in ascending order in Heap Sort?",
        "answer": "We use a max-heap so that the largest element is at the root, which can be extracted and placed at the end of the array, progressively sorting the array in ascending order."
    },
    lambda: {
        "question": "What happens during the 'extract max' operation in Heap Sort?",
        "answer": "During 'extract max', the root (maximum element) is swapped with the last element of the heap, the heap size is reduced by one, and heapify is called to restore the heap property."
    },
    lambda: {
        "question": "Explain the term 'complete binary tree' and its relevance to heaps.",
        "answer": "A complete binary tree is one where all levels are fully filled except possibly the last, which is filled from left to right. This structure allows heaps to be efficiently represented as arrays."
    },
    lambda: {
        "question": "How does Heap Sort differ from Quick Sort?",
        "answer": "Heap Sort uses a heap data structure and has a guaranteed O(n log n) worst-case time, while Quick Sort uses partitioning and has an average O(n log n) but worst-case O(n^2). Heap Sort is not stable, whereas Quick Sort can be stable depending on implementation."
    },
    lambda: {
        "question": "Explain the significance of 'heap property' in Heap Sort.",
        "answer": "Heap property ensures that for every node in the heap, the value is greater than or equal to its children in max-heap, which is critical for efficiently finding and removing the largest element."
    },
    lambda: {
        "question": "Why is Heap Sort suitable for large datasets?",
        "answer": "Heap Sort is suitable for large datasets because it has a predictable O(n log n) time complexity and sorts in-place without requiring extra memory."
    },
    lambda: {
        "question": "Explain the difference between building a heap and sorting using a heap.",
        "answer": "Building a heap arranges the input array into a heap structure to satisfy heap properties, while sorting involves repeatedly extracting the root and restoring the heap until the array is sorted."
    },
    lambda: {
        "question": "What role does swapping play in Heap Sort?",
        "answer": "Swapping moves the maximum element to its correct sorted position and helps in maintaining the heap structure by exchanging elements during heapify."
    },
    lambda: {
        "question": "Describe how Heap Sort uses the 'divide and conquer' approach.",
        "answer": "Heap Sort divides the problem by building a heap (divide) and then conquering by repeatedly extracting the maximum and heapifying, sorting the array step-by-step."
    },
    lambda: {
        "question": "What is meant by Heap Sort being a comparison-based sorting algorithm?",
        "answer": "Heap Sort sorts elements by comparing them to maintain heap order and decide their relative position during heap construction and extraction."
    },
    lambda: {
        "question": "Explain why Heap Sort requires maintaining heap property after each extraction.",
        "answer": "After extracting the root, the heap may violate the heap property, so heapify is needed to restore this property for correct further extractions."
    },
    lambda: {
        "question": "Why does Heap Sort not require extra space unlike Merge Sort?",
        "answer": "Heap Sort sorts in-place by modifying the original array, whereas Merge Sort requires additional space to merge sorted subarrays."
    },
    lambda: {
        "question": "How is the parent node index calculated in an array-based heap?",
        "answer": "For a node at index i, the parent node index is calculated as (i - 1) // 2."
    },
    lambda: {
        "question": "What is the significance of the root node in a heap during Heap Sort?",
        "answer": "The root node holds the largest value in a max-heap and is repeatedly extracted to place elements in sorted order."
    },
    lambda: {
        "question": "Describe the role of the last element during the heap extraction process.",
        "answer": "The last element is swapped with the root to remove the maximum element from the heap, then the heap size is decreased."
    },
    lambda: {
        "question": "Why is Heap Sort considered an unstable sort?",
        "answer": "Because equal elements can be swapped out of their original relative order during heapify."
    },
    lambda: {
        "question": "Explain the difference between heapify up and heapify down.",
        "answer": "Heapify up is used when inserting a new element to move it upwards to maintain heap property; heapify down is used after extraction to move root downwards and restore heap order."
    },
    lambda: {
        "question": "What is the time complexity of building a heap from an unsorted array?",
        "answer": "Building a heap from an unsorted array has O(n) time complexity."
    },
    lambda: {
        "question": f"Explain why the array {generate_array_heap1()} is first converted into a heap in Heap Sort.",
        "answer": "Converting the array into a heap helps organize the elements so that the maximum (or minimum) element can be efficiently extracted to sort the array."
    },
    lambda: {
        "question": f"Given the array {generate_array_heap1()}, explain what heap property means for this array when represented as a binary heap.",
        "answer": "The heap property ensures that each parent node is greater than or equal to its children in a max-heap, enabling efficient sorting."
    },
    lambda: {
        "question": f"For the array {generate_array_heap1()}, describe the steps involved in building a max-heap.",
        "answer": "Building a max-heap involves rearranging the elements so that each subtree satisfies the max-heap property, usually by calling heapify from the bottom non-leaf nodes up."
    },
    lambda: {
        "question": f"Explain how the array {generate_array_heap1()} changes after the first extract max operation in Heap Sort.",
        "answer": "After extracting the max (root), the last element swaps with root, heap size reduces by one, and heapify is called to restore the heap property."
    },
    lambda: {
        "question": f"Why is Heap Sort efficient for sorting arrays like {generate_array_heap1()}?",
        "answer": "Heap Sort efficiently sorts such arrays by leveraging the heap structure, enabling O(n log n) time complexity without extra space."
    },
    lambda: {
        "question": f"Explain the role of heapify on the array {generate_array_heap1()} during Heap Sort.",
        "answer": "Heapify maintains the heap property by moving nodes down the tree to their correct positions."
    },
    lambda: {
        "question": f"Consider the array {generate_array_heap1()}. How does Heap Sort use the concept of a complete binary tree in this array?",
        "answer": "The array is viewed as a complete binary tree where indices map to parent and children nodes enabling efficient heap operations."
    },
    lambda: {
        "question": f"Explain why Heap Sort is an in-place algorithm using the array {generate_array_heap1()} as example.",
        "answer": "Heap Sort sorts the array by swapping elements within the original array without needing extra space."
    },
    lambda: {
        "question": f"Given the array {generate_array_heap1()}, explain why Heap Sort is not a stable sort.",
        "answer": "Because Heap Sort swaps elements that may be far apart, equal elements may change relative order."
    },
    lambda: {
        "question": f"Explain the extraction process of the max element from array {generate_array_heap1()} in Heap Sort.",
        "answer": "The root max element is swapped with the last element, heap size reduces, and heapify restores the heap."
    },
    lambda: {
        "question": f"How does Heap Sort convert the unordered array {generate_array_heap1()} into a max-heap?",
        "answer": "By repeatedly heapifying from bottom to top starting at the last non-leaf node."
    },
    lambda: {
        "question": f"Explain the time complexity of Heap Sort on the array {generate_array_heap1()}.",
        "answer": "Building the heap is O(n), and each extraction is O(log n), so total is O(n log n)."
    },
    lambda: {
        "question": f"For the array {generate_array_heap1()}, what happens if heapify is not performed after extracting max?",
        "answer": "The heap property would be violated, leading to incorrect sorting."
    },
    lambda: {
        "question": f"Why does Heap Sort treat the array {generate_array_heap1()} as a binary tree instead of a simple list?",
        "answer": "Because the binary heap structure allows efficient parent-child relationships for sorting."
    },
    lambda: {
        "question": f"Describe how swapping is used in Heap Sort on the array {generate_array_heap1()}.",
        "answer": "Swapping moves the max element to the end and maintains the heap structure."
    },
    lambda: {
        "question": f"Explain how heapify maintains heap property on the array {generate_array_heap1()}.",
        "answer": "Heapify compares a node with its children and swaps if necessary, recursively fixing violations."
    },
    lambda: {
        "question": f"What role does the array length play in Heap Sort with array {generate_array_heap1()}?",
        "answer": "Array length determines the heap size and number of extract operations."
    },
    lambda: {
        "question": f"How are the indices of parent and children nodes calculated in the array {generate_array_heap1()}?",
        "answer": "For node i, left child is 2*i+1, right child 2*i+2, and parent (i-1)//2."
    },
    lambda: {
        "question": f"Explain why Heap Sort performs better than selection sort on the array {generate_array_heap1()}.",
        "answer": "Heap Sort uses a heap to efficiently find max elements in O(log n) time rather than scanning the entire array each time."
    },
    lambda: {
        "question": f"Explain the space complexity of Heap Sort using the array {generate_array_heap1()}.",
        "answer": "Heap Sort requires O(1) extra space as it sorts in-place."
    },
    lambda: {
        "question": f"What is the significance of the root element in heapifying the array {generate_array_heap1()}?",
        "answer": "The root holds the maximum value in max-heap and is key for extraction."
    },
    lambda: {
        "question": f"How does Heap Sort ensure the array {generate_array_heap1()} becomes sorted after all extractions?",
        "answer": "By repeatedly extracting max and restoring the heap until size reduces to zero."
    },
    lambda: {
        "question": f"Why is heapify called repeatedly on array {generate_array_heap1()} during Heap Sort?",
        "answer": "To fix violations of heap property after each extraction."
    },
    lambda: {
        "question": f"Describe the structure of the array {generate_array_heap1()} after building the max-heap.",
        "answer": "The array represents a binary heap where each parent node is greater than its children."
    },
    lambda: {
        "question": f"What advantage does Heap Sort offer for the array {generate_array_heap1()} compared to bubble sort?",
        "answer": "Heap Sort has better time complexity O(n log n) and is more efficient for large arrays."
    }

],
"EXPQ": [
    lambda: {
        "question": "Heap Sort first converts the array into a ___.",
        "answer": "heap"
    },
    lambda: {
        "question": "In a max-heap, the root node contains the ___ element.",
        "answer": "largest"
    },
    lambda: {
        "question": "The left child of a node at index i in an array-based heap is at index ___.",
        "answer": "2*i + 1"
    },
    lambda: {
        "question": "The parent index of a node at index i is calculated as ___.",
        "answer": "(i - 1) // 2"
    },
    lambda: {
        "question": "Heap Sort has a worst-case time complexity of ___.",
        "answer": "O(n log n)"
    },
    lambda: {
        "question": "The process of fixing the heap after insertion or extraction is called ___.",
        "answer": "heapify"
    },
    lambda: {
        "question": "Heap Sort is an ___ sorting algorithm.",
        "answer": "in-place"
    },
    lambda: {
        "question": "Heap Sort is considered an ___ sorting algorithm because it compares elements.",
        "answer": "comparison-based"
    },
    lambda: {
        "question": "Heap Sort builds a ___ from the input array before sorting.",
        "answer": "max-heap"
    },
    lambda: {
        "question": "The number of children a node can have in a binary heap is ___.",
        "answer": "2"
    },
    lambda: {
        "question": "Heap Sort is ___ stable, meaning it may reorder equal elements.",
        "answer": "not"
    },
    lambda: {
        "question": "Heap Sort repeatedly extracts the ___ element to sort the array.",
        "answer": "maximum"
    },
    lambda: {
        "question": "In array representation, the root of the heap is stored at index ___.",
        "answer": "0"
    },
    lambda: {
        "question": "The 'extract max' operation swaps the root with the ___ element in the heap.",
        "answer": "last"
    },
    lambda: {
        "question": "Heap Sort sorts the array in ___ order using a max-heap.",
        "answer": "ascending"
    },
    lambda: {
        "question": "The height of a binary heap with n elements is approximately ___.",
        "answer": "log n"
    },
    lambda: {
        "question": "Heap Sort requires ___ extra space apart from the input array.",
        "answer": "O(1)"
    },
    lambda: {
        "question": "The operation to restore heap property after removing the root is called ___.",
        "answer": "heapify"
    },
    lambda: {
        "question": "A complete binary tree is filled from ___ to right at the last level.",
        "answer": "left"
    },
    lambda: {
        "question": "The parent of node i in a heap is at index ___.",
        "answer": "(i - 1) // 2"
    },
    lambda: {
        "question": "Heap Sort is ___ suitable for sorting large datasets.",
        "answer": "efficiently"
    },
    lambda: {
        "question": "Swapping the root with the last element is called ___.",
        "answer": "extraction"
    },
    lambda: {
        "question": "Heap Sort maintains the heap property using the ___ operation.",
        "answer": "heapify"
    },
    lambda: {
        "question": "Heap Sort has a space complexity of ___.",
        "answer": "O(1)"
    },
    lambda: {
        "question": "The maximum number of children for a node in a binary heap is ___.",
        "answer": "2"
    },
     lambda: {
        "question": f"Heap Sort first converts the array {generate_array_heap1()} into a ___.",
        "answer": "heap"
    },
    lambda: {
        "question": f"In a max-heap built from {generate_array_heap1()}, the root node contains the ___ element.",
        "answer": "largest"
    },
    lambda: {
        "question": f"The left child of a node at index i in the array {generate_array_heap1()} is at index ___.",
        "answer": "2*i + 1"
    },
    lambda: {
        "question": f"The parent index of a node at index i in array {generate_array_heap1()} is ___.",
        "answer": "(i - 1) // 2"
    },
    lambda: {
        "question": f"Heap Sort has a worst-case time complexity of ___.",
        "answer": "O(n log n)"
    },
    lambda: {
        "question": f"The process of fixing the heap after insertion or extraction on {generate_array_heap1()} is called ___.",
        "answer": "heapify"
    },
    lambda: {
        "question": f"Heap Sort is an ___ sorting algorithm as demonstrated on the array {generate_array_heap1()}.",
        "answer": "in-place"
    },
    lambda: {
        "question": f"Heap Sort is considered a ___ sorting algorithm because it compares elements in the array {generate_array_heap1()}.",
        "answer": "comparison-based"
    },
    lambda: {
        "question": f"Heap Sort builds a ___ from the input array {generate_array_heap1()} before sorting.",
        "answer": "max-heap"
    },
    lambda: {
        "question": f"The number of children each node has in the binary heap represented by {generate_array_heap1()} is ___.",
        "answer": "2"
    },
    lambda: {
        "question": f"Heap Sort is ___ stable, meaning equal elements in {generate_array_heap1()} may change order.",
        "answer": "not"
    },
    lambda: {
        "question": f"Heap Sort repeatedly extracts the ___ element from {generate_array_heap1()} to sort the array.",
        "answer": "maximum"
    },
    lambda: {
        "question": f"In array {generate_array_heap1()}, the root of the heap is stored at index ___.",
        "answer": "0"
    },
    lambda: {
        "question": f"The 'extract max' operation swaps the root with the ___ element in {generate_array_heap1()}.",
        "answer": "last"
    },
    lambda: {
        "question": f"Heap Sort sorts the array {generate_array_heap1()} in ___ order using a max-heap.",
        "answer": "ascending"
    },
    lambda: {
        "question": f"The height of a binary heap with n elements like {generate_array_heap1()} is approximately ___.",
        "answer": "log n"
    },
    lambda: {
        "question": f"Heap Sort requires ___ extra space apart from the input array {generate_array_heap1()}.",
        "answer": "O(1)"
    },
    lambda: {
        "question": f"The operation to restore heap property after removing the root in {generate_array_heap1()} is called ___.",
        "answer": "heapify"
    },
    lambda: {
        "question": f"A complete binary tree is filled from ___ to right at the last level in the array {generate_array_heap1()}.",
        "answer": "left"
    },
    lambda: {
        "question": f"The parent of node i in a heap represented by {generate_array_heap1()} is at index ___.",
        "answer": "(i - 1) // 2"
    },
    lambda: {
        "question": f"Heap Sort is ___ suitable for sorting large datasets like {generate_array_heap1()}.",
        "answer": "efficiently"
    },
    lambda: {
        "question": f"Swapping the root with the last element in {generate_array_heap1()} is called ___.",
        "answer": "extraction"
    },
    lambda: {
        "question": f"Heap Sort maintains the heap property in {generate_array_heap1()} using the ___ operation.",
        "answer": "heapify"
    },
    lambda: {
        "question": f"Heap Sort has a space complexity of ___ when sorting arrays like {generate_array_heap1()}.",
        "answer": "O(1)"
    },
    lambda: {
        "question": f"The maximum number of children for a node in a binary heap represented by {generate_array_heap1()} is ___.",
        "answer": "2"
    }
]
}


# Level 2 (Intermediate) Questions
def generate_array_heap2(size=None, low=1, high=50):
    if size is None:
        size = random.randint(6, 11)
    return [random.randint(low, high) for _ in range(size)]

level_2 = {
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
        lambda: {"question": "Heap Sort builds the heap starting from the middle of the array. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort can be used to find the k largest elements in an array efficiently. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort requires the input to be partially sorted before sorting. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort’s heapify operation maintains the heap property by pushing elements down the tree. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort can sort linked lists efficiently. (True/False)", "answer": "False"},
        lambda: {"question": "In a max-heap, the largest element is always at the root. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort does not compare elements directly but uses key comparisons. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort’s space complexity is O(1) for in-place sorting. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort can be parallelized easily. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort is efficient for sorting data stored on disk due to sequential access patterns. (True/False)", "answer": "False"},
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
        },
        lambda: {
            "question": "In Heap Sort, the heap is usually represented as:",
            "options": ["Linked list", "Binary tree", "Array", "Graph"],
            "answer": "Array"
        },
        lambda: {
            "question": "Which property does a max-heap satisfy?",
            "options": ["Parent smaller than children", "Parent greater than or equal to children", "Parent equals children", "No property"],
            "answer": "Parent greater than or equal to children"
        },
        lambda: {
            "question": "Heap Sort’s space complexity is:",
            "options": ["O(n)", "O(log n)", "O(1)", "O(n log n)"],
            "answer": "O(1)"
        },
        lambda: {
            "question": "What is the first step in Heap Sort?",
            "options": ["Sort the array", "Build a heap", "Extract elements", "Swap elements"],
            "answer": "Build a heap"
        },
        lambda: {
            "question": "Which of these is true about Heap Sort?",
            "options": ["It’s stable", "It uses recursion only", "It sorts in place", "It requires extra arrays"],
            "answer": "It sorts in place"
        },
        lambda: {
            "question": "In a max-heap, the largest element is:",
            "options": ["At the last leaf", "At the root", "At the middle", "Anywhere"],
            "answer": "At the root"
        },
        lambda: {
            "question": "What does the heapify operation do?",
            "options": ["Builds the heap", "Maintains heap property", "Sorts the array", "Finds the median"],
            "answer": "Maintains heap property"
        },
        lambda: {
            "question": "When heapify is called on a node, it:",
            "options": ["Moves the node up", "Moves the node down", "Swaps random elements", "Does nothing"],
            "answer": "Moves the node down"
        },
        lambda: {
            "question": "Which of the following is true about heap sort’s performance?",
            "options": ["Best case O(n)", "Average and worst case O(n log n)", "Worst case O(n^2)", "Best case O(log n)"],
            "answer": "Average and worst case O(n log n)"
        },
        lambda: {
            "question": "Heap Sort’s sorting order with a max-heap is:",
            "options": ["Ascending", "Descending", "Random", "Unsorted"],
            "answer": "Ascending"
        },
        lambda: {
            "question": "Which of these operations is not part of Heap Sort?",
            "options": ["Heapify", "Merge", "Swap", "Extract max"],
            "answer": "Merge"
        },
        lambda: {
            "question": "Heap Sort builds the heap starting from which part of the array?",
            "options": ["Root", "Leaves", "Middle", "Random"],
            "answer": "Middle"
        },
        lambda: {
            "question": "What is the parent index of a node at index i in an array heap?",
            "options": ["i/2", "(i-1)//2", "2i + 1", "2i + 2"],
            "answer": "(i-1)//2"
        },
        lambda: {
            "question": "How many children can a node in a binary heap have?",
            "options": ["1", "2", "3", "4"],
            "answer": "2"
        },
        lambda: {
            "question": "Heap Sort is based on which data structure?",
            "options": ["Stack", "Queue", "Heap", "Graph"],
            "answer": "Heap"
        },
        lambda: {
            "question": "Which of the following sorting algorithms is not comparison-based?",
            "options": ["Heap Sort", "Counting Sort", "Quick Sort", "Merge Sort"],
            "answer": "Counting Sort"
        },
        lambda: {
            "question": "Heap Sort swaps the root element with which element during sorting?",
            "options": ["Last element", "First element", "Middle element", "Second element"],
            "answer": "Last element"
        },
        lambda: {
            "question": "Heap Sort is most similar to which other sorting algorithm?",
            "options": ["Quick Sort", "Selection Sort", "Bubble Sort", "Insertion Sort"],
            "answer": "Selection Sort"
        }
    ],
    "MTQ": [
        lambda: {
            "question": "Match the terms to their Heap Sort descriptions:\n1. Build Heap\n2. Extract Root\n3. Heapify\n4. Swap\n5. Complete Binary Tree\n6. Max-Heap\n7. Min-Heap\n8. Parent Node\n9. Child Node\n10. In-place Sort",
            "pairs": {
                "1": "Construct initial heap from array",
                "2": "Remove the root element",
                "3": "Restore heap property after changes",
                "4": "Exchange two elements in array",
                "5": "Binary tree filled level-wise without gaps",
                "6": "Parent greater than or equal to children",
                "7": "Parent less than or equal to children",
                "8": "Node with children nodes below",
                "9": "Nodes directly below a parent",
                "10": "Sort using constant extra space"
            },
            "answer": "1->Construct initial heap from array, 2->Remove the root element, 3->Restore heap property after changes, 4->Exchange two elements in array, 5->Binary tree filled level-wise without gaps, 6->Parent greater than or equal to children, 7->Parent less than or equal to children, 8->Node with children nodes below, 9->Nodes directly below a parent, 10->Sort using constant extra space"
        },
        lambda: {
            "question": "Match these Heap Sort terms:\n1. Heapify\n2. Max-Heap\n3. Min-Heap\n4. Root\n5. Leaf Node\n6. Array Representation\n7. Extract Max\n8. Swap\n9. Complexity\n10. Stability",
            "pairs": {
                "1": "Maintain heap property",
                "2": "Heap with largest root",
                "3": "Heap with smallest root",
                "4": "Top node of heap",
                "5": "Node with no children",
                "6": "Heap stored in array",
                "7": "Remove largest element",
                "8": "Exchange two elements",
                "9": "O(n log n) for Heap Sort",
                "10": "Preserves original order of equal elements"
            },
            "answer": "1->Maintain heap property, 2->Heap with largest root, 3->Heap with smallest root, 4->Top node of heap, 5->Node with no children, 6->Heap stored in array, 7->Remove largest element, 8->Exchange two elements, 9->O(n log n) for Heap Sort, 10->Preserves original order of equal elements"
        },
         lambda: {
        "question": "Match the Heap Sort terms with their descriptions:",
        "pairs": {
            "Heapify": "Process to maintain heap property",
            "Max-Heap": "Heap with largest element at root",
            "Min-Heap": "Heap with smallest element at root",
            "Root": "Top element of the heap",
            "Leaf Node": "Node without children"
        },
        "answer": {
            "Heapify": "Process to maintain heap property",
            "Max-Heap": "Heap with largest element at root",
            "Min-Heap": "Heap with smallest element at root",
            "Root": "Top element of the heap",
            "Leaf Node": "Node without children"
        }
    },
    lambda: {
        "question": "Match the Heap Sort array index with the node relationship:",
        "pairs": {
            "Parent index i": "Children indices 2*i + 1 and 2*i + 2",
            "Left child index": "2*i + 1",
            "Right child index": "2*i + 2",
            "Last node index": "n-1",
            "Root index": "0"
        },
        "answer": {
            "Parent index i": "Children indices 2*i + 1 and 2*i + 2",
            "Left child index": "2*i + 1",
            "Right child index": "2*i + 2",
            "Last node index": "n-1",
            "Root index": "0"
        }
    },
    lambda: {
        "question": "Match Heap Sort terms with their time complexity:",
        "pairs": {
            "Heapify operation": "O(log n)",
            "Building the heap": "O(n)",
            "Heap Sort overall": "O(n log n)",
            "Accessing root": "O(1)",
            "Swapping elements": "O(1)"
        },
        "answer": {
            "Heapify operation": "O(log n)",
            "Building the heap": "O(n)",
            "Heap Sort overall": "O(n log n)",
            "Accessing root": "O(1)",
            "Swapping elements": "O(1)"
        }
    },
    lambda: {
        "question": "Match Heap Sort phases with their purpose:",
        "pairs": {
            "Heap building": "Create max-heap from array",
            "Heap extraction": "Remove root and rebuild heap",
            "Sorting": "Repeated root extraction to sort array",
            "Heapify": "Restore heap property",
            "Final array": "Sorted in ascending order"
        },
        "answer": {
            "Heap building": "Create max-heap from array",
            "Heap extraction": "Remove root and rebuild heap",
            "Sorting": "Repeated root extraction to sort array",
            "Heapify": "Restore heap property",
            "Final array": "Sorted in ascending order"
        }
    },
    lambda: {
        "question": "Match Heap Sort terms with their memory usage:",
        "pairs": {
            "In-place algorithm": "Uses constant extra memory",
            "Heap representation": "Array",
            "Auxiliary space": "O(1)",
            "Recursive calls": "O(log n) stack space in some implementations",
            "Temporary variable for swap": "O(1)"
        },
        "answer": {
            "In-place algorithm": "Uses constant extra memory",
            "Heap representation": "Array",
            "Auxiliary space": "O(1)",
            "Recursive calls": "O(log n) stack space in some implementations",
            "Temporary variable for swap": "O(1)"
        }
    },
    lambda: {
        "question": "Match Heap Sort terms with their stability and ordering:",
        "pairs": {
            "Heap Sort stability": "Not stable",
            "Sorting order with max-heap": "Ascending",
            "Sorting order with min-heap": "Descending",
            "Equal elements order": "May change",
            "Stable sorting algorithm example": "Merge Sort"
        },
        "answer": {
            "Heap Sort stability": "Not stable",
            "Sorting order with max-heap": "Ascending",
            "Sorting order with min-heap": "Descending",
            "Equal elements order": "May change",
            "Stable sorting algorithm example": "Merge Sort"
        }
    },
    lambda: {
        "question": "Match Heap Sort terminology with their description:",
        "pairs": {
            "Heap property": "Parent is greater (max-heap) or smaller (min-heap) than children",
            "Complete binary tree": "All levels filled except possibly last",
            "Leaf node": "Has no children",
            "Internal node": "Has at least one child",
            "Heap height": "O(log n)"
        },
        "answer": {
            "Heap property": "Parent is greater (max-heap) or smaller (min-heap) than children",
            "Complete binary tree": "All levels filled except possibly last",
            "Leaf node": "Has no children",
            "Internal node": "Has at least one child",
            "Heap height": "O(log n)"
        }
    },
    lambda: {
        "question": "Match Heap Sort terms with their array implementation properties:",
        "pairs": {
            "Root element index": "0",
            "Parent of node i": "(i - 1) // 2",
            "Left child of i": "2*i + 1",
            "Right child of i": "2*i + 2",
            "Heap size": "Variable decreasing during sort"
        },
        "answer": {
            "Root element index": "0",
            "Parent of node i": "(i - 1) // 2",
            "Left child of i": "2*i + 1",
            "Right child of i": "2*i + 2",
            "Heap size": "Variable decreasing during sort"
        }
    },
    lambda: {
        "question": "Match Heap Sort terminology with explanation:",
        "pairs": {
            "Heapify process": "Ensures subtree satisfies heap property",
            "Extract max": "Swap root with last element",
            "Build max heap": "Call heapify bottom-up",
            "Sorted array": "Extracted elements in order",
            "In-place sorting": "No extra array used"
        },
        "answer": {
            "Heapify process": "Ensures subtree satisfies heap property",
            "Extract max": "Swap root with last element",
            "Build max heap": "Call heapify bottom-up",
            "Sorted array": "Extracted elements in order",
            "In-place sorting": "No extra array used"
        }
    },
    lambda: {
        "question": "Match Heap Sort step with its description:",
        "pairs": {
            "Initialize heap": "Convert array to max heap",
            "Extract element": "Swap root with last heap element",
            "Reduce heap size": "Exclude last element from heap",
            "Heapify root": "Restore heap property from root",
            "Repeat until heap empty": "Sort entire array"
        },
        "answer": {
            "Initialize heap": "Convert array to max heap",
            "Extract element": "Swap root with last heap element",
            "Reduce heap size": "Exclude last element from heap",
            "Heapify root": "Restore heap property from root",
            "Repeat until heap empty": "Sort entire array"
        }
    },
    lambda: {
        "question": "Match Heap Sort concepts with their attributes:",
        "pairs": {
            "Heap sort time complexity": "O(n log n)",
            "Heap sort space complexity": "O(1)",
            "Heapify complexity": "O(log n)",
            "Heap structure": "Complete binary tree",
            "Sorting technique": "Comparison-based"
        },
        "answer": {
            "Heap sort time complexity": "O(n log n)",
            "Heap sort space complexity": "O(1)",
            "Heapify complexity": "O(log n)",
            "Heap structure": "Complete binary tree",
            "Sorting technique": "Comparison-based"
        }
    },
    lambda: {
        "question": "Match Heap Sort terminology with their correct example:",
        "pairs": {
            "Max heap example root": "100",
            "Min heap example root": "5",
            "Heapify example": "Adjust subtree with root 50",
            "Swap example": "Root 100 with last 20",
            "Sorted array example": "[5, 10, 20, 50, 100]"
        },
        "answer": {
            "Max heap example root": "100",
            "Min heap example root": "5",
            "Heapify example": "Adjust subtree with root 50",
            "Swap example": "Root 100 with last 20",
            "Sorted array example": "[5, 10, 20, 50, 100]"
        }
    },
    lambda: {
        "question": "Match Heap Sort steps with their order:",
        "pairs": {
            "Step 1": "Build max heap",
            "Step 2": "Swap root with last element",
            "Step 3": "Reduce heap size",
            "Step 4": "Heapify root",
            "Step 5": "Repeat steps 2 to 4"
        },
        "answer": {
            "Step 1": "Build max heap",
            "Step 2": "Swap root with last element",
            "Step 3": "Reduce heap size",
            "Step 4": "Heapify root",
            "Step 5": "Repeat steps 2 to 4"
        }
    },
    lambda: {
        "question": "Match Heap Sort concepts with their definitions:",
        "pairs": {
            "Heap": "Special tree-based data structure",
            "Heapify": "Fix heap property violation",
            "Max heap": "Largest element at root",
            "Min heap": "Smallest element at root",
            "Sort order": "Ascending by default"
        },
        "answer": {
            "Heap": "Special tree-based data structure",
            "Heapify": "Fix heap property violation",
            "Max heap": "Largest element at root",
            "Min heap": "Smallest element at root",
            "Sort order": "Ascending by default"
        }
    },
    lambda: {
        "question": "Match Heap Sort terms with their characteristics:",
        "pairs": {
            "Heap Sort advantage": "Good worst-case performance",
            "Heap Sort disadvantage": "Not stable",
            "Heap Sort space": "In-place",
            "Heap Sort average case": "O(n log n)",
            "Heap Sort worst case": "O(n log n)"
        },
        "answer": {
            "Heap Sort advantage": "Good worst-case performance",
            "Heap Sort disadvantage": "Not stable",
            "Heap Sort space": "In-place",
            "Heap Sort average case": "O(n log n)",
            "Heap Sort worst case": "O(n log n)"
        }
    },
    lambda: {
        "question": "Match Heap Sort operations with their descriptions:",
        "pairs": {
            "Build heap": "Create max heap from unsorted array",
            "Heapify": "Fix heap property in subtree",
            "Extract root": "Remove largest element",
            "Swap": "Exchange two elements in array",
            "Reduce heap": "Exclude last element after extraction"
        },
        "answer": {
            "Build heap": "Create max heap from unsorted array",
            "Heapify": "Fix heap property in subtree",
            "Extract root": "Remove largest element",
            "Swap": "Exchange two elements in array",
            "Reduce heap": "Exclude last element after extraction"
        }
    },
    lambda: {
        "question": "Match Heap Sort terms with their array indexing formulas:",
        "pairs": {
            "Parent of node i": "(i - 1) // 2",
            "Left child of i": "2*i + 1",
            "Right child of i": "2*i + 2",
            "Root node index": "0",
            "Heap size variable": "Decreases by 1 after extraction"
        },
        "answer": {
            "Parent of node i": "(i - 1) // 2",
            "Left child of i": "2*i + 1",
            "Right child of i": "2*i + 2",
            "Root node index": "0",
            "Heap size variable": "Decreases by 1 after extraction"
        }
    },
    lambda: {
        "question": "Match Heap Sort process steps with their effect:",
        "pairs": {
            "Heapify": "Ensures max heap property",
            "Swap root": "Moves largest to end",
            "Decrease heap size": "Removes last sorted element",
            "Repeat heapify": "Maintains heap property",
            "Final array": "Sorted ascending"
        },
        "answer": {
            "Heapify": "Ensures max heap property",
            "Swap root": "Moves largest to end",
            "Decrease heap size": "Removes last sorted element",
            "Repeat heapify": "Maintains heap property",
            "Final array": "Sorted ascending"
        }
    },
    lambda: {
        "question": "Match Heap Sort terms with their types:",
        "pairs": {
            "Heap": "Complete binary tree",
            "Max heap": "Heap with max root",
            "Min heap": "Heap with min root",
            "Heapify": "Operation to fix heap",
            "Sort": "Comparison-based sorting"
        },
        "answer": {
            "Heap": "Complete binary tree",
            "Max heap": "Heap with max root",
            "Min heap": "Heap with min root",
            "Heapify": "Operation to fix heap",
            "Sort": "Comparison-based sorting"
        }
    },
    lambda: {
        "question": "Match Heap Sort concepts with the related algorithm:",
        "pairs": {
            "Heap Sort": "Sorting using heap data structure",
            "Quick Sort": "Divide and conquer",
            "Merge Sort": "Divide and merge",
            "Bubble Sort": "Repeated swaps",
            "Insertion Sort": "Incremental sorting"
        },
        "answer": {
            "Heap Sort": "Sorting using heap data structure",
            "Quick Sort": "Divide and conquer",
            "Merge Sort": "Divide and merge",
            "Bubble Sort": "Repeated swaps",
            "Insertion Sort": "Incremental sorting"
        }
    },
    lambda: {
        "question": "Match Heap Sort terms with their examples:",
        "pairs": {
            "Max heap root": "50",
            "Min heap root": "5",
            "Heapify root": "Adjust node 30",
            "Swap operation": "Exchange 50 and 10",
            "Sorted array": "[5, 10, 20, 30, 50]"
        },
        "answer": {
            "Max heap root": "50",
            "Min heap root": "5",
            "Heapify root": "Adjust node 30",
            "Swap operation": "Exchange 50 and 10",
            "Sorted array": "[5, 10, 20, 30, 50]"
        }
    },
    lambda arr=generate_array_heap2(): {
        "question": f"Match the indices with the elements in the heap array: {arr}",
        "pairs": {
            f"Element at index 0": str(arr[0]),
            f"Element at index 1": str(arr[1]),
            f"Element at index 2": str(arr[2]),
            f"Element at index 3": str(arr[3]),
            f"Element at index 4": str(arr[4])
        },
        "answer": {
            f"Element at index 0": str(arr[0]),
            f"Element at index 1": str(arr[1]),
            f"Element at index 2": str(arr[2]),
            f"Element at index 3": str(arr[3]),
            f"Element at index 4": str(arr[4])
        }
    },

    lambda arr=generate_array_heap2(): {
        "question": f"Match parent nodes with their children in the heap array: {arr}",
        "pairs": {
            f"Parent at index 0": f"Children: {arr[1]} (index 1), {arr[2]} (index 2)",
            f"Parent at index 1": f"Children: {arr[3]} (index 3), {arr[4]} (index 4)",
            f"Parent at index 2": f"No children (leaf node)"
        },
        "answer": {
            f"Parent at index 0": f"Children: {arr[1]} (index 1), {arr[2]} (index 2)",
            f"Parent at index 1": f"Children: {arr[3]} (index 3), {arr[4]} (index 4)",
            f"Parent at index 2": f"No children (leaf node)"
        }
    },

    lambda arr=generate_array_heap2(): {
        "question": f"Match the heapify process with affected nodes in array: {arr}",
        "pairs": {
            f"Heapify root at index 0": f"Affects indices 0,1,2 with values {arr[0]}, {arr[1]}, {arr[2]}",
            f"Heapify node at index 1": f"Affects indices 1,3,4 with values {arr[1]}, {arr[3]}, {arr[4]}",
            f"Heapify node at index 2": f"Node at index 2 ({arr[2]}) is a leaf"
        },
        "answer": {
            f"Heapify root at index 0": f"Affects indices 0,1,2 with values {arr[0]}, {arr[1]}, {arr[2]}",
            f"Heapify node at index 1": f"Affects indices 1,3,4 with values {arr[1]}, {arr[3]}, {arr[4]}",
            f"Heapify node at index 2": f"Node at index 2 ({arr[2]}) is a leaf"
        }
    },

    lambda arr=generate_array_heap2(): {
        "question": f"Match the following swaps during heap sort on array: {arr}",
        "pairs": {
            f"Swap root index 0 ({arr[0]}) with last index 4 ({arr[4]})": "Positions swapped to move max to end",
            f"Swap index 0 ({arr[4]}) with child index 1 ({arr[1]})": "Heapify step after swap",
            f"Swap index 1 ({arr[1]}) with child index 3 ({arr[3]})": "Next heapify step"
        },
        "answer": {
            f"Swap root index 0 ({arr[0]}) with last index 4 ({arr[4]})": "Positions swapped to move max to end",
            f"Swap index 0 ({arr[4]}) with child index 1 ({arr[1]})": "Heapify step after swap",
            f"Swap index 1 ({arr[1]}) with child index 3 ({arr[3]})": "Next heapify step"
        }
    },

    lambda arr=generate_array_heap2(): {
        "question": f"Match the heap array elements with their parent indices for array: {arr}",
        "pairs": {
            f"Parent of node at index 1 ({arr[1]})": f"Index 0 ({arr[0]})",
            f"Parent of node at index 2 ({arr[2]})": f"Index 0 ({arr[0]})",
            f"Parent of node at index 3 ({arr[3]})": f"Index 1 ({arr[1]})",
            f"Parent of node at index 4 ({arr[4]})": f"Index 1 ({arr[1]})"
        },
        "answer": {
            f"Parent of node at index 1 ({arr[1]})": f"Index 0 ({arr[0]})",
            f"Parent of node at index 2 ({arr[2]})": f"Index 0 ({arr[0]})",
            f"Parent of node at index 3 ({arr[3]})": f"Index 1 ({arr[1]})",
            f"Parent of node at index 4 ({arr[4]})": f"Index 1 ({arr[1]})"
        }
    },
    
    lambda arr=generate_array_heap2(): {
        "question": f"Match each node with its children indices and values in heap array: {arr}",
        "pairs": {
            f"Node at index 0 ({arr[0]})": f"Children at indices 1 ({arr[1]}), 2 ({arr[2]})",
            f"Node at index 1 ({arr[1]})": f"Children at indices 3 ({arr[3]}), 4 ({arr[4]})",
            f"Node at index 2 ({arr[2]})": f"No children (leaf node)"
        },
        "answer": {
            f"Node at index 0 ({arr[0]})": f"Children at indices 1 ({arr[1]}), 2 ({arr[2]})",
            f"Node at index 1 ({arr[1]})": f"Children at indices 3 ({arr[3]}), 4 ({arr[4]})",
            f"Node at index 2 ({arr[2]})": f"No children (leaf node)"
        }
    },

    lambda arr=generate_array_heap2(): {
        "question": f"Match Heap Sort step description with affected array indices in: {arr}",
        "pairs": {
            "Build max heap": "Heapify nodes from last parent to root",
            f"Heapify node index 1": f"Check indices 1, 3, 4 with values {arr[1]}, {arr[3]}, {arr[4]}",
            f"Swap root with index 4": f"Swap {arr[0]} and {arr[4]} to move max element",
            "Reduce heap size": "Exclude last element after swap"
        },
        "answer": {
            "Build max heap": "Heapify nodes from last parent to root",
            f"Heapify node index 1": f"Check indices 1, 3, 4 with values {arr[1]}, {arr[3]}, {arr[4]}",
            f"Swap root with index 4": f"Swap {arr[0]} and {arr[4]} to move max element",
            "Reduce heap size": "Exclude last element after swap"
        }
    },

    lambda arr=generate_array_heap2(): {
        "question": f"Match the heap array element with its corresponding role in array: {arr}",
        "pairs": {
            f"Root element (index 0)": str(arr[0]),
            f"Last leaf element (index 4)": str(arr[4]),
            f"Parent of node at index 3": f"Index 1 ({arr[1]})",
            f"Left child of node at index 1": f"Index 3 ({arr[3]})",
            f"Right child of node at index 1": f"Index 4 ({arr[4]})"
        },
        "answer": {
            f"Root element (index 0)": str(arr[0]),
            f"Last leaf element (index 4)": str(arr[4]),
            f"Parent of node at index 3": f"Index 1 ({arr[1]})",
            f"Left child of node at index 1": f"Index 3 ({arr[3]})",
            f"Right child of node at index 1": f"Index 4 ({arr[4]})"
        }
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
        lambda: {"question": "Explain why Heap Sort is called an in-place algorithm.", "answer": "Because it requires only a constant amount of extra space."},
        lambda: {"question": "Describe the role of the swap operation in Heap Sort.", "answer": "It moves the root to the end and prepares the heap for the next iteration."},
        lambda: {"question": "What would happen if the array is already a max-heap at the start of Heap Sort?", "answer": "Heap Sort proceeds to extract elements; no rebuilding heap needed initially."},
        lambda: {"question": "Explain the difference between max-heap and min-heap.", "answer": "Max-heap has parent nodes greater than children; min-heap has parent nodes smaller than children."},
        lambda: {"question": "How does Heap Sort ensure the array is sorted after all root extractions?", "answer": "By swapping and heapifying repeatedly until the heap size reduces to zero."},
        lambda: {"question": "Why is Heap Sort preferred over Bubble Sort for large datasets?", "answer": "Because it has a better worst-case time complexity of O(n log n)."},
        lambda: {"question": "Describe the iterative process of heapify.", "answer": "Starting at a node, compare with children and swap with the larger child if needed, repeat downwards."},
        lambda: {"question": "How does Heap Sort handle sorting in descending order using a max-heap?", "answer": "It produces ascending order; for descending order, a min-heap can be used."},
        lambda: {"question": "Why can't Heap Sort guarantee stability?", "answer": "Because swapping during heapify can change the relative order of equal elements."},
        lambda: {"question": "Explain the meaning of the term 'complete binary tree' in the context of heaps.", "answer": "A binary tree where all levels are fully filled except possibly the last, which is filled left to right."},
        lambda: {"question": "What is the time complexity of building a heap from an unordered array?", "answer": "O(n)"},
        lambda: {"question": "Explain how the height of the heap affects the time complexity of heapify.", "answer": "Heapify operates down the height of the heap, which is O(log n)."},
        lambda: {"question": "Why does Heap Sort repeatedly swap the root with the last element?", "answer": "To remove the largest element from the heap and place it at its correct sorted position."},
        lambda: {"question": "What role does the array length play in Heap Sort iterations?", "answer": "It determines the heap size which decreases after each extraction."},
        lambda: {"question": "How does Heap Sort differ from Merge Sort in terms of extra space?", "answer": "Heap Sort is in-place; Merge Sort requires O(n) extra space."},
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
        },
        lambda: {
            "question": "Fill in: The height of a heap with n elements is approximately __.",
            "answer": "log base 2 of n"
        },
        lambda: {
            "question": "Complete: Heap Sort has a worst-case time complexity of __.",
            "answer": "O(n log n)"
        },
        lambda: {
            "question": "Fill in: Heap Sort uses a __ (max/min) heap to sort elements in ascending order.",
            "answer": "max"
        },
        lambda: {
            "question": "Fill in the blank: Heap Sort’s space complexity is __ because it sorts in-place.",
            "answer": "O(1)"
        },
        lambda: {
            "question": "Complete: The process of restoring the heap property after swapping is called __.",
            "answer": "heapify"
        },
        lambda: {
            "question": "Fill in: The root element of a max-heap is the __ element.",
            "answer": "largest"
        },
        lambda: {
            "question": "Complete: In Heap Sort, elements are extracted from the __ of the heap.",
            "answer": "root"
        },
        lambda: {
            "question": "Fill in: The children of node i in the heap array are at indices __ and __.",
            "answer": "2*i + 1, 2*i + 2"
        },
        lambda: {
            "question": "Complete: Heap Sort builds the heap by calling __ starting from the middle of the array.",
            "answer": "heapify"
        },
        lambda: {
            "question": "Fill in: Heap Sort is not a __ sorting algorithm because it swaps elements that may affect order of equal elements.",
            "answer": "stable"
        },
        lambda: {
            "question": "Complete: The array representation of a heap requires __ space.",
            "answer": "O(n)"
        },
        lambda: {
            "question": "Fill in: The heapify operation runs in __ time in the worst case.",
            "answer": "O(log n)"
        },
        lambda: {
            "question": "Complete: Heap Sort repeatedly swaps the root with the __ element of the heap.",
            "answer": "last"
        },
        lambda: {
            "question": "Fill in: The height of a complete binary tree with n nodes is __.",
            "answer": "O(log n)"
        },
        lambda: {
            "question": "Complete: Heap Sort’s average and worst-case time complexity are both __.",
            "answer": "O(n log n)"
        },
        lambda: {
            "question": "Fill in: A min-heap has the smallest element at the __.",
            "answer": "root"
        },
        lambda: {
            "question": "Complete: Heap Sort is called __ because it sorts using only a constant amount of extra memory.",
            "answer": "in-place"
        },
        lambda: {
            "question": "Fill in: Heap Sort is based on the __ data structure.",
            "answer": "heap"
        },
        lambda: {
            "question": "Complete: Heap Sort is __ efficient for sorting large datasets than Bubble Sort.",
            "answer": "more"
        },
        lambda: {
            "question": "Fill in: The array length decreases by __ after each extraction in Heap Sort.",
            "answer": "1"
        },
        lambda: {
            "question": "Complete: Heap Sort sorts the array in __ order by default with a max-heap.",
            "answer": "ascending"
        },
        lambda: {
            "question": "Fill in: Heap Sort’s heap structure is a __ binary tree.",
            "answer": "complete"
        }
    ]
}

# Level 3 (Advanced) Questions
def generate_array_heap3(size=None, low=1, high=100):
    if size is None:
        size = random.randint(8, 12)
    return [random.randint(low, high) for _ in range(size)]

level_3 = {
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
        lambda: {"question": "The max-heap property requires each parent to be greater than or equal to its children. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort has a space complexity of O(n). (True/False)", "answer": "False"},
        lambda: {"question": "Heapify operation has a time complexity of O(log n). (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort works by repeatedly extracting the minimum element from the heap. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort can handle duplicate elements without modification. (True/False)", "answer": "True"},
        lambda: {"question": "A binary heap is always a complete binary tree. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort is stable by nature. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort can be implemented without recursion. (True/False)", "answer": "True"},
        lambda: {"question": "The leaf nodes in a heap are all at the last two levels. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort's efficiency is unaffected by the initial ordering of elements. (True/False)", "answer": "True"},
        lambda: {"question": "Building a heap from an unsorted array takes O(n) time. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort performs fewer swaps than Quick Sort on average. (True/False)", "answer": "False"},
        lambda: {"question": "Heap Sort does not require a separate merge step. (True/False)", "answer": "True"},
        lambda: {"question": "A min-heap always stores the smallest element at the root. (True/False)", "answer": "True"},
        lambda: {"question": "Heap Sort cannot be applied to data structures other than arrays. (True/False)", "answer": "False"},
    ],

    "MCQ": [
        lambda: {
            "question": "What is the height of a binary heap with 31 nodes?",
            "options": ["4", "5", "6", "7"],
            "answer": "5"
        },
        lambda: {
            "question": f"Given an array, what is the index of the left child of the element at index 2?",
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
        },
        lambda: {
            "question": "Which operation takes O(log n) time in Heap Sort?",
            "options": ["Building the heap", "Extracting max/min", "Inserting into heap", "All of the above"],
            "answer": "All of the above"
        },
        lambda: {
            "question": "What is the worst-case time complexity of heapify on a node?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
            "answer": "O(log n)"
        },
        lambda: {
            "question": "What type of binary tree does Heap Sort rely on?",
            "options": ["Full binary tree", "Complete binary tree", "Perfect binary tree", "Degenerate tree"],
            "answer": "Complete binary tree"
        },
        lambda: {
            "question": "Which index formula gives the right child of node at index i?",
            "options": ["2*i", "2*i + 1", "2*i + 2", "i/2"],
            "answer": "2*i + 2"
        },
        lambda: {
            "question": "What happens after extracting the root in Heap Sort?",
            "options": [
                "Heap size increases",
                "Heap property is restored by heapify",
                "Array is sorted",
                "No changes"
            ],
            "answer": "Heap property is restored by heapify"
        },
        lambda: {
            "question": "Which of these is a min-heap property?",
            "options": [
                "Parent is smaller than children",
                "Parent is larger than children",
                "Heap height is minimal",
                "Heap is stable"
            ],
            "answer": "Parent is smaller than children"
        },
        lambda: {
            "question": "Heap Sort is best described as a:",
            "options": [
                "Divide and conquer algorithm",
                "Greedy algorithm",
                "Comparison-based sorting algorithm",
                "Non-comparison based algorithm"
            ],
            "answer": "Comparison-based sorting algorithm"
        },
        lambda: {
            "question": "Which part of Heap Sort takes linear time?",
            "options": [
                "Building the heap",
                "Extracting elements",
                "Heapify operation",
                "Swapping elements"
            ],
            "answer": "Building the heap"
        },
        lambda: {
            "question": "In an array representation of heap, what is the index of the parent of node at index i?",
            "options": ["(i-1)//2", "(i+1)//2", "2*i + 1", "2*i + 2"],
            "answer": "(i-1)//2"
        },
        lambda: {
            "question": "What is the main disadvantage of Heap Sort?",
            "options": [
                "Requires extra memory",
                "Not stable",
                "High time complexity",
                "Cannot sort arrays"
            ],
            "answer": "Not stable"
        },
        lambda: {
            "question": "Which data structure is used in Heap Sort?",
            "options": [
                "Binary search tree",
                "Binary heap",
                "Linked list",
                "Hash table"
            ],
            "answer": "Binary heap"
        },
        lambda: {
            "question": "Which is true about Heap Sort?",
            "options": [
                "It is a stable sorting algorithm",
                "It uses extra space proportional to n",
                "It sorts in-place",
                "It requires a balanced BST"
            ],
            "answer": "It sorts in-place"
        },
        lambda: {
            "question": "What does the heapify function do?",
            "options": [
                "Builds the initial heap",
                "Maintains heap property for subtree",
                "Extracts the max element",
                "Swaps two elements"
            ],
            "answer": "Maintains heap property for subtree"
        },
        lambda: {
            "question": "Heap Sort is preferred over Quick Sort when:",
            "options": [
                "Stability is needed",
                "Worst-case time is critical",
                "Memory is very limited",
                "Input is almost sorted"
            ],
            "answer": "Worst-case time is critical"
        },
        lambda: {
            "question": "Heap Sort is an example of which algorithm design technique?",
            "options": ["Dynamic programming", "Greedy", "Divide and conquer", "Backtracking"],
            "answer": "Divide and conquer"
        },
        lambda: {
            "question": "Heap Sort's worst-case time complexity is:",
            "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
            "answer": "O(n log n)"
        },
        lambda: {
            "question": "Which index in the array corresponds to the root of the heap?",
            "options": ["0", "1", "n-1", "n/2"],
            "answer": "0"
        },
        lambda: {
            "question": "What is the main step after removing the root element in Heap Sort?",
            "options": [
                "Insert new element",
                "Heapify the root",
                "Sort the array",
                "Build a new heap"
            ],
            "answer": "Heapify the root"
        },
        lambda: {
            "question": "In a max-heap, which node is the maximum?",
            "options": ["Root", "Leaf", "Left child", "Right child"],
            "answer": "Root"
        },
        lambda: {
            "question": "Heap Sort uses which of the following?",
            "options": [
                "Auxiliary arrays",
                "In-place array manipulations",
                "Linked lists",
                "Hash maps"
            ],
            "answer": "In-place array manipulations"
        },
        # Dynamic questions with lambda functions
        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given the heap array: {arr}\nWhat are the children indices of the element at index 3?",
                "options": [[7,8], [6,7], [9,10], [5,6]],
                "answer": [7,8]  # left=2*3+1=7, right=2*3+2=8
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"In the heap array {arr}, if the element at index 5 is 20, what are the possible indices of its children?",
                "options": [[11,12], [10,11], [8,9], [5,6]],
                "answer": [11,12]  # left=2*5+1=11, right=2*5+2=12
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given the heap array: {arr}\nIs the subtree rooted at index 1 a valid max-heap if arr[1]={arr[1]}, arr[3]={arr[3]}, and arr[4]={arr[4]}?",
                "options": ["Yes", "No"],
                "answer": "Yes" if arr[1] >= arr[3] and arr[1] >= arr[4] else "No"
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given the heap array: {arr}\nWhich index should be heapified first to restore max-heap property after replacing root with the last element?",
                "options": [0, 1, 2, 3],
                "answer": 0
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"In the heap array {arr}, what is the height of the node at index 0?",
                "options": [2, 3, 4, 1],
                "answer": 3  # height is floor(log2(n)) = for n ~8-12, height ~3
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"For the heap array {arr}, what is the maximum possible index of a leaf node?",
                "options": [len(arr)//2, len(arr)-1, len(arr)//2 - 1, len(arr)//3],
                "answer": len(arr)-1
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given heap array: {arr}\nIf the element at index 4 is swapped with element at index 9, which operation must be performed to restore heap property?",
                "options": ["Heapify Up", "Heapify Down", "Build Heap", "No operation needed"],
                "answer": "Heapify Down"
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given heap array: {arr}\nWhat is the index of the right child of the root?",
                "options": [1, 2, 3, 4],
                "answer": 2
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"In the heap array {arr}, which of the following is true about the parent and its children?\nParent: arr[2]={arr[2]}, Left child: arr[5]={arr[5]}, Right child: arr[6]={arr[6]}",
                "options": [
                    "Parent is greater than or equal to both children",
                    "Parent is less than at least one child",
                    "Parent is equal to both children",
                    "Cannot determine"
                ],
                "answer": "Parent is greater than or equal to both children" if arr[2]>=arr[5] and arr[2]>=arr[6] else "Parent is less than at least one child"
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given the heap array {arr}\nWhat is the formula to find the left child index of node i?",
                "options": ["2*i", "2*i + 1", "2*i + 2", "i/2"],
                "answer": "2*i + 1"
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"In the heap array {arr}, which node is the last internal node (non-leaf)?",
                "options": [len(arr)//2 - 1, len(arr)//2, len(arr)//2 + 1, len(arr)-1],
                "answer": len(arr)//2 - 1
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given the heap array: {arr}\nWhat is the index of the root node?",
                "options": [0, 1, len(arr)-1, len(arr)//2],
                "answer": 0
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given the heap array: {arr}\nWhich is the parent of node at index 8?",
                "options": [3, 4, 7, 6],
                "answer": 3
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"In the heap array {arr}, if the node at index 6 is swapped with the root, which step must follow to restore heap?",
                "options": ["Heapify Down", "Heapify Up", "Build Heap", "No operation"],
                "answer": "Heapify Down"
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given the heap array: {arr}\nWhat is the number of leaf nodes in this heap?",
                "options": [len(arr)//2, len(arr)//2 + 1, len(arr)//3, len(arr)//4],
                "answer": len(arr) - (len(arr)//2)
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"In the heap array {arr}, what is the index of the last node?",
                "options": [len(arr), len(arr)-1, len(arr)//2, len(arr)//2 - 1],
                "answer": len(arr)-1
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given the heap array: {arr}\nIf the element at index 0 is less than one of its children, what operation should be performed?",
                "options": ["Heapify Up", "Heapify Down", "Swap with sibling", "No operation"],
                "answer": "Heapify Down"
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"In the heap array {arr}, the node at index 5 has children indices 11 and 12. Which of these are valid indices?",
                "options": [
                    f"Only index 11 (if {len(arr)}>11)",
                    f"Only index 12 (if {len(arr)}>12)",
                    "Both 11 and 12",
                    "Neither"
                ],
                "answer": f"Only index 11 (if {len(arr)}>11)" if len(arr) > 11 and len(arr) <= 12 else "Neither"
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given heap array: {arr}\nWhat is the parent index of node 10?",
                "options": [4, 5, 6, 9],
                "answer": 4
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Which index corresponds to the left child of node at index 4 in the heap array {arr}?",
                "options": [8, 9, 10, 7],
                "answer": 9
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"In the heap array {arr}, if node at index 3 is swapped with node at index 7, what operation is needed to restore heap?",
                "options": ["Heapify Up", "Heapify Down", "Build Heap", "No operation"],
                "answer": "Heapify Down"
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"Given the heap array {arr}, what is the formula for the right child of node i?",
                "options": ["2*i", "2*i + 1", "2*i + 2", "i//2"],
                "answer": "2*i + 2"
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"What is the index of the leftmost leaf node in the heap array {arr}?",
                "options": [len(arr)//2, len(arr)//2 - 1, len(arr)//2 + 1, len(arr) - 1],
                "answer": len(arr)//2
            }
        )(),

        lambda: (lambda arr=generate_array_heap3():
            {
                "question": f"In the heap array {arr}, which of the following nodes are leaf nodes?",
                "options": [[len(arr)//2, len(arr)//2 + 1, len(arr) - 1], [0, 1, 2], [1, 2, 3], [len(arr)//3, len(arr)//4]],
                "answer": [len(arr)//2, len(arr)//2 + 1, len(arr) - 1]
            }
        )(),
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
        },
        lambda: {
            "question": "Match Heap Sort terms:\n1. Max-Heap\n2. Min-Heap\n3. Heap Size\n4. Leaf Node",
            "pairs": {
                "1": "Parent nodes are greater than or equal to children",
                "2": "Parent nodes are less than or equal to children",
                "3": "Number of elements in heap",
                "4": "Node with no children"
            },
            "answer": "1->Parent nodes are greater than or equal to children, 2->Parent nodes are less than or equal to children, 3->Number of elements in heap, 4->Node with no children"
        },
        lambda: {
            "question": "Match the terms:\n1. Heapify\n2. Build-Heap\n3. Root\n4. Child",
            "pairs": {
                "1": "Restore heap property for a node",
                "2": "Create heap from unordered array",
                "3": "Top node in heap",
                "4": "Node below another node"
            },
            "answer": "1->Restore heap property for a node, 2->Create heap from unordered array, 3->Top node in heap, 4->Node below another node"
        },
        lambda: {
            "question": "Match Heap Sort steps:\n1. Swap root with last element\n2. Reduce heap size\n3. Heapify root\n4. Repeat until sorted",
            "pairs": {
                "1": "Place max element at the end",
                "2": "Exclude last element from heap",
                "3": "Fix heap property after extraction",
                "4": "Continue sorting process"
            },
            "answer": "1->Place max element at the end, 2->Exclude last element from heap, 3->Fix heap property after extraction, 4->Continue sorting process"
        },
        lambda: {
            "question": "Match the array indices:\n1. Parent of i\n2. Left child of i\n3. Right child of i\n4. Root index",
            "pairs": {
                "1": "(i-1)//2",
                "2": "2*i + 1",
                "3": "2*i + 2",
                "4": "0"
            },
            "answer": "1->(i-1)//2, 2->2*i + 1, 3->2*i + 2, 4->0"
        },
        lambda: {
            "question": "Match Heap Sort concepts:\n1. Stability\n2. In-place\n3. Time complexity\n4. Auxiliary space",
            "pairs": {
                "1": "Heap Sort is not stable",
                "2": "Heap Sort sorts in-place",
                "3": "O(n log n)",
                "4": "O(1)"
            },
            "answer": "1->Heap Sort is not stable, 2->Heap Sort sorts in-place, 3->O(n log n), 4->O(1)"
        },
        lambda: {
            "question": "Match Heap Sort terms:\n1. Max-Heap\n2. Min-Heap\n3. Extract-Max\n4. Heapify",
            "pairs": {
                "1": "Largest element at root",
                "2": "Smallest element at root",
                "3": "Remove root element",
                "4": "Maintain heap property"
            },
            "answer": "1->Largest element at root, 2->Smallest element at root, 3->Remove root element, 4->Maintain heap property"
        },
        lambda: {
            "question": "Match Heap Sort phases:\n1. Build Heap\n2. Sort Phase\n3. Extraction\n4. Heapify",
            "pairs": {
                "1": "Initialize heap structure",
                "2": "Swap and heapify repeatedly",
                "3": "Remove max element",
                "4": "Restore heap property"
            },
            "answer": "1->Initialize heap structure, 2->Swap and heapify repeatedly, 3->Remove max element, 4->Restore heap property"
        },
        lambda: {
            "question": "Match Heap Sort terms with descriptions:\n1. Complete binary tree\n2. Heap property\n3. Root\n4. Leaf",
            "pairs": {
                "1": "All levels filled except possibly last",
                "2": "Parent is greater than children",
                "3": "Top element in heap",
                "4": "Node with no children"
            },
            "answer": "1->All levels filled except possibly last, 2->Parent is greater than children, 3->Top element in heap, 4->Node with no children"
        },
        lambda: {
            "question": "Match Heap Sort terms:\n1. Swap\n2. Extract Max\n3. Heapify\n4. Build Heap",
            "pairs": {
                "1": "Exchange two elements",
                "2": "Remove root element",
                "3": "Restore heap property",
                "4": "Create heap from array"
            },
            "answer": "1->Exchange two elements, 2->Remove root element, 3->Restore heap property, 4->Create heap from array"
        },
        lambda: {
            "question": "Match Heap Sort data structure terms:\n1. Heap Size\n2. Capacity\n3. Indexing\n4. Height",
            "pairs": {
                "1": "Number of elements in heap",
                "2": "Maximum possible elements",
                "3": "Position of node in array",
                "4": "Number of levels in heap"
            },
            "answer": "1->Number of elements in heap, 2->Maximum possible elements, 3->Position of node in array, 4->Number of levels in heap"
        },
        lambda: {
            "question": "Match Heap Sort terms:\n1. Leaf Node\n2. Internal Node\n3. Parent\n4. Child",
            "pairs": {
                "1": "Node without children",
                "2": "Node with at least one child",
                "3": "Node above child",
                "4": "Node below parent"
            },
            "answer": "1->Node without children, 2->Node with at least one child, 3->Node above child, 4->Node below parent"
        },
        lambda: {
            "question": "Match Heap Sort properties:\n1. Stability\n2. Time Complexity\n3. Space Complexity\n4. Type",
            "pairs": {
                "1": "Not stable",
                "2": "O(n log n)",
                "3": "O(1)",
                "4": "Comparison-based sort"
            },
            "answer": "1->Not stable, 2->O(n log n), 3->O(1), 4->Comparison-based sort"
        },
        lambda: {
            "question": "Match the Heap Sort steps:\n1. Build Heap\n2. Extract Max\n3. Heapify\n4. Repeat",
            "pairs": {
                "1": "Initialize heap",
                "2": "Remove root",
                "3": "Fix heap",
                "4": "Until sorted"
            },
            "answer": "1->Initialize heap, 2->Remove root, 3->Fix heap, 4->Until sorted"
        },
        lambda: {
            "question": "Match Heap Sort terms:\n1. Complete Binary Tree\n2. Max Heap\n3. Min Heap\n4. Heapify",
            "pairs": {
                "1": "Fully filled tree levels",
                "2": "Parent >= children",
                "3": "Parent <= children",
                "4": "Restore heap property"
            },
            "answer": "1->Fully filled tree levels, 2->Parent >= children, 3->Parent <= children, 4->Restore heap property"
        },
        lambda: {
            "question": "Match Heap Sort terms:\n1. Swap\n2. Extract\n3. Heap Size\n4. Height",
            "pairs": {
                "1": "Exchange elements",
                "2": "Remove max element",
                "3": "Number of elements",
                "4": "Number of levels"
            },
            "answer": "1->Exchange elements, 2->Remove max element, 3->Number of elements, 4->Number of levels"
        },
        lambda: {
            "question": "Match Heap Sort steps:\n1. Insert\n2. Heapify Up\n3. Extract\n4. Heapify Down",
            "pairs": {
                "1": "Add element to heap",
                "2": "Restore heap up",
                "3": "Remove root",
                "4": "Restore heap down"
            },
            "answer": "1->Add element to heap, 2->Restore heap up, 3->Remove root, 4->Restore heap down"
        },
        lambda: {
            "question": "Match Heap Sort characteristics:\n1. Time Complexity\n2. Space Complexity\n3. Stability\n4. In-place",
            "pairs": {
                "1": "O(n log n)",
                "2": "O(1)",
                "3": "No",
                "4": "Yes"
            },
            "answer": "1->O(n log n), 2->O(1), 3->No, 4->Yes"
        },
        lambda: {
            "question": "Match the Heap Sort terms:\n1. Parent\n2. Left Child\n3. Right Child\n4. Root",
            "pairs": {
                "1": "Node above children",
                "2": "2*i + 1",
                "3": "2*i + 2",
                "4": "Index 0"
            },
            "answer": "1->Node above children, 2->2*i + 1, 3->2*i + 2, 4->Index 0"
        }
    ],

    "ECQ": [
    lambda: {"question": "Explain the process of building a max heap from an unsorted array.", "answer": "By heapifying each non-leaf node from the bottom up."},
    lambda: {"question": "Describe how the heapify operation maintains the heap property.", "answer": "It swaps a node with its largest child recursively."},
    lambda: {"question": "Why is Heap Sort not considered a stable sorting algorithm?", "answer": "Because it may change the order of equal elements."},
    lambda: {"question": "Discuss the space complexity of Heap Sort and why it is O(1).", "answer": "Because it requires no extra space except a few variables."},
    lambda: {"question": "Explain the time complexity of Heap Sort in worst, average, and best cases.", "answer": "All are O(n log n)."},
    lambda: {"question": "Describe the difference between a max-heap and a min-heap.", "answer": "In a max-heap, parent >= children; in min-heap, parent <= children."},
    lambda: {"question": "How does Heap Sort compare with Quick Sort in terms of worst-case performance?", "answer": "Heap Sort has better worst-case O(n log n); Quick Sort can degrade to O(n^2)."},
    lambda: {"question": "Explain the role of the binary heap data structure in Heap Sort.", "answer": "It is used to efficiently extract the maximum element."},
    lambda: {"question": "Why is Heap Sort considered an in-place sorting algorithm?", "answer": "Because it sorts using constant additional memory."},
    lambda: {"question": "Describe how extraction of the root works in Heap Sort.", "answer": "Swap root with last element, reduce heap size, and heapify root."},
    lambda: {"question": "Explain why the height of a heap is floor(log n).", "answer": "Because a binary heap is a complete binary tree."},
    lambda: {"question": "Discuss the advantages and disadvantages of Heap Sort.", "answer": "Advantages: O(n log n) worst-case; Disadvantages: not stable."},
    lambda: {"question": "How does the array representation of a heap facilitate efficient sorting?", "answer": "Allows O(1) access to children and parent."},
    lambda: {"question": "Explain the significance of the heap property in Heap Sort.", "answer": "It ensures the root is always the largest/smallest."},
    lambda: {"question": "Describe the steps to restore the heap property after removing the root.", "answer": "Move last element to root and heapify down."},
    lambda: {"question": "Explain the difference between Heap Sort and Merge Sort.", "answer": "Heap Sort is in-place; Merge Sort is stable but uses O(n) space."},
    lambda: {"question": "What makes Heap Sort suitable for sorting large data sets?", "answer": "Consistent O(n log n) performance and low memory usage."},
    lambda: {"question": "How is the heap size adjusted during the sorting process?", "answer": "It is reduced by one after each extraction."},
    lambda: {"question": "Describe how duplicate values are handled in Heap Sort.", "answer": "They are sorted but may not maintain original order."},
    lambda: {"question": "Explain the process of heapifying down vs heapifying up.", "answer": "Heapify down is used in sorting; up is used in insertion."},
    lambda: {"question": "Why does building a heap take O(n) time, not O(n log n)?", "answer": "Because most heapify calls are on shallow subtrees."},
    lambda: {"question": "Discuss practical scenarios where Heap Sort is preferred.", "answer": "When memory is limited and worst-case performance is critical."},
    lambda: {"question": "Explain how Heap Sort works on nearly sorted data.", "answer": "Performance remains O(n log n), no optimization for order."},
    lambda: {"question": "How does Heap Sort maintain its efficiency regardless of input order?", "answer": "It builds a heap and processes elements uniformly."},
    lambda: {"question": "Discuss the effect of the initial array arrangement on Heap Sort.", "answer": "Heap Sort is not affected by initial order of elements."}
],
    "EXPQ": [
    lambda: {"question": "Complete the expression for the left child index in a heap array: left_child(i) = ____", "answer": "2*i + 1"},
    lambda: {"question": "Complete the expression for the parent index of a node i: parent(i) = ____", "answer": "(i - 1) // 2"},
    lambda: {"question": "Fill in the blank: The worst-case time complexity of heapify operation is O(____)", "answer": "log n"},
    lambda: {"question": "Fill in the blank: Heap Sort builds a ____ heap from the input array before sorting.", "answer": "max"},
    lambda: {"question": "Complete the sentence: Heap Sort has a space complexity of O(____) since it sorts in-place.", "answer": "1"},
    lambda: {"question": "Fill in the blank: In Heap Sort, the root node is always the ____ element in a max heap.", "answer": "largest"},
    lambda: {"question": "Complete the statement: Heap Sort sorts the array by repeatedly ____ the root element.", "answer": "extracting"},
    lambda: {"question": "Fill in the blank: The height of a heap with n nodes is floor(log base ____ of n).", "answer": "2"},
    lambda: {"question": "Complete the expression for the right child index in a heap array: right_child(i) = ____", "answer": "2*i + 2"},
    lambda: {"question": "Fill in the blank: Heap Sort's worst-case time complexity is O(n ____ n).", "answer": "log"},
    lambda: {"question": "Complete the statement: Heap Sort is not a ____ sorting algorithm because it may reorder equal elements.", "answer": "stable"},
    lambda: {"question": "Fill in the blank: The heap property ensures that every parent node is ____ than or equal to its children in a max heap.", "answer": "greater"},
    lambda: {"question": "Complete the expression: The parent of node i is at index ____.", "answer": "(i - 1) // 2"},
    lambda: {"question": "Fill in the blank: The initial step in Heap Sort is to ____ the input array into a heap.", "answer": "heapify"},
    lambda: {"question": "Complete the sentence: After extracting the root, Heap Sort ____ the heap to maintain the heap property.", "answer": "heapifies"},
    lambda: {"question": "Fill in the blank: Heap Sort sorts the array ____ (in ascending/descending) order by using a max heap.", "answer": "ascending"},
    lambda: {"question": "Complete the expression for the total number of nodes in a complete binary tree with height h: 2^(h+1) - ____.", "answer": "1"},
    lambda: {"question": "Fill in the blank: Heap Sort's space complexity is O(____) because it does not require additional arrays.", "answer": "1"},
    lambda: {"question": "Complete the statement: Heap Sort uses a ____ tree structure for efficient sorting.", "answer": "binary"},
    lambda: {"question": "Fill in the blank: The leaf nodes of a heap are located in the ____ levels of the tree.", "answer": "last"},
    lambda: {"question": "Complete the expression: The maximum number of nodes at level i of a binary heap is ____.", "answer": "2^i"},
    lambda: {"question": "Fill in the blank: The extract max operation in Heap Sort takes O(____) time.", "answer": "log n"},
    lambda: {"question": "Complete the sentence: Heap Sort is preferred over Quick Sort when worst-case time complexity is ____.", "answer": "important"},
    lambda: {"question": "Fill in the blank: Heap Sort rearranges elements by ____ (swapping/comparing) parent and child nodes.", "answer": "swapping"},
    lambda: {"question": "Complete the statement: Heap Sort is classified as a ____-based sorting algorithm.", "answer": "comparison"}
]
}

heap_question_bank = {
    "1": level_1,
    "2": level_2,
    "3": level_3,
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
    level = input("Choose Level (1: Level1, 2: Level2, 3: Level3): ").strip()
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