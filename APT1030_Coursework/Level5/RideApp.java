package Level5;
import java.util.Scanner;

public class RideApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Creating an instance of our Engine object
        PricingEngine engine = new PricingEngine();

        System.out.print("Enter Distance (KM): ");
        double dist = sc.nextDouble();

        double total = engine.computeTotal(dist);
        System.out.println("Total Fare: " + total + " KES");
        
        sc.close();
    }
}