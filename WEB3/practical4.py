import hashlib,time

class B:
    def __init__(s,i,d,p): s.i,s.d,s.p=i,d,p; s.h=hashlib.sha256(f"{i}{time.time()}{d}{p}".encode()).hexdigest()

class BC:
    def __init__(s): s.c=[B(0,"Genesis","0")]
    def add(s,d): s.c.append(B(len(s.c),d,s.c[-1].h))

class App:
    def __init__(s): s.bc,s.a=BC(),{}
    def create(s,i,o,v): s.a[i]={"owner":o,"value":v}; s.bc.add(("create",i,o,v))
    def transfer(s,i,n): s.a[i]["owner"]=n; s.bc.add(("transfer",i,n))

app=App()
app.create("A1","Alice",500)
app.transfer("A1","Bob")
print(app.a["A1"])
print(app.bc.c[1].d, app.bc.c[2].d)
