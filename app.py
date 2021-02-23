x = 2
y = 4

x1 = 1/2 * (x+y)

# print(x1)

def fOfX(x):
    formula = x**3 - 9*x + 1
    return formula

px = x1
# print(px, "ffffffffff")
for i in range(5):
    if fOfX(x1) > 0:
        x1 = 1/2 * (x + x1)
        # print(x1, "x11111111")
        print(fOfX(x1))
    if fOfX(x1) < 0:
        # print(x1, "sdfdghfffsfdg")
        x1 = 1/2 * (x1 + px)
        print(fOfX(x1))

