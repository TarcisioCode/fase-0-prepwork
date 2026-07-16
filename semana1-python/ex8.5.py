fh = open("mboxshort.txt","r")
lst = list()
count = 0
print(dir(lst))
for line in fh:
    if not line.startswith("From "):
        continue
    splitada = line.split()
    print(splitada[1])
    count = count + 1


print("There were", count, "lines in the file with From as the first word")
