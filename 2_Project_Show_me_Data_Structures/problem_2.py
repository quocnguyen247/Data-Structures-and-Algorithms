import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.exists(path):
        return []

    file_paths = []
    stack = [path]

    while stack:
        current_path = stack.pop()
        if os.path.isdir(current_path):
            for item in os.listdir(current_path):
                stack.append(os.path.join(current_path, item))
        elif os.path.isfile(current_path) and current_path.endswith(suffix):
            file_paths.append(current_path)

    return file_paths

# Test Case 1: Valid directory with files
print('***** Test Case 1 *****')
result = find_files('.c', 'testdir')
print(result)

# Test Case 2: Empty directory
print('***** Test Case 2 *****')
result = find_files('.c', 'testdir/subdir2')
print(result)

# Test Case 3: Non-existent directory
print('***** Test Case 3 *****')
result = find_files('.c', 'non-existent-dir')
print(result)