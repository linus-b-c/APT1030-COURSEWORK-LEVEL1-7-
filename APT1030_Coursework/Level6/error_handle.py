# Function to check access
def check_access(role):
    if role != "Doctor":
        # Raise a specific error type
        raise PermissionError("Access Denied: You must be a Doctor to view these records.")
    else:
        print("Access Granted. Loading Patient Files...")

# Main program block
try:
    user_role = input("Enter your role: ")
    check_access(user_role)
except PermissionError as e:
    # This catches the error so the program doesn't crash
    print(f"SECURITY ALERT: {e}")

print("System Status: Online (Program continued successfully)")