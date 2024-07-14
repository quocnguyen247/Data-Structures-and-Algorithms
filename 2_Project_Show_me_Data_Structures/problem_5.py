import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + self.data + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.add_block("Genesis Block", "0")

    def add_block(self, data, previous_hash):
        timestamp = datetime.now()
        block = Block(timestamp, data, previous_hash)
        self.chain.append(block)

    def print_chain(self):
        for block in self.chain:
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Current Hash:", block.hash)
            print()

# Test Case 1: Adding blocks to the blockchain
print('***** Test Case 1 *****')
blockchain = Blockchain()
blockchain.add_block("Transaction 1", blockchain.chain[-1].hash)
blockchain.add_block("Transaction 2", blockchain.chain[-1].hash)
blockchain.add_block("Transaction 3", blockchain.chain[-1].hash)
blockchain.print_chain()

# Test Case 2: Empty blockchain
print('***** Test Case 2 *****')
blockchain = Blockchain()
blockchain.print_chain()

# Test Case 3: Large blockchain
print('***** Test Case 3 *****')
blockchain = Blockchain()
for i in range(100):
    blockchain.add_block(f"Transaction {i+1}", blockchain.chain[-1].hash)
blockchain.print_chain()