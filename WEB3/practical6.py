import hashlib, time

class Block:
    def __init__(s,i,d,p):
        s.h=hashlib.sha256(f"{i}{time.time()}{d}{p}".encode()).hexdigest()
        s.d=d

class RewardChain:
    def __init__(s):
        s.c=[Block(0,"Genesis","0")]
        s.r={}
    def reward(s,m,p):
        s.r[m]=s.r.get(m,0)+p
        s.c.append(Block(len(s.c),{"member":m,"points":p,"total":s.r[m]},s.c[-1].h))
    def trace(s,m):
        return [b.d for b in s.c if isinstance(b.d,dict) and b.d["member"]==m]

rc=RewardChain()
rc.reward("M1",10)
rc.reward("M2",20)
rc.reward("M1",15)

print("Member M1 trace:", rc.trace("M1"))
print("Member M2 trace:", rc.trace("M2"))
