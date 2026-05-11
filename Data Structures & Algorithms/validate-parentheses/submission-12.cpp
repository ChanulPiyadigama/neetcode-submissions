#include <unordered_map> 

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> opens;
        unordered_map<char, char> pairs = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}
        };

        for (char c : s){
            if (pairs.count(c)){
                opens.push(c);
            } else{
                if (opens.empty() || pairs[opens.top()] != c){
                    return false;
                }
                opens.pop();
            }
        }
        return opens.empty();

        

    }
};
