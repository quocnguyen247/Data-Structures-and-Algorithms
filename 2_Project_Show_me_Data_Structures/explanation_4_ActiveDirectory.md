## Explanation_4: Active Directory

### Requirement:
The task involves implementing a function for efficient lookup to determine whether a user is present in a group or its subgroups.

### Summary:
- The code includes a Group class that handles group-related operations like adding groups, adding users, and retrieving group information.
- The `is_user_in_group` function is designed to check if a user exists in a specific group or any of its subgroups.
    - It first checks if the user is directly in the given group. If found, it returns True.
    - If the user is not in the group, it recursively looks through all subgroups and returns True if the user is found in any subgroup. Otherwise, it returns False.

### Time and Space Complexity:
#### Time Complexity:
- O(l): Checking if a user exists in the users list of a group where l is the length of the users list.
- O(g): Iterating through the list of groups at each level.
- O(n*(l+g)): Considering a tree with n nodes (groups), the time complexity for each node involves searching through user and group lists.
- The total time complexity can be expressed as O(n * (l + g)) where n is the total number of groups.

#### Space Complexity:
- Input Space:
    - users: O(l)
    - group_list: O(g)
    - Input space for one iteration: O(g + l)
    - Input space for depth iterations: O(depth * (g + l))
- Auxiliary Space:
    - The call stack requires O(depth) space due to recursive function calls that traverse the depth of the directory structure.
- Total Space Complexity:
    - Total Space = Input Space + Auxiliary Space
    - Total Space Complexity = O(depth * (g + l)) + O(depth)
    - Simplified to O(depth * (g + l))

### Conclusion:
The implementation efficiently handles group membership checks for users across groups and subgroups, offering a balance between time complexity for lookup operations and space complexity required for maintaining group and user information in memory.