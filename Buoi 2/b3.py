n= int(input("Nhap so luong n: "))

for i in range(1,n+1):
    print(f"Nhap thong tin hoc vien {i}")
    hoten=input("Nhap ho ten: ")
    tx1=float(input("Nhap diem tx1: "))
    tx2=float(input("Nhap diem tx2: "))
    tong=tx1+tx2
    if tong==200:
        loai="Xuat sac"
    elif tong>=150:
        loai="Gioi"
    elif tong>=100:
        loai="Kha"
    else:
        loai="TB"
    print(f"{i} {hoten} {tong} {loai}")