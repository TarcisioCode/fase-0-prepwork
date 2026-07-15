fh = open("box.txt","r")
lst = list()

for line in fh:
    line = line.rstrip()
    splitada = line.split()
    for i in range(len(splitada)):
        if splitada[i] in lst:
            continue
        lst.append(splitada[i])

lst.sort()

print(lst)
