class BOOK:
    def __init__(self, id, title, author, year, status):
        self.id= id
        self.title= title
        self.author=author
        self.year=year
        self.status= status
    def in_thongtin(self):
        print (f"id:{self.id}, title:{self.title}, author: :{self.author}, year: {self.year}, status: {self.status}")
class LIBRARY:
    def __init__(self, ds= None):
        if ds is None:
            self.ds= []
        else:
            self.ds=ds

    def them_sach(self, book):
        self.ds.append(book)
        print("Them sach thanh cong")

    def del_sach(self,id):
        for p in self.ds:
            if p.id== id:
                self.ds.remove(p)
                print("Xoa sach thanh cong")
                return
        print("Khong thay sach de xoa")
    
    def find_title(self, find):
        result=[]
        for p in self.ds:
            if find.lower() in p.title.lower():
                result.append()
        return result
    
    def find_author(self, find):
        result=[]
        for p in self.ds:
            if find.lower() in p.author.lower():
                result.append()
        return result
    
    def muon_sach (self, id):
        for p in self.ds:
            if p.id== id:
                if p.status== "borrowed":
                    print("Sach da duoc muon")
                else:
                    print("Ban da muon sach thanh cong")
                    return
        print("Khong thay sach de muon ")
    
    def tra_sach (self, id):
        for p in self.ds:
            if p.id== id:
                if p.status== "avaiable":
                    print("Sach chua duoc muon, nen khong tra")
                else:
                    print("Ban da tra sach thanh cong")
                    return
        print("Khong thay sach de tra")

lib = LIBRARY()

b1 = BOOK(1, "Python cơ bản", "Nguyễn A", 2021)
b2 = BOOK(2, "Lập trình OOP", "Trần B", 2020)

lib.them_sach(b1)
lib.them_sach(b2)

lib.muon_sach(1)
lib.tra_sach(1)

lib.del_sach(2)

for b in lib.find_title("python"):
    b.in_thongtin()

            
                    




                
            
        

        



        
