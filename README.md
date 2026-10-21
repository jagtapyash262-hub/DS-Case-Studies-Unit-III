
# Data-Structure-Unit-3-Case-Study-

A Python case study demonstrating the implementation of Stack and Queue operations using Linked Lists.

# Stack and Queue Using Linked Lists

A Python case study for implementing stack and queue data structures using a singly linked list.

A stack follows the LIFO (Last In, First Out) principle, while a queue follows the FIFO (First In, First Out) principle.

## Features

### Stack Operations

- `push` adds an element to the top of the stack.
- `pop` removes the top element from the stack.
- `peek` displays the top element without removing it.
- `display` shows all stack elements from top to bottom.
- Follows LIFO (Last In, First Out).

### Queue Operations

- `enqueue` adds an element to the rear of the queue.
- `dequeue` removes an element from the front of the queue.
- `peek` displays the front element without removing it.
- `display` shows all queue elements from front to rear.
- Follows FIFO (First In, First Out).

## Data Structure Used

**Singly Linked List**

A linked list consists of nodes. Each node stores data and a reference to the next node.

In this case study:
- The stack uses a `top` pointer.
- The queue uses `front` and `rear` pointers.
- Nodes are created dynamically as elements are added.
- Elements can be removed without shifting other elements.

## Requirements

- Python 3.7 or newer
- No external packages are required.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python CaseStudy3.py
   ```

If your system uses `python3`, run:

   ```bash
   python3 CaseStudy3.py
   ```

## Sample Output

See `sample_output.txt` for the complete program output.

### Stack Example

```text
Stack elements (top to bottom): 30 20 10
Top element: 30
30 popped from stack
Stack elements (top to bottom): 20 10
```

### Queue Example

```text
Queue elements (front to rear): 10 20 30
Front element: 10
10 removed from queue
Queue elements (front to rear): 20 30
```

## Time Complexity

| Operation | Time Complexity |
|---|---|
| Stack Push | O(1) |
| Stack Pop | O(1) |
| Stack Peek | O(1) |
| Stack Display | O(n) |
| Queue Enqueue | O(1) |
| Queue Dequeue | O(1) |
| Queue Peek | O(1) |
| Queue Display | O(n) |

Here, `n` represents the number of elements in the data structure.

## Advantages

- Dynamic memory allocation.
- Efficient insertion and deletion at the required ends.
- No fixed-size limit imposed by an array.
- Stack and queue operations are easy to implement using linked lists.

## Limitations

- Each node requires additional memory for a pointer.
- Elements cannot be accessed directly by index.
- Traversing and displaying all elements takes O(n) time.

## Applications

### Stack

- Undo and redo operations.
- Function call management.
- Expression evaluation.
- Browser history.

### Queue

- Printer job scheduling.
- Customer service systems.
- Task scheduling.
- Request processing.

## Conclusion

This case study demonstrates how stack and queue operations can be implemented using a singly linked list in Python.

The stack follows LIFO, whereas the queue follows FIFO. Both data structures support efficient insertion and deletion operations when implemented with suitable pointers.

## Files Included

- `CaseStudy3.py` — Python implementation of stack and queue operations.
- `sample_output.txt` — Sample program output.
- `README.md` — Case study documentation.
