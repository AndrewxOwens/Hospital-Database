# Jian (Andrew) Owens    12/2/22


global PRIVATE , SEMI, WARD, TELEPHONE, TELEVISION
PRIVATE =  225.00
SEMI = 165.00
WARD = 95.00
TELEPHONE = 1.75
TELEVISION = 3.50

name = ""
days = 0
roomType = ""

#Getting the Patient Info

def patient():
    patientName = str(input("Please Enter Patient Name: "))
    daysSpent = int(input("Please Enter Days (Int):   "))
    patientRoom = str(input("Please Enter Room Type [P], [S], [W]:    "))
    if patientRoom != "P" or "S" or "W":
        print("Please type in an actual Room Type Please [P], [S], [W]  ")
    

    return (patientName, daysSpent, patientRoom)

# Calculates how much each room will cost for how many days you stay

def getRoomCharge(days,roomType):
    daysSpent = days
    patientRoom = roomType
    if patientRoom == "P":
        return (daysSpent * PRIVATE)
    elif patientRoom == "S":
        return (daysSpent * SEMI)
    elif patientRoom == "W":
        return (daysSpent * WARD)
    return 0

# Calculates how much Telephone charge will cost for how many days you stay

def getTELECharge(days):
    return (days * TELEPHONE)

# Calculates how much Television charge will cost for how many days you stay

def getTVCharge(days):
    return (days * TELEVISION)

# Calculates the total cost for how many days you stay including TV/Telephone charge 

def getTotalCharge(days, roomType):
    return ( getRoomCharge(days,roomType) + getTELECharge(days) + getTVCharge(days) )
