text = "X-DSPAM-Confidence:    0.8475"

atpos = text.find(":")
split = text[atpos+1:]
split = split.strip()
float_num = float(split)
print(float_num)