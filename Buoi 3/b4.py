s = "An:8.5, Binh:7.0, An:9.0, Cuong:6.5, Binh:8.0, Dung:7.5"

ds1 = []
for dt in s.split(", "):
    name, score = dt.split(":")
    ds1.append((name, float(score)))
print("Danh sách (tên, điểm):", ds1)

ds2 = {name for name, _ in ds1}
print("Tên duy nhất:", ds2)

ds3 = []
for ten in ds2:
    ds_ten = [diem for t, diem in ds1 if t == ten]
    avg = sum(ds_ten) / len(ds_ten)
    ds3.append((ten, avg))
    print(f"{ten}: {avg}")

print("Điểm trung bình:", ds3)

max_avg = max(ds3, key=lambda x: x[1])
min_avg = min(ds3, key=lambda x: x[1])
print("Cao nhất:", max_avg)
print("Thấp nhất:", min_avg)

ds4 = []
while sx:
    gt_max = max(sx, key=lambda x: x[1])
    ds4.append(gt_max)
    sx.remove(gt_max)

print("Danh sách giảm dần:", tuple(ds4))
