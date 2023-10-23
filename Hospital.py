# Jian (Andrew) Owens    12/2/22


import Patient

totalPrivateRoomCharges = 0
totalSemiPrivateRoomCharges = 0
totalWardRoomCharges = 0
totalTelephoneCharges = 0
totalTelevisionCharges = 0
totalReceipts = 0


PatientName = ""
days = 0
RoomType = ""

def Hospital():
    mainmenu()

#Displays mainmenu where the user chooses which option to includes entering patient info, daily summary, and exiting the program

def mainmenu():

    taskOver = False
    print("         Community Hospital          ")
    print()
    print("         Main Menu           ")
    print()
    while taskOver == False: 
        print("1) Enter Patient Billing Information")
        print("2) Print Daily Summary Report")
        print("3) Exit")
        print()
        selection = input("Selection: ")
        if selection == "1":
            billinginfo = patientbillinginfo()
        elif selection == "2":
            printSummaryReport(billinginfo)
        elif selection == "3":
            print("Program Exited!")
            print()
            taskOver = True
            exit()
        else:
            print()
            print("Please enter [1], [2], or [3]...")
            print()

#Displays a menu that allows the user to enter a patient's billing info which includes the patient's name, the number of days the
#patient stayed in the hospital, and the type of room (private, semi-private, ward).
#Once the patient info is retrieved a patient object is created and a
#billing report is generated that includes the patient's name, length of stay, and the charges incurred including the bill total.
#The totals that are used to print the hospitals daily summary report are updated.

def patientbillinginfo():
    print("\n         Community Hospital          ")
    print("\nPatient Billing Report          ")

    #=========== PATIENT INITIALIZER ==========#
    patient = Patient.patient()
    PatientName = patient[0]
    days = patient[1]
    RoomType = patient[2]
    #==========================================#

    totalPrivateRoomCharges = 0
    totalSemiPrivateRoomCharges = 0
    totalWardRoomCharges = 0
    totalTelephoneCharges = 0
    totalTelevisionCharges = 0
    totalReceipts = 0

#Chooses which roomtype and than calculates the Total 

    if RoomType == "P":
        totalPrivateRoomCharges += Patient.getRoomCharge(days, RoomType)
    elif RoomType == "S":
        totalSemiPrivateRoomCharges += Patient.getRoomCharge(days, RoomType)
    elif RoomType == "W":
        totalWardRoomCharges += Patient.getRoomCharge(days, RoomType)

    totalTelephoneCharges += Patient.getTELECharge(days)
    totalTelevisionCharges += Patient.getTVCharge(days)
    totalReceipts += Patient.getTotalCharge(days,RoomType)

    n = Patient.getRoomCharge(days,RoomType)
    b = Patient.getTELECharge(days)
    a = Patient.getTVCharge(days)
    c = Patient.getTotalCharge(days,RoomType)

    print("\n        Community Hospital"
		 , "\n    Patient Billing Statement"
	     , f"\n\nPatient Name: {PatientName}"
		 , f"\nNumber of Days in Hospital: {days}"
		 , f"\n\nRoom Charge: ${n}"
		 , f"\nTelephone Charge: ${b}"
		 , f"\nTelevision Charge: ${a}"
	     , f"\n\nTotal Due: ${c}\n")

    billinglist = []
    billinglist.append(totalPrivateRoomCharges)
    billinglist.append(totalSemiPrivateRoomCharges)
    billinglist.append(totalWardRoomCharges)
    billinglist.append(totalTelephoneCharges)
    billinglist.append(totalTelevisionCharges)
    billinglist.append(totalReceipts)
    return billinglist
    
    
#A summary report is printed that includes the daily total room charges for each type of room, 
#the daily total telephone charges, and the daily total television charges. 
# The report also includes the total receipts for the day.

def printSummaryReport(billinginfo):

    print("        Community Hospital"
		 + "\n\n      Daily Billing Summary"
		 + "\n\nRoom Charges"
	     + f"\nPrivate: ${billinginfo[0]}"
	     + f"\nSemi: ${billinginfo[1]}"
		 + f"\nWard: ${billinginfo[2]}"
		 + f"\nTelephone Charges: ${billinginfo[3]}"
		 + f"\nTelevision Charges: ${billinginfo[4]}"
		 + f"\n\nTotal Receipts: {billinginfo[5]}\n" )
    
def main():
    print("\nBy: Jian (Andrew) Owens")
    print("COM S 127 Sec. D\n")
    Hospital()

if __name__ == "__main__":
    main()