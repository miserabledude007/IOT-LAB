# Importing Time module
import time

# Initializing variables
Vehicle_Number = ['TN37-RK-6102']
Vehicle_Type = ['Car']
vehicle_Name = ['Audi']
Owner_Name = ['RK']
Date = ['06-10-2000']
Time = ['17:34:00']
bikes = 100
cars = 250
bicycles = 78

def main():
    global bikes, cars, bicycles
    
    while True:
        print("-----------------------------------------------------")
        print("\t\tParking Management System")
        print("-------------------------------------------------------")
        print("1. Vehicle Entry")
        print("2. Remove Entry")
        print("3. View Parked Vehicle")
        print("4. View Left Parking Space")
        print("5. Amount Details")
        print("6. Bill")
        print("7. Close Program")
        print("+---------------------------------------------+")
        
        try:
            ch = int(input("\tSelect option: "))
        except ValueError:
            print("###### Please Enter a Valid Option ######")
            continue
        
        if ch == 1:
            # Vehicle Entry
            while True:
                Vno = input("\tEnter vehicle number (XXXX-XX-XXXX) - ").upper()
                if Vno == "":
                    print("###### Enter Vehicle No. ######")
                elif Vno in Vehicle_Number:
                    print("###### Vehicle Number Already Exists ######")
                elif len(Vno) == 12:
                    Vehicle_Number.append(Vno)
                    break
                else:
                    print("###### Enter Valid Vehicle Number ######")
            
            while True:
                Vtype = input("\tEnter vehicle type (Bicycle=A/Bike=B/Car=C): ").lower()
                if Vtype == "":
                    print("###### Enter Vehicle Type ######")
                elif Vtype == "a":
                    Vehicle_Type.append("Bicycle")
                    bicycles -= 1
                    break
                elif Vtype == "b":
                    Vehicle_Type.append("Bike")
                    bikes -= 1
                    break
                elif Vtype == "c":
                    Vehicle_Type.append("Car")
                    cars -= 1
                    break
                else:
                    print("###### Please Enter Valid Option ######")
            
            while True:
                vname = input("\tEnter vehicle name - ")
                if vname == "":
                    print("###### Please Enter Vehicle Name ######")
                else:
                    vehicle_Name.append(vname)
                    break
            
            while True:
                OName = input("\tEnter owner name - ")
                if OName == "":
                    print("###### Please Enter Owner Name ######")
                else:
                    Owner_Name.append(OName)
                    break
            
            while True:
                date = input("\tEnter Date (DD-MM-YYYY) - ")
                if date == "":
                    print("###### Enter Date ######")
                elif len(date) != 10:
                    print("###### Enter Valid Date ######")
                else:
                    Date.append(date)
                    break
            
            while True:
                time_input = input("\tEnter Time (HH:MM:SS) - ")
                if time_input == "":
                    print("###### Enter Time ######")
                elif len(time_input) != 8:
                    print("###### Please Enter Valid Time ######")
                else:
                    Time.append(time_input)
                    break

            print("\n............................................................Record")

        elif ch == 2:
            # Remove Entry
            while True:
                Vno = input("\tEnter vehicle number to Delete (XXXX-XX-XXXX) - ").upper()
                if Vno == "":
                    print("###### Enter Vehicle No. ######")
                elif len(Vno) == 12:
                    if Vno in Vehicle_Number:
                        i = Vehicle_Number.index(Vno)
                        Vehicle_Number.pop(i)
                        Vehicle_Type.pop(i)
                        vehicle_Name.pop(i)
                        Owner_Name.pop(i)
                        Date.pop(i)
                        Time.pop(i)
                        print("\n............................................................Removed Successfully")
                        break
                    else:
                        print("###### No Such Entry ######")
                else:
                    print("###### Enter Valid Vehicle Number ######")
        
        elif ch == 3:
            # View Parked Vehicles
            count = 0
            print("------------------------------------------------------------------------------------------------------")
            print("\t\t\t\tParked Vehicle")
            print("------------------------------------------------------------------------------------------------------")
            print("Vehicle No.\tVehicle Type\tVehicle Name\tOwner Name\tDate\t\tTime")
            print("------------------------------------------------------------------------------------------------------")
            for i in range(len(Vehicle_Number)):
                count += 1
                print(f"{Vehicle_Number[i]}\t\t{Vehicle_Type[i]}\t\t{vehicle_Name[i]}\t\t{Owner_Name[i]}\t\t{Date[i]}\t\t{Time[i]}")
            print("------------------------------------------------------------------------------------------------------")
            print(f"------------------------------------------ Total Records - {count} ---------------------------------------")
            print("--------------------------------------------------------------------")
        
        elif ch == 4:
            # View Spaces Left
            print("------------------------------------------------------------------------------------------------------")
            print("\t\t\t\tSpaces Left For Parking")
            print("------------------------------------------------------------------------------------------------------")
            print(f"\tSpaces Available for Bicycle - {bicycles}")
            print(f"\tSpaces Available for Bike - {bikes}")
            print(f"\tSpaces Available for Car - {cars}")
            print("---------------------------------------------------------------------")
        
        elif ch == 5:
            # Parking Rate
            print("------------------------------------------------------------------------------------------------------")
            print("\t\t\t\tParking Rate")
            print("------------------------------------------------------------------------------------------------------")
            print("*1. Bicycle Rs20 / Hour")
            print("*2. Bike Rs40 / Hour")
            print("*3. Car Rs60 / Hour")
            print("---------------------------------------------------------------------")
        
        elif ch == 6:
            # Generate Bill
            print(".............................................................. Generating Bill ..........................................................................")
            while True:
                Vno = input("\tEnter vehicle number to Generate Bill (XXXX-XX-XXXX) - ").upper()
                if Vno == "":
                    print("###### Enter Vehicle No. ######")
                elif len(Vno) == 12:
                    if Vno in Vehicle_Number:
                        i = Vehicle_Number.index(Vno)
                        print(f"\tVehicle Check-in Time - {Time[i]}")
                        print(f"\tVehicle Check-in Date - {Date[i]}")
                        print(f"\tVehicle Type - {Vehicle_Type[i]}")
                        
                        while True:
                            try:
                                hr = int(input("\tEnter No. of Hours Vehicle Parked - "))
                                if hr < 0:
                                    print("###### Please Enter Valid Hours ######")
                                else:
                                    if Vehicle_Type[i] == "Bicycle":
                                        amt = hr * 20
                                    elif Vehicle_Type[i] == "Bike":
                                        amt = hr * 40
                                    elif Vehicle_Type[i] == "Car":
                                        amt = hr * 60
                                    
                                    ac = 0.18 * amt
                                    total_charge = amt + ac
                                    print(f"\tParking Charge - {amt}")
                                    print(f"\tAdditional Charge (18%) - {ac}")
                                    print(f"\tTotal Charge - {total_charge}")
                                    print("..............................................................Thank you for using our service...........................................................................")
                                    input("\tPress Any Key to Proceed - ")
                                    break
                            except ValueError:
                                print("###### Please Enter a Valid Number ######")
                        break
                    else:
                        print("###### No Such Entry ######")
                else:
                    print("###### Enter Valid Vehicle Number ######")

        elif ch == 7:
            # Close Program
            print("..............................................................Thank you for using our service...........................................................................")
            print(" **********(: Bye Bye :)**********")
            break
        
        else:
            print("###### Please Enter a Valid Option ######")

# Run the main function
if __name__ == "__main__":
    main()
