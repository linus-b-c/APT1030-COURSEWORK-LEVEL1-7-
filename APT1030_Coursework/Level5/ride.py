# Functional Approach: No classes, no side effects
base_fare = 200
cost_per_km = 50

# Lambda Function: (Input Distance 'd') -> Result
calc_fare = lambda d: base_fare + (d * cost_per_km)

def run_functional_engine():
    print("--- Nairobi Ride-Hailing (Functional Python) ---")
    try:
        dist = float(input("Enter distance in KM: "))
        # We "apply" the lambda function to the input
        total = calc_fare(dist)
        print(f"Total Fare: {total:,.2f} KES")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    run_functional_engine()