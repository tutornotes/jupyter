import hashlib
import time

# Block Class
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()


# Blockchain Class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    def display(self):
        for block in self.chain:
            print("Index:", block.index)
            print("Data:", block.data)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)
            print("-" * 40)


# Global Finance Application
class FinanceApp:
    def __init__(self):
        self.blockchain = Blockchain()

    # Transaction (send money)
    def transact(self, sender, receiver, amount):
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        }
        self.blockchain.add_block(transaction)


# Driver Code
app = FinanceApp()

app.transact("Alice", "Bob", 1000)
app.transact("Bob", "Charlie", 500)
app.transact("Charlie", "David", 200)

# Display blockchain data
app.blockchain.display()