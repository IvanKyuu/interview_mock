#include <iostream>
#include <queue>
#include <vector>

using std::cout;
using std::endl;
using std::priority_queue;
using std::vector;

#define min(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _b : _a; })

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<int> pq = priority_queue<int>();
        int queue_size = min(k, nums.size());
        int i = 0;
        vector<int> ret = {};
        for (; i < queue_size-1; ++i) {
            while (!pq.empty() && pq.top() < nums[i]) {
                pq.pop();
            }
            if ((pq.empty()) || (nums[i] > pq.top() && (pq.size() < k))) {
                pq.push(nums[i]);
            }
        }
        for (; i < nums.size(); ++i) {
            while (! pq.empty() && pq.top() < nums[i]) {
                pq.pop();
            }
            if ((pq.empty()) || (nums[i] > pq.top() && (pq.size() < k))) {
                pq.push(nums[i]);
            }
            ret.emplace_back(pq.top());
            pq.pop();
        }
        return ret;
    }
};

int main() {
    cout << "int is " << sizeof(int) << " bytes." << endl;
}
