m = int(input())
n = int(input())

weights = []
for i in range(n):
    weight = int(input())
    weights.append(weight)

weights.sort()

boat = 0
first = 0
last = n - 1

while first <= last:
    if weights[first] + weights[last] <= m:
        first += 1
    last -= 1
    boat += 1

print(boat)
