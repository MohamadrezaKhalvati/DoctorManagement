class Doctors:
    def __init__(
        self, doctor_id, name, specialization, contact_phone_number, doctor_email
    ):
        self.doctor_id = doctor_id
        self.doctor_name = name
        self.specialization = specialization
        self.contact_phone_number = contact_phone_number
        self.doctor_email = doctor_email

    def create_doctor(self):
        doctor = self.make_object()

        try:
            with open("doctors.txt", "a") as file:
                file.write(f"{medicine}\n")
            print("doctor entry created successully.")

        except ExceptionType as e:
            print("doctors information doesn't write in doctors file")

    def get_doctors_data(self):
        try:
            with open("doctors.txt", "r") as file:
                doctors = self.filter_data(file)
                return doctors
        except ExceptionType as e:
            print("error")

    def read_medicines(self):
        medcines = self.get_medicines_data()
        print(f"List of medicines:\n {medicines}")

    def make_object(self):
        return {
            "doctor_id": self.doctor_id,
            "doctor_name": self.doctor_name,
            "specialization": self.specialization,
            "contact_phone_number": self.contact_phone_number,
            "doctor_email": self.doctor_email,
        }

    def filter_data(self, data):
        raw_data = data.readlines()
        text_to_remove = "\n"
        updated_data = []
        for data in raw_data:
            updated_data.append(data.replace(text_to_remove, ""))
        return updated_data

    def display_info(self):
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Name: {self.doctor_name}")
        print(f"Specialization: {self.specialization}")
        print(f"Contact Number: {self.contact_phone_number}")
        print(f"Email: {self.doctor_email}")
