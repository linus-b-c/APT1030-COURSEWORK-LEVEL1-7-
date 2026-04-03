package Level4;
import java.util.Scanner;

public class NHIFSystem {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("=== NHIF Portal: Java Edition ===");
        
        // 1. User Input
        System.out.print("Enter Patient Name: ");
        String name = input.nextLine();
        
        System.out.print("Enter Policy Number: ");
        String policy = input.nextLine();
        
        System.out.print("Enter Bill Amount (KES): ");
        double bill = input.nextDouble();

        // 2. Object Instantiation (Using the module)
        Patient member = new Patient(name, policy);

        // 3. Method Call (Abstraction)
        double payout = member.calculateClaim(bill);
        double coPay = bill * 0.10;

        // 4. Output
        System.out.println("\n------------------------------");
        System.out.println("Patient: " + member.getName());
        System.out.println("NHIF Payout (90%): KES " + payout);
        System.out.println("User Co-payment (10%): KES " + coPay);
        System.out.println("------------------------------");
        
        input.close();
    }
}
