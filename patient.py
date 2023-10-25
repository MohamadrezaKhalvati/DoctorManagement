import random
import json


class Patient:
    def __init__(
        self, name="", age="", gender="", phone_number="", identification_id=""
    ):
        self.patient_id = random.randint(0, 1000)
        self.identification_id = identification_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.medicine = []

    def create_patient(self):
        patient = self.make_object()
        try:
            with open("patients.txt", "a") as file:
                file.write(f"{patient}\n")
            print("Patient entity created successfully")
        except ExceptionType as e:
            print("patient doesn't write in patient file")

    def get_patient_data(self):
        try:
            with open("patients.txt", "r") as file:
                patients = self.filter_data(file)
                return patients
        except ExceptionType as e:
            print("error")

    def filter_data(self, data):
        raw_data = data.readlines()
        text_to_remove = "\n"
        updated_data = []
        for data in raw_data:
            updated_data.append(data.replace(text_to_remove, ""))
        return list(zip(range(len(raw_data)), updated_data))

    def read_patient(self):
        patients = self.get_patient_data()
        print("List of patients: ")
        for line, patient in patients:
            print(f"{patient[1]}")

    def make_object(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "phone_number": self.phone_number,
            "identification_id": self.identification_id,
            "medicine": self.medicine,
        }

    def find_patient(self, identification_id):
        patients = self.get_patient_data()
        chosen_patient = ""
        chosen_line = None
        selected_text = f'"identification_id": "{identification_id}"'
        for line, patient in patients:
            if selected_text in patient:
                chosen_patient = patient
        return chosen_line, chosen_patient

    def add_medicine_to_patient(self, chosen_patient, chosen_medicine_name):
        patient = aziz.find_patient(identification_id=chosen_patient)
        patient = json.loads(patient)
        patient_medicines = patient["medicine"]
        patient_medicines.append(chosen_medicine_name)

    def save(self):
        patient = self.make_object()
        line, _ = self.find_patient(self.identification_id)
        try:
            with open("patients.txt", "rw") as file:
                raw_data = file.readlines()
                raw_data[line] = f"{patient}\n"
                file.writelines(raw_data)
            print("Patient entity saved successfully")
        except ExceptionType as e:
            print("Patient doesn't save in patient file")


if __name__ == "__main__":
    alireza = Patient(
        name="alireza",
        age=23,
        gender="Male",
        phone_number="09178337280",
        identification_id="2283260531",
    )
    # alireza.create_patient()
    diba = Patient(
        name="diba",
        age=23,
        gender="Female",
        phone_number="09034801628",
        identification_id="3490477766",
    )
    # diba.create_patient()
    aziz = Patient(
        name="aziz",
        age=23,
        gender="Male",
        phone_number="09178337280",
        identification_id="3131234556",
    )
    aziz.create_patient()


# end main
