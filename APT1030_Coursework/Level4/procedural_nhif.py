# procedural_nhif.py

def get_patient_data():
    """Captures input and returns a dictionary (Data Structure)"""
    name = input("Enter Patient Name: ")
    policy = input("Enter Policy Number: ")
    bill = float(input("Enter Hospital Bill Amount (KES): "))
    return {"name": name, "policy": policy, "bill": bill}

def calculate_nhif_payout(amount):
    """Pure functional logic"""
    co_payment = amount * 0.10
    return amount - co_payment

def run_system():
    # Procedural flow: Step 1 -> Step 2 -> Step 3
    data = get_patient_data()
    payout = calculate_nhif_payout(data["bill"])
    
    print(f"\nPatient: {data['name']}")
    print(f"NHIF Payout: KES {payout:,.2f}")

if __name__ == "__main__":
    run_system()