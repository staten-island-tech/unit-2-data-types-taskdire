bill = int(input("What was the value of the bill? "))
tip = input("How was the service? ")
if tip == "bad":
    total = bill * 1
elif tip == "okay":
    total = bill * 1.15
elif tip == "good":
    total = bill * 1.20
elif tip == "great":
    total = bill * 1.25


print(total)




