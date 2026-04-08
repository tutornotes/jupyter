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

    def get_votes(self):
        return [block.data for block in self.chain if isinstance(block.data, dict)]


# Voting Application
class VotingApp:
    def __init__(self):
        self.blockchain = Blockchain()
        self.voters = {}

    # Cast vote
    def vote(self, voter_id, candidate):
        if voter_id in self.voters:
            return "Already Voted"

        self.voters[voter_id] = candidate

        self.blockchain.add_block({
            "voter": voter_id,
            "candidate": candidate
        })

        return "Vote Cast Successfully"

    # Count votes
    def count_votes(self):
        result = {}
        for vote in self.voters.values():
            result[vote] = result.get(vote, 0) + 1
        return result


# Driver Code
app = VotingApp()

print(app.vote("V1", "Alice"))
print(app.vote("V2", "Bob"))
print(app.vote("V3", "Alice"))
print(app.vote("V1", "Bob"))  # duplicate vote

print("\nVote Count:", app.count_votes())
print("\nBlockchain Data:", app.blockchain.get_votes())