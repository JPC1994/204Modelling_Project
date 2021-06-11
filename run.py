from nnf import Var
from lib204 import Encoding

# Input a set of courses into Var
# Use to generate propositions from the course list
def generateCourseList(setName, cSet):
    aList = []
    for course in cSet:
        cVar = Var("%s%s" % (setName, course))
        aList.append(cVar)
    return aList

# Use to generate a four by two list
def generateCell(cSet):
    aCell = {}
    for i in range(4):
        for j in range(2):
            for c in range(len(cSet)):
                aCell[(i, j, c)] = Var("%s%d%d" % (cSet[c], i, j))
    return aCell

# Generate a table
# To store course taken time
def generateTable(row, column):
    table = {}
    for i in range(row):
        for j in range(column):
            table[(i,j)] = []
    return table

def printSchedule(timetable):
    for i in range(4):
        for j in range(2):
          print("Year %d Semester %d:" % (i+1, j+1))
          print(timetable[(i,j)])
# Checking if the time table is still valid
# Students can't take the same course at the same semester
# There is a max of 5 course per semester
# Course already taken won't be recomend to take twice.
def validCheck(cart, i, j, table, inC):
    if len(cart) > 5:
        print("Cart exceed limit.")
        return False
    for m in range(len(cart)-1):
        if cart[-1] == cart[m]:
            print("Course already in cart.")
            return False
    for m in range(len(coursesTaken)):
        if cart[-1] == coursesTaken[m]:
            print("Course already taken.")
            return False
    return True

# material implication
def imp(left, right):
    return(left.negate() | right)

# material equivalence, if and only if
def iff(left, right):
    return(left.negate() | right) & (right.negate() | left)

# exclusive disjunction, xor
def xor(left, right):
    return((left.negate() & right) | (left & right.negate()))

# Checking if y_i can be satisfied by current taken courses
# If a course is avaliable for current semester
# Combine all constraints together
# Use the satisfied_by functin to check if the function is satisfied by a model
# If true, then put the course into course avaliable and allow student to take them
def inputT(Y, i):
    s = Var('s')
    for c in Y.constraints:
        s = s & c
    dic = {'s': True}
    for course in cL:
        dic.update({'x'+course: False})
    for course in coursesTaken:
        dic.update({'x'+course: True})
    for course in cL:
        dic.update({'y'+course: False})
    for course in courseCart:
        dic.update({'y'+course: True})
    dic.update({'y'+i: True})
    result = s.satisfied_by(dic)
    if result == True:
        coursesAvailable.update({len(coursesAvailable): i})
    else:
        return

# Check if student can be graduate
# Student needs to complete all the required courses for their degree plan
def checkGraduation():
    s = Var('s')
    for c in G.constraints:
        s = s & c
    dic = {'s': True}
    for course in cL:
        dic.update({'x'+course: False})
        dic.update({'z'+course: True})
    for course in coursesTaken:
        dic.update({'x'+course: True})
    result = s.satisfied_by(dic)
    if result == True:
        return True
    else:
        return False

def updateCoursesAvailable(courses):
  for i in range(len(courses)):
    for key, value in coursesAvailable.items():
      if value == courses[i]:
        del coursesAvailable[key]
        break

# Check time slot of courses
# Does the course table satisfy constraints
def checkTimeSlot():
    s = Var('s')
    for c in F.constraints:
        s = s & c
    dic = {'s': True}
    for course in cL:
        for i in range(4):
            for j in range(2):
                dic.update({course+str(i)+str(j): False})
    for course in courseTable:
        dic.update({course: True})
    result = s.satisfied_by(dic)
    return result

# Map graduation requirements into constraints
def graduation(G):
    for i in range(len(cR)):
        if (i == 0) | (i == 1):
             G.add_constraint(imp(cR[0] | cR[1], xor(cT[0], cT[1])))
        if (i == 3) | (i == 24) | (i == 23):
            G.add_constraint(imp((cR[3] & cR[24]) | cR[23], xor(cT[3] & cT[24], cT[23])))
        if (i == 12) | (i == 13):
            G.add_constraint(imp(cR[12] | cR[13], xor(cT[12], cT[13])))

        if (i != 0) & (i != 1) & (i != 3) & (i != 23) & (i != 24) & (i != 12) & (i != 13):
            G.add_constraint(imp(cR[i], cT[i]))

