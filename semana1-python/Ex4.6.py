def computepay(hours, rate):
    print("In computepay",hours,rate)
    if hours > 40:
        reg = fh * fr
        otp=(fh - 40.0) * (fr * 0.5)
        xp = reg + otp
    else:
        pay = hours * rate
    print("Returning",pay)

sh = input("Enter Hours")
sr = input("Enter Rate")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay:",xp)