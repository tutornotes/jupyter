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

    def get_asset_history(self, asset_id):
        return [
            block.data for block in self.chain
            if isinstance(block.data, dict) and block.data.get("asset_id") == asset_id
        ]


# IoT Asset Tracking Application
class IoTAssetApp:
    def __init__(self):
        self.blockchain = Blockchain()
        self.assets = {}

    # Register asset (simulating IoT device input)
    def register_asset(self, asset_id, location, status):
        self.assets[asset_id] = {"location": location, "status": status}

        self.blockchain.add_block({
            "action": "register",
            "asset_id": asset_id,
            "location": location,
            "status": status
        })

    # Update asset (IoT updates)
    def update_asset(self, asset_id, location, status):
        if asset_id in self.assets:
            self.assets[asset_id] = {"location": location, "status": status}

            self.blockchain.add_block({
                "action": "update",
                "asset_id": asset_id,
                "location": location,
                "status": status
            })

    # Get current asset data
    def get_asset(self, asset_id):
        return self.assets.get(asset_id, None)

    # Track full history
    def track_asset(self, asset_id):
        return self.blockchain.get_asset_history(asset_id)


# Driver Code
app = IoTAssetApp()

app.register_asset("A1", "Warehouse", "Idle")
app.update_asset("A1", "In Transit", "Moving")
app.update_asset("A1", "Store", "Delivered")

app.register_asset("A2", "Factory", "Idle")
app.update_asset("A2", "Warehouse", "Moving")

print("Current A1:", app.get_asset("A1"))
print("A1 History:", app.track_asset("A1"))

print("\nCurrent A2:", app.get_asset("A2"))
print("A2 History:", app.track_asset("A2"))