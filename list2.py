a = input()
b = list(map(int, input().split()))      # 1 2 3 4 5
b.insert(0, b.pop())                     # 5 1 2 3 4
print(b)