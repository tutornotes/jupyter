import hashlib,time
class Block:
    def __init__(s,i,d,p): s.i,s.t,s.d,s.p=i,time.time(),d,p; s.h=hashlib.sha256(f"{i}{s.t}{d}{p}".encode()).hexdigest()
class Blockchain:
    def __init__(s): s.c=[Block(0,"Genesis","0")]
    def invoke(s,d): s.c.append(Block(len(s.c),d,s.c[-1].h))
    def query(s,k): return [b.d for b in s.c if isinstance(b.d,dict) and b.d.get("car_id")==k]
class Auction:
    def __init__(s): s.bc=Blockchain(); s.cars={}
    def add_car(s,id,owner,price): s.cars[id]={"owner":owner,"price":price}; s.bc.invoke({"car_id":id,"owner":owner,"price":price,"action":"add"})
    def bid(s,id,bidder,bid):
        car = s.cars.get(id)
        if car and bid>car["price"]:
            car["owner"]=bidder
            car["price"]=bid
            s.bc.invoke({"car_id":id,"owner":bidder,"price":bid,"action":"bid"})
    def history(s,id): return s.bc.query(id)
app=Auction()
app.add_car("C1","Alice",5000)
app.bid("C1","Bob",5500)
app.bid("C1","Charlie",5400)
print(app.cars["C1"])
print(app.history("C1"))
