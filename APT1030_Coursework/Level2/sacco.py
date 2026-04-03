# Level 2 & 3: SACCO Contribution Tracker
def sacco_tracker():
    print("--- SACCO Member Registration (Python) ---")
    
    # Member Details
    name = input("Enter Member Name: ")
    member_id = input("Enter Member ID: ")
    
    total_savings = 0.0
    
    # Requirement: Input for 6 months using a loop (Iteration)
    print(f"\nEnter contributions for {name} (ID: {member_id}):")
    for month in range(1, 7):
        contribution = float(input(f"Month {month} Contribution (KES): "))
        total_savings += contribution # Accumulating total
        
    print("-" * 30)
    print(f"Member: {name}")
    print(f"Total Savings after 6 months: KES {total_savings:,.2f}")

sacco_tracker()