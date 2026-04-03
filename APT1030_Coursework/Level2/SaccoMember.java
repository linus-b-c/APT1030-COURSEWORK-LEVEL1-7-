package Level2;
import java.util.Scanner;

public class SaccoMember {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("--- SACCO Member Registration (Java) ---");
        
        // Explicit Data Typing
        System.out.print("Enter Member Name: ");
        String name = scanner.nextLine();
        
        System.out.print("Enter Member ID: ");
        int memberId = scanner.nextInt();
        
        double totalSavings = 0.0;
        
        // Iteration for 6 months
        for (int i = 1; i <= 6; i++) {
            System.out.print("Month " + i + " Contribution (KES): ");
            double monthlyContrib = scanner.nextDouble();
            totalSavings += monthlyContrib;
        }
        
        System.out.println("\n--- Statement ---");
        System.out.println("Member Name: " + name);
        System.out.println("Member ID: " + memberId);
        System.out.printf("Total Savings: KES %.2f%n", totalSavings);
        
        scanner.close();
    }
}