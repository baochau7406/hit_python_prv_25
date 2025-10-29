import math

x=float(input("Nhap x: "))
n=int(input("Nhap n: "))
T=0
for i in range(n+1):
    T+=(x**i)/math.factorial(i)
print ("Vay e^x xap xi bang: ", T)

n=int(input("Nhap n: "))
S=0
for i in range(1,n+1):
    S+=1/math.factorial(i)
print("S= ", S)
