#include <iostream>
#include <string>

int main() {
    std::string usernameDB = "adminKE";
    std::string passwordDB = "254Secure";
    std::string userInput, passInput;

    std::cout << "Enter Username: ";
    std::cin >> userInput;
    std::cout << "Enter Password: ";
    std::cin >> passInput;

    if (userInput == usernameDB && passInput == passwordDB) {
        std::cout << "Access Granted" << std::endl;
    } else {
        std::cout << "Invalid Credentials" << std::endl;
    }

    return 0;
}