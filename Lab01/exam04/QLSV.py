from SinhVien import SinhVien

class QLSV:
    listSinhVien = []
    
    def generateID(self):
        maxId = 1
        if(self.numberOfStudents() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId =  maxId + 1
        return maxId
    
    def numberOfStudents(self):
        return self.listSinhVien.__len__()
    
    def addStudent(self):
        svId = self.generateID()
        name = input("Input student name: ")
        sex = input("Input student sex: ")
        major = input("Input student major: ")
        diemTB = float(input("Input average score: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.academicStanding(sv)
        self.listSinhVien.append(sv)
    
    def updateStudent(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Input student name: ")
            sex = input("Input student sex: ")
            major = input("Input student major: ")
            diemTB = float(input("Input average score: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.academicStanding(sv)
        else: 
            print("Student have ID = {} does not exist.".format(ID))
            
    def sortByID(self):
        self.listSinhVien.sort(key = lambda x: x._id, reverse=False)
        
    def sortByName(self):
        self.listSinhVien.sort(key = lambda x: x._name, reverse=False)
        
    def sortByAC(self):
        self.listSinhVien.sort(key = lambda x: x._diemTB, reverse=False)
        
    def findByID(self, ID):
        searchResult = None
        if(self.numberOfStudents() > 0):
            for sv in self.listSinhVien:
                if(sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, name):
        listSV = []
        if(self.numberOfStudents() > 0):
            for sv in self.listSinhVien:
                if(sv._name.upper() == name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def academicStanding(self, sv:SinhVien):
        if(sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"
    
    def showStudent(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Average score", "Acedemic standing"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<14}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
                
        print("\n")
        
    def getListStudent(self):
        return self.listSinhVien