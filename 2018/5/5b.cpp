#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[]) {
    // read string
    string ogstring;
    string str;
    int shortest = INT32_MAX;
    ifstream f(argv[1]);
    
    if (!f.is_open()) {
        cout << "uh oh.\n";
        return -1;
    }

    getline(f, ogstring);

    for (char c : "abcdefghijklmnopqrstuvwxyz") {
        // remove letters
        str = ogstring;
        auto compfunc = [&c](char cmpc) {
            return cmpc == c || cmpc == toupper(c);
        };
        str.erase(remove_if(str.begin(), str.end(), compfunc), str.end());
        
        // react
        int i = 0;
        while (i < str.length() - 1) {
            // pretty print i's position
            // cout << str << endl;
            // for (int j = 0; j < i; j++) {
            //     cout << " ";
            // }
            // cout << "^\n";

            char& c = str[i];
            char& nc = str[i+1];

            if (c != nc && tolower(c) == tolower(nc)) {
                // match. react
                int end = max(i+2, (int)str.length());
                str.erase(i, 2);
                i = max(0, i-1);
            } else {
                // no match. move on
                i++;
            }
        }

        // check length
        shortest = str.size() < shortest ? str.size() : shortest;
    }

    cout << shortest << endl;

    return 0;
}
