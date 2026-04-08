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

    def trace_member(self, member_id):
        return [
            block.data for block in self.chain
            if isinstance(block.data, dict) and block.data.get("member") == member_id
        ]


# Rewards Web App Logic (Backend Simulation)
class RewardsApp:
    def __init__(self):
        self.blockchain = Blockchain()
        self.rewards = {}

    # Assign reward points
    def add_reward(self, member, points):
        self.rewards[member] = self.rewards.get(member, 0) + points

        self.blockchain.add_block({
            "member": member,
            "points_added": points,
            "total": self.rewards[member]
        })

    # Get total rewards
    def get_total(self, member):
        return self.rewards.get(member, 0)

    # Track & trace rewards
    def trace_rewards(self, member):
        return self.blockchain.trace_member(member)


# Driver Code
app = RewardsApp()

app.add_reward("M1", 10)
app.add_reward("M2", 20)
app.add_reward("M1", 15)

print("Total M1:", app.get_total("M1"))
print("Total M2:", app.get_total("M2"))

print("\nM1 Trace:", app.trace_rewards("M1"))
print("M2 Trace:", app.trace_rewards("M2"))