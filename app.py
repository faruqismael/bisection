# bisection formula to solve non-linear equation @faruqismael

# x = 2
# y = 4

def fOfX(x):
    formula = x**3 - 9*x + 1
    return formula

def bisection(x,y):
    x1 = 1/2 * (x+y)
    px = x1
    for i in range(5):
        if fOfX(x1) > 0:
            x1 = 1/2 * (x + x1)
            print(fOfX(x1))
        elif fOfX(x1) < 0:
            x1 = 1/2 * (x1 + px)
            print(fOfX(x1))

x = int(input("enter the number to display +ve number when inserting in f(x): "))
y = int(input("enter the number to display -ve number when inserting in f(x): "))
bisection(x,y)
