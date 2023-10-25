import random

## important : id must be uniqe


class Medicine:
    def __init__(self, name="", description="", price="", quantity=""):
        self.medicine_id = random.randint(0, 1000)
        self.medicine_name = medicine_name
        self.medicine_description = medicine_description
        self.medicine_price = medicine_price
        self.medicine_quantity = medicine_quantity

    def create_medicine(self):
        medicine = self.make_object()
        print(medicine)
        try:
            with open("medicines.txt", "a") as file:
                file.write(f"{medicine}\n")
            print("Medicine entry created successfully.")

        except ExceptionType as e:
            print("medicine doesn't write in medicines file")

    def get_medicines_data(self):
        try:
            with open("medicines.txt", "r") as file:
                medicines = self.filter_data(file)
                return medicines
        except ExceptionType as e:
            print("error")

    def read_medicines(self):
        medcines = self.get_medicines_data()
        print(f"List of medicines:\n {medicines}")

    def make_object(self):
        return {
            "medicine_id": self.medicine_id,
            "medicine_name": self.medicine_name,
            "medicine_description": self.medicine_description,
            "medicine_price": self.medicine_price,
            "medicine_quantity": self.medicine_quantity,
        }

    def find_medicine(self, medicine_name):
        medicines = self.get_medicines_data()
        chosen_medicine = ""
        selected_text = f"'name': '{medicine_name}'"
        for medicine in medicine_name:
            if medicine in medicines:
                chosen_medicine = medicine
        return chosen_medicine

    def filter_data(self, data):
        raw_data = data.readlines()
        text_to_remove = "\n"
        updated_data = []
        for data in raw_data:
            updated_data.append(data.replace(text_to_remove, ""))
        return updated_data
