import hashlib, time, random

class Block:
    def __init__(s,i,d,p):
        s.i,s.t,s.d,s.p=i,time.time(),d,p
        s.h=hashlib.sha256(f"{i}{s.t}{d}{p}".encode()).hexdigest()

class Blockchain:
    def __init__(s): s.c=[Block(0,"Genesis","0")]
    def add(s,d): s.c.append(Block(len(s.c),d,s.c[-1].h))
    def query(s,asset_id): return [b.d for b in s.c if isinstance(b.d,dict) and b.d.get("asset_id")==asset_id]

class IoTAssetApp:
    def __init__(s): s.bc=Blockchain(); s.assets={}
    def register_asset(s,asset_id,location,status):
        s.assets[asset_id]={"location":location,"status":status}
        s.bc.add({"asset_id":asset_id,"location":location,"status":status,"action":"register"})
    def update_asset(s,asset_id,location,status):
        if asset_id in s.assets:
            s.assets[asset_id]={"location":location,"status":status}
            s.bc.add({"asset_id":asset_id,"location":location,"status":status,"action":"update"})

app = IoTAssetApp()

app.register_asset("A1","Warehouse", "Idle")
app.update_asset("A1","In Transit", "Moving")
app.update_asset("A1","Store","Delivered")
app.register_asset("A2","Factory","Idle")
app.update_asset("A2","Warehouse","Moving")

print("A1 History:", app.bc.query("A1"))
print("A2 History:", app.bc.query("A2"))
