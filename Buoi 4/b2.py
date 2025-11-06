strings= input("Nhap tu: ")
ds= set(strings)
print(ds)

dem=[]
for i in ds:
    lan= strings.count(i)
    dem.append(lan)
print(dem)



