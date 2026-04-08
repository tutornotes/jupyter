import hashlib
import time

# (a) Block class with attributes initialization
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index                          # block position
        self.timestamp = time.time()                # creation time
        self.data = data                            # transaction data
        self.previous_hash = previous_hash          # link to previous block
        self.hash = self.calculate_hash()           # current block hash

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()


# (b) Blockchain initialization
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    # (c) Transaction function
    def transact(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    # (d) Validation function
    def valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.previous_hash != previous.hash:
                return False

            if current.hash != current.calculate_hash():
                return False

        return True


# Driver Code
bc = Blockchain()

bc.transact({"user": "A", "amount": 100})
bc.transact({"user": "B", "amount": 50})

for block in bc.chain:
    print(block.index, block.data, block.hash)

print("Blockchain Valid:", bc.valid())