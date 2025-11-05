strings = input("Nhập vào chuỗi bất kỳ: ")

ds = ""
for char in strings:
    if char.isalpha() or char.isspace():
        ds += char

ds = ds.lower()
print(f"Chuỗi chuẩn hóa: {ds}")

nguyen_am = "ueoai"
dem_nguyen_am = sum(1 for char in ds if char in nguyen_am)
dem_phu_am = sum(1 for char in ds if char.isalpha() and char not in nguyen_am)

print(f"Số nguyên âm: {dem_nguyen_am}")
print(f"Số phụ âm: {dem_phu_am}")

ds1 = ds.split()         
ds2 = []
for tu in ds1:                       
    a = tu[::-1]              
    ds2.append(a)
print(f"Đảo từng từ: {ds2}")

ds3 = ds.replace(" ", "")
if ds3 == ds3[::-1]:
    print("Palindrome: True")
else:
    print("Palindrome: False")
