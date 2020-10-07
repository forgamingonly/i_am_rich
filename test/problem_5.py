import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = str(self.data).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return ('Timestamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}'.format(self.timestamp, self.data, self.previous_hash, self.hash))

class Blockchain:

    def __init__(self):
        self.current_block = None

    def add_block(self, value):
        timestamp = time.gmtime()
        data = value
        previous_hash = self.current_block.hash if self.current_block else 0
        self.current_block = Block(timestamp, data, previous_hash)

print("-------------------------------")
# testcase - length=3
blockchain = Blockchain()

blockchain.add_block(1)
print(blockchain.current_block)
blockchain.add_block(2)
print(blockchain.current_block)
blockchain.add_block(3)
print(blockchain.current_block)

print("-------------------------------")

# Edge testcase - length 0 blockchain
zero_chain = Blockchain()
print(zero_chain.current_block)

print("-------------------------------")
# testcase - length=5
blockchain = Blockchain()

blockchain.add_block(11)
print(blockchain.current_block)
blockchain.add_block(22)
print(blockchain.current_block)
blockchain.add_block(33)
print(blockchain.current_block)
blockchain.add_block(44)
print(blockchain.current_block)
blockchain.add_block(55)
print(blockchain.current_block)
print("-------------------------------")