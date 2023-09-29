num = int(input("Number: "))
kitson = []

for i in range(1, num + 1):
    if num % i == 0:
        kitson.extend([i])

print(kitson)