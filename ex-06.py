def computepay(hours, rate) :
    print("In Computepay", hours, rate)
    if hours > 40:
        print("Overtime")
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        print(reg,otp)
        pay = reg + otp
    else:
        print("Regular")
        pay = hours * rate
    print("Returning", pay)
    return pay
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)


print(fh, fr)
xp = computepay(fh, fr)

# xp = float(xh) * float(xr)
print("Pay:",xp)