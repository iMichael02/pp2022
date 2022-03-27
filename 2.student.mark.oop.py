class Student:
    def __init__(self, sid, sname, sdob):
        self.id = sid
        self.name = sname
        self.dob = sdob
    def printSt(self):
        print(f"{self.id}\t{self.name}\t{self.dob}")
        
class Course:
    def __init__(self, cid, cname):
        self.id = cid
        self.name = cname
    def printC(self):
        print(f"{self.id}\t{self.name}")
        
StList = []
CrsList = []

def inputSt():
    
    print("Input student information:")
    stCountInput = int(input("Enter students number: "))
    for i in range(0, stCountInput):
        sid = str(input(f"Enter {i+1}th student ID: "))
        sname = str(input(f"Enter {i+1}th student name: "))
        sdob = str(input(f"Enter {i+1}th student date of birth: "))
        StList.append(Student(sid, sname, sdob))
        print("=============================================")
        
def inputCrs():
    
    print("Input course information:")
    crsCountInput = int(input("Enter courses number: "))
    for i in range(0, crsCountInput):
        cid = str(input(f"Enter {i+1}th course ID: "))
        cname = str(input(f"Enter {i+1}th course name: "))
        CrsList.append(Course(cid, cname))
        print("=============================================")
        
def inputMarks():
    
    print("Input student marks:")
    cid = str(input("Enter course ID: "))
    print("=============================================")
    for course in CrsList:
        if course.id == cid:
            marksList = {}
            for student in StList:
                mark = float(input(f"Enter mark for student with ID {student.id}: "))
                thisMark = {course.name:mark}
                student.marks = thisMark
                marksList.update({student.id:mark})
                course.marksList = marksList
                print("=============================================")
        break
                
def listCourses():
    
    print("List courses:")
    print("ID\tName")
    for course in CrsList:
        print(f"{course.id}\t{course.name}\n")
        
    print("=============================================")
    
def listStudents():
    
    print("List students:")
    print("ID\tName\tD.O.B")
    for student in StList:
        print(f"{student.id}\t{student.name}\t{student.dob}\t")
    print("=============================================")
        
def showMarks():
    
    print("Show marks:")
    cid = str(input("Enter course ID: "))
    print("ID\tMark")
    for course in CrsList:
        if course.id == cid:
            sid = list(course.marksList.keys())
            smark = list(course.marksList.values())
            for i in range(0, len(sid)):    
                print(f"{sid[i]}\t{smark[i]}")
        break
    print("=============================================")
            
inputSt()
inputCrs()
inputMarks()
listCourses()
listStudents()
showMarks()