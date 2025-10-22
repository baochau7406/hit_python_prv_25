s = "CLB Tin Hoc HIT truc thuoc Truong CNTT"

print("Chào mừng đến CLB Tin Học HIT")

print("CLB Tin Học HIT trực thuộc Trường CNTT - 10 điểm")

# In ra các chữ cái in hoa trong chuỗi
hoa= ','.join([ch for ch in s if ch.isupper()])
print("Cac chu cai in hoa trong chuoi:", hoa)

# In ra các chữ cái in thường trong chuỗi
thuong= ','.join([ch for ch in s if ch.islower()])
print("Cac chu cai in thuong trong chuoi:", thuong)

# Kiểm tra xem có từ 'CNTT' trong chuỗi không
print("CNTT có trong chuỗi không?", "CNTT" in s)

# Đổi chữ hoa thành chữ thường và ngược lại
print("Đổi hoa ↔ thường:", s.swapcase())
