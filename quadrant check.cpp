#include <iostream>
using namespace std;

int main() {
    int A = 10;
    int B = 6;

    if (A > 0 && B > 0)
        cout << "Ist Quadrant";
    else if (A < 0 && B > 0)
        cout << "IInd Quadrant";
    else if (A < 0 && B < 0)
        cout << "IIIrd Quadrant";
    else if (A > 0 && B < 0)
        cout << "IVth Quadrant";
    else if (A == 0 && B == 0)
        cout << "Origin";

    return 0;
}