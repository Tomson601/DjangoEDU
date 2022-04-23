from cmath import sqrt
from delta import delta

print("ax^2 + bx + c = 0")
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

print("Δ = ", delta(a, b, c))

if delta(a, b, c) < 0:
    print("Δ is lower than 0, equation has no solutions")

elif delta(a, b, c) == 0:
    x = (-1*b)/(2*a)
    print("x = ", x)
    
else:
    print("Formula has 2 roots:")
    x1 = ((-b)-(sqrt(delta(a, b, c))))/(2*a)
    x2 = ((-b)+(sqrt(delta(a, b, c))))/(2*a)
    
    print("x1 = ", x1)
    print("x2 = ", x2)
