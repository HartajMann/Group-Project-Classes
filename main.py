# 15-12-2022
# this project is created by hartaj and abdullah anwar both contributed equally in the project
# we created a project for the alberta hospital it displays info about the doctors list we can serach doctors by name
# and id, edit thier id and add new doctors, patients its shows patients list, id,we can edit patients, add new
# laboratory tells about different lab test and their result,we can add new lab and their price, facility it shows
# facilities avaliable in the hospital, and we can add new facilities.

from classes import Doctor
from classes import Facility
from classes import Laboratory
from classes import Patient
# Main
b=0
while b!=1:
    print("Welcome to Alberta Hospital (AH) Managment system")
    no = input(
        "Select from the following options, or select 0 to stop:\n1-Doctors\n2-Facilities\n3-Laboratories\n4-Patients\n")
# calling doctor
    if no == "1":
        i = 0
        a = Doctor()
        while i != 6:
            doctorList = a.readDoctorsFile()
            no2 = input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by "
                        "name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n")
            if no2 == '1':
                a.displayDoctorsList(doctorList)
                print("Back to the prevoius Menu")
            elif no2 == '2':
                a.searchDoctorById(doctorList)
                print("Back to the prevoius Menu")
            elif no2 == '3':
                a.searchDoctorByName(doctorList)
                print("Back to the prevoius Menu")
            elif no2 == '4':
                newInfo = a.addDrToFile(doctorList)
                x = a.formatDrInfo(newInfo)
                a.writeListOfDoctorsToFile(x)
                print("Back to the prevoius Menu")
            elif no2 == '5':
                newInfo = a.editDoctorInfo(doctorList)
                x = a.formatDrInfo(newInfo)
                a.writeListOfDoctorsToFile(x)
                print("Back to the prevoius Menu")
            elif no2 == '6':
                break
            else:
                print("Wrong no enterd try again.")
                print("Back to the prevoius Menu")
                break
# calling facility
    elif no == '2':
        i = 0
        a = Facility()
        while i != 3:
            no2 = input("Facilities Menu:\n1-Display Facilities list\n2-Add Facility\n3-Back to the Main Menu\n")
            if no2 == '1':
                a.displayFacilities()
                print("Back to the prevoius Menu")
            elif no2 == '2':
                facilityName = input("Enter Facility name:")
                a.addFacility(facilityName)
                a.writeListOffacilitiesToFile()
                print("Back to the prevoius Menu")
            elif no2 == '3':
                break
            else:
                print("Wrong no enterd try again.")
                print("Back to the prevoius Menu")
                break
# calling laboratory
    elif no == '3':
        i = 0
        a = Laboratory('', '')
        while i != 3:
            a.readLaboratoriesFile()
            no2 = input("Laboratories Menu:\n1-Display laboratories list\n2-Add laboratory\n3-Back to the Main Menu\n")
            if no2 == '1':
                a.displayLabsList()
                print("Back to the prevoius Menu")
            elif no2 == '2':
                a.addLabToFile()
                print("Back to the prevoius Menu")
            elif no2 == '3':
                break
# calling patient 
    elif no == '4':
        i = 0
        a = Patient('', '', '', '', '')
        while i != 3:
            a.readPatientsFile()
            no2 = input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - "
                        "Edit patient info\n5 - Back to the Main Menu\n")
            if no2 == '1':
                a.displayPatientsList()
                print("Back to the prevoius Menu")
            elif no2 == '2':
                a.searchPatientById()
                print("Back to the prevoius Menu")
            elif no2 == '3':
                a.addPatientToFile()
                print("Back to the prevoius Menu")
            elif no2 == '4':
                a.editPatientInfo()
                print("Back to the prevoius Menu")
            elif no2 == '5':
                break
    else:
        quit()
