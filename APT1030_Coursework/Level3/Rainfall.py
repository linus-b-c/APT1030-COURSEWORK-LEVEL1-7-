# Rainfall Advisory System
try:
    rainfall = float(input("Enter Rainfall (mm): "))
    temp = float(input("Enter Temperature (°C): "))

    if rainfall < 200:
        print("Status: Irrigation Required")
    elif rainfall >= 200 and temp > 30:
        print("Status: Monitor Soil")
    else:
        print("Status: Normal Conditions")
except ValueError:
    print("Please enter valid numerical data.")