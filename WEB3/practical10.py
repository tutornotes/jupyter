import hashlib, time

class Block:
    def __init__(s,i,d,p):
        s.i,s.t,s.d,s.p=i,time.time(),d,p
        s.h=hashlib.sha256(f"{i}{s.t}{d}{p}".encode()).hexdigest()

class Blockchain:
    def __init__(s): s.c=[Block(0,"Genesis","0")]
    def add(s,d): s.c.append(Block(len(s.c),d,s.c[-1].h))
    def history(s): return [b.d for b in s.c if isinstance(b.d,dict)]

class VotingApp:
    def __init__(s): s.bc=Blockchain(); s.votes={}
    def vote(s,voter,candidate):
        if voter in s.votes:
            return "Voter has already voted"
        s.votes[voter]=candidate
        s.bc.add({"voter":voter,"candidate":candidate})
        return "Vote cast"
    def tally(s):
        t={}
        for c in s.votes.values(): t[c]=t.get(c,0)+1
        return t

app = VotingApp()

print(app.vote("Alice","Candidate1"))
print(app.vote("Bob","Candidate2"))
print(app.vote("Charlie","Candidate1"))
print(app.vote("Alice","Candidate2"))
print("\nVote Tally:", app.tally())
print("\nBlockchain History:", app.bc.history())
