package Level6;
import java.util.Scanner;

public class AccessControl {
    // Method that "throws" an exception
    public static void checkAccess(String role) throws Exception {
        if (!role.equalsIgnoreCase("Doctor")) {
            throw new Exception("SECURITY ERROR: Access restricted to Doctors only.");
        }
        System.out.println("Access Granted. Loading Records...");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Identify Role: ");
        String role = sc.nextLine();

        try {
            checkAccess(role);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}