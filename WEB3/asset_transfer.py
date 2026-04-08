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


# Asset Transfer Application
class AssetApp:
    def __init__(self):
        self.blockchain = Blockchain()
        self.assets = {}

    # Create asset
    def create_asset(self, asset_id, owner, value):
        self.assets[asset_id] = {"owner": owner, "value": value}
        self.blockchain.add_block({
            "action": "create",
            "asset_id": asset_id,
            "owner": owner,
            "value": value
        })

    # Transfer ownership
    def transfer_asset(self, asset_id, new_owner):
        if asset_id in self.assets:
            self.assets[asset_id]["owner"] = new_owner
            self.blockchain.add_block({
                "action": "transfer",
                "asset_id": asset_id,
                "new_owner": new_owner
            })


# Driver Code
app = AssetApp()

# Create assets
app.create_asset("A1", "Alice", 500)
app.create_asset("A2", "Bob", 300)

# Transfer ownership
app.transfer_asset("A1", "Charlie")

# Display Blockchain
for block in app.blockchain.chain:
    print(block.index, block.data, block.hash)

# Display current ownership
print("\nCurrent Assets:", app.assets)