## Explanation_1: LRU Cache

### Requirement:
The LRU (Least Recently Used) Cache should have fast lookup operations, both get() and set() functions, with a time complexity of O(1).

### Summary:
To achieve this, the implementation uses two main data structures:
1. Hashtable: Provides constant lookup time.
2. Doubly Linked List: Enables constant time addition and removal of nodes if the node address is known.

### Time and Space Complexity:

#### Time Complexity:
By combining a Hashtable for fast lookups with a Doubly Linked List for efficient node manipulation, all operations become O(1) in terms of time complexity.

#### Space Complexity:
- Input Space:
    - Dictionary space: O(n)
    - Doubly Linked List space: O(n)
    - Total Input space: O(n + n) => O(n)
- Auxiliary Space:
    - The auxiliary space is the temporary space allocated by the algorithm to solve the problem, excluding the input size.
    - In this case, the auxiliary space is constant, let's say 4 bytes, denoted as O(1).
- Total Space Complexity:
    - Total Space = Input Size + Auxiliary Space = O(n + 1) => O(n)