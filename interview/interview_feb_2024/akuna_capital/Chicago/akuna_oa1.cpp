#include <iostream>
#include <vector>
#include "solution.h" // Assume solution.h contains the declaration of computeDifference


void runTestCase(const std::vector<int>& deck, int expected) {
    int result = computeDifference(deck);
    std::cout << "Deck: ";
    for (int card : deck) {
        std::cout << card << " ";
    }
    std::cout << "\nExpected Difference: " << expected << "\n";
    std::cout << "Computed Difference: " << result << "\n";
    std::cout << "Test " << (result == expected ? "PASSED" : "FAILED") << "\n\n";
}

int main() {
    // Test Case 1
    std::vector<int> deck1 = {3, 7, 2, 6, 5};
    runTestCase(deck1, -1); // As per the example given

    // Test Case 2
    std::vector<int> deck2 = {4, 9, 3};
    runTestCase(deck2, -2); // Miriam draws 4 and 3 (4+3=7), Alejandro draws 9, difference = 7 - 9 = -2

    // Test Case 3
    std::vector<int> deck3 = {2, 4, 6, 8};
    runTestCase(deck3, -4);

    // Test Case 4
    std::vector<int> deck4 = {1, 3, 5, 7, 9};
    runTestCase(deck4, 9); // Miriam ends up with an extra card, winning by a small margin

    // Add more test cases as needed
    std::vector<int> deck5 = {2, 4, 10, 8};
    runTestCase(deck5, 0);

    return 0;
}