# Course slot constraints:
# Course are not recommand to take twice in 4 years of study
def timeSlot(F):
    for i in range(len(cL)):
        if (i == 0) | (i == 1):
             F.add_constraint(xor(xor(cTT[(0,0,0)],xor(cTT[(0,1,0)],xor(cTT[(1,0,0)],xor(cTT[(1,1,0)],xor(cTT[(2,0,0)],xor(cTT[(2,1,0)],xor(cTT[(3,0,0)],cTT[(3,1,0)]))))))),\
                                  xor(cTT[(0,0,1)],xor(cTT[(0,1,1)],xor(cTT[(1,0,1)],xor(cTT[(1,1,1)],xor(cTT[(2,0,1)],xor(cTT[(2,1,1)],xor(cTT[(3,0,1)],cTT[(3,1,1)])))))))))
        if (i == 3) | (i == 24) | (i == 23):
            F.add_constraint(xor(xor(cTT[(0,0,3)],xor(cTT[(0,1,3)],xor(cTT[(1,0,3)],xor(cTT[(1,1,3)],xor(cTT[(2,0,3)],xor(cTT[(2,1,3)],xor(cTT[(3,0,3)],cTT[(3,1,3)])))))))&\
                             xor(cTT[(0,0,24)],xor(cTT[(0,1,24)],xor(cTT[(1,0,24)],xor(cTT[(1,1,24)],xor(cTT[(2,0,24)],xor(cTT[(2,1,24)],xor(cTT[(3,0,24)],cTT[(3,1,24)]))))))),\
                             xor(cTT[(0,0,23)],xor(cTT[(0,1,23)],xor(cTT[(1,0,23)],xor(cTT[(1,1,23)],xor(cTT[(2,0,23)],xor(cTT[(2,1,23)],xor(cTT[(3,0,23)],cTT[(3,1,23)])))))))))
        if (i == 12) | (i == 13):
            F.add_constraint(xor(xor(cTT[(0,0,12)],xor(cTT[(0,1,12)],xor(cTT[(1,0,12)],xor(cTT[(1,1,12)],xor(cTT[(2,0,12)],xor(cTT[(2,1,12)],xor(cTT[(3,0,12)],cTT[(3,1,12)]))))))),\
                                 xor(cTT[(0,0,13)],xor(cTT[(0,1,13)],xor(cTT[(1,0,13)],xor(cTT[(1,1,13)],xor(cTT[(2,0,13)],xor(cTT[(2,1,13)],xor(cTT[(3,0,13)],cTT[(3,1,13)])))))))))
            
        if (i != 0) & (i != 1) & (i != 3) & (i != 23) & (i != 24) & (i != 12) & (i != 13):   
            F.add_constraint(xor(cTT[(0,0,i)],xor(cTT[(0,1,i)],xor(cTT[(1,0,i)],xor(cTT[(1,1,i)],xor(cTT[(2,0,i)],xor(cTT[(2,1,i)],xor(cTT[(3,0,i)],cTT[(3,1,i)]))))))))

