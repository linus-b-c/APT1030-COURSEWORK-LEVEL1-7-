def record_session():
    # Variable declared inside the function (Local Scope)
    patient_secret = "Confidential Data"
    print(f"Inside function: {patient_secret}")

record_session()

# Attempting to access outside
try:
    print(patient_secret)
except NameError as e:
    print(f"\nInterpreter Response: {e}")