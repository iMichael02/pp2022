import math
import numpy as np
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

class Student:
    def __init__(self, sid, sname, sdob):
        self.id = sid
        self.name = sname
        self.dob = sdob
        self.marks = {}
        self.gpa = 0
    def calGpa(self):
        markList = list(self.marks.values())
        markList = np.array(markList)
        courseList = list(self.marks.keys())
        creditList = []
        for i in range(0, len(courseList)):
            for course in CrsList:
                if course.name == courseList[i]:
                    creditList.append(course.credit)
        self.gpa = np.average(markList, weights=creditList)
        
class Course:
    def __init__(self, cid, cname, cre):
        self.id = cid
        self.name = cname
        self.credit = cre
        
StList = []
CrsList = []

def inputSt(stdscr):
    
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(0, 50, "Input student information:")
    stdscr.addstr(1, 0, "Enter students number: ")
    win1 = curses.newwin(1 , 10, 1, 23)
    box1 = Textbox(win1)
    rectangle(stdscr, 0, 22, 2, 34)
    stdscr.refresh()
    box1.edit()
    stCountInput = int(box1.gather())
    stdscr.addstr(3, 0, "=======================================================")
    stdscr.refresh()
    for i in range(0, stCountInput):
        stdscr.addstr(5, 0, f"Enter {i+1}th student ID: ")
        win2 = curses.newwin(1 , 10, 5, 23)
        box2 = Textbox(win2)
        rectangle(stdscr, 4, 22, 6, 34)
        stdscr.refresh()
        box2.edit()
        sid = str(box2.gather())
        stdscr.addstr(7, 0, f"Enter {i+1}th student name: ")
        win3 = curses.newwin(1 , 30, 7, 25)
        box3 = Textbox(win3)
        rectangle(stdscr, 6, 24, 8, 56)
        sname = str(box3.gather())
        stdscr.refresh()
        stdscr.addstr(9, 0, f"Enter {i+1}th student date of birth: ")
        win4 = curses.newwin(1 , 10, 9, 34)
        box4 = Textbox(win4)
        rectangle(stdscr, 8, 33, 6, 45)
        sdob = str(box4.gather())
        StList.append(Student(sid, sname, sdob))
        stdscr.refresh()
        
def inputCrs(stdscr):
    
    stdscr.addstr(0, 50, "Input course information:")
    stdscr.addstr(1, 0, "Enter courses number: ")
    win1 = curses.newwin(1 , 10, 1, 22)
    box1 = Textbox(win1)
    rectangle(stdscr, 0, 21, 2, 33)
    stdscr.refresh()
    box1.edit()
    crsCountInput = int(input("Enter courses number: "))
    print("=======================================================")
    for i in range(0, crsCountInput):
        cid = str(input(f"Enter {i+1}th course ID: "))
        cname = str(input(f"Enter {i+1}th course name: "))
        cre = int(input(f"Enter {i+1}th course credits: "))
        CrsList.append(Course(cid, cname, cre))
        print("=======================================================")
        
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
        
def inputMarks(stdscr):
    
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(0, 30, "Input student marks:")
    stdscr.addstr(1, 0, "Enter course ID: ")
    win1 = curses.newwin(1 , 10, 1, 17)
    box1 = Textbox(win1)
    rectangle(stdscr, 0, 16, 2, 28)
    stdscr.refresh()
    box1.edit()
    cid = str(box1.gather())
    stdscr.addstr(3, 0, "=======================================================")
    for course in CrsList:
        if course.id == cid:
            marksList = {}
            for student in StList:
                stdscr.addstr(5, 0, f"Enter mark for student with ID {student.id}: ")
                win2 = curses.newwin(1 , 10, 5, 17)
                box2 = Textbox(win2)
                rectangle(stdscr, 4, 16, 6, 28)
                stdscr.refresh()
                box2.edit()
                mark = float(box2.gather())
                mark = round_down(mark, 1)
                thisMark = {course.name:mark}
                student.marks.update(thisMark)
                marksList.update({student.id:mark})
                course.marksList = marksList
                
def listCourses(stdscr):
    
    print("List courses:")
    print("ID\t\tName\t\tCredits")
    if len(CrsList) != 0:
        for course in CrsList:
            print(f"{course.id}\t\t{course.name}\t\t{course.credit}")
        print("=======================================================")
    else:
        pass
    
def listStudents(stdscr):
    
    print("List students:")
    print("ID\t\tName\t\t\tD.O.B")
    if len(StList) != 0:
        for student in StList:
            print(f"{student.id}\t\t{student.name}\t\t\t{student.dob}")
        print("=======================================================")
    else:
        pass
        
def showMarks(stdscr):
    
    print("Show marks:")
    cid = str(input("Enter course ID: "))
    print("ID\t\tMark")
    if len(CrsList) != 0:
        for course in CrsList:
            if course.id == cid:
                sid = list(course.marksList.keys())
                smark = list(course.marksList.values())
                if len(sid) != 0 and len(smark) != 0:
                    for i in range(0, len(sid)):    
                        print(f"{sid[i]}\t\t{smark[i]}")
                elif len(sid) != 0 and len(smark) == 0:
                    print("No mark has been added to this course yet")
                elif len(sid) == 0 and len(smark) != 0:
                    print("There is no student")
        print("=======================================================")
    else:
        pass
    
def sortByGpa():
    gpaList = []
    for student in StList:
        gpaList.append(student.gpa)

def quickSort(arr: list, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        
def partition(arr: list, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.getch()
            
wrapper(main)
inputSt()
inputCrs()
inputMarks()
inputMarks()
listCourses()
listStudents()
st = StList[0]
showMarks()
st.calGpa()
print(st.gpa)