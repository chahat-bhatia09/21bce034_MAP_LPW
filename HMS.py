#staff #patient #doctor
# patient_id = int(input("Give Your ID:"))
# doctor_id = int(input("Give Your ID:"))
# staff_id = int(input("Give Your ID:"))

# while(True):
val= input("Do you want to continue?(Y/N)")
if val == "Y":
    print("Welcome to the Hospital Management System")
    print("1. Patient Registration")
    print("2. Doctor Registration")
    print("3. Staff Registration")
    print("4. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("Patient Registration")
        patient_id = int(input("Give Your ID:"))
        patient_name = input("Give Your Name:")
        patient_age = int(input("Give Your Age:"))
        patient_gender = input("Give Your Gender:")
        print("Patient Registered Successfully")
        print("Patient_id:",patient_id)
        print("Patient_name:",patient_name)
        print("Patient_age:",patient_age)
        print("Patient_gender",patient_gender)
    elif choice == 2:
        print("Doctor Registration")
        doctor_id = int(input("Give Your ID:"))
        doctor_name = input("Give Your Name:")
        doctor_specialization = input("Give Your Specialization:")
        doctor_gender = input("Give Your Gender:")
        print("Doctor Registered Successfully")
        print("Doctor_id:",doctor_id)
        print("Doctor_name:",doctor_name)
        print("Doctor_specialization:",doctor_specialization)
        print("Doctor_gender",doctor_gender)
    elif choice == 3:
        print("Staff Registration")
        staff_id = int(input("Give Your ID:"))
        staff_name = input("Give Your Name:")
        staff_age = int(input("Give Your Age:"))
        staff_gender = input("Give Your Gender:")
        print("Staff Registered Successfully")
        print("Staff_id:",staff_id)
        print("Staff_name:",staff_name)
        print("Staff_age:",staff_age)
        print("Staff_gender",staff_gender)
    elif choice == 4:
        print("Exiting the Hospital Management System")
        # break
    else:
        print("Invalid Choice")
        
