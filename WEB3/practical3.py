import hashlib, time

class Block:
    def __init__(s,i,d,p):
        s.i,s.t,s.d,s.p=i,time.time(),d,p
        s.h=hashlib.sha256(f"{i}{s.t}{d}{p}".encode()).hexdigest()

class Blockchain:
    def __init__(s):
        s.c=[Block(0,"Genesis","0")]
    def transact(s,d):
        s.c.append(Block(len(s.c),d,s.c[-1].h))
    def query(s,i):
        return s.c[i].d if i<len(s.c) else None
    def valid(s):
        return all(s.c[i].p==s.c[i-1].h for i in range(1,len(s.c)))

bc=Blockchain()
bc.transact({"user":"A","amount":100})
bc.transact({"user":"B","amount":50})

print(bc.query(1))
print(bc.query(2))
print(bc.valid())
