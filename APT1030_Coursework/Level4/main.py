# main.py
from nhif_logic import Patient

def start_portal():
    print("=== NHIF Digital Claims System ===")
    
    # 1. Input: Capturing user data
    name = input("Enter Patient Name: ")
    policy = input("Enter NHIF Policy Number: ")
    
    # 2. Instantiation: Creating the Object
    member = Patient(name, policy)
    
    try:
        bill_amount = float(input("Enter Hospital Bill Amount (KES): "))
        
        # 3. Method Call: Abstraction in action
        payout = member.calculate_claim(bill_amount)
        co_pay = bill_amount * 0.10
        
        # Output Results
        print("\n" + "="*30)
        print(member.get_details())
        print(f"Total Bill:    KES {bill_amount:,.2f}")
        print(f"NHIF Coverage: KES {payout:,.2f} (90%)")
        print(f"Co-payment:    KES {co_pay:,.2f} (10%)")
        print("="*30)
        
    except ValueError:
        print("Error: Please enter a valid numerical amount for the bill.")

if __name__ == "__main__":
    start_portal()