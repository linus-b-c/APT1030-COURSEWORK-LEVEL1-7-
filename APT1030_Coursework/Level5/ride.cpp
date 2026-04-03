#include <iostream>
using namespace std;

// Procedural Function: Focuses on the action (calculating)
double calculateFare(double distance) {
    double baseFare = 200.0;
    double costPerKm = 50.0;
    return baseFare + (distance * costPerKm);
}

int main() {
    double distance;
    cout << "--- Nairobi Ride-Hailing (Procedural C++) ---" << endl;
    cout << "Enter distance in KM: ";
    cin >> distance;

    double total = calculateFare(distance);
    cout << "Total Fare: " << total << " KES" << endl;

    return 0;
}