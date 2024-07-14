class TrieNode:
    def __init__(self):
        """
        Initialize this node in the Trie.
        """
        self.children = {}  # Dictionary of TrieNode children
        self.is_end_of_word = False  # Boolean to check if it's the end of a word
    
    def insert(self, char):
        """
        Add a child node for a given character.
        
        Args:
            char (str): Character to add as a child node
        """
        if char not in self.children:
            self.children[char] = TrieNode()
    
    def suffixes(self, suffix=''):
        """
        Recursive function that collects all suffixes for complete words below this node.
        
        Args:
            suffix (str): Current suffix being built
        
        Returns:
            list: List of all suffixes starting from this node
        """
        suffixes = []
        if self.is_end_of_word:
            suffixes.append(suffix)
        
        for char, child_node in self.children.items():
            suffixes.extend(child_node.suffixes(suffix + char))
        
        return suffixes

class Trie:
    def __init__(self):
        """
        Initialize the Trie with an empty root node.
        """
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Insert a word into the Trie.
        
        Args:
            word (str): Word to be inserted into the Trie
        """
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.is_end_of_word = True
    
    def find(self, prefix):
        """
        Find the node that represents the end of the given prefix.
        
        Args:
            prefix (str): Prefix to find in the Trie
        
        Returns:
            TrieNode: Node where the prefix ends or None if not found
        """
        if prefix is None:
            return None
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node
    
    def exists(self, word):
        """
        Check if a word exists in the Trie.
        
        Args:
            word (str): Word to check in the Trie
        
        Returns:
            bool: True if the word exists, False otherwise
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_end_of_word

    def prefix_words(self, prefix):
        """
        Find all words in the Trie that start with the given prefix.
        
        Args:
            prefix (str): Prefix to search for
        
        Returns:
            list: List of words that start with the given prefix
        """
        node = self.find(prefix)
        if not node:
            return []
        return [prefix + suffix for suffix in node.suffixes()]

# Test code
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
print(wordList)
word_trie = Trie()

print("\t Test Insert and exists functions\n")
# Add words
for word in wordList:
    word_trie.insert(word)

# Test words
test_words = [
    "ant", "anthology", "antagonist", "antonym", "anth",
    "fun", "function", "factory", "fu",
    "trie", "trigger", "trigonometry", "tripod", "tri"
]

for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))


print("\n\t Test find/prefix/suffix function\n")
test_prefixes = ['a', 'an', 'ant', 'anto', 'anth', '', None]
for prefix in test_prefixes:
    prefixNode = word_trie.find(prefix)
    if prefixNode:
        print('"{}" is a prefix \n'.format(prefix))
        print('TrieNode: \n{}'.format(prefixNode.children.items()))
        print('Words with prefix "{}" : {}'.format(prefix, word_trie.prefix_words(prefix)))
        print('Auto-complete:')
        print('\n'.join(prefixNode.suffixes()))
        print('\n')
    else:
        print('"{}" is not a prefix.\n {}\n'.format(prefix, prefixNode))
