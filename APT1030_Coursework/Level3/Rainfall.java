package Level3;
import java.util.Scanner;

public class Rainfall {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Rainfall (mm): ");
        double rain = sc.nextDouble();
        System.out.print("Temp (°C): ");
        double temp = sc.nextDouble();

        int mode;
        // Nested If Logic
        if (rain < 200) {
            mode = 1; // Irrigation Required
        } else if (temp > 30) {
            mode = 2; // Monitor Soil
        } else {
            mode = 3; // Normal
        }

        // Switch Statement for Readability
        switch (mode) {
            case 1: System.out.println("ADVISORY: Irrigation Required"); break;
            case 2: System.out.println("ADVISORY: Monitor Soil"); break;
            default: System.out.println("ADVISORY: Normal Conditions"); break;
        }
    }
}