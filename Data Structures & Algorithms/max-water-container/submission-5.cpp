using namespace std;

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1;
        int maxArea = 0;

        while (l < r){
            int h = min(heights[l], heights[r]);
            int width = r-l;

            maxArea = max(maxArea, h*width);

            if (heights[l] < heights[r]){
                l++;
            } else {
                r--;
            }
        }
        return maxArea;
    }
};
