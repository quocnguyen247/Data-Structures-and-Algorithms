class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True

    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True

    return False

# Test cases
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test Case 1
print("Test Case 1:")
print(is_user_in_group("sub_child_user", parent))  # True
print(is_user_in_group("sub_child_user", child))  # True
print(is_user_in_group("sub_child_user", sub_child))  # True

# Test Case 2 (Edge case: User not in any group)
print("\nTest Case 2:")
print(is_user_in_group("unknown_user", parent))  # False

# Test Case 3 (Edge case: Empty group)
print("\nTest Case 3:")
empty_group = Group("empty")
print(is_user_in_group("sub_child_user", empty_group))  # False