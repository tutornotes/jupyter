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

    def query_history(self, car_id):
        return [
            block.data for block in self.chain
            if isinstance(block.data, dict) and block.data.get("car_id") == car_id
        ]


# Car Auction Application
class CarAuction:
    def __init__(self):
        self.blockchain = Blockchain()
        self.cars = {}

    # Add car to auction
    def add_car(self, car_id, owner, price):
        self.cars[car_id] = {"owner": owner, "price": price}
        self.blockchain.add_block({
            "action": "add",
            "car_id": car_id,
            "owner": owner,
            "price": price
        })

    # Place bid
    def bid(self, car_id, bidder, bid_amount):
        if car_id in self.cars and bid_amount > self.cars[car_id]["price"]:
            self.cars[car_id]["owner"] = bidder
            self.cars[car_id]["price"] = bid_amount

            self.blockchain.add_block({
                "action": "bid",
                "car_id": car_id,
                "owner": bidder,
                "price": bid_amount
            })

    # Get current car details
    def get_car(self, car_id):
        return self.cars.get(car_id, None)

    # Get auction history
    def get_history(self, car_id):
        return self.blockchain.query_history(car_id)


# Driver Code
app = CarAuction()

app.add_car("C1", "Alice", 5000)
app.bid("C1", "Bob", 5500)
app.bid("C1", "Charlie", 6000)

print("Current Car:", app.get_car("C1"))
print("\nAuction History:", app.get_history("C1"))