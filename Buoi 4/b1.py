hang= list(input().split())
print(hang)
set_ten = set()
for a in hang:
    set_ten.add(a)
print(set_ten)
t= tuple(set_ten)
print (t)
dem= len(t)
print(f"So luong hang hoa la: {dem} ")
ban_chay=["Laptop",]
print (f"San pham ban chay trong kho: {hang[1]} {hang[2]}")
print (f"San pham khong nam ban chay trong kho: {hang[4]} {hang[0]} {hang[6]}")




