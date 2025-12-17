strings= input("Nhap tu: ")
ds= set(strings)
print(ds)

d={}
for i in ds:
    if i in d:
            d[i] += 1
    else:
            d[i] = 1
print(d)



