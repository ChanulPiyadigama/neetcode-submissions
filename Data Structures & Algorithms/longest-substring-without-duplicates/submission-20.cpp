using namespace std;
#include <unordered_set>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()){
            return 0;
        }

        unordered_set<char> seen;
        int maxLength = 0;
        int start = 0;

        for (int i = 0; i < s.size(); i++){
            while ( seen.count(s[i]) > 0 ){
                seen.erase(s[start]);
                start++;
            }
            seen.insert(s[i]);
            maxLength = max(maxLength, (int)seen.size());
        }
        return maxLength;
    }
};
