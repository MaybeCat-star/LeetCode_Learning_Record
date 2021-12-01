#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size(), m = needle.size();
        if (m == 0) {
            return 0;
        }
        vector<int> pi(m);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && needle[i] != needle[j]) {
                j = pi[j - 1];
            }
            if (needle[i] == needle[j]) {
                j++;
            }
            pi[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && haystack[i] != needle[j]) {
                j = pi[j - 1];
            }
            if (haystack[i] == needle[j]) {
                j++;
            }
            if (j == m) {
                return i - m + 1;
            }
        }
        return -1;
    }


    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCount = 0, count = 0;
        int n = nums.size();
        for(int i = 0; i < n; i++){
            if (nums[i] == 1){
                count++;
            }else{
                maxCount = max(maxCount, count);
                count = 0;
            }
        }
    return max(maxCount, count);
    }


};



// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode-solution-ds6y/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。