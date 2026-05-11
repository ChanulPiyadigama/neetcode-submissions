#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false; 
        
        unordered_map<char, int> tally;

        for(int i=0; i < s.size(); i++){
            tally[s[i]] +=1;
        }

        for(int i=0; i<t.size(); i++){
            if (tally[t[i]] == 0){
                return false;
            }
            tally[t[i]] -= 1;
        }
        return true;
    }
};