# all set of prerequisite for every single course
# y_i is true when student can take the course with coude i
# constraint for y_i: need to complete prerequisite courses to take those courses
class Prerequisite:
    def cs101():
        Y = encoding()
        Y.add_constraint(cA[0])
        Y.add_constraint(xor(cT[1], cA[0]))
        Y.add_constraint(xor(cA[1], cA[0]))
        inputT(Y, 'cs101')
    def cs110():
        Y = encoding()
        Y.add_constraint(cA[1])
        Y.add_constraint(xor(cT[0], cA[1]))
        Y.add_constraint(xor(cA[0], cA[1]))
        inputT(Y, 'cs110')
    def cs121():
        Y = encoding()
        Y.add_constraint(cA[2])
        Y.add_constraint(iff(xor(cT[0], cT[1]), cA[2]))
        inputT(Y, 'cs121')
    def cs102():
        Y = encoding()
        Y.add_constraint(cA[3])
        Y.add_constraint(xor(cT[23], cA[3]))
        Y.add_constraint(xor(cA[23], cA[3]))
        inputT(Y, 'cs102')
    def cs124():
        Y = encoding()
        Y.add_constraint(cA[4])
        Y.add_constraint(iff(cT[2], cA[4]))
        inputT(Y, 'cs124')
    def cs203():
        Y = encoding()
        Y.add_constraint(cA[5])
        Y.add_constraint(iff(xor(cT[23], cT[24] & cT[3]) & cT[2], cA[5]))
        inputT(Y, 'cs203')
    def cs204():
        Y = encoding()
        Y.add_constraint(cA[6])
        Y.add_constraint(iff(xor(cT[23], cT[24] & cT[3]) & cT[2], cA[6]))
        inputT(Y, 'cs204')
    def cs221():
        Y = encoding()
        Y.add_constraint(cA[7])
        Y.add_constraint(iff(cT[4], cA[7]))
        inputT(Y, 'cs221')
    def cs223():
        Y = encoding()
        Y.add_constraint(cA[8])
        Y.add_constraint(iff(cT[4] & cT[6], cA[8]))
        inputT(Y, 'cs223')
    def cs235():
        Y = encoding()
        Y.add_constraint(cA[9])
        Y.add_constraint(iff(cT[4] & cT[5], cA[9]))
        inputT(Y, 'cs235')
    def cs324():
        Y = encoding()
        Y.add_constraint(cA[10])
        Y.add_constraint(iff(cT[7] & cT[9], cA[10]))
        inputT(Y, 'cs324')
    def cs360():
        Y = encoding()
        Y.add_constraint(cA[11])
        Y.add_constraint(iff(cT[4] & cT[6], cA[11]))
        inputT(Y, 'cs360')
    def cs322():
        Y = encoding()
        Y.add_constraint(cA[12])
        Y.add_constraint(iff(cT[8] & cT[9], cA[12]))
        Y.add_constraint(xor(cT[13], cA[12]))
        Y.add_constraint(xor(cA[13], cA[12]))
        inputT(Y, 'cs322')
    def cs326():
        Y = encoding()
        Y.add_constraint(cA[13])
        Y.add_constraint(iff(cT[8] & cT[9], cA[13]))
        Y.add_constraint(xor(cT[12], cA[13]))
        Y.add_constraint(xor(cA[12], cA[13]))
        inputT(Y, 'cs326')
    def cs365():
        Y = encoding()
        Y.add_constraint(cA[14])
        Y.add_constraint(iff(cT[9] & cT[6], cA[14]))
        inputT(Y, 'cs365')
    def cs422():
        Y = encoding()
        Y.add_constraint(cA[15])
        Y.add_constraint(iff(cT[8], cA[15]))
        inputT(Y, 'cs422')
    def cs462():
        Y = encoding()
        Y.add_constraint(cA[16])
        Y.add_constraint(iff(cT[8], cA[16]))
        inputT(Y, 'cs462')
    def cs466():
        Y = encoding()
        Y.add_constraint(cA[17])
        Y.add_constraint(iff(cT[14], cA[17]))
        inputT(Y, 'cs466')
    def cs465():
        Y = encoding()
        Y.add_constraint(cA[18])
        Y.add_constraint(iff(cT[6] & cT[8] & cT[11], cA[18]))
        inputT(Y, 'cs465')
    def cs467():
        Y = encoding()
        Y.add_constraint(cA[19])
        Y.add_constraint(iff(cT[6], cA[19]))
        inputT(Y, 'cs467')
    def cs497():
        Y = encoding()
        Y.add_constraint(cA[20])
        Y.add_constraint(iff(cT[14], cA[20]))
        inputT(Y, 'cs497')
    def cs499():
        Y = encoding()
        Y.add_constraint(cA[21])
        Y.add_constraint(iff(cT[14], cA[21]))
        inputT(Y, 'cs499')
    def st263():
        Y = encoding()
        Y.add_constraint(cA[22])
        inputT(Y, 'st263')
    def mt110():
        Y = encoding()
        Y.add_constraint(cA[23])
        Y.add_constraint(xor(cT[3], cA[23]))
        Y.add_constraint(xor(cA[3], cA[23]))
        Y.add_constraint(xor(cT[24], cA[23]))
        Y.add_constraint(xor(cA[24], cA[23]))
        inputT(Y, 'mt110')
    def mt111():
        Y = encoding()
        Y.add_constraint(cA[24])
        Y.add_constraint(xor(cT[23], cA[24]))
        Y.add_constraint(xor(cA[23], cA[24]))
        inputT(Y, 'mt111')
    def mt121():
        Y = encoding()
        Y.add_constraint(cA[25])
        inputT(Y, 'mt121')
    
# checking if each course for current degree plan meet their prerequisites
def checkPrerequisite():
    for i in range(len(cL)):
        getattr(Prerequisite, cL[i])()

# Encode constraints
def encoding():
    E = Encoding()
    return E

# Example theory that test the graduation constraints
# For the purpose of testing
def example_theory():
    E = Encoding()

    cL = ["cs101", "cs110", "cs121", "cs102", "cs124", "cs203", "cs204",
          "cs221", "cs223", "cs235", "cs324", "cs360", "cs322", "cs326",
          "cs365", "cs422", "cs462", "cs466", "cs465", "cs467", "cs497",
          "cs499", "st263", "mt110", "mt111", "mt121"]

    cT = generateCourseList('x', cL)
    cR = generateCourseList('z', cL)
    
    for i in range(len(cR)):
        if (i == 0) | (i == 1):
            E.add_constraint(cR[0] | cR[1])
            E.add_constraint(imp(cR[0] | cR[1], xor(cT[0], cT[1])))
        if (i == 3) | (i == 24) | (i == 23):
            E.add_constraint((cR[3] & cR[24]) | cR[23])
            E.add_constraint(imp((cR[3] & cR[24]) | cR[23], xor(cT[3] & cT[24], cT[23])))
        if (i == 12) | (i == 13):
            E.add_constraint(cR[12] | cR[13])
            E.add_constraint(imp(cR[12] | cR[13], xor(cT[12], cT[13])))

        if (i != 0) & (i != 1) & (i != 3) & (i != 23) & (i != 24) & (i != 12) & (i != 13):
            E.add_constraint(cR[i])
            E.add_constraint(imp(cR[i], cT[i]))

    return E

