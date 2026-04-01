#include <iostream>
#include <string>
using namespace std;

int getVowelCount(string str){
    int reversevow = 0;
    int vowCount = 0;
   for(int i=0; i<str.length(); i++){
       if(str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u' ||
          str[i]=='A' || str[i]=='E' || str[i]=='I' || str[i]=='O' || str[i]=='U'){
           vowCount++;
           reversevow++;
       }
    }
    return vowCount;
}
int main() {
    string s;
    cout << "Enter a string: ";
    getline(cin, s);

    int reverserow = getVowelCount(s);
    cout << "reverseed meaning: " << reverserow << endl;

    return 0;
}
