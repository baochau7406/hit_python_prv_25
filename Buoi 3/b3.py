s = input("Nhập vào văn bản: ").lower()
words = s.split()

ds = []
for w in words:
    if w not in ds:
        ds.append(w)
print("Từ duy nhất:", ds)

counts = [words.count(w) for w in ds]
for w, c in zip(ds, counts):
    print(f"Từ '{w}' xuất hiện {c} lần")

print("Từ xuất hiện nhiều nhất:", ds[counts.index(max(counts))])

print("Từ dài nhất:", max(ds, key=len))

print("Tổng số ký tự:", sum(len(w) for w in words))


sx = ds[:]  
ds1 = []
while sx:
    gt_max = max(sx, key=len)
    ds1.append(gt_max)
    sx.remove(gt_max)
print("Danh sách giam dan:", ds1)
