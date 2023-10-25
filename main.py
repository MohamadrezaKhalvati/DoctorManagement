from medicine import Medicine
from patient import Patient
import time

if __name__ == "__main__":
    while True:
        patient_admin = Patient()
        medicine_admin = Medicine()
        print("Are you a doctor or patient : \n")
        print("1.Doctor")
        print("2.Patient")
        first_choice = input("Enter number of your choice:  ")

        if first_choice == "1":  ## Doctor case
            print("1.add patient")
            print("2.add medicine")
            print("3.prescribing medication for a patient")
            break
            choice = input("Enter number of your chooice:")
            if choice == "1":
                name = input("Enter patient name :")
                age = input("Enter patient age:")
                gender = input("Enter patient gender:")
                identification_id = input("Enter patient identification id")
                phone_number = input("Enter patient phone number:")
                patient = Patient(
                    name=name,
                    age=age,
                    gender=gender,
                    phone_number=phone_number,
                    identification_id=identification_id,
                )
                patient.create_patient()
            elif choice == "2":
                medicine_name = input("Enter medicine name:")
                medicine_description = input("Enter medicine description:")
                medicine_price = input("Enter medicine description:")
                medicine_quantity = input("Enter medicine description:")
                medicine = Medicine(
                    name=medicine_name,
                    description=medicine_description,
                    price=medicine_price,
                    quantity=medicine_quantity,
                )
                medicine.create_medicine()
            elif choice == "3":
                chosen_patient = input("Enter patient identification id")
                chosen_medicine = input("Enter medicine name:")
                patient_data = patient_admin.find_patient(chosen_patient)

            else:
                print("Enter valid number.")
        elif first_choice == "2":  ## patient case
            print("1.display my info")
            print("2.my medicine")
            choice: input("Enter number of your choice: ")
            if choice == "1":  ## disllay my info
                entered_identification_id = input("Enter your identification id: ")
                patient = admin.find_patient(
                    identification_id=entered_identification_id
                )
                print("patient : \n")
                patient(patient)
            elif choice == "2":  ## my medicine
                medicine_name = input("Enter your medicine name")
                medicine = medicine_admin.find_medicine(medicine_name=medicine_name)
                print("medicine : \n")
                print(medicine)
            else:
                print("Enter valid number: 1 or 2!")
        else:
            print("Enter valid number : 1 or 2 ! ")
            break
