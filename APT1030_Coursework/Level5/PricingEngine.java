package Level5;

public class PricingEngine {
    // Encapsulated Data (State)
    private final double baseFare = 200.0;
    private final double costPerKm = 50.0;

    // Method (Behavior)
    public double computeTotal(double distance) {
        return this.baseFare + (distance * this.costPerKm);
    }
}