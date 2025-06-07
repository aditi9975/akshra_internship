import random

def random_n(min_val=5, max_val=15):
    return random.randint(min_val, max_val)

def random_choice(choices):
    return random.choice(choices)

templates = {
    "level1": {
        "TFQ": [
            lambda: {
                "question": "True or False: Linear Search checks each element in the array one by one.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can only be used on sorted arrays.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search stops searching after finding the key.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search always finds the key if it exists in the array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is also called sequential search.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can skip elements in the array.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search is efficient for small arrays.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search returns -1 if the key is not found.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search compares the key with every element in the array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used for both numbers and strings.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is faster than Binary Search for large arrays.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search always starts from the first element.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can find multiple occurrences of the key.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be used on linked lists.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search does not modify the original array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is a recursive algorithm by default.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search is easy to implement.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to search for a character in a string.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is not suitable for very large datasets.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to search in a list of names.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can only be used with integers.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search is a type of brute-force algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to find the minimum value in an array.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be implemented using a for loop.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to check if an array is empty.",
                "answer": "False"
            }
        ],
        "MCQ": [
            lambda: {
                "question": "What does Linear Search do?",
                "options": [
                    "Checks each element one by one",
                    "Divides the array in half",
                    "Sorts the array",
                    "Skips elements randomly"
                ],
                "answer": "Checks each element one by one"
            },
            lambda: {
                "question": "Which of the following is true about Linear Search?",
                "options": [
                    "It works only on sorted arrays",
                    "It can be used on any array",
                    "It is faster than Binary Search for large arrays",
                    "It requires the array to be reversed"
                ],
                "answer": "It can be used on any array"
            },
            lambda: {
                "question": "What is the best-case time complexity of Linear Search?",
                "options": [
                    "O(1)",
                    "O(n)",
                    "O(log n)",
                    "O(n^2)"
                ],
                "answer": "O(1)"
            },
            lambda: {
                "question": "What is returned if the key is not found in Linear Search?",
                "options": [
                    "-1",
                    "0",
                    "None",
                    "The last element"
                ],
                "answer": "-1"
            },
            lambda: {
                "question": "Which loop is commonly used in Linear Search?",
                "options": [
                    "for loop",
                    "while loop",
                    "do-while loop",
                    "Both for and while loop"
                ],
                "answer": "Both for and while loop"
            },
            lambda: {
                "question": "Which of these is NOT a feature of Linear Search?",
                "options": [
                    "Works on unsorted arrays",
                    "Compares each element",
                    "Requires sorted array",
                    "Simple to implement"
                ],
                "answer": "Requires sorted array"
            },
            lambda: {
                "question": "What is the worst-case time complexity of Linear Search?",
                "options": [
                    "O(n)",
                    "O(1)",
                    "O(log n)",
                    "O(n log n)"
                ],
                "answer": "O(n)"
            },
            lambda: {
                "question": "Which data structure can Linear Search be used on?",
                "options": [
                    "Array",
                    "Linked List",
                    "Both Array and Linked List",
                    "None"
                ],
                "answer": "Both Array and Linked List"
            },
            lambda: {
                "question": "Which of the following is a disadvantage of Linear Search?",
                "options": [
                    "Slow for large arrays",
                    "Cannot be used on unsorted arrays",
                    "Difficult to implement",
                    "Needs extra memory"
                ],
                "answer": "Slow for large arrays"
            },
            lambda: {
                "question": "Which of these is the first step in Linear Search?",
                "options": [
                    "Compare key with first element",
                    "Sort the array",
                    "Compare key with last element",
                    "Reverse the array"
                ],
                "answer": "Compare key with first element"
            },
            lambda: {
                "question": "What happens if the key is found in Linear Search?",
                "options": [
                    "Return its index",
                    "Continue searching",
                    "Return -1",
                    "Delete the key"
                ],
                "answer": "Return its index"
            },
            lambda: {
                "question": "Which of these is NOT required for Linear Search?",
                "options": [
                    "Sorted array",
                    "Array or list",
                    "Key to search",
                    "Loop"
                ],
                "answer": "Sorted array"
            },
            lambda: {
                "question": "Which of the following is a correct statement?",
                "options": [
                    "Linear Search can be used for strings",
                    "Linear Search only works for numbers",
                    "Linear Search sorts the array",
                    "Linear Search skips elements"
                ],
                "answer": "Linear Search can be used for strings"
            },
            lambda: {
                "question": "What is the output if the array is empty in Linear Search?",
                "options": [
                    "-1",
                    "0",
                    "Error",
                    "None"
                ],
                "answer": "-1"
            },
            lambda: {
                "question": "Which of these is the main advantage of Linear Search?",
                "options": [
                    "Simple to code",
                    "Fast for large arrays",
                    "Needs sorted array",
                    "Uses binary logic"
                ],
                "answer": "Simple to code"
            },
            lambda: {
                "question": "Which of these is NOT a valid use of Linear Search?",
                "options": [
                    "Finding a name in a list",
                    "Finding a number in an array",
                    "Sorting an array",
                    "Searching for a character in a string"
                ],
                "answer": "Sorting an array"
            },
            lambda: {
                "question": "What is the main reason to use Linear Search?",
                "options": [
                    "Array is small or unsorted",
                    "Array is always sorted",
                    "Need fast search in large arrays",
                    "Need to sort the array"
                ],
                "answer": "Array is small or unsorted"
            },
            lambda: {
                "question": "Which of these is true for Linear Search?",
                "options": [
                    "It can be used on both sorted and unsorted arrays",
                    "It is only for sorted arrays",
                    "It is faster than Binary Search",
                    "It requires extra space"
                ],
                "answer": "It can be used on both sorted and unsorted arrays"
            },
            lambda: {
                "question": "Which of these is the correct way to stop Linear Search?",
                "options": [
                    "When key is found",
                    "After checking half the array",
                    "After sorting the array",
                    "After finding the maximum value"
                ],
                "answer": "When key is found"
            },
            lambda: {
                "question": "Which of these is NOT a property of Linear Search?",
                "options": [
                    "Checks each element",
                    "Needs sorted array",
                    "Simple logic",
                    "Works on lists"
                ],
                "answer": "Needs sorted array"
            },
            lambda: {
                "question": "Which of these is the correct return value if key is not found?",
                "options": [
                    "-1",
                    "0",
                    "The last element",
                    "None"
                ],
                "answer": "-1"
            },
            lambda: {
                "question": "Which of these is the best case for Linear Search?",
                "options": [
                    "Key at first position",
                    "Key at last position",
                    "Key not present",
                    "Array is empty"
                ],
                "answer": "Key at first position"
            },
            lambda: {
                "question": "Which of these is the worst case for Linear Search?",
                "options": [
                    "Key at last position",
                    "Key at first position",
                    "Key at middle position",
                    "Array is empty"
                ],
                "answer": "Key at last position"
            },
            lambda: {
                "question": "Which of these is NOT a step in Linear Search?",
                "options": [
                    "Compare key with each element",
                    "Sort the array",
                    "Return index if found",
                    "Return -1 if not found"
                ],
                "answer": "Sort the array"
            },
            lambda: {
                "question": "Which of these is a correct statement about Linear Search?",
                "options": [
                    "It is easy to understand",
                    "It is always faster than Binary Search",
                    "It needs a sorted array",
                    "It skips elements"
                ],
                "answer": "It is easy to understand"
            }
        ],
        "MTQ": [
            lambda: {
                "question": "Match the Linear Search concepts:",
                "pairs": {
                    "Unsorted array": "Works fine",
                    "Start from": "First element",
                    "Time Complexity": "O(n)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the following:",
                "pairs": {
                    "Best case": "Key at first position",
                    "Worst case": "Key at last position",
                    "Not found": "Returns -1"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the step to its description:",
                "pairs": {
                    "Compare key": "With each element",
                    "If found": "Return index",
                    "If not found": "Return -1"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the term to its meaning:",
                "pairs": {
                    "Sequential": "One after another",
                    "Unsorted": "No order needed",
                    "Brute-force": "Tries all possibilities"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the scenario to the result:",
                "pairs": {
                    "Key at start": "Best case",
                    "Key at end": "Worst case",
                    "Key missing": "Return -1"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the code to its function:",
                "pairs": {
                    "for i in range(len(arr))": "Loop through array",
                    "if arr[i] == key": "Check for match",
                    "return i": "Return index"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the data type to Linear Search usage:",
                "pairs": {
                    "Array": "Can use",
                    "List": "Can use",
                    "Dictionary": "Cannot use directly"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search type to its property:",
                "pairs": {
                    "Linear Search": "No sorting needed",
                    "Binary Search": "Needs sorted array",
                    "Hash Search": "Uses hash table"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the loop to its use in Linear Search:",
                "pairs": {
                    "for loop": "Commonly used",
                    "while loop": "Can be used",
                    "do-while loop": "Not in Python"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the return value to the situation:",
                "pairs": {
                    "Index": "Key found",
                    "-1": "Key not found",
                    "None": "Not used"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the complexity to the case:",
                "pairs": {
                    "O(1)": "Best case",
                    "O(n)": "Worst case",
                    "O(log n)": "Not for Linear Search"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the statement to its result:",
                "pairs": {
                    "Key is present": "Return index",
                    "Key is absent": "Return -1",
                    "Array is empty": "Return -1"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the code part to its meaning:",
                "pairs": {
                    "arr[i] == key": "Check for equality",
                    "i in range(len(arr))": "Loop variable",
                    "return i": "Return position"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search to its requirement:",
                "pairs": {
                    "Linear Search": "No order needed",
                    "Binary Search": "Sorted array",
                    "Jump Search": "Sorted array"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the property to the search:",
                "pairs": {
                    "Simple": "Linear Search",
                    "Efficient for large arrays": "Binary Search",
                    "Needs hash function": "Hash Search"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the scenario to the number of comparisons:",
                "pairs": {
                    "Key at first": "1",
                    "Key at last": "n",
                    "Key not present": "n"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search to its loop:",
                "pairs": {
                    "Linear Search": "for loop",
                    "Binary Search": "while loop",
                    "Hash Search": "No loop"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the return value to the code:",
                "pairs": {
                    "return i": "Key found",
                    "return -1": "Key not found",
                    "break": "Stop loop"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search to its speed:",
                "pairs": {
                    "Linear Search": "Slow for large arrays",
                    "Binary Search": "Fast for sorted arrays",
                    "Hash Search": "Very fast"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search to its use case:",
                "pairs": {
                    "Linear Search": "Small or unsorted arrays",
                    "Binary Search": "Large sorted arrays",
                    "Hash Search": "Quick lookup"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the code to its output:",
                "pairs": {
                    "arr = []": "Empty array",
                    "arr = [1,2,3]": "Array with 3 elements",
                    "arr = [key]": "Array with key"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the search to its other name:",
                "pairs": {
                    "Linear Search": "Sequential Search",
                    "Binary Search": "Half-interval Search",
                    "Hash Search": "Direct Access"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the array to the search result:",
                "pairs": {
                    "[1,2,3], key=2": "Found at index 1",
                    "[4,5,6], key=7": "Not found",
                    "[], key=1": "Not found"
                },
                "answer": "Correct mapping"
            }
        ],
        "ECQ": [
            lambda: {
                "question": "Fill in the blank: for i in range(len(arr)): if arr[i] == key: return ____",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: If key is not found in the array, return ____",
                "answer": "-1"
            },
            lambda: {
                "question": "Fill in the blank: arr = [1,2,3]; key = 2; for i in range(len(arr)): if arr[i] == key: ____",
                "answer": "return i"
            },
            lambda: {
                "question": "Fill in the blank: To check if array is empty, use if len(arr) == ____",
                "answer": "0"
            },
            lambda: {
                "question": "Fill in the blank: Linear Search uses a ____ to go through the array.",
                "answer": "loop"
            },
            lambda: {
                "question": "Fill in the blank: To compare key with element, use arr[i] ____ key",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: The index of the first element is ____",
                "answer": "0"
            },
            lambda: {
                "question": "Fill in the blank: To return not found, use return ____",
                "answer": "-1"
            },
            lambda: {
                "question": "Fill in the blank: The last index in array arr of size n is ____",
                "answer": "n-1"
            },
            lambda: {
                "question": "Fill in the blank: To start Linear Search, use for i in ____",
                "answer": "range(len(arr))"
            },
            lambda: {
                "question": "Fill in the blank: To check if key is present, use if arr[i] ____ key",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To stop the loop after finding key, use ____",
                "answer": "return i"
            },
            lambda: {
                "question": "Fill in the blank: Linear Search is also called ____ Search.",
                "answer": "Sequential"
            },
            lambda: {
                "question": "Fill in the blank: The time complexity of Linear Search is ____",
                "answer": "O(n)"
            },
            lambda: {
                "question": "Fill in the blank: To search for key in arr, use ____ in arr",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: To get the length of arr, use ____",
                "answer": "len(arr)"
            },
            lambda: {
                "question": "Fill in the blank: To check if arr is not empty, use if len(arr) ____ 0",
                "answer": ">"
            },
            lambda: {
                "question": "Fill in the blank: To print the index, use print(____)",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: To check each element, use a ____",
                "answer": "loop"
            },
            lambda: {
                "question": "Fill in the blank: To compare two values, use ____ operator",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To return the index, use ____ statement",
                "answer": "return"
            },
            lambda: {
                "question": "Fill in the blank: To search for a string in a list, use ____ Search",
                "answer": "Linear"
            },
            lambda: {
                "question": "Fill in the blank: To check if key is not in arr, use if key ____ arr",
                "answer": "not in"
            },
            lambda: {
                "question": "Fill in the blank: To start from the first element, use index ____",
                "answer": "0"
            },
            lambda: {
                "question": "Fill in the blank: To return not found, use ____ -1",
                "answer": "return"
            }
        ],
        "NQ": [
            lambda: (lambda n: {
                "question": f"If the array has {n} elements, how many comparisons does Linear Search take in the worst case?",
                "answer": str(n)
            })(random_choice([5, 7, 8, 10, 12, 15])),
            lambda: (lambda n: {
                "question": f"If the key is at the first position in an array of {n} elements, how many comparisons are needed?",
                "answer": "1"
            })(random_choice([5, 6, 8, 9, 10, 12])),
            lambda: (lambda n: {
                "question": f"If the key is at the last position in an array of {n} elements, how many comparisons are needed?",
                "answer": str(n)
            })(random_choice([6, 7, 9, 11, 13, 14])),
            lambda: (lambda n: {
                "question": f"If the key is not present in an array of {n} elements, how many comparisons are made?",
                "answer": str(n)
            })(random_choice([5, 8, 10, 11, 12, 14])),
            lambda: (lambda n, idx: {
                "question": f"In an array of {n} elements, if the key is at index {idx}, how many comparisons are needed?",
                "answer": str(idx + 1)
            })(random_choice([7, 8, 9, 10, 12]), random_choice([2, 3, 4, 5])),
            lambda: (lambda n: {
                "question": f"If you search for a key in an array of {n} elements and it is not found, what is the return value?",
                "answer": "-1"
            })(random_choice([5, 6, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If the key is at index 2 in an array of {n} elements, how many comparisons are needed?",
                "answer": "3"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the key is at index 0 in an array of {n} elements, how many comparisons are needed?",
                "answer": "1"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the key is at index 4 in an array of {n} elements, how many comparisons are needed?",
                "answer": "5"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If the array has {n} elements and the key is not present, how many times is the loop executed?",
                "answer": str(n)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In an array of {n} elements, what is the maximum number of comparisons Linear Search can make?",
                "answer": str(n)
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If the key is at index 1 in an array of {n} elements, how many comparisons are needed?",
                "answer": "2"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In an array of {n} elements, if the key is at index 3, how many comparisons are needed?",
                "answer": "4"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the key is not present in an array of {n} elements, what is the output?",
                "answer": "-1"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the array has {n} elements and the key is at the last index, how many comparisons are needed?",
                "answer": str(n)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the key is at index 3 in an array of {n} elements, how many comparisons are needed?",
                "answer": "4"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In an array of {n} elements, if the key is at index 0, how many comparisons are needed?",
                "answer": "1"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the array has {n} elements and the key is not present, what is the return value?",
                "answer": "-1"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the key is at index 2 in an array of {n} elements, how many comparisons are needed?",
                "answer": "3"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In an array of {n} elements, what is the minimum number of comparisons Linear Search can make?",
                "answer": "1"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the key is at index 1 in an array of {n} elements, how many comparisons are needed?",
                "answer": "2"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the key is at index 4 in an array of {n} elements, how many comparisons are needed?",
                "answer": "5"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the array has {n} elements and the key is at the first index, how many comparisons are needed?",
                "answer": "1"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"In an array of {n} elements, if the key is not present, how many comparisons are made?",
                "answer": str(n)
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the key is at index 3 in an array of {n} elements, how many comparisons are needed?",
                "answer": "4"
            })(random_choice([5, 6, 7, 8, 9]))
        ]
    },

    "level2": {
        "TFQ": [
            lambda: {
                "question": "True or False: Linear Search checks each element until the key is found or the end is reached.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can only be used on arrays with unique elements.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search always requires O(n) comparisons, even if the key is at the first position.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search is also known as sequential search.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to find multiple occurrences of a key.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is more efficient than Binary Search for large sorted arrays.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be implemented using recursion.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search stops searching after finding the first match.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used on linked lists.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search requires the array to be sorted.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search is not suitable for very large datasets.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to find the minimum value in an array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search always returns the index of the last occurrence of the key.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be used on both arrays and lists in Python.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is a brute-force algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to check if an array is empty.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to count the number of times a key appears.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is not affected by duplicate elements in the array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to search for a substring in a string.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is always faster than Binary Search.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to find the maximum value in an array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is a recursive algorithm by default.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to search in a tuple.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to search for None values in a list.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is not suitable for real-time applications with large data.",
                "answer": "True"
            }
        ],
        "MCQ": [
            lambda: {
                "question": "What is the best-case time complexity of Linear Search?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
                "answer": "O(1)"
            },
            lambda: {
                "question": "Which of the following is true about Linear Search?",
                "options": [
                    "It requires sorted data",
                    "It checks elements sequentially",
                    "It skips every alternate element",
                    "It always returns -1"
                ],
                "answer": "It checks elements sequentially"
            },
            lambda: {
                "question": "Which data structure is NOT suitable for Linear Search?",
                "options": ["Array", "Linked List", "Hash Table", "List"],
                "answer": "Hash Table"
            },
            lambda: {
                "question": "What does Linear Search return if the key is not found?",
                "options": ["0", "-1", "None", "IndexError"],
                "answer": "-1"
            },
            lambda: {
                "question": "Which of the following is a disadvantage of Linear Search?",
                "options": [
                    "Requires sorted data",
                    "Inefficient for large datasets",
                    "Cannot find duplicates",
                    "Needs extra space"
                ],
                "answer": "Inefficient for large datasets"
            },
            lambda: {
                "question": "Which scenario gives the worst-case performance for Linear Search?",
                "options": [
                    "Key at first index",
                    "Key at last index",
                    "Key in the middle",
                    "Key not present"
                ],
                "answer": "Key not present"
            },
            lambda: {
                "question": "Which of the following can Linear Search NOT do?",
                "options": [
                    "Find the first occurrence of a key",
                    "Find the last occurrence of a key",
                    "Count all occurrences of a key",
                    "Sort the array"
                ],
                "answer": "Sort the array"
            },
            lambda: {
                "question": "Which is the average number of comparisons in Linear Search for n elements?",
                "options": [
                    "n/2",
                    "n",
                    "log n",
                    "n^2"
                ],
                "answer": "n/2"
            },
            lambda: {
                "question": "Which of the following is NOT a property of Linear Search?",
                "options": [
                    "Works on unsorted data",
                    "Can find multiple keys",
                    "Requires extra memory",
                    "Simple to implement"
                ],
                "answer": "Requires extra memory"
            },
            lambda: {
                "question": "Which of the following is the correct way to implement Linear Search in Python?",
                "options": [
                    "for i in range(len(arr)): if arr[i] == key: return i",
                    "arr.sort(); return arr.index(key)",
                    "while arr[i] != key: i += 1",
                    "arr.find(key)"
                ],
                "answer": "for i in range(len(arr)): if arr[i] == key: return i"
            },
            lambda: {
                "question": "Which of the following is NOT a valid use case for Linear Search?",
                "options": [
                    "Finding a student's roll number in a list",
                    "Searching for a word in a dictionary",
                    "Finding a book in an unsorted shelf",
                    "Checking if a value exists in a list"
                ],
                "answer": "Searching for a word in a dictionary"
            },
            lambda: {
                "question": "Which of the following is the correct output if key is not found in Linear Search?",
                "options": ["-1", "0", "None", "False"],
                "answer": "-1"
            },
            lambda: {
                "question": "Which of the following is the main advantage of Linear Search?",
                "options": [
                    "Fast for large datasets",
                    "Works on unsorted data",
                    "Requires sorted data",
                    "Uses binary search logic"
                ],
                "answer": "Works on unsorted data"
            },
            lambda: {
                "question": "Which of the following is NOT a step in Linear Search?",
                "options": [
                    "Compare key with current element",
                    "Move to next element if not found",
                    "Divide array into halves",
                    "Return index if found"
                ],
                "answer": "Divide array into halves"
            },
            lambda: {
                "question": "Which of the following is the correct time complexity for Linear Search in the average case?",
                "options": ["O(n)", "O(1)", "O(log n)", "O(n^2)"],
                "answer": "O(n)"
            },
            lambda: {
                "question": "Which of the following is NOT a limitation of Linear Search?",
                "options": [
                    "Slow for large arrays",
                    "Cannot handle duplicates",
                    "Inefficient for sorted arrays",
                    "Checks every element"
                ],
                "answer": "Cannot handle duplicates"
            },
            lambda: {
                "question": "Which of the following is the correct way to search for a key in a list using Linear Search?",
                "options": [
                    "Use a for loop to check each element",
                    "Sort the list and use binary search",
                    "Use a hash map",
                    "Use recursion only"
                ],
                "answer": "Use a for loop to check each element"
            },
            lambda: {
                "question": "Which of the following is NOT true about Linear Search?",
                "options": [
                    "It is easy to implement",
                    "It is efficient for small datasets",
                    "It is faster than binary search for large datasets",
                    "It can be used on unsorted data"
                ],
                "answer": "It is faster than binary search for large datasets"
            },
            lambda: {
                "question": "Which of the following is the correct return value if the key is found at index 3?",
                "options": ["3", "4", "0", "-1"],
                "answer": "3"
            },
            lambda: {
                "question": "Which of the following is NOT a feature of Linear Search?",
                "options": [
                    "Works on unsorted data",
                    "Can find all occurrences",
                    "Requires extra space",
                    "Simple logic"
                ],
                "answer": "Requires extra space"
            },
            lambda: {
                "question": "Which of the following is the correct way to count occurrences of a key using Linear Search?",
                "options": [
                    "Use a counter and increment for each match",
                    "Return after first match",
                    "Sort the array first",
                    "Use binary search"
                ],
                "answer": "Use a counter and increment for each match"
            },
            lambda: {
                "question": "Which of the following is NOT a valid result of Linear Search?",
                "options": [
                    "Index of key",
                    "-1 if not found",
                    "Number of comparisons",
                    "Sorted array"
                ],
                "answer": "Sorted array"
            },
            lambda: {
                "question": "Which of the following is the correct way to search for a string in a list using Linear Search?",
                "options": [
                    "Compare each element with the string",
                    "Sort the list first",
                    "Use binary search",
                    "Use hash map"
                ],
                "answer": "Compare each element with the string"
            },
            lambda: {
                "question": "Which of the following is NOT a valid input for Linear Search?",
                "options": [
                    "List of integers",
                    "List of strings",
                    "Dictionary",
                    "Tuple"
                ],
                "answer": "Dictionary"
            }
        ],
        "MTQ": [
            lambda: {
                "question": "Match the Linear Search term to its meaning:",
                "pairs": {
                    "Best Case": "Key at first index",
                    "Worst Case": "Key not present",
                    "Average Case": "Key in middle"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search step to its description:",
                "pairs": {
                    "Compare": "Check if element equals key",
                    "Move": "Go to next element",
                    "Return": "Give index if found"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the scenario to the number of comparisons:",
                "pairs": {
                    "Key at index 0": "1 comparison",
                    "Key at index n-1": "n comparisons",
                    "Key not present": "n comparisons"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search property to its explanation:",
                "pairs": {
                    "Unsorted data": "Works fine",
                    "Duplicates": "Can find all",
                    "Sorted data": "Not required"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Python code to its function:",
                "pairs": {
                    "for i in range(len(arr))": "Iterate through array",
                    "if arr[i] == key": "Check for match",
                    "return i": "Return index"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search outcome to its result:",
                "pairs": {
                    "Key found": "Return index",
                    "Key not found": "Return -1",
                    "Multiple keys": "Return first index"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search type to its feature:",
                "pairs": {
                    "Iterative": "Uses loop",
                    "Recursive": "Calls itself",
                    "Hybrid": "Not common"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search application to its example:",
                "pairs": {
                    "Find student": "Roll number in list",
                    "Find book": "Title in shelf",
                    "Find value": "Number in array"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search limitation to its effect:",
                "pairs": {
                    "Slow": "Large arrays",
                    "Simple": "Easy to code",
                    "No sorting": "Works on any order"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search code to its output:",
                "pairs": {
                    "arr = [1,2,3]; key=2": "Index 1",
                    "arr = [4,5,6]; key=7": "-1",
                    "arr = [7,8,9]; key=7": "Index 0"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search scenario to its complexity:",
                "pairs": {
                    "Best case": "O(1)",
                    "Worst case": "O(n)",
                    "Average case": "O(n)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search use to its result:",
                "pairs": {
                    "Find first match": "Return index",
                    "Find all matches": "Return list of indices",
                    "Count matches": "Return count"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search logic to its step:",
                "pairs": {
                    "Start": "First element",
                    "Check": "Compare with key",
                    "End": "Return result"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search code to its error:",
                "pairs": {
                    "No return": "Does not give index",
                    "No loop": "Does not check all",
                    "No comparison": "Does not find key"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search feature to its benefit:",
                "pairs": {
                    "Simple": "Easy to understand",
                    "No sorting": "Works on any data",
                    "Flexible": "Any data type"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search result to its meaning:",
                "pairs": {
                    "Index": "Key found",
                    "-1": "Key not found",
                    "Multiple indices": "Duplicates found"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search code to its output:",
                "pairs": {
                    "arr = [10,20,30]; key=20": "Index 1",
                    "arr = [5,6,7]; key=8": "-1",
                    "arr = [2,2,2]; key=2": "Index 0"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search step to its action:",
                "pairs": {
                    "Initialize": "Set i=0",
                    "Compare": "arr[i]==key",
                    "Increment": "i+=1"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search scenario to its output:",
                "pairs": {
                    "Key at start": "1 comparison",
                    "Key at end": "n comparisons",
                    "Key not found": "n comparisons"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search logic to its result:",
                "pairs": {
                    "Key found": "Return index",
                    "Key not found": "Return -1",
                    "Multiple keys": "Return first index"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search code to its function:",
                "pairs": {
                    "for i in arr": "Iterate elements",
                    "if i==key": "Check match",
                    "break": "Stop loop"
                },
                "answer": "Correct mapping"
            }
        ],
        "ECQ": [
            lambda: {
                "question": "Fill in the blank: for i in range(len(arr)): if arr[i] == key: return ____",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: if arr[i] != key: continue else: return ____",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: To check if key is present, use 'if key ____ arr:'",
                "answer": "in"
            },
            lambda: {
                "question": "Fill in the blank: To count occurrences, use 'arr.____(key)'",
                "answer": "count"
            },
            lambda: {
                "question": "Fill in the blank: To return -1 if not found, use 'return ____'",
                "answer": "-1"
            },
            lambda: {
                "question": "Fill in the blank: To start search, use 'for i ____ range(len(arr)):'",
                "answer": "in"
            },
            lambda: {
                "question": "Fill in the blank: To compare, use 'if arr[i] ____ key:'",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To increment index, use 'i ____ 1'",
                "answer": "+="
            },
            lambda: {
                "question": "Fill in the blank: To break loop after finding key, use '____'",
                "answer": "break"
            },
            lambda: {
                "question": "Fill in the blank: To return index, use 'return ____'",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: To check if array is empty, use 'if len(arr) ____ 0:'",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To search for a string, use 'if arr[i] ____ key:'",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To search in a tuple, use 'if key ____ arr:'",
                "answer": "in"
            },
            lambda: {
                "question": "Fill in the blank: To return first match, use 'return ____'",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: To search for None, use 'if arr[i] ____ None:'",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To check all elements, use 'for ____ in arr:'",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: To return after first match, use '____'",
                "answer": "return"
            },
            lambda: {
                "question": "Fill in the blank: To search in reverse, use 'for i in range(len(arr)-1, ____,-1):'",
                "answer": "-1"
            },
            lambda: {
                "question": "Fill in the blank: To check for duplicates, use 'if arr.count(key) ____ 1:'",
                "answer": ">"
            },
            lambda: {
                "question": "Fill in the blank: To search for minimum, use 'min(arr) ____ key'",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To search for maximum, use 'max(arr) ____ key'",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To check if key is not present, use 'if key ____ arr:'",
                "answer": "not in"
            },
            lambda: {
                "question": "Fill in the blank: To return all indices, use '[i for i in range(len(arr)) if arr[i] ____ key]'",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To check if key is at first index, use 'if arr[0] ____ key:'",
                "answer": "=="
            },
            lambda: {
                "question": "Fill in the blank: To check if key is at last index, use 'if arr[-1] ____ key:'",
                "answer": "=="
            }
        ],
        "NQ": [
            lambda: (lambda n: {
                "question": f"If the array has {n} elements, how many comparisons does Linear Search take in the worst case?",
                "answer": str(n)
            })(random_choice([5, 7, 10, 12, 15])),
            lambda: (lambda n: {
                "question": f"If the key is at index 0 in an array of size {n}, how many comparisons are needed?",
                "answer": "1"
            })(random_choice([6, 8, 11, 13, 14])),
            lambda: (lambda n: {
                "question": f"If the key is at index {n-1} in an array of size {n}, how many comparisons are needed?",
                "answer": str(n)
            })(random_choice([5, 9, 12, 13, 15])),
            lambda: (lambda n, idx: {
                "question": f"In an array of size {n}, if the key is at index {idx}, how many comparisons are needed?",
                "answer": str(idx + 1)
            })(random_choice([7, 8, 10, 12, 14]), random_choice([2, 3, 4, 5, 6])),
            lambda: (lambda n: {
                "question": f"If the key is not present in an array of size {n}, how many comparisons are made?",
                "answer": str(n)
            })(random_choice([6, 8, 10, 11, 13])),
            lambda: (lambda n: {
                "question": f"If the key is at the middle index in an array of size {n}, how many comparisons are needed?",
                "answer": str((n // 2) + 1)
            })(random_choice([7, 9, 11, 13, 15])),
            lambda: (lambda n: {
                "question": f"If the key is at index 1 in an array of size {n}, how many comparisons are needed?",
                "answer": "2"
            })(random_choice([5, 6, 8, 10, 12])),
            lambda: (lambda n: {
                "question": f"If the key is at index 2 in an array of size {n}, how many comparisons are needed?",
                "answer": "3"
            })(random_choice([7, 8, 9, 10, 11])),
            lambda: (lambda n: {
                "question": f"If the key is at index 3 in an array of size {n}, how many comparisons are needed?",
                "answer": "4"
            })(random_choice([8, 9, 10, 11, 12])),
            lambda: (lambda n: {
                "question": f"If the key is at index 4 in an array of size {n}, how many comparisons are needed?",
                "answer": "5"
            })(random_choice([9, 10, 11, 12, 13])),
            lambda: (lambda n: {
                "question": f"If the key is at index 5 in an array of size {n}, how many comparisons are needed?",
                "answer": "6"
            })(random_choice([10, 11, 12, 13, 14])),
            lambda: (lambda n: {
                "question": f"If the key is at index 6 in an array of size {n}, how many comparisons are needed?",
                "answer": "7"
            })(random_choice([11, 12, 13, 14, 15])),
            lambda: (lambda n: {
                "question": f"If the key is at index 7 in an array of size {n}, how many comparisons are needed?",
                "answer": "8"
            })(random_choice([12, 13, 14, 15, 16])),
            lambda: (lambda n: {
                "question": f"If the key is at index 8 in an array of size {n}, how many comparisons are needed?",
                "answer": "9"
            })(random_choice([13, 14, 15, 16, 17])),
            lambda: (lambda n: {
                "question": f"If the key is at index 9 in an array of size {n}, how many comparisons are needed?",
                "answer": "10"
            })(random_choice([14, 15, 16, 17, 18])),
            lambda: (lambda n: {
                "question": f"If the key is at index 10 in an array of size {n}, how many comparisons are needed?",
                "answer": "11"
            })(random_choice([15, 16, 17, 18, 19])),
            lambda: (lambda n: {
                "question": f"If the key is at index 11 in an array of size {n}, how many comparisons are needed?",
                "answer": "12"
            })(random_choice([16, 17, 18, 19, 20])),
            lambda: (lambda n: {
                "question": f"If the key is at index 12 in an array of size {n}, how many comparisons are needed?",
                "answer": "13"
            })(random_choice([17, 18, 19, 20, 21])),
            lambda: (lambda n: {
                "question": f"If the key is at index 13 in an array of size {n}, how many comparisons are needed?",
                "answer": "14"
            })(random_choice([18, 19, 20, 21, 22])),
            lambda: (lambda n: {
                "question": f"If the key is at index 14 in an array of size {n}, how many comparisons are needed?",
                "answer": "15"
            })(random_choice([19, 20, 21, 22, 23])),
            lambda: (lambda n: {
                "question": f"If the key is at index 15 in an array of size {n}, how many comparisons are needed?",
                "answer": "16"
            })(random_choice([20, 21, 22, 23, 24])),
            lambda: (lambda n: {
                "question": f"If the key is at index 16 in an array of size {n}, how many comparisons are needed?",
                "answer": "17"
            })(random_choice([21, 22, 23, 24, 25])),
            lambda: (lambda n: {
                "question": f"If the key is at index 17 in an array of size {n}, how many comparisons are needed?",
                "answer": "18"
            })(random_choice([22, 23, 24, 25, 26])),
            lambda: (lambda n: {
                "question": f"If the key is at index 18 in an array of size {n}, how many comparisons are needed?",
                "answer": "19"
            })(random_choice([23, 24, 25, 26, 27])),
            lambda: (lambda n: {
                "question": f"If the key is at index 19 in an array of size {n}, how many comparisons are needed?",
                "answer": "20"
            })(random_choice([24, 25, 26, 27, 28]))
        ]
    },

    "level3": {
        "TFQ": [
            lambda: {
                "question": "True or False: Linear Search checks each element sequentially until the key is found or the end is reached.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can only be used on sorted arrays.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: The best-case time complexity of Linear Search is O(1).",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search always requires examining every element in the array.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be implemented using both iterative and recursive approaches.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is more efficient than Binary Search for large sorted arrays.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to find all occurrences of a key in an array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is also known as sequential search.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be stopped as soon as the key is found.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is not suitable for linked lists.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to search in a string.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search modifies the original array.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search is a brute-force algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to search for a substring in a string.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is always faster than Hash Table lookup.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be used on both arrays and linked lists.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is a recursive algorithm by default.",
                "answer": "False"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to find the minimum value in an array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is not affected by duplicate elements in the array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to count the number of times a key appears.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is a stable search algorithm.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be used to search in a two-dimensional array.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is not suitable for real-time applications with large datasets.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search can be parallelized to improve performance.",
                "answer": "True"
            },
            lambda: {
                "question": "True or False: Linear Search is the most efficient search algorithm for small unsorted arrays.",
                "answer": "True"
            }
        ],
        "MCQ": [
            lambda: {
                "question": "Which of the following best describes Linear Search?",
                "options": [
                    "Checks each element one by one",
                    "Divides the array into halves",
                    "Uses a hash table",
                    "Sorts the array before searching"
                ],
                "answer": "Checks each element one by one"
            },
            lambda: {
                "question": "What is the worst-case time complexity of Linear Search?",
                "options": ["O(n)", "O(1)", "O(log n)", "O(n^2)"],
                "answer": "O(n)"
            },
            lambda: {
                "question": "Which data structure is NOT suitable for Linear Search?",
                "options": ["Hash Table", "Array", "Linked List", "String"],
                "answer": "Hash Table"
            },
            lambda: {
                "question": "In which scenario does Linear Search perform best?",
                "options": [
                    "Key is at the first position",
                    "Key is at the last position",
                    "Key is not present",
                    "Array is sorted"
                ],
                "answer": "Key is at the first position"
            },
            lambda: {
                "question": "Which of the following is TRUE about Linear Search?",
                "options": [
                    "It can find multiple occurrences of a key",
                    "It only works on sorted arrays",
                    "It requires O(log n) time",
                    "It cannot be used on linked lists"
                ],
                "answer": "It can find multiple occurrences of a key"
            },
            lambda: {
                "question": "What does Linear Search return if the key is not found?",
                "options": ["-1", "0", "None", "IndexError"],
                "answer": "-1"
            },
            lambda: {
                "question": "Which of the following is NOT a characteristic of Linear Search?",
                "options": [
                    "Sequential access",
                    "Works on unsorted data",
                    "Requires sorted data",
                    "Can be used on lists"
                ],
                "answer": "Requires sorted data"
            },
            lambda: {
                "question": "Which is the best case for Linear Search?",
                "options": [
                    "Key at first index",
                    "Key at last index",
                    "Key not present",
                    "Array is empty"
                ],
                "answer": "Key at first index"
            },
            lambda: {
                "question": "Which of the following is a disadvantage of Linear Search?",
                "options": [
                    "Inefficient for large datasets",
                    "Cannot be used on unsorted arrays",
                    "Requires extra memory",
                    "Only works with numbers"
                ],
                "answer": "Inefficient for large datasets"
            },
            lambda: {
                "question": "Which of the following can Linear Search NOT do?",
                "options": [
                    "Find the first occurrence of a key",
                    "Find all occurrences of a key",
                    "Work on unsorted arrays",
                    "Skip elements randomly"
                ],
                "answer": "Skip elements randomly"
            },
            lambda: {
                "question": "Which statement is FALSE about Linear Search?",
                "options": [
                    "It can be implemented recursively",
                    "It always examines every element",
                    "It can be used on strings",
                    "It is simple to implement"
                ],
                "answer": "It always examines every element"
            },
            lambda: {
                "question": "Which of the following is the main advantage of Linear Search?",
                "options": [
                    "Simplicity",
                    "Speed on large arrays",
                    "Requires sorted data",
                    "Uses binary logic"
                ],
                "answer": "Simplicity"
            },
            lambda: {
                "question": "Which of the following is NOT a valid use case for Linear Search?",
                "options": [
                    "Searching in a small unsorted array",
                    "Searching in a large sorted array",
                    "Finding all occurrences of a value",
                    "Searching in a linked list"
                ],
                "answer": "Searching in a large sorted array"
            },
            lambda: {
                "question": "What is the average number of comparisons in Linear Search (key present)?",
                "options": ["n/2", "n", "1", "log n"],
                "answer": "n/2"
            },
            lambda: {
                "question": "Which of the following is TRUE about Linear Search?",
                "options": [
                    "It is a brute-force algorithm",
                    "It requires the array to be sorted",
                    "It is faster than Binary Search",
                    "It cannot be used on strings"
                ],
                "answer": "It is a brute-force algorithm"
            },
            lambda: {
                "question": "Which of the following is NOT required for Linear Search?",
                "options": [
                    "Sorted array",
                    "Array or list",
                    "Key to search",
                    "Loop or recursion"
                ],
                "answer": "Sorted array"
            },
            lambda: {
                "question": "Which of the following is a limitation of Linear Search?",
                "options": [
                    "Inefficient for large datasets",
                    "Cannot find duplicates",
                    "Requires sorted data",
                    "Cannot be used on strings"
                ],
                "answer": "Inefficient for large datasets"
            },
            lambda: {
                "question": "Which of the following is the correct order of steps in Linear Search?",
                "options": [
                    "Start from first element, compare, move to next, repeat",
                    "Divide array, compare middle, repeat",
                    "Sort array, then search",
                    "Hash key, then search"
                ],
                "answer": "Start from first element, compare, move to next, repeat"
            },
            lambda: {
                "question": "Which of the following is NOT a possible output of Linear Search?",
                "options": [
                    "Index of key",
                    "-1",
                    "None",
                    "All indices of key"
                ],
                "answer": "None"
            },
            lambda: {
                "question": "Which of the following is TRUE about Linear Search?",
                "options": [
                    "It can be used to search in a two-dimensional array",
                    "It requires extra memory",
                    "It is always faster than Binary Search",
                    "It cannot be used on linked lists"
                ],
                "answer": "It can be used to search in a two-dimensional array"
            },
            lambda: {
                "question": "Which of the following is NOT a feature of Linear Search?",
                "options": [
                    "Works on unsorted data",
                    "Can find all occurrences",
                    "Requires sorted data",
                    "Simple implementation"
                ],
                "answer": "Requires sorted data"
            },
            lambda: {
                "question": "Which of the following is the best use case for Linear Search?",
                "options": [
                    "Small unsorted arrays",
                    "Large sorted arrays",
                    "Searching in a database",
                    "Searching in a hash table"
                ],
                "answer": "Small unsorted arrays"
            },
            lambda: {
                "question": "Which of the following is NOT true about Linear Search?",
                "options": [
                    "It is efficient for small datasets",
                    "It can be used on linked lists",
                    "It requires the array to be sorted",
                    "It is easy to implement"
                ],
                "answer": "It requires the array to be sorted"
            },
            lambda: {
                "question": "Which of the following is a correct statement about Linear Search?",
                "options": [
                    "It can be used to search for a character in a string",
                    "It requires the array to be sorted",
                    "It is always faster than Binary Search",
                    "It cannot be used on lists"
                ],
                "answer": "It can be used to search for a character in a string"
            },
            lambda: {
                "question": "Which of the following is NOT a valid reason to use Linear Search?",
                "options": [
                    "Array is small and unsorted",
                    "Need to find all occurrences",
                    "Array is very large and sorted",
                    "Implementation simplicity"
                ],
                "answer": "Array is very large and sorted"
            }
        ],
        "MTQ": [
            lambda: {
                "question": "Match the scenario to the Linear Search outcome:",
                "pairs": {
                    "Key at first index": "Best case",
                    "Key at last index": "Worst case",
                    "Key not present": "All elements checked"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search step to its description:",
                "pairs": {
                    "Compare element": "Check if it matches key",
                    "Move to next": "If not matched",
                    "Return index": "If matched"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the data structure to Linear Search applicability:",
                "pairs": {
                    "Array": "Applicable",
                    "Linked List": "Applicable",
                    "Hash Table": "Not applicable"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the time complexity to the scenario:",
                "pairs": {
                    "Best case": "O(1)",
                    "Worst case": "O(n)",
                    "Average case": "O(n)"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search property to its explanation:",
                "pairs": {
                    "Stable": "Order of equal elements preserved",
                    "Brute-force": "Checks all possibilities",
                    "Unsorted data": "Works fine"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search variant to its feature:",
                "pairs": {
                    "Iterative": "Uses loop",
                    "Recursive": "Calls itself",
                    "Both": "Same time complexity"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search result to the situation:",
                "pairs": {
                    "Returns index": "Key found",
                    "Returns -1": "Key not found",
                    "Returns all indices": "Multiple occurrences"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search limitation to its impact:",
                "pairs": {
                    "Inefficient for large data": "Slow performance",
                    "Checks every element": "High time complexity",
                    "No need for sorting": "Simple implementation"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search use case to the reason:",
                "pairs": {
                    "Small array": "Simple and fast",
                    "Unsorted data": "No sorting needed",
                    "Find all matches": "Can check every element"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search step to its action:",
                "pairs": {
                    "Start at index 0": "First comparison",
                    "Increment index": "Move to next element",
                    "End of array": "Key not found"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search property to its description:",
                "pairs": {
                    "Sequential": "Checks elements in order",
                    "Non-adaptive": "Does not skip elements",
                    "Simple": "Easy to implement"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search scenario to the number of comparisons:",
                "pairs": {
                    "Key at index 0": "1",
                    "Key at index n-1": "n",
                    "Key not present": "n"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search application to the data type:",
                "pairs": {
                    "String": "Character search",
                    "List": "Element search",
                    "2D array": "Row-wise search"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search feature to its benefit:",
                "pairs": {
                    "No extra memory": "Space efficient",
                    "Works on any data": "Versatile",
                    "Simple logic": "Easy to debug"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search output to the input:",
                "pairs": {
                    "Key found": "Index returned",
                    "Key not found": "-1 returned",
                    "Multiple keys": "All indices returned"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search variant to its implementation:",
                "pairs": {
                    "Iterative": "For/while loop",
                    "Recursive": "Function calls itself",
                    "Both": "Same result"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search scenario to the result:",
                "pairs": {
                    "Key at first index": "Best case",
                    "Key at last index": "Worst case",
                    "Key not present": "All elements checked"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search property to its limitation:",
                "pairs": {
                    "Checks all elements": "Slow for large arrays",
                    "No sorting needed": "Works on any data",
                    "Simple": "Not optimal for big data"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search step to its function:",
                "pairs": {
                    "Compare": "Check for match",
                    "Increment": "Move to next",
                    "Return": "Output result"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search scenario to the number of comparisons:",
                "pairs": {
                    "Key at index 2": "3",
                    "Key at index 4": "5",
                    "Key not present in 5 elements": "5"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search property to its effect:",
                "pairs": {
                    "Stable": "Order preserved",
                    "Brute-force": "Checks all",
                    "Versatile": "Works on many types"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search scenario to the output:",
                "pairs": {
                    "Key found": "Index",
                    "Key not found": "-1",
                    "Multiple matches": "List of indices"
                },
                "answer": "Correct mapping"
            },
            lambda: {
                "question": "Match the Linear Search feature to its advantage:",
                "pairs": {
                    "No sorting": "Works on any data",
                    "Simple": "Easy to code",
                    "No extra space": "Memory efficient"
                },
                "answer": "Correct mapping"
            }
        ],
        "ECQ": [
            lambda: {
                "question": "Fill in the blank: for i in range(len(arr)): if arr[i] == key: return ____",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: if arr[i] != key: continue else: return ____",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: def linear_search(arr, key): for i in range(len(arr)): if arr[i] == key: return ____ return -1",
                "answer": "i"
            },
            lambda: {
                "question": "Fill in the blank: To check if key is not found, return ____",
                "answer": "-1"
            },
            lambda: {
                "question": "Fill in the blank: To search for all occurrences, use ____ to store indices.",
                "answer": "a list"
            },
            lambda: {
                "question": "Fill in the blank: To search in a string, use for i in range(len(s)): if s[i] == ____: return i",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: The best-case time complexity of Linear Search is ____.",
                "answer": "O(1)"
            },
            lambda: {
                "question": "Fill in the blank: The worst-case time complexity of Linear Search is ____.",
                "answer": "O(n)"
            },
            lambda: {
                "question": "Fill in the blank: Linear Search is also called ____ search.",
                "answer": "sequential"
            },
            lambda: {
                "question": "Fill in the blank: To implement recursive Linear Search, call the function with ____.",
                "answer": "next index"
            },
            lambda: {
                "question": "Fill in the blank: To count all occurrences, increment ____ each time key is found.",
                "answer": "a counter"
            },
            lambda: {
                "question": "Fill in the blank: To search in a 2D array, use ____ loops.",
                "answer": "nested"
            },
            lambda: {
                "question": "Fill in the blank: To return all indices, append i to ____ when arr[i] == key.",
                "answer": "a list"
            },
            lambda: {
                "question": "Fill in the blank: Linear Search works on ____ arrays.",
                "answer": "unsorted"
            },
            lambda: {
                "question": "Fill in the blank: To stop search after first match, use ____ statement.",
                "answer": "return"
            },
            lambda: {
                "question": "Fill in the blank: To search in a linked list, use a ____ to traverse nodes.",
                "answer": "pointer"
            },
            lambda: {
                "question": "Fill in the blank: Linear Search is a ____ algorithm.",
                "answer": "brute-force"
            },
            lambda: {
                "question": "Fill in the blank: To search for a character in a string, compare ____ with key.",
                "answer": "s[i]"
            },
            lambda: {
                "question": "Fill in the blank: To search in reverse, start from ____ index.",
                "answer": "last"
            },
            lambda: {
                "question": "Fill in the blank: To check if array is empty, use if len(arr) == ____.",
                "answer": "0"
            },
            lambda: {
                "question": "Fill in the blank: To search for minimum value, compare arr[i] with ____.",
                "answer": "current minimum"
            },
            lambda: {
                "question": "Fill in the blank: To search for maximum value, compare arr[i] with ____.",
                "answer": "current maximum"
            },
            lambda: {
                "question": "Fill in the blank: To search for a substring, use ____ in s.",
                "answer": "key"
            },
            lambda: {
                "question": "Fill in the blank: To search in a list of dictionaries, compare ____ with key.",
                "answer": "dictionary value"
            },
            lambda: {
                "question": "Fill in the blank: To search in a tuple, use for i in range(len(t)): if t[i] == ____.",
                "answer": "key"
            }
        ],
        "NQ": [
            lambda: (lambda n: {
                "question": f"If the array has {n} elements, how many comparisons does Linear Search take in the worst case?",
                "answer": str(n)
            })(random_choice([5, 7, 10, 12, 15])),
            lambda: (lambda n: {
                "question": f"If the key is at index 0 in an array of size {n}, how many comparisons are needed?",
                "answer": "1"
            })(random_choice([6, 8, 9, 11, 13])),
            lambda: (lambda n, idx: {
                "question": f"In an array of size {n}, if the key is at index {idx}, how many comparisons are needed in Linear Search?",
                "answer": str(idx + 1)
            })(random_choice([8, 10, 12, 14]), random_choice([2, 3, 4, 5])),
            lambda: (lambda n: {
                "question": f"If the key is not present in an array of size {n}, how many comparisons are made?",
                "answer": str(n)
            })(random_choice([7, 9, 11, 13, 15])),
            lambda: (lambda n: {
                "question": f"If the key is at the last index in an array of size {n}, how many comparisons are needed?",
                "answer": str(n)
            })(random_choice([5, 6, 8, 10, 12])),
            lambda: (lambda n: {
                "question": f"If the key is at index 2 in an array of size {n}, how many comparisons are needed?",
                "answer": "3"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If the key is at index 4 in an array of size {n}, how many comparisons are needed?",
                "answer": "5"
            })(random_choice([7, 8, 9, 10, 11])),
            lambda: (lambda n: {
                "question": f"If the key is not present in an array of size {n}, what is the return value?",
                "answer": "-1"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If you want to find all occurrences of a key in an array of size {n}, what is the maximum number of comparisons?",
                "answer": str(n)
            })(random_choice([8, 10, 12, 14, 15])),
            lambda: (lambda n: {
                "question": f"If the key is at index 1 in an array of size {n}, how many comparisons are needed?",
                "answer": "2"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If the array has {n} elements and the key is at index {n-2}, how many comparisons are needed?",
                "answer": str(n-1)
            })(random_choice([7, 8, 9, 10, 11])),
            lambda: (lambda n: {
                "question": f"If the key is at index 3 in an array of size {n}, how many comparisons are needed?",
                "answer": "4"
            })(random_choice([7, 8, 9, 10, 11])),
            lambda: (lambda n: {
                "question": f"If the key is at index {n//2} in an array of size {n}, how many comparisons are needed?",
                "answer": str(n//2 + 1)
            })(random_choice([8, 10, 12, 14, 16])),
            lambda: (lambda n: {
                "question": f"If the key is at index {n-1} in an array of size {n}, how many comparisons are needed?",
                "answer": str(n)
            })(random_choice([6, 8, 10, 12, 14])),
            lambda: (lambda n: {
                "question": f"If the key is at index 0 in an array of size {n}, what is the best-case number of comparisons?",
                "answer": "1"
            })(random_choice([5, 7, 9, 11, 13])),
            lambda: (lambda n: {
                "question": f"If the key is not present in an array of size {n}, what is the worst-case number of comparisons?",
                "answer": str(n)
            })(random_choice([6, 8, 10, 12, 14])),
            lambda: (lambda n: {
                "question": f"If the key is at index 2 in an array of size {n}, what is the number of comparisons?",
                "answer": "3"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the key is at index 1 in an array of size {n}, what is the number of comparisons?",
                "answer": "2"
            })(random_choice([5, 6, 7, 8, 9])),
            lambda: (lambda n: {
                "question": f"If the key is at index 3 in an array of size {n}, what is the number of comparisons?",
                "answer": "4"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If the key is at index 4 in an array of size {n}, what is the number of comparisons?",
                "answer": "5"
            })(random_choice([7, 8, 9, 10, 11])),
            lambda: (lambda n: {
                "question": f"If the key is not present in an array of size {n}, what is the return value?",
                "answer": "-1"
            })(random_choice([6, 7, 8, 9, 10])),
            lambda: (lambda n: {
                "question": f"If the key is at index {n//2} in an array of size {n}, what is the number of comparisons?",
                "answer": str(n//2 + 1)
            })(random_choice([7, 9, 11, 13, 15])),
            lambda: (lambda n: {
                "question": f"If the key is at index 0 in an array of size {n}, what is the number of comparisons?",
                "answer": "1"
            })(random_choice([8, 10, 12, 14, 16])),
            lambda: (lambda n: {
                "question": f"If the key is at index {n-1} in an array of size {n}, what is the number of comparisons?",
                "answer": str(n)
            })(random_choice([7, 9, 11, 13, 15])),
            lambda: (lambda n: {
                "question": f"If the key is at index 2 in an array of size {n}, what is the number of comparisons?",
                "answer": "3"
            })(random_choice([8, 10, 12, 14, 16])),
            lambda: (lambda n: {
                "question": f"If the key is at index 1 in an array of size {n}, what is the number of comparisons?",
                "answer": "2"
            })(random_choice([7, 9, 11, 13, 15]))
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
