fh = open("mboxshort.txt","r")
lst = list()
dc = dict()


for line in fh:
    if not line.startswith("From "):
        continue
    splitada = line.split()
    lst.append(splitada[1])
for email in lst:
        dc[email] = dc.get(email,0) + 1   
print(dc) 
bigname = None
bigcount = None
print(dc.items())
for email,contagem in dc.items():
    if bigcount is None or contagem > bigcount:
        bigcount = contagem
        bigname = email
        print(bigname)
    
print(email,bigcount)
