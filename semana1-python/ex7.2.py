fname = 'mbox.txt'
fh = open(fname,"r")
count = 0
soma = 0
print(fh)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence"):
        continue
    print(line)
    number = line.find(":")
    n1 = float(line[number + 1:])
    soma = n1 + soma
    count = count + 1
print("Average spam confidence:", soma/count)