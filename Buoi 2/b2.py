import math

n=int(input("Nhap so nguyen duong n: "))
while n<=0:
    n=int(input("Nhap lai so nguyen duong n: "))
dem =0
for i in range(2,n):
    if i**0.5==int(i**0.5):
        dem+=1
print(dem)