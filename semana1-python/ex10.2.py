fh = open("mboxshort.txt","r")
lst_hrs = list()
dc = dict()
count = 0

dc = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    horas = line.split()[5].split(":")[0]
    dc[horas] = dc.get(horas, 0) + 1

for h, c in sorted(dc.items()):
    print(h, c)
