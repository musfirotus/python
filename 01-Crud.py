data = []

class Employee:
    def __init__(self):
        self.data = data

    def read(self):
        print(self.data)

    def create(self, data):
        self.data.append(data)
        return self

    def delete(self, id):
        for i, d in enumerate(data):
            if d['id'] == id:
                return data.pop(i)
    
    def update(self, id, datas):
        for i, val in enumerate(self.data):
            if val['id'] == id:
                datas = list(datas.items())
                datas.insert(0,("id",id))
                self.data[i] = dict(datas)
        return self.data


employee = Employee()
# employee.read()
employee.create({"id":1,"fullname":"ratna putri", "address":"jakarta", "salary":5000000, "phone":"099903"}) # id generate secara otomatis ketika data bertambah 	
employee.create({"id":2,"fullname":"mega mendung", "address":"jakarta", "salary":10000000, "phone":"343234"})
# employee.read() # return semua data employee yang sudah ditambahkan
# employee.delete(2) # menghapus data employe dengan id 2
# employee.read() # return semua data employee yang sudah ditambahkan
# employee.update(2,{"fullname":"raisa andriana", "address":"bekasi", "salary":1000000, "phone":"9939999"}) # mengubah data dengan id 2, return semua data employee