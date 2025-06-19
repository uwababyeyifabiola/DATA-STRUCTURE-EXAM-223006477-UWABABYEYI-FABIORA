#include <iostream>        // For input/output
using namespace std;

// Define Denomination structure
struct Denomination {
    int value;             // Note value
    int* count;            // Pointer to number of notes
};

// Abstract base class for cash dispenser
class CashDispenser {
protected:
    Denomination* denoms;  // Pointer to array of denominations
    int size;              // Number of denominations
public:
    CashDispenser(Denomination* d, int s) : denoms(d), size(s) {}
    virtual bool dispense(int amount) = 0; // Pure virtual function
    virtual ~CashDispenser() {}
};

// Greedy strategy: use biggest notes first
class GreedyDispenser : public CashDispenser {
public:
    GreedyDispenser(Denomination* d, int s) : CashDispenser(d, s) {}
    bool dispense(int amount) override {
        cout << "Greedy Dispense: " << amount << endl;
        for (int i = 0; i < size; ++i) {
            Denomination* d = denoms + i;               // Pointer arithmetic
            int use = min(amount / d->value, *d->count); // Max notes we can use
            if (use > 0) {
                cout << use << " x " << d->value << endl;
                amount -= use * d->value;
                *d->count -= use;
            }
        }
        return amount == 0;
    }
};

// Optimal strategy (min number of notes)
class OptimalDispenser : public CashDispenser {
public:
    OptimalDispenser(Denomination* d, int s) : CashDispenser(d, s) {}
    bool dispense(int amount) override {
        cout << "Optimal Dispense: " << amount << endl;
        int amt = amount;
        for (int i = size - 1; i >= 0; --i) {           // Simple optimal: try smaller notes last
            while (amt >= denoms[i].value && *denoms[i].count > 0) {
                cout << "1 x " << denoms[i].value << endl;
                amt -= denoms[i].value;
                (*denoms[i].count)--;
            }
        }
        return amt == 0;
    }
};

// Add a denomination by resizing the array
void addDenomination(Denomination*& denoms, int& size, int value, int count) {
    Denomination* newArr = new Denomination[size + 1];   // Create new bigger array
    for (int i = 0; i < size; ++i) newArr[i] = denoms[i]; // Copy old items
    newArr[size].value = value;                           // Add new denomination
    newArr[size].count = new int(count);                  // Allocate count
    delete[] denoms;                                      // Delete old array
    denoms = newArr;                                      // Point to new array
    size++;                                               // Increase size
}

// Remove a denomination
void removeDenomination(Denomination*& denoms, int& size, int value) {
    int idx = -1;
    for (int i = 0; i < size; ++i)
        if (denoms[i].value == value) idx = i;           // Find index to remove

    if (idx == -1) return;                               // Not found
    Denomination* newArr = new Denomination[size - 1];   // New smaller array
    for (int i = 0, j = 0; i < size; ++i)
        if (i != idx) newArr[j++] = denoms[i];           // Copy others
    delete denoms[idx].count;                            // Delete count
    delete[] denoms;                                     // Delete old array
    denoms = newArr;                                     // Point to new
    size--;                                              // Decrease size
}

int main() {
    int size = 0;
    Denomination* denoms = NULL;                      // Dynamic array of denominations

    addDenomination(denoms, size, 100, 3);               // Add 3 x 100
    addDenomination(denoms, size, 50, 4);                // Add 4 x 50
    addDenomination(denoms, size, 20, 5);                // Add 5 x 20

    CashDispenser** machines = new CashDispenser*[2];    // Array of 2 machines
    machines[0] = new GreedyDispenser(denoms, size);     // Greedy dispenser
    machines[1] = new OptimalDispenser(denoms, size);    // Optimal dispenser

    machines[0]->dispense(270);                          // Try to dispense 270 using greedy
    machines[1]->dispense(90);                           // Try to dispense 90 using optimal

    // Cleanup memory
    for (int i = 0; i < size; ++i) delete denoms[i].count;
    delete[] denoms;
    delete machines[0];
    delete machines[1];
    delete[] machines;

    return 0;
}
