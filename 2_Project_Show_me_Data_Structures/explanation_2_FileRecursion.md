## Explanation_2: File Recursion

### Requirement:
The objective is to implement code that finds all files under a directory (and its subdirectories) with a specific file extension, such as ".c".

### Summary:
The provided `find_files` function takes a file extension suffix and a directory path as input. It recursively searches for files with the given extension in the specified directory and its subdirectories. The function collects all matching file paths in a list and returns it.

### Time and Space Complexity:

#### Time Complexity:
The time complexity of the `find_files` function is O(n), where n is the total number of files and folders returned by all calls to `os.listdir()`. The function iterates over the list of files to find folders, then again to extract files with the specified extension. Overall, it has a linear time complexity of O(n) due to the number of items returned by `os.listdir()`.

#### Space Complexity:
- Input Space:
    - suffix (str) - O(1)
    - path (str) - O(1)
    - Input space for depth iterations => O(depth * Average number of directories in each level)
- Auxiliary Space:
    - Recursion uses a call stack for function calls.
    - The space required in the call stack is O(depth) as the recursive function exhausts when it reaches the depth of directory traversal.
- Total Space Complexity:
    - Total Space = Input Space + Auxiliary Space
    - Total Space Complexity = O(depth * Average number of directories in each level + depth)
    - Simplified to O(depth * Average number of directories in each level)
