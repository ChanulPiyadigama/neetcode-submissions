class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(0, nums.size()-1, nums, target);
    }
private:
    int binarySearch(int start, int end, vector<int>& nums, int target){
        if (start >  end){
            return -1;
        }

        int mid = start + (end-start) / 2;

        if ( nums[mid] == target){
            return mid;
        }
        if (nums[mid] > target){
            return binarySearch(start, mid - 1, nums, target);
        } else{
            return binarySearch(mid+1, end, nums, target);
        }
    }
};
