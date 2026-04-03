# nhif_logic.py

class Patient:
    def __init__(self, name, policy_number):
        # Encapsulation: Data is bundled inside the object
        self._name = name
        self._policy_number = policy_number

    # Method: Defines the behavior of the Patient object
    def calculate_claim(self, amount):
        """
        Deducts 10% co-payment and returns the NHIF coverage amount.
        """
        co_payment = amount * 0.10
        return amount - co_payment

    # Getter method to safely access the private name
    def get_details(self):
        return f"Member: {self._name} | Policy: {self._policy_number}"