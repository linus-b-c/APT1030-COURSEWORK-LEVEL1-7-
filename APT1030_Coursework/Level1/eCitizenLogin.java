package Level1;
import java.util.Scanner;
public class eCitizenLogin {
    public static void main(String[] args) {
        String usernameDB = "adminKE";
        String passwordDB = "254Secure";

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Username: ");
        String userInput = sc.nextLine();
        System.out.print("Enter Password: ");
        String passInput = sc.nextLine();

        // In Java, we use .equals() for string comparison
        if (userInput.equals(usernameDB) && passInput.equals(passwordDB)) {
            System.out.println("Access Granted");
        } else {
            System.out.println("Invalid Credentials");
        }
        sc.close();
    }
}