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

    def validate(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i-1].hash:
                return False
        return True


# Fitness Rewards App
class FitnessRewards:
    def __init__(self):
        self.blockchain = Blockchain()
        self.rewards = {}

    # Add reward points
    def add_reward(self, member, points):
        self.rewards[member] = self.rewards.get(member, 0) + points

        self.blockchain.add_block({
            "member": member,
            "points_added": points,
            "total_points": self.rewards[member]
        })


# Driver Code
app = FitnessRewards()

app.add_reward("M1", 10)
app.add_reward("M2", 20)
app.add_reward("M1", 15)

# Display blockchain
for block in app.blockchain.chain:
    print(block.index, block.data, block.hash)

# Display rewards
print("\nRewards:", app.rewards)

# Validate blockchain
print("\nBlockchain Valid:", app.blockchain.validate())