# 12345 / десятки тысяч / тысячи / сотни / десятки / единицы
a, b, c, d, e = map(int, input().split())
b = (d ** e * c) // (a-b)
print(float(b)) 