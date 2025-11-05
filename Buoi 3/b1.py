numbers = [2, 3, 2, 5, 3, -4, 10, 5]

ds = []
for n in numbers:
    if n not in ds:
        ds.append(n)
print("Danh sách sau khi loại trùng: ",ds)

ds1 = [n**2 if n % 2 == 0 else n**3 for n in ds ]
print("List moi:", ds1)

ds2 = [numbers[i] for i in range(0, 8, 2)]
average = sum(ds2)/ len(ds2)
print("Giá trị tb ở vị trí chỉ số chẵn:", average)

sx = ds1[:]  
ds3 = []
while sx:
    gt_min = min(sx, key=abs)
    ds3.append(gt_min)
    sx.remove(gt_min)
print("Danh sách sắp xếp theo trị tuyệt đối:", ds3)