if __name__ == "__main__":
    # Courses student can take
    # This set of courses only contain required course for general computing degree
    # cs for CISC, st for STATS, and mt for MATH
    cL = ["cs101", "cs110", "cs121", "cs102", "cs124", "cs203", "cs204",
          "cs221", "cs223", "cs235", "cs324", "cs360", "cs322", "cs326",
          "cs365", "cs422", "cs462", "cs466", "cs465", "cs467", "cs497",
          "cs499", "st263", "mt110", "mt111", "mt121"]

    # Create sets to keep on track of courses at different status
    # Store which propositon is true
    coursesTaken = []
    coursesAvailable = {}
    courseCart = []
    courseTable = []
    
    # Generate course list store Var
    # This three list contains all propositions used in the model
    # cT contains x_i, cA contains y_i, cR contains z_i
    cT = generateCourseList('x', cL)
    cA = generateCourseList('y', cL)
    cR = generateCourseList('z', cL)

    # Generate possible timetable
    # cTT contains w_i_y_s(y for year, s for semester)
    cTT = generateCell(cL)
    F = encoding()
    timeSlot(F)
    print("Check time table constraint: ", F.is_satisfiable())

    # Create a time table to keep track what course is taken at which time period
    timetable = generateTable(4, 2)

    # Generate all constraints for graduation
    G = encoding()
    graduation(G)
    # Check wheather the degree plan can be finished(If not then the function is wrong)
    s = G.is_satisfiable()
    sl = G.solve()
    print("Is graduation satisfiable?: ", s)
    for keys, values in sl.items():
      print(keys, values)
    counter=0
    # Degree planning by different semesters
    # i for 4 years and j for 2 semesters each year
    while checkGraduation() == False:
      counter+=1
      print("--------------------------------------------------------------------")
      print("Trial ", counter)
      for i in range(4):
          # If student satisfy graduation requirements, then student can be graduate
          if checkGraduation() == True:
                  break
          for j in range(2):
              if checkGraduation() == True:
                  break
              # Reset the course cart for each semester's course selection
              courseCart = []
              loop = True
              check = True
              # Running through the constraints to give optional degree planning
              while loop == True:
                  if (len(courseCart)>=5): break
                  coursesAvailable = {}
                  checkPrerequisite()
                  updateCoursesAvailable(courseCart)
                  updateCoursesAvailable(coursesTaken)
                  if (len(coursesAvailable)<=0): break

                  print("\n")
                  print("Year %d Semester %d" % (i+1, j+1))
                  print("Courses Currently Avaliable: ")
                  print("Index \t","Course Code")
                                    
                  for keys, values in coursesAvailable.items():
                    print(" ",keys,"\t   ", values)

                  print("Input array index to put a course into course cart: ")
                  print("Or input x to end current semester's planning.")
                  inC = input()
                  if (inC == 'x') | (inC == 'X'):
                      loop = False
                      break
                  if not (int(inC) in coursesAvailable):
                      print("Index out of bound.")
                      continue

                  # Student can choose to put avaliable courses into cart
                  courseCart.append(coursesAvailable[int(inC)])
                  # Checking if a coures is valid for taken time wice
                  check = validCheck(courseCart, i, j, timetable, inC)
                  if check == False:
                      courseCart.pop()[-1]
                  print("Courses this semester: ", courseCart)
                  
              # Map selected courses to true on course taken for next semester
              for course in courseCart:
                  coursesTaken.append(course)
                  timetable[i,j].append(course)
                  courseTable.append(course+str(i)+str(j))
              print("Courses taken previously: ", coursesTaken)
              if checkGraduation() == True:
                  print("\n")
                  print("Student met graduation requirements.")
                  print("\n")
                  print("Student's course schedule for graduation: ")
                  printSchedule(timetable)
                  break

      # If student can't finish their degree on time
      if checkGraduation() == False:
          print("\n")
          print("Student failed to graduate in time with current's schedule.")
          print("\n")
          print("Failed course schedule: ")
          printSchedule(timetable)
      # Check if there exist any course takes mutiple times(Which is not recommanded)
      if checkTimeSlot() == True:
          print("\n")
          print("Successfully created time table with no muti-taken courses.")
      else:
          print("Unable to create time table.")
