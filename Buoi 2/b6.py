menu= []
total = 0

while True:
    name=input("Nhập tên món : ")
    price=input(f"Nhập giá của món {name}:")
    if name.lower() == 'x': 
        break
    elif name.lower() == 'pass':
        continue
    elif name.lower() == 'skip':  
        continue

    if not price.isdigit():
        print("Giá không hợp lệ, bỏ qua")
        continue

    price = int(price)
    menu.append((name, price))
    total += price

so_mon = len(menu)
if total > 200000:
    discount = total * 0.1
else:
    discount = 0

tong_phaitra = total - discount

print(f"Số món: {so_mon}")
print(f"Tổng tiền trước giảm: {total} VND")
print(f"Giảm giá: {int(discount)} VND")
print(f"Tổng tiền phải trả: {int(tong_phaitra)} VND")
