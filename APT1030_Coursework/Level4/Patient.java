package Level4;

public class Patient {
    // Encapsulation: private fields protect sensitive member data
    private String name;
    private String policyNumber;

    // Constructor: Initializes the object
    public Patient(String name, String policyNumber) {
        this.name = name;
        this.policyNumber = policyNumber;
    }

    /**
     * Method: calculateClaim
     * Implements the business logic for NHIF co-payment (10%)
     */
    public double calculateClaim(double amount) {
        double coPayment = amount * 0.10;
        return amount - coPayment;
    }

    // Getter Method to access the private name field
    public String getName() {
        return name;
    }
}