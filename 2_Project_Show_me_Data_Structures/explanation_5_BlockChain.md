## Explanation_5: Blockchain Implementation
### Requirement:
A Blockchain is a digital ledger that is implemented as a sequence of blocks, which are linked and secured using cryptography. Each block in a blockchain contains a cryptographic hash of the previous block, a timestamp that indicates when the block was created, and transaction data. For our blockchain, we will be utilizing the SHA-256 hashing algorithm, the timestamp of when the block was created, and string data to represent the transactions.

The goal is to use the concepts of linked lists and cryptographic hashing to create a basic blockchain implementation.

### Implementation Overview:
The code provided contains two Python classes: Block and Blockchain.

### Class Block:
The Block class represents the structure of each individual block in the blockchain. It is analogous to a node in a linked list. The class contains the following attributes:

- timestamp: The time at which the block was created.
- data: The information stored inside the block, typically representing transactions.
- previous_hash: The hash of the previous block in the chain, which establishes the link.
- hash: The block's own hash, calculated by the calc_hash method.
- The calc_hash method creates a SHA-256 hash by combining the block's timestamp, data, and previous hash, converting the combined string to UTF-8 bytes, and then applying the hashing algorithm.

### Class Blockchain:
The Blockchain class is responsible for managing the chain of blocks. It contains a single attribute:

chain: A list that contains all the blocks in the blockchain.
The class includes the following methods:

- __init__: The constructor method that initializes the blockchain with a genesis block.
- add_block: A method to add a new block to the chain. It takes the data and previous hash as arguments.
- print_chain: A method to print the details of each block in the blockchain.
- The Blockchain class starts with a genesis block, which is the first block in the blockchain. The genesis block's previous_hash is set to "0".

### Testing:
Three test cases are provided to demonstrate the functionality of the blockchain implementation:

- Test Case 1: Adding multiple blocks to the blockchain and printing the chain.
- Test Case 2: Printing an empty blockchain that contains only the genesis block.
- Test Case 3: Adding a large number of blocks (100) to the blockchain and printing the entire chain.
### Time and Space Complexity:
#### Time Complexity:
- The add_block method has a time complexity of O(1), as it appends a new block to the end of the list representing the blockchain.
- The print_chain method has a time complexity of O(n), where n is the number of blocks in the blockchain.
#### Space Complexity:
- The space complexity is O(n), where n is the number of blocks in the blockchain. Each block uses constant space, and the space required for the entire blockchain grows linearly with the number of blocks.

### Conclusion:
The code provided creates a simple blockchain where blocks are linked using hashes. It demonstrates the core principles of blockchain technology, including immutability, transparency, and the use of cryptographic hashes to secure the chain.