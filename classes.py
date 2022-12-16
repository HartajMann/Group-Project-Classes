# doctor class
class Doctor:
# reading file
    def readDoctorsFile(self, filename="doctors.txt"):
        doctorList = []
        with open(filename, 'r') as file:
            for lines in file:
                lines = lines.rstrip('\n')
                lines = lines.split('_')
                doctorList.append(lines)
        return doctorList
# displaying info
    def displayDoctorsList(self, doctorList):
        for lines in doctorList:
            print(lines[0].ljust(8), lines[1].ljust(8), lines[2].ljust(8), lines[3].ljust(8), lines[4].ljust(8),
                  lines[5].ljust(8))
# searching doctor
    def searchDoctorById(self, doctorList):
        x = 0
        id = input("Enter the doctor Id:\n")
        for lines in doctorList:
            if id == lines[0]:
                print("Id".ljust(8), "Name".ljust(8), "Speciality".ljust(8), "timing".ljust(8),
                      "Qualification".ljust(8), "Room Number")
                print(lines[0].ljust(8), lines[1].ljust(8), lines[2].ljust(8), lines[3].ljust(8), lines[4].ljust(8),
                      lines[5].ljust(8))
                x = 1
        if x == 0:
            print("Can't find the doctor with the same ID on the system")
# searching name
    def searchDoctorByName(self, doctorList):
        x = 0
        name = input("Enter doctor name:\n")
        for lines in doctorList:
            if name == lines[1]:
                print("Id".ljust(8), "Name".ljust(8), "Speciality".ljust(8), "timing".ljust(8),
                      "Qualification".ljust(8), "Room Number")
                print(lines[0].ljust(8), lines[1].ljust(8), lines[2].ljust(8), lines[3].ljust(8), lines[4].ljust(8),
                      lines[5].ljust(8))
                x = 1
        if x == 0:
            print("Can't find the doctor with the same name on the system")
# editing info
    def editDoctorInfo(self, doctorList):
        id = input("Please enter the id of the doctor that you want to edit their information:")
        for lines in doctorList:
            if id == lines[0]:
                lines[1] = input("Enter new Name:")
                lines[2] = input("Enter new Specilist in:")
                lines[3] = input("Enter new Timing:")
                lines[4] = input("Enter new Qualification:")
                lines[5] = input("Enter new Room number:")
                index = doctorList.index(lines)
                doctorList[index] = lines
                return doctorList
# adding to file
    def addDrToFile(self, doctorList):
        self.id = input("Enter the doctor’s ID:")
        self.name = input("Enter the doctor’s name:")
        self.speciality = input("Enter the doctor’s specility:")
        self.timing = input("Enter the doctor’s timing (e.g., 7am-10pm):")
        self.qualification = input("Enter the doctor’s qualification:")
        self.roomNumber = input("Enter the doctor’s room number:")
        newInfo = [self.id, self.name, self.speciality, self.timing, self.qualification, self.roomNumber]
        doctorList.append(newInfo)
        return doctorList
# formating
    def formatDrInfo(self, doctorList):
        x = ''
        for lines in doctorList:
            line = lines[0] + '_' + lines[1] + '_' + lines[2] + '_' + lines[3] + '_' + lines[4] + '_' + lines[
                5] + '\n'
            x = x + line
        return x
# writing to file
    def writeListOfDoctorsToFile(self, x):
        filename = 'doctors.txt'
        with open(filename, 'w') as file:
            file.write(x)

# for facility
class Facility:
    def __init__(self):
        self.facilityList = []
        with open("facilities.txt", "r") as file:
            lines = file.readlines()
            for text in lines:
                self.facilityList.append(text.split("\n")[0])
# adding facility
    def addFacility(self, facilityName):
        self.facilityList.append(facilityName)
# disylaing facilities
    def displayFacilities(self):
        for facilityName in self.facilityList:
            print(facilityName)
# writing to files
    def writeListOffacilitiesToFile(self):
        with open("facilities.txt", "w") as file:
            for facilityName in self.facilityList:
                file.write(facilityName + "\n")

# for laboratory
class Laboratory:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.labArray = []
# reading from file
    def readLaboratoriesFile(self):
        with open("laboratories.txt", 'r') as file:
            for lines in file:
                lines = lines.rstrip('\n')
                lines = lines.split('_')
                self.labArray.append(lines)
            return self.labArray
# displaying the list
    def displayLabsList(self):
        for lines in self.labArray:
            print(lines[0].ljust(5), lines[1].ljust(5))
# entring info
    def enterLaboratoryInfo(self):
        self.name = input("Enter Laboratory facility:\n")
        self.cost = input("Enter Laboratory cost:\n")
# formating
    def formatLabInfo(self):
        return f"{self.name}_{self.cost}"
# addding to file
    def addLabToFile(self):
        self.enterLaboratoryInfo()
        file = open("laboratories.txt", "a")
        file.write(self.formatLabInfo() + "\n")
        file.close()
# writing to file
    def writeListOfLabsToFile(self):
        file = open("laboratories.txt", "a")
        for line in self.labArray:
            file.write("\n" + line.formatLabInfo())

# for patient
class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
        self.patientList = []
# reading patient file
    def readPatientsFile(self):
        with open("patients.txt", 'r') as file:
            for lines in file:
                lines = lines.rstrip('\n')
                lines = lines.split('_')
                self.patientList.append(lines)
        return self.patientList
# displaying results
    def displayPatientsList(self):
        for lines in self.patientList:
            print(lines[0].ljust(8), lines[1].ljust(8), lines[2].ljust(8), lines[3].ljust(8), lines[4].ljust(8))
# searching id
    def searchPatientById(self):
        idP = input("Enter the Patient Id:\n")
        flag = 1
        for lines in self.patientList:
            if lines[0] == idP:
                print('id'.ljust(8), 'Name'.ljust(8), 'Disease'.ljust(8), 'Gender'.ljust(8), 'Age'.ljust(8))
                print(lines[0].ljust(8), lines[1].ljust(8), lines[2].ljust(8), lines[3].ljust(8), lines[4].ljust(8))
                flag = 0
        if flag == 1:
            print("Can't find the Patient with the same id on the system")
# entring new info
    def enterPatientInfo(self):
        self.pid = input("Enter Patient id:\n")
        self.name = input("Enter Patient name:\n")
        self.disease = input("Enter Patient disease:\n")
        self.gender = input("Enter Patient gender:\n")
        self.age = input("Enter Patient age:\n")
# writing tofile
    def writeListOfPatientsToFile(self):
        with open("patients.txt", "w") as file:
            for line in self.patientList:
                file.write(line.formatPatientInfo() + "\n")
# adding to file
    def addPatientToFile(self):
        with open("patients.txt", "a") as file:
            self.enterPatientInfo()
            file.write(self.formatPatientInfo() + "\n")
# formatting
    def formatPatientInfo(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"
# editing patient info
    def editPatientInfo(self):
        idp = input("Please enter the id of the patient that you want to edit their information: \n")
        newarray = []
        for line in self.patientList:
            if idp == line[0]:
                line[1] = input("Enter new Name:\n")
                line[2] = input("Enter new disease:\n")
                line[3] = input("Enter new gender:\n")
                line[4] = input("Enter new age:\n")
                newarray.append(line)
            else:
                newarray.append(line)

        file = open("patients.txt", "w")
        for lines in newarray:
            file = open("patients.txt", "a")
            file.write("%s_%s_%s_%s_%s" % (lines[0], lines[1], lines[2], lines[3], lines[4]) + "\n")
            file.close()
a